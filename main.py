"""
main.py — Dish Diary

A food photo blog that uses AI to write captions.
Upload a food photo + a short note → AI writes the caption → it's on your blog.

Routes:
  GET  /         — blog page, shows all posts newest first
  GET  /upload   — upload form
  POST /upload   — saves photo, generates caption, saves post, redirects to /
"""

import os
import json
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from ai_helper import ask_ai

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
POSTS_FILE = "posts.json"
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif", "webp"}

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

CAPTION_PROMPT = (
    "You are a food blogger who writes short, vivid, enthusiastic captions "
    "for food photos. Write ONE caption (2-3 sentences max) that makes the "
    "reader hungry. Be specific and sensory — mention flavors, textures, smells. "
    "Do not start with 'I'."
)


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


def load_posts():
    if not os.path.exists(POSTS_FILE):
        return []
    with open(POSTS_FILE) as f:
        return json.load(f)


def save_posts(posts):
    with open(POSTS_FILE, "w") as f:
        json.dump(posts, f, indent=2)


@app.route("/")
def index():
    posts = load_posts()
    posts = list(reversed(posts))
    return render_template("index.html", posts=posts)


@app.route("/upload", methods=["GET"])
def upload_form():
    return render_template("upload.html")


@app.route("/upload", methods=["POST"])
def upload_post():
    file = request.files.get("photo")
    note = request.form.get("note", "").strip()

    if not file or file.filename == "":
        return redirect(url_for("upload_form"))

    if not allowed_file(file.filename):
        return redirect(url_for("upload_form"))

    filename = secure_filename(file.filename)
    # Make filename unique using a timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_")
    filename = timestamp + filename
    file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))

    # Build the prompt for AI
    if note:
        prompt = f"Write a caption for a food photo. The dish is: {note}"
    else:
        prompt = "Write a caption for a food photo. Describe it as if it looks absolutely delicious."

    caption = ask_ai(prompt, system_prompt=CAPTION_PROMPT)

    posts = load_posts()
    posts.append({
        "filename": f"static/uploads/{filename}",
        "caption": caption,
        "date": datetime.now().strftime("%B %d, %Y"),
    })
    save_posts(posts)

    return redirect(url_for("index"))


if __name__ == "__main__":
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, use_reloader=True)
