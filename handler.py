from transformers import AutoProcessor, AutoModelForVision2Seq
from PIL import Image
import base64
import io
import torch

# Carrega modelo e processor na inicialização
try:
    model_id = "Qwen/Qwen2.5-VL-7B-Instruct"
    processor = AutoProcessor.from_pretrained(model_id)
    model = AutoModelForVision2Seq.from_pretrained(model_id, torch_dtype=torch.float16, device_map="auto")
    print("Modelo carregado com sucesso.")
except Exception as e:
    print("Erro ao carregar modelo:", e)
    model = None

def base64_to_image(image_base64):
    try:
        image_data = base64.b64decode(image_base64)
        return Image.open(io.BytesIO(image_data)).convert("RGB")
    except Exception as e:
        print("Erro ao converter imagem:", e)
        return None

def handler(event):
    try:
        prompt = event["input"].get("prompt", "")
        image_base64 = event["input"].get("image_base64", "")

        if not prompt or not image_base64:
            return {"error": "prompt ou image_base64 ausente."}

        image = base64_to_image(image_base64)
        if image is None:
            return {"error": "Erro ao converter imagem."}

        inputs = processor(prompt=prompt, images=image, return_tensors="pt").to(model.device)
        output = model.generate(**inputs, max_new_tokens=512)
        response = processor.batch_decode(output, skip_special_tokens=True)[0]

        return {"response": response}
    except Exception as e:
        return {"error": str(e)}
