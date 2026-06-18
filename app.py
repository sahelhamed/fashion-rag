import json

# 1. خواندن دیتای لباس‌ها
with open("clothes.json", "r", encoding="utf-8") as f:
    clothes = json.load(f)

# 2. جدا کردن آیتم‌ها بر اساس نوع
tops = [c for c in clothes if c["type"] == "top"]
skirts = [c for c in clothes if c["type"] == "skirt"]
shoes = [c for c in clothes if c["type"] == "shoes"]

# 3. یک تابع ساده پیشنهاد استایل
def suggest_style(skirt_color):
    print("\n🎀 پیشنهاد استایل برای دامن شما:\n")

    for top in tops:
        for shoe in shoes:
            print(f"- دامن {skirt_color} + {top['color']} {top['style']} + {shoe['style']}")

# 4. تست
user_skirt_color = "blue"
suggest_style(user_skirt_color)