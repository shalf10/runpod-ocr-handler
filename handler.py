from PIL import Image
import base64
import io

def base64_to_image(image_base64):
    image_data = base64.b64decode(image_base64)
    return Image.open(io.BytesIO(image_data))

def handler(event):
    prompt = event["input"].get("prompt")
    image_base64 = event["input"].get("image_base64")
    image = base64_to_image(image_base64)

    # Agora passe `image` e `prompt` para o modelo multimodal
    output = model.chat(
        image=image,
        messages=[{"role": "user", "content": prompt}]
    )

    return output
    
