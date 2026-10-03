import os
import requests

# Read API key from environment variable
api_key = os.getenv("OPENROUTER_API_KEY")

# MedTech question for our first API test
question = "For an IV Cannula Design History File, what documents should typically be considered for design inputs, design outputs, verification, validation, risk management, and design traceability?"
# Send the question to OpenRouter
response = requests.post(
    "https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    },
    json={
        "model": "openrouter/free",
        "messages": [
            {
                "role": "user",
                "content": question
            }
        ]
    }
)

# Check whether the API request was successful
if response.status_code == 200:
    data = response.json()

    answer = data["choices"][0]["message"]["content"]

    print("\n--- MedTech Copilot ---\n")
    print(answer)
else:
    print("\nAPI request failed.")
    print("Status code:", response.status_code)
    print("Response:", response.text)