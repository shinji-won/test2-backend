import torch
from torchvision import models, transforms
from torchvision.models import ResNet18_Weights
from PIL import Image
import requests

device = "cuda" if torch.cuda.is_available() else "cpu"

# 사전 학습된 ResNet18 모델 로드 (최신 방식)
model = models.resnet18(weights=ResNet18_Weights.IMAGENET1K_V1)
model.eval().to(device)

# ImageNet 클래스 이름 불러오기
LABELS_URL = "https://raw.githubusercontent.com/pytorch/hub/master/imagenet_classes.txt"
imagenet_classes = requests.get(LABELS_URL).text.strip().split("\n")

# 이미지 전처리
transform = transforms.Compose(
    [
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ]
)


def predict_image(image_path: str):
    image = Image.open(image_path).convert("RGB")
    img_t = transform(image).unsqueeze(0).to(device)
    with torch.no_grad():
        outputs = model(img_t)
        probs = torch.nn.functional.softmax(outputs, dim=1)[0]
        top_prob, top_class = probs.topk(1)
        return imagenet_classes[top_class.item()], top_prob.item()
