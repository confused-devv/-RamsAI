import os
import requests
from PIL import Image
from io import BytesIO

# 🛡️ Replace with your Hugging Face token
HUGGINGFACE_TOKEN = "HF_token"

API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
headers = {
    "Authorization": f"Bearer {HUGGINGFACE_TOKEN}"
}

def generate_image(prompt: str, output_path="static/dish.png"):
    payload = {
        "inputs": prompt,
        "options": {"wait_for_model": True}
    }

    print(f"🖼️ Generating image for: {prompt}")
    response = requests.post(API_URL, headers=headers, json=payload)
    response.raise_for_status()

    image = Image.open(BytesIO(response.content))

    # 🔧 Make sure the output folder exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    image.save(output_path)
    print(f"✅ Image saved to {output_path}")
    return output_path
