import os
import sys
from google import genai

def start_chat_session():
    # 1. Verify API Key existence
    api_key = os.getenv("ColabVSCODE")
    if not api_key:
        print("Error: ColabVSCODE environment variable is not set.", file=sys.stderr)
        sys.exit(1)

    # 2. Initialize the Client
    client = genai.Client(api_key=api_key)

    # 3. Initialize a multi-turn chat object
    chat = client.chats.create(model="gemini-3.6-flash")

    print("==================================================")
    print(" Gemini Agent Active (Multi-Turn Chat Mode)")
    print(" Type 'exit' or 'quit' to terminate the session.")
    print("==================================================\n")

    # 4. Interactive message loop
    while True:
        try:
            user_input = input("You: ").strip()
            if not user_input:
                continue

            if user_input.lower() in ["exit", "quit"]:
                print("\nTerminating session. Goodbye!")
                break

            # Send message retaining previous conversation context
            response = chat.send_message(user_input)
            print(f"\nGemini: {response.text}\n")

        except KeyboardInterrupt:
            print("\nSession interrupted by user. Exiting...")
            break
        except Exception as e:
            print(f"\nAPI Error: {e}\n")

if __name__ == "__main__":
    start_chat_session()