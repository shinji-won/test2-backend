# Dockerfile.backend (ModuleNotFoundError 해결)
FROM python:3.10-slim

# 작업 디렉토리
WORKDIR /app

# 시스템 의존성(컴파일 필요 패키지)
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    gcc g++ libgl1 libglib2.0-0 ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# pip 업그레이드
RUN pip install --upgrade pip

# FastAPI 등 경량 의존성 설치
# FastAPI & 기타 의존성 설치
RUN pip install --no-cache-dir --prefer-binary \
    fastapi uvicorn sqlalchemy pymysql pillow python-multipart requests cryptography

# PyTorch CPU 전용 wheel 설치
RUN pip install --no-cache-dir torch torchvision --index-url https://download.pytorch.org/whl/cpu

# backend 폴더 전체를 /app/backend로 복사
COPY ./ ./

# 실행 (backend.main 모듈로 uvicorn 실행)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]