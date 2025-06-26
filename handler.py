from PIL import Image
import base64
import io
import pytesseract

def handler(event):
    # event['input'] contém seu payload
    input_data = event.get("input", {})
    image_b64 = input_data.get("image_base64")

    if not image_b64:
        return {"error": "Imagem base64 não enviada"}

    image_bytes = base64.b64decode(image_b64)
    image = Image.open(io.BytesIO(image_bytes))

    text = pytesseract.image_to_string(image)

    return {"text": text.strip()}
