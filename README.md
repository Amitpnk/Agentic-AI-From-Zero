# Agentic AI From Zero

Notes, slides, diagrams and labs for a 2-day hands-on workshop: **Generative AI** (Day 1) and **Agentic AI** (Day 2).

**Website (for presenting):** https://amitpnk.github.io/Agentic-AI-From-Zero/

| Session | Notes (web) | Notes (Markdown) | Slides | Lab |
| --- | --- | --- | --- | --- |
| 1. How LLMs work | [notes](session-01/notes.html) | [notes.md](session-01/notes.md) | [slides](session-01/slides.html) | — |
| 2. Prompt engineering | [notes](session-02/notes.html) | [notes.md](session-02/notes.md) | [slides](session-02/slides.html) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Amitpnk/Agentic-AI-From-Zero/blob/main/labs/session-02-prompt-lab.ipynb) |
| 3. Building with LLM APIs | [notes](session-03/notes.html) | [notes.md](session-03/notes.md) | [slides](session-03/slides.html) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Amitpnk/Agentic-AI-From-Zero/blob/main/labs/session-03-chatbot-lab.ipynb) |
| 4. RAG | [notes](session-04/notes.html) | [notes.md](session-04/notes.md) | [slides](session-04/slides.html) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Amitpnk/Agentic-AI-From-Zero/blob/main/labs/session-04-rag-lab.ipynb) |

**Projects:** six hands-on projects that build up to a campus helpdesk agent. See [projects/README.md](projects/README.md).

## Structure

```
index.html                 Workshop home page
assets/                    Shared CSS and the interactive temperature demo
session-NN/notes.html      Session notes (web) with examples, quiz, instructor guide
session-NN/notes.md        Same notes in Markdown (readable on GitHub)
session-NN/slides.html     Slide deck (reveal.js)
session-NN/diagrams/       draw.io sources (.drawio) and exported .svg
projects/                  Project list (index.html + README.md) and capstone diagram
labs/                      Google Colab notebooks
labs/data/                 Sample documents for the labs (fictional college FAQ)
scripts/export-diagrams.sh Re-export every .drawio to .svg (needs draw.io desktop)
```

## Diagrams

Diagrams are made in [draw.io](https://www.drawio.com/). Edit the `.drawio` file (desktop app, VS Code extension, or app.diagrams.net), then run:

```bash
bash scripts/export-diagrams.sh
```

The exported `.svg` files embed the diagram, so they can also be opened and edited directly in draw.io.

## Using the slides

- `→` / `Space` next slide, `Esc` overview, `F` full screen, `S` speaker notes
- Export to PDF: open `slides.html?print-pdf` in Chrome and print to PDF

## GitHub Pages

The site is served by GitHub Pages from the root of the `main` branch (`.nojekyll` is included so files are served as-is). Push or merge to `main` and the site updates in a minute or two.

## Run locally

Open `index.html` in a browser, or run `python -m http.server` and visit http://localhost:8000.
