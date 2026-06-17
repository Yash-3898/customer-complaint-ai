from openai import OpenAI
import json

client = OpenAI(
    api_key="EMPTY",
    base_url="http://localhost:8000/v1"
)

def classify_complaint(complaint: str):

    prompt = f"""
You are a customer complaint classification system.

Categories:
- Billing
- Technical
- Account
- Security

Priority Levels:
- Critical
- High
- Medium
- Low

Return ONLY valid JSON.

Complaint:
{complaint}
"""

    response = client.chat.completions.create(
        model="Qwen/Qwen2.5-7B-Instruct",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    result = response.choices[0].message.content

    return json.loads(result)