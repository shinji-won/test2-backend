import os
from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session
from db import SessionLocal
from models import Prediction
from ai_model import predict_image

router = APIRouter(prefix="/predict", tags=["Prediction"])

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
async def predict(file: UploadFile = File(...), db: Session = Depends(get_db)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as f:
        f.write(await file.read())

    label, confidence = predict_image(file_path)

    record = Prediction(image_path=file_path, predicted_label=label, confidence=confidence)
    db.add(record)
    db.commit()
    db.refresh(record)

    return {"label": label, "confidence": confidence, "image_path": file_path}
