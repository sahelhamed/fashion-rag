import os
import requests

from dotenv import load_dotenv

load_dotenv()


def generate_style_advice(
    selected_item,
    retrieved_items
):
    items_text = "\n".join(
        [
            f"- {item}"
            for item in retrieved_items
        ]
    )

    prompt = f"""
You are a professional fashion stylist.

Selected item:
{selected_item}

Available items:
{items_text}

Create:
1. Recommended outfit
2. Why it works
3. Styling tips

Keep answer concise.
"""

    response = requests.post(
        f"{os.getenv('ARVAN_BASE_URL')}/chat/completions",
        headers={
            "Authorization": f"apikey {os.getenv('ARVAN_API_KEY')}",
            "Content-Type": "application/json"
        },
        json={
            "model": "DeepSeek-V3.1",
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "temperature": 0.7,
            "max_tokens": 500
        }
    )

    print("STATUS:", response.status_code)
    print("RESPONSE:", response.text)

    response.raise_for_status()

    return (
        response.json()
        ["choices"][0]
        ["message"]["content"]
    )