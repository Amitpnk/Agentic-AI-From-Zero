# CampusBuddy API: deploy starter (Session 9)

A production-style version of the CampusBuddy agent, wrapped in a web API. Use it to try the ideas from [Session 9](../../session-09/notes.md) and as the deploy step of the [capstone](../../projects/README.md#project-6--campus-helpdesk-agent-capstone).

| File | What it does |
| --- | --- |
| `campus_tools.py` | The tools from Session 7 (exam timetable, library hours, weather) |
| `agent.py` | The agent: **read-only tools**, capped loop, tool errors can't crash it, and a **trace** for every request (timings, tokens, cost) |
| `app.py` | FastAPI web API: `POST /ask`, `GET /health`, API-key check, simple rate limit, input size limit |
| `evals.py` | Runs a fixed test set and prints a report; exits with an error if the pass rate is too low |
| `Dockerfile` | Packages the app as a container (runs as a non-root user) |

## 1. Run it on your laptop

```bash
pip install -r requirements.txt

# macOS / Linux
export GEMINI_API_KEY="your-gemini-key"
export APP_API_KEY="choose-a-long-random-key"
# Windows PowerShell:  $env:GEMINI_API_KEY="..." ; $env:APP_API_KEY="..."

uvicorn app:app --reload
```

Open http://localhost:8000/docs to try it in the browser, or:

```bash
curl -X POST http://localhost:8000/ask \
  -H "Content-Type: application/json" \
  -H "X-API-Key: choose-a-long-random-key" \
  -d '{"question": "When is my OS exam?"}'
```

You get the answer plus a `trace_id`, latency, tokens and cost. The full trace (every LLM call and tool call) is printed in the server log as one JSON line.

## 2. Evaluate it

```bash
python evals.py
```

Add a case to `EVAL_SET` every time you find a bug or a bad answer. Run it after every change to the prompt, model or tools. In CI (for example GitHub Actions), a failing exit code can stop a bad version from being deployed.

## 3. Run it in a container

```bash
docker build -t campusbuddy .
docker run -p 8080:8080 -e GEMINI_API_KEY="your-gemini-key" -e APP_API_KEY="choose-a-long-random-key" campusbuddy
```

## 4. Deploy it

### Google Cloud Run (serverless containers)

Needs a Google Cloud project with billing enabled (Cloud Run has a monthly free tier; check the current limits).

```bash
# Store the Gemini key in Secret Manager, not in the code or command history
echo -n "your-gemini-key" | gcloud secrets create gemini-api-key --data-file=-

gcloud run deploy campusbuddy \
  --source . \
  --region asia-south1 \
  --allow-unauthenticated \
  --set-env-vars APP_API_KEY=choose-a-long-random-key \
  --set-secrets GEMINI_API_KEY=gemini-api-key:latest
```

`--allow-unauthenticated` makes the URL public; our own `APP_API_KEY` check still protects it. If the deploy reports a permission error on the secret, give the Cloud Run service account the **Secret Manager Secret Accessor** role.

### Other options

| Option | Notes |
| --- | --- |
| **Render**, **Railway** | Connect your GitHub repo, they build the Dockerfile. Free or cheap tiers for demos (check current terms). |
| **Hugging Face Spaces** (Docker) | Free CPU Spaces, good for a public demo. |
| **AWS App Runner**, **Azure Container Apps** | Same idea as Cloud Run on AWS and Azure. |
| **AWS Lambda / Google Cloud Functions** | True serverless functions; mind the time limits for slow agents. |

## Before real students use it

- [ ] `python evals.py` passes, including safety cases
- [ ] Keys are in a secret manager, not in code or GitHub
- [ ] The API needs a key (or user login) and has a rate limit
- [ ] Logs and traces are collected somewhere you can search
- [ ] A daily budget alert is set on your Gemini / cloud account
- [ ] You start with a small pilot group, not the whole college
