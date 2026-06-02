"""
main.py — YOUR APP.

This is the file the Run button runs. Right now it's a tiny working AI tool
called "Explain Anything." Type a topic, get a plain-English explanation back.

This is your starting point. Over the next two weeks, you'll grow this into
whatever you want to build. Start by changing SYSTEM_PROMPT below — that one
line changes your whole tool's personality.
"""

import os
from flask import Flask, render_template, request, jsonify
from ai_helper import ask_ai

app = Flask(__name__)

# ─────────────────────────────────────────────────────────────────────────────
# 👇 CHANGE THIS to make the tool yours. Try:
#   "You explain things like a hyped sports announcer calling the play-by-play."
#   "You explain things in exactly 3 bullet points, each under 10 words."
#   "You explain things like a grumpy cat with a podcast."
# ─────────────────────────────────────────────────────────────────────────────
SYSTEM_PROMPT = "You explain any topic in one clear, simple sentence a teenager would understand."


@app.route("/")
def home():
    """Shows the web page (the part your users see)."""
    return render_template("index.html")


@app.route("/ask", methods=["POST"])
def ask():
    """Takes the user's input, sends it to the AI, returns the answer."""
    user_input = request.json.get("input", "")
    if not user_input.strip():
        return jsonify({"answer": "Type something first!"})

    answer = ask_ai(user_input, system_prompt=SYSTEM_PROMPT)
    return jsonify({"answer": answer})


if __name__ == "__main__":
    # 0.0.0.0 + the PORT Replit gives us = your app shows up in the preview window.
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
