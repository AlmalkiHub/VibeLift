# prompts.py

def build_prompt(name, mood, time_of_day, tone):
    tone_instructions = {
        "Inspirational 🌟": "Give a bold, uplifting, high-energy motivational message that feels like a TED Talk.",
        "Friendly 😊": "Respond like a supportive best friend offering cheerful encouragement.",
        "Tough Love 💥": "Be brutally honest and push them hard, but with care. No sugarcoating.",
        "Spiritual 🌿": "Use calming, soulful language that speaks to purpose, peace, and inner strength."
    }

    instruction = tone_instructions.get(tone, tone_instructions["Inspirational 🌟"])

    return (
        f"{name} is feeling {mood.lower()} this {time_of_day.lower()}.\n"
        f"Your job is to generate a motivational message that is short, emotional, and meaningful.\n"
        f"Tone: {tone}\n"
        f"{instruction}\n"
        "End your message with one inspiring quote and a final call to action for the user to carry with them."
    )

def generate_image_prompt(mood, time_of_day, tone):
    return (
        f"Create a high-quality, artistic image that captures the feeling of someone who is {mood.lower()} "
        f"during the {time_of_day.lower()}. The tone of the image should reflect a {tone.lower()} mood. "
        f"The scene should evoke emotion and match the user's energy and tone. Do not include text in the image."
    )
