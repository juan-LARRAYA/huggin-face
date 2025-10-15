from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from io import BytesIO
from PIL import Image
import base64
import numpy as np
import torch

from transformers import pipeline, CLIPProcessor, CLIPModel, AutoImageProcessor, AutoModelForImageClassification

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global variables for models
clip_model = None
clip_processor = None
vit_classifier = None
detr_detector = None

def load_pipelines():
    global clip_model, clip_processor, vit_classifier, detr_detector

    print("Loading the 3 most popular vision models from Hugging Face...")

    # 1. CLIP - Most popular multimodal model
    print("Loading CLIP (openai/clip-vit-base-patch32)...")
    clip_model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
    clip_processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

    # 2. ViT - Most popular image classifier
    print("Loading ViT (google/vit-base-patch16-224)...")
    vit_classifier = pipeline("image-classification", model="google/vit-base-patch16-224")

    # 3. DETR - Most popular object detector
    print("Loading DETR (facebook/detr-resnet-50)...")
    detr_detector = pipeline("object-detection", model="facebook/detr-resnet-50")

    print("All models loaded successfully!")
    return True

# Load models on startup
load_pipelines()


def read_imagefile(file) -> Image.Image:
    img = Image.open(BytesIO(file)).convert("RGB")
    return img


@app.get("/")
async def root():
    return {"message": "HF Vision Demo API - 3 Most Popular Vision Models",
            "models": ["CLIP (openai/clip-vit-base-patch32)",
                      "ViT (google/vit-base-patch16-224)",
                      "DETR (facebook/detr-resnet-50)"]}


@app.post("/classify")
async def classify(file: UploadFile = File(...)):
    """Image classification using ViT (Vision Transformer)"""
    data = await file.read()
    img = read_imagefile(data)
    results = vit_classifier(img)
    return {"model": "ViT (google/vit-base-patch16-224)", "results": results}


@app.post("/clip")
async def clip_classify(file: UploadFile = File(...)):
    """Zero-shot classification using CLIP with custom text prompts"""
    data = await file.read()
    img = read_imagefile(data)

    # Common categories for demonstration
    text_prompts = [
        "a photo of a person", "a photo of an animal", "a photo of a car",
        "a photo of food", "a photo of a building", "a photo of nature",
        "a photo of technology", "a photo of furniture", "a photo of clothing"
    ]

    inputs = clip_processor(text=text_prompts, images=img, return_tensors="pt", padding=True)

    with torch.no_grad():
        outputs = clip_model(**inputs)
        logits_per_image = outputs.logits_per_image
        probs = logits_per_image.softmax(dim=1)

    results = []
    for i, prompt in enumerate(text_prompts):
        results.append({
            "label": prompt.replace("a photo of ", ""),
            "score": float(probs[0][i])
        })

    # Sort by score
    results = sorted(results, key=lambda x: x["score"], reverse=True)

    return {"model": "CLIP (openai/clip-vit-base-patch32)", "results": results}


@app.post("/detect")
async def detect(file: UploadFile = File(...)):
    """Object detection using DETR"""
    data = await file.read()
    img = read_imagefile(data)
    results = detr_detector(img)
    return {"model": "DETR (facebook/detr-resnet-50)", "results": results}


@app.post("/clip-custom")
async def clip_custom(file: UploadFile = File(...), prompts: str = ""):
    """CLIP classification with custom text prompts (comma-separated)"""
    data = await file.read()
    img = read_imagefile(data)

    if not prompts:
        return {"error": "Please provide comma-separated text prompts"}

    text_prompts = [prompt.strip() for prompt in prompts.split(",")]

    inputs = clip_processor(text=text_prompts, images=img, return_tensors="pt", padding=True)

    with torch.no_grad():
        outputs = clip_model(**inputs)
        logits_per_image = outputs.logits_per_image
        probs = logits_per_image.softmax(dim=1)

    results = []
    for i, prompt in enumerate(text_prompts):
        results.append({
            "label": prompt,
            "score": float(probs[0][i])
        })

    # Sort by score
    results = sorted(results, key=lambda x: x["score"], reverse=True)

    return {"model": "CLIP (openai/clip-vit-base-patch32)", "results": results}
