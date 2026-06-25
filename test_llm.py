from services.llm_stylist import (
    generate_style_advice
)

answer = generate_style_advice(
    "white top",
    [
        "black skirt",
        "brown boots",
        "white sneakers"
    ]
)

print(answer)