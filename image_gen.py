import requests
from urllib.parse import quote

prompts = [
    "Jesus standing in storm cinematic",
    "disciples shocked biblical scene",
    "golden heavenly light biblical"
]

for i, prompt in enumerate(prompts):

    url = f"https://image.pollinations.ai/prompt/{quote(prompt)}"

    image = requests.get(url).content

    with open(f"scene{i}.jpg", "wb") as f:
        f.write(image)

print("Images Generated")