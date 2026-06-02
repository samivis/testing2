# replit.md — Project Context

Replit Agent reads this file automatically on every request. Students: you don't need to read this — but your Agent does. Your daily guides are Agent Skills — invoke them by name or follow the in-class slides.

## What this is

This is a student project for **AI Builders Camp**, a coding camp for ages 13–17. The student is building an AI-powered web app over 8 sessions. The student is a beginner. Keep explanations simple, encouraging, and free of unnecessary jargon.

## Instructor

- **Name:** Samidha Visai
- **Replit:** `svisai` (has collaborator access to this Repl)
- **GitHub:** `samivis` (has collaborator access to this repo)
- **Email:** svisai.tools@gmail.com

## Tech stack (do not change without asking the student)

- **Language:** Python 3.11
- **Web framework:** Flask
- **AI:** Replit Managed AI Integrations (OpenAI-compatible), accessed through `ai_helper.py`
- **Frontend:** plain HTML/CSS/JS in `templates/` and `static/` (no React, no build step)

## How AI works in this project — IMPORTANT

- The student does **NOT** have an OpenAI API key and should never be asked for one.
- AI access comes from Replit Managed AI via two environment variables that are set up automatically: `AI_INTEGRATIONS_OPENAI_BASE_URL` and `AI_INTEGRATIONS_OPENAI_API_KEY`.
- If those env vars are missing, run the Replit AI integration setup — do not ask the student for keys.
- All AI calls should go through the `ask_ai()` helper in `ai_helper.py`, which already handles the connection. Reuse it instead of creating new OpenAI clients.
- Default model is `gpt-4o-mini` (fast and affordable). Only change it if the student asks.
- For gpt-4o models: do not set `temperature`, and use `max_completion_tokens` (not `max_tokens`).

## How to run

- The Run button runs `main.py`, a Flask app that binds to `0.0.0.0` on the `PORT` env var (default 5000).
- `main.py` is the student's main app. It starts as a simple "Explain Anything" tool and grows across camp.

## Agent Skills

This project includes Agent Skills in `.agents/skills/`. Each skill is a step-by-step workflow the student can invoke by telling Agent to "use the [skill-name] skill."

Current skills, by camp day:

| Skill | Day | What it does |
|---|---|---|
| `create-spec` | 2 | Write a tech spec, then scaffold the project structure from it |
| `design-spec` | 4 | Turn design references into a `design-spec.md` |
| `build-v1` | 4 | Build v1 from both specs, then evaluate and iterate |
| `add-automation` | 6 | Add one automation: scheduled job, bot, or recurring task |
| `ethics-review` | 7 | Review the app for privacy, bias, security, safety, transparency |
| `gtm-plan` | 7 | Write a pitch + GTM plan, polish the README, ship one GTM action |

Skills are generated from the curriculum using the make-lesson-starter command.

## When helping the student

- Make the smallest change that solves their request. Don't rewrite their whole app.
- Explain what you changed in plain English.
- Keep the structure simple — one main app in `main.py`, not a sprawl of files.
- Encourage them. They're 13–17 and just learning. A working app they understand beats a fancy one they don't.
