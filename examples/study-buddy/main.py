"""
Study Buddy — turns any chunk of text into a 5-question quiz.

This is an EXAMPLE to read for ideas. Run it in the Shell:
    python3 examples/study-buddy/main.py

The big idea: a specific prompt (role + format) turns the AI into a focused tool.
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

# This system prompt is what makes it a STUDY tool instead of a generic chatbot.
SYSTEM_PROMPT = """You are a study tutor for high school students.
Given a chunk of text, write exactly 5 multiple-choice quiz questions about it.
Each question has 4 options labeled (A)-(D). After all 5 questions, list the
correct answers. Keep the language simple."""

# Try changing this to your own notes, or a paragraph from a textbook.
notes = """The water cycle is the path that water takes as it moves around Earth.
Water evaporates from oceans and lakes into the air, condenses into clouds,
falls as rain or snow (precipitation), and collects back in bodies of water."""

response = client.chat.completions.create(
    model="gpt-5-mini",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": notes},
    ],
    max_completion_tokens=8192,
)

print(response.choices[0].message.content)
