"""
Rec Engine — recommends something based on what you tell it.

This is an EXAMPLE to read for ideas. Run it in the Shell:
    python3 examples/rec-engine/main.py

The big idea: collect a little info from the user, then ask the AI to make a
specific, personalized pick. This is how "what should I watch / read / cook?"
tools work.
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

SYSTEM_PROMPT = """You are a movie recommendation expert.
Given someone's mood and how much time they have, recommend exactly ONE movie.
Give the title, the year, one sentence on why it fits, and where it might be
streaming. Don't list a bunch of options — commit to one great pick."""

# These would normally come from the user. Try changing them.
mood = "I want something funny but also kind of heartfelt"
time_available = "about 90 minutes"

user_request = f"My mood: {mood}. Time I have: {time_available}."

response = client.chat.completions.create(
    model="gpt-5-mini",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_request},
    ],
    max_completion_tokens=8192,
)

print(f"Looking for: {user_request}\n")
print(response.choices[0].message.content)
