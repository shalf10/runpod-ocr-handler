from PIL import Image
import base64
import io
import torch
from transformers import AutoModelForVision2Seq, AutoProcessor

# Carrega o modelo e processor
model_id = "Qwen/Qwen2.5-VL-7B-Instruct"
processor = AutoProcessor.from_pretrained(model_id)
model = AutoModelForVision2Seq.from_pretrained(model_id, torch_dtype=torch.float16, device_map="auto")

def base64_to_image(image_base64):
    image_data = base64.b64decode(image_base64)
    return Image.open(io.BytesIO(image_data)).convert("RGB")

def handler(event):
    prompt = event["input"].get("prompt", "")
    image_base64 = event["input"].get("image_base64", None)

    if not image_base64:
        return {"error": "No image provided"}

    image = base64_to_image(image_base64)

    inputs = processor(prompt=prompt, images=image, return_tensors="pt").to(model.device)
    output = model.generate(**inputs, max_new_tokens=512)

    result = processor.batch_decode(output, skip_special_tokens=True)[0]
    return {"response": result}
