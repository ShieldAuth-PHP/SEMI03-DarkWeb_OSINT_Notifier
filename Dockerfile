FROM python:3.11-slim

# 의존성 설치
RUN apt-get update && apt-get install -y \
    libssl-dev \
    libffi-dev \
    chromium \
    chromium-driver \
    tor \
    xvfb \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# 환경 변수 설정
ENV DISPLAY=:99

# 작업 디렉토리 설정
WORKDIR /app

# 프로젝트 파일 복사
COPY . .

# Python 의존성 설치
RUN pip install --no-cache-dir -r requirements.txt

# Xvfb 실행 후 Python 메인 스크립트 실행
ENTRYPOINT ["sh", "-c", "Xvfb :99 -screen 0 1024x768x16 & python main.py"]
