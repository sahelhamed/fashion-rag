import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("ARVAN_API_KEY"),
    base_url=os.getenv("ARVAN_BASE_URL")
)


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

    response = client.chat.completions.create(
        model="DeepSeek-V3.1",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.7,
        max_tokens=500
    )

    return (
        response
        .choices[0]
        .message
        .content
    )