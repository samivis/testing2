"""
Vibe Check Bot — reads a message and tells you the vibe before you send it.

This is an EXAMPLE to read for ideas. Run it in the Shell:
    python3 examples/vibe-check-bot/main.py

The big idea: the AI can RATE and EXPLAIN, not just generate. Useful for
"should I send this text?" moments.
"""

import os
from openai import OpenAI

if not os.environ.get("AI_INTEGRATIONS_OPENAI_BASE_URL"):
    print("AI isn't connected yet. Open your main app, click the Agent panel, and say:")
    print("'Please set up Replit AI so my app can make AI calls.' Then run this again.")
    raise SystemExit

client = OpenAI(
    base_url=os.environ.get("AI_INTEGRATIONS_OPENAI_BASE_URL"),
    api_key=os.environ.get("AI_INTEGRATIONS_OPENAI_API_KEY"),
)

SYSTEM_PROMPT = """You are a friendly communication coach for teenagers.
Given a message someone is about to send, do three things:
1. Name the vibe in 1-3 words (e.g. "warm and casual", "a little harsh").
2. Give it a score from 1 to 10 for how it will land with the reader.
3. Suggest one small tweak to improve it.
Keep it short and kind."""

# Try changing this to a message you'd actually send.
message = "hey can you send me the notes i missed class and im totally lost"

response = client.chat.completions.create(
    model="gpt-5-mini",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": message},
    ],
    max_completion_tokens=8192,
)

print(f"Message: {message}\n")
print(response.choices[0].message.content)
