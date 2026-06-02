"""
reminder_bot.py — your first automation 🤖

Day 6 "try it": make something happen AUTOMATICALLY, without you clicking Run.

This little program posts a homework reminder into Discord. Once it works,
you'll Publish it as a Scheduled Deployment so it pings the channel before
class — every time, on its own. THAT is automation: code that does a real
thing in the world while you're not even looking.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SET IT UP (about 10 minutes)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Get a Discord "webhook" — a private link that lets your code post to a channel.
     • Open a Discord server you can manage. Not an admin of the class server?
       Click the green + on the left to make your OWN free server (10 seconds) —
       it's a perfect sandbox and you control everything.
     • Pick a channel  →  hover it  →  ⚙️ Edit Channel  →  Integrations
       →  Webhooks  →  New Webhook  →  "Copy Webhook URL"

2. Store that URL as a Secret so it stays private (never paste it into your code):
     • In Replit, open the Tools panel  →  Secrets
     • New secret →  key:  DISCORD_WEBHOOK_URL    value: (paste your URL)

3. Click Run. Check your Discord channel — your reminder should appear. 🎉

4. Make it automatic:  Publish  →  Scheduled Deployment
     • Run command:  python3 day-06/reminder_bot.py
     • Schedule: before class (for example, weekdays at 10:30 AM)
   Now it pings the channel on its own, even with your browser closed.

Scheduling feels fiddly? No stress — just clicking Run still fires it, and that
still counts: you made code do a real thing automatically. That's the whole idea.
"""

import os
import json
import urllib.request

# The reminder you want to send. Change this to anything you like!
REMINDER = (
    "📚 Heads up — AI Builders Camp class starts soon! "
    "Bring your project and a question you're stuck on. See you there! 🚀"
)

# ─────────────────────────────────────────────────────────────────────────────
# BONUS: make the reminder fresh and fun EVERY time, using the AI you already know.
# Flip this to True and ask_ai() will write a new reminder on each run.
# ─────────────────────────────────────────────────────────────────────────────
USE_AI = False


def build_message():
    """Return the text to post — either your fixed reminder or an AI-written one."""
    if USE_AI:
        from ai_helper import ask_ai
        return ask_ai(
            "Write a short, upbeat one-line reminder that AI Builders Camp class "
            "starts soon. Include one emoji. Keep it under 25 words.",
            system_prompt="You are a hype friend sending fun class reminders to teenagers.",
        )
    return REMINDER


def send_to_discord(message):
    """Post a message to your Discord channel using your webhook."""
    webhook_url = os.environ.get("DISCORD_WEBHOOK_URL")
    if not webhook_url:
        print("No DISCORD_WEBHOOK_URL secret found yet.")
        print("Add it in Tools → Secrets — see the setup steps at the top of this file.")
        return

    data = json.dumps({"content": message}).encode("utf-8")
    request = urllib.request.Request(
        webhook_url,
        data=data,
        headers={"Content-Type": "application/json"},
    )
    urllib.request.urlopen(request)
    print("Sent to Discord! Go check your channel. ✅")


if __name__ == "__main__":
    send_to_discord(build_message())
