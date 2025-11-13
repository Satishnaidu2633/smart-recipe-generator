from transformers import CLIPProcessor, CLIPModel
from PIL import Image
import torch

def recognize_ingredients(image):
    model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
    processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

    labels = ["tomato", "onion", "cheese", "chicken", "rice", "egg", "bread", "apple", "paneer", "capsicum", "carrot", "potato", "lemon", "broccoli"]
    inputs = processor(text=labels, images=image, return_tensors="pt", padding=True)
    outputs = model(**inputs)
    probs = outputs.logits_per_image.softmax(dim=1)
    top_idx = torch.topk(probs, 5).indices[0].tolist()
    return [labels[i] for i in top_idx]
