from transformers import AutoProcessor, AutoModelForVision2Seq
from PIL import Image
import base64
import io
import torch

def handler(event):
    return {"status": "online"}
