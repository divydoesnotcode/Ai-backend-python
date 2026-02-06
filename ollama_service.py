import requests
import json

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "ministral-3:8b"


def generate_vendors_llm(item, location):

    prompt = f"""
Return vendor list in JSON format.

Schema:
{{
  "vendors": [
    {{
      "name": "",
      "address": "",
      "phone": "",
      "email": "",
      "website": ""
    }}
  ]
}}

Item: {item}
Location: {location}

Return ONLY JSON.
"""

    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "format": "json",
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)

    return json.loads(response.json()["response"])