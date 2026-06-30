# AI Image Classifier API

FastAPI 기반 AI 이미지 분류 API 서비스

## 🚀 배포 자동화

GitHub Actions를 통해 ECR 이미지 빌드 및 ECS 배포가 자동으로 진행됩니다.

### 필요한 GitHub Secrets

GitHub Repository의 Settings > Secrets and variables > Actions에서 다음 시크릿을 추가하세요:

#### AWS 인증 정보
- `AWS_ACCESS_KEY_ID`: AWS 액세스 키 ID
- `AWS_SECRET_ACCESS_KEY`: AWS 시크릿 액세스 키
- `AWS_REGION`: AWS 리전 (예: `ap-northeast-2`)
- `AWS_ACCOUNT_ID`: AWS 계정 ID (12자리 숫자)

#### ECR 설정
- `ECR_REPO`: ECR 저장소 이름 (예: `my-app-repo`)

#### ECS 설정
- `ECS_CLUSTER_NAME`: ECS 클러스터 이름 (예: `my-cluster`)
- `ECS_SERVICE_NAME`: ECS 서비스 이름 (예: `my-service`)
- `ECS_TASK_DEFINITION`: ECS 태스크 정의 이름 (예: `my-task-def`)
- `ECS_CONTAINER_NAME`: 컨테이너 이름 (예: `my-container`)

### 배포 프로세스

1. `main` 브랜치에 푸시
2. GitHub Actions 자동 실행
   - Docker 이미지 빌드
   - ECR에 이미지 푸시
   - ECS 태스크 정의 업데이트
   - ECS 서비스 재배포
3. 배포 완료 대기 (자동)

## 🛠️ 로컬 개발 환경 설정

### 1. 환경 변수 설정

`.env` 파일을 생성하고 데이터베이스 연결 정보를 입력하세요:

```bash
cp .env.example .env
```

`.env` 파일 예시:
```
DATABASE_URL=mysql+pymysql://root:password@localhost:3306/database?charset=utf8mb4
```

### 2. 패키지 설치

```bash
pip install -r requirements.txt
```

### 3. 서버 실행

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## 📡 API 엔드포인트

### Health Check
- `GET /health` - ALB 헬스체크용 기본 엔드포인트
- `GET /` - 서비스 상태 확인

### Image Classification
- `POST /predict` - 이미지 분류 예측

## 🏥 헬스체크 설정 (ALB)

ALB 타겟 그룹 설정:
- **경로**: `/health`
- **성공 코드**: `200`
- **정상 임계값**: 2-3
- **비정상 임계값**: 2
- **제한 시간**: 5초
- **간격**: 30초

## 🐳 Docker

### 로컬에서 Docker 빌드 및 실행

```bash
# 이미지 빌드
docker build -t ai-classifier-api .

# 컨테이너 실행
docker run -p 8000:8000 --env-file .env ai-classifier-api
```

## 📝 기술 스택

- **FastAPI**: 웹 프레임워크
- **PyTorch**: AI 모델
- **SQLAlchemy**: ORM
- **MySQL**: 데이터베이스
- **Docker**: 컨테이너화
- **AWS ECS**: 컨테이너 오케스트레이션
- **AWS ECR**: 컨테이너 레지스트리

