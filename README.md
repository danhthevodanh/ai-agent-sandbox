# ai-agent-sandbox

A Python command-line application that runs a persistent, multi-turn conversation with Google's Gemini model using the Google GenAI SDK.

## What it does

- Reads a Gemini API key from the `ColabVSCODE` environment variable
- Initialises a multi-turn chat session with `gemini-3.6-flash` so the model remembers everything said earlier in the same run
- Loops on user input: sends each message to Gemini and prints the response
- Exits cleanly on `exit`, `quit`, or `Ctrl+C`
- Reports a missing API key or an API failure with a clear error message instead of crashing silently

## How it was built

- Single-file Python script (`main.py`) using the `google-genai` SDK
- Used `client.chats.create(model=...)` to create a stateful chat object that accumulates conversation history automatically
- Wrapped the input loop in `try/except` to catch both `KeyboardInterrupt` and API errors separately, giving different exit messages for each
- Used `os.getenv` rather than hardcoding credentials; the key never touches the repository

## Setup

```bash
git clone https://github.com/danhthevodanh/ai-agent-sandbox.git
cd ai-agent-sandbox

pip install -r requirements.txt

export ColabVSCODE="your-gemini-api-key"
python main.py
```

## Project structure

| File | Purpose |
|------|---------|
| `main.py` | Gemini client setup, chat session init, input/response loop |
| `requirements.txt` | `google-genai` and `python-dotenv` |
| `.gitignore` | Excludes `.env`, `__pycache__`, virtual environments |

## Tech stack

Python 3.9+, Google GenAI SDK (`google-genai`)

## License

MIT
