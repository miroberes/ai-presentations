#!/usr/bin/env python
# coding: utf-8

import os
import requests
import json

# === Set up the OpenAI API credentials and URL ===
API_KEY = os.environ["OPENAI_API_KEY"]
API_URL = "https://api.openai.com/v1/completions"

# === Define headers for API request ===
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}",
}

# === Define the request body ===
data = {
    "model": "gpt-4o-mini",
    "input": [
        {"role": "system", "content": "You are a standup comedian."},
        {"role": "user", "content": "Tell me a joke about a mouse."}
    ],
}

# === Send POST request ===
response = requests.post(API_URL, headers=headers, data=json.dumps(data))

# === Parse and print the response ===
if response.status_code == 200:
    result = response.json()
    print(result)
    print(result["output"][0]["content"][0]["text"])
else:
    print(f"Request failed: {response.status_code}")
    print(response.text)

