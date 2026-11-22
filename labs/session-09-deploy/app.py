"""CampusBuddy as a web API.

Run locally:   uvicorn app:app --reload        then open http://localhost:8000/docs
"""
import logging
import os
import time
from collections import defaultdict, deque

from fastapi import FastAPI, Header, HTTPException, Request
from pydantic import BaseModel, Field

from agent import MODEL, run_agent

logging.basicConfig(level=logging.INFO, format="%(message)s")

app = FastAPI(title="CampusBuddy API", description="Ask the ABC Engineering College helpdesk agent a question.")

APP_API_KEY = os.environ.get("APP_API_KEY")                # clients send it in the X-API-Key header
RATE_LIMIT = int(os.environ.get("RATE_LIMIT_PER_MINUTE", "10"))
_recent = defaultdict(deque)                               # caller -> times of recent requests


class Question(BaseModel):
    question: str = Field(min_length=2, max_length=500, examples=["When is my OS exam?"])


class Answer(BaseModel):
    answer: str
    trace_id: str
    latency_ms: int
    tokens: int
    cost_usd: float


def _caller(request: Request) -> str:
    forwarded = request.headers.get("x-forwarded-for")      # set by Cloud Run and most load balancers
    return forwarded.split(",")[0].strip() if forwarded else (request.client.host if request.client else "unknown")


def _check_rate_limit(caller: str) -> None:
    # Simple in-memory limit. It resets on restart and isn't shared between instances:
    # in real production use your API gateway or a shared store like Redis.
    now, recent = time.time(), _recent[caller]
    while recent and now - recent[0] > 60:
        recent.popleft()
    if len(recent) >= RATE_LIMIT:
        raise HTTPException(status_code=429, detail="Too many questions. Please wait a minute.")
    recent.append(now)


@app.get("/health")
def health():
    return {"status": "ok", "model": MODEL}


@app.post("/ask", response_model=Answer)
def ask(body: Question, request: Request, x_api_key: str | None = Header(default=None)):
    if APP_API_KEY and x_api_key != APP_API_KEY:
        raise HTTPException(status_code=401, detail="Missing or wrong API key.")
    _check_rate_limit(_caller(request))
    trace = run_agent(body.question)
    return Answer(answer=trace["answer"], trace_id=trace["trace_id"], latency_ms=trace["latency_ms"],
                  tokens=trace["tokens_in"] + trace["tokens_out"], cost_usd=trace["cost_usd"])
