# Gemini Multi-Turn Chat Agent

`ai-agent-sandbox` is a small Python command-line application that lets a user
have an ongoing conversation with Google's Gemini model.

## What it does

- Reads the Gemini API key from the `ColabVSCODE` environment variable.
- Starts a chat session with `gemini-3.6-flash`.
- Sends each user message to Gemini while keeping the earlier messages in the
  same conversation.
- Stops when the user enters `exit`, `quit`, or presses `Ctrl+C`.
- Reports a missing API key or API failure instead of starting silently.

## How to run it

1. Install Python 3.9 or newer.
2. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set the API key without putting it in the repository:

   ```bash
   export ColabVSCODE="your-gemini-api-key"
   ```

4. Start the agent:

   ```bash
   python main.py
   ```

## Project structure

| File | Purpose |
| --- | --- |
| `main.py` | Starts the Gemini client, opens the chat, and handles the input loop. |
| `requirements.txt` | Lists the Google GenAI and environment-variable packages. |
| `.gitignore` | Keeps keys, virtual environments, and generated Python files out of Git. |

## Resume description

Built a Python command-line Gemini chat agent using the Google GenAI SDK. Added
environment-variable API-key handling, persistent multi-turn conversation
context, clean exit commands, keyboard-interrupt handling, and visible API
error messages.

## Recent work

- Created the initial Python agent structure.
- Switched the model configuration to `gemini-3.6-flash`.
- Replaced one-off text generation with a multi-turn interactive chat session.
