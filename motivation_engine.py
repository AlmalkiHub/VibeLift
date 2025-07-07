import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def build_prompt(name, mood_description, time_of_day, tone):
    return f"""
You are a personal motivational coach AI. Your job is to give a short, personalized motivational message.

User’s name: {name}
Mood: {mood_description}
Time of day: {time_of_day}
Preferred tone: {tone}

Now write a powerful, positive, human-like motivational message in a warm and natural tone, ending with a short quote or call to action.
"""

def generate_message(prompt):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are a wise and emotionally intelligent motivational coach."},
                  {"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

def generate_image(mood_description):
    image_response = client.images.generate(
        prompt=f"A stunning digital artwork representing the mood: {mood_description}",
        model="dall-e-3",
        n=1,
        size="1024x1024"
    )
    return image_response.data[0].url

def get_motivation(name, mood_description, time_of_day, tone):
    prompt = build_prompt(name, mood_description, time_of_day, tone)
    message = generate_message(prompt)
    image_url = generate_image(mood_description)
    return message, image_url
