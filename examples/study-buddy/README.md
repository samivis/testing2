# Study Buddy

Turns any chunk of text into a 5-question multiple-choice quiz.

**The idea worth stealing:** the system prompt locks the AI into one job (make a quiz) and one format (5 questions, A–D, answers at the end). That's what turns a generic chatbot into a useful *tool*.

## Run it
```
python3 examples/study-buddy/main.py
```

## Make it your own
- Change `notes` to your real homework text.
- Ask for 10 questions, or true/false, or flashcards instead.
- Turn it into a web app: copy the prompt idea into your `main.py` and add a text box (see how the starter app works).
