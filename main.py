from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from db import engine, SessionLocal
from models import Base
from routers import predict
from sqlalchemy import text


# DB 테이블 생성
Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI Image Classifier API")

origins = [
    "http://localhost:3000",       
    "https://d3s00e84xvu6qq.cloudfront.net"
]

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 라우터 등록
app.include_router(predict.router)


@app.get("/")
def root():
    return {"message": "EKS 자동 배포 완전 성공!!!!--!!"}


@app.get("/health", status_code=status.HTTP_200_OK, tags=["Health"])
def health_check():
    """
    ALB 헬스체크용 기본 엔드포인트
    단순히 서버가 살아있는지 확인
    """
    return {"status": "healthy", "service": "AI Image Classifier API"}
