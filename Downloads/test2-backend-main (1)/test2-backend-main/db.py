import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Docker Compose 환경변수 사용
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    # "mysql+pymysql://root:1234@43.201.8.142:3306/sjw2?charset=utf8mb4"
      "mysql+pymysql://root:1234@localhost:3306/sjw2?charset=utf8mb4"
)

# SQLAlchemy 엔진 생성
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,  # MySQL 연결 유지
    echo=False           # 쿼리 로그 필요하면 True
)

# 세션 생성
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base 클래스
Base = declarative_base()

# ✅ Dependency 용 함수 (FastAPI에서 Session 주입 가능)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
