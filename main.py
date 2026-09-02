import os
from google import genai

def run_agent():
    # Retrieve API key passed from environment
    api_key = os.getenv("ColabVSCODE")
    if not api_key:
        raise ValueError("ColabVSCODE not found in environment variables.")

    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="Write a 1-sentence status report confirming the agent node is active.",
    )
    print(f"Agent Output:\n{response.text}")

if __name__ == "__main__":
    run_agent()