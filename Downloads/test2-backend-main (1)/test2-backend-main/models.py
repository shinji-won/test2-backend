from sqlalchemy import Column, Integer, String, Float, DateTime, func
from db import Base


class Prediction(Base):
    __tablename__ = "predictions"
    id = Column(Integer, primary_key=True, index=True)
    image_path = Column(String(255), nullable=False)
    predicted_label = Column(String(100), nullable=False)
    confidence = Column(Float, nullable=False)
    created_at = Column(DateTime, default=func.now())
