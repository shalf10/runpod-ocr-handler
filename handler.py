from PIL import Image
import base64
import io
import pytesseract

def handler(event):
    image_b64 = event.get("image_base64")
    if not image_b64:
        return {"error": "Imagem base64 não enviada"}

    image_bytes = base64.b64decode(image_b64)
    image = Image.open(io.BytesIO(image_bytes))

    text = pytesseract.image_to_string(image)

    return {
        "output": text.strip()
    }
