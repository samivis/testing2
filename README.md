# AI Builders Camp — Starter Template

Welcome to camp. This is your starting point. In two weeks, you'll turn it into a real, deployed AI app that lives at your own link — something you can put on a résumé or a college app.

**Instructor:** Samidha Visai · **Ages:** 13–17 · **Format:** 8 sessions over 2 weeks

---

## Start here (Day 1, ~10 minutes)

1. **Click the green `Run` button** at the top. A simple app called **Explain Anything** opens in the preview window. That's your starter app working.
2. **Connect AI.** Open the **Agent** panel (top right) and type:
   > "Please set up Replit AI so my app can make AI calls."

   This connects your app to AI using your **Replit credits** — no OpenAI account, no API key, no copying secret codes. You do this once.
3. **Click `Run` again** and type something into the app. You should get an AI answer back.
4. **Invite your instructor** so they can help you directly without screensharing:
   - Click **Share** (top right of the editor)
   - Type `svisai` and add as a collaborator
   - You only do this once — your instructor will have access all camp
5. **Open `main.py`** and change the `SYSTEM_PROMPT` line to make it yours.

That's it — you're a builder now. Each day, follow along at **[aibuilderscamp.com](https://aibuilderscamp.com)** — the lesson page has the slides, what to try, and your homework. This repo is your workspace: when your instructor says "run this" or "do this homework," everything's already set up here for you.

---

## Connect with the camp

**Discord (our camp community):** [discord.gg/DK3CCuSge](https://discord.gg/DK3CCuSge)
Post in **#general** any time you're stuck, finished something, or just want to share. Introduce yourself with:

> Hey everyone! I'm [your name] and I'm all set up for AI Builders Camp! My Replit username is [replit-username] and my GitHub is [github-username]. Ready to build! 🚀

**GitHub (your portfolio):**
- Push this project to a public GitHub repo so your work is saved outside Replit
- In Replit, click the **Version control** icon (left sidebar) → **Create a GitHub repository** → make it **public**
- Then invite your instructor as a collaborator: go to your repo on GitHub → **Settings** → **Collaborators** → **Add people** → search `samivis`

---

## How this template is organized

```
main.py              ← YOUR APP. The Run button runs this. You grow it all camp.
templates/index.html ← what your app looks like (the web page)
static/style.css     ← your app's colors and styling
ai_helper.py         ← your shortcut to AI. Just import ask_ai and use it.
replit.md            ← tells your Replit Agent about the project (it reads this automatically)
.agents/skills/      ← guided workflows your Agent knows how to follow

examples/            ← three finished mini-apps to read for ideas
```

You build ONE app across all of camp — it lives in `main.py` and gets better every day.

---

## Using AI in your code

Anywhere in your Python code, you can do this:

```python
from ai_helper import ask_ai

answer = ask_ai("Write a haiku about pizza")
print(answer)
```

Want to change the AI's personality? Pass a `system_prompt`:

```python
answer = ask_ai(
    "Tell me about the moon",
    system_prompt="You are a pirate who loves astronomy."
)
```

---

## The 8 days

| Day | You build |
|---|---|
| 1 | Your first AI tool, deployed to a live link |
| 2 | A tech spec + scaffolded project, ready to design |
| 3 | Design references — your app's visual identity starts here |
| 4 | A design spec + working v1, built from your specs |
| 5 | Midpoint demo + feature direction for week 2 |
| 6 | Automation — a scheduled job, bot, or recurring task |
| 7 | Ethics review + GTM plan + final polish |
| 8 | Demo Day 🎉 |

---

## Stuck? Three things to try

1. **Ask the Agent.** It can see your code. Describe what's wrong in plain English.
2. **Read the error message.** It usually says which file and line broke.
3. **Post in Discord** at [discord.gg/DK3CCuSge](https://discord.gg/DK3CCuSge). Someone's probably hit the same thing.

You've got this. Let's build.
