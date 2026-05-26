import google.generativeai as genai
import os

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.0-flash"
)

prompt = """
Create a viral Bible YouTube Shorts video.

Requirements:
- 30 seconds
- 3 scenes
- Emotional storytelling
- Strong hook
- Cinematic narration
- Cinematic image prompts
- YouTube title
- Hashtags
"""

response = model.generate_content(prompt)

text = response.text

print(text)

with open("script.txt", "w", encoding="utf-8") as f:
    f.write(text)