FROM --platform=linux/arm64 ubuntu:20.04

# 자동으로 타임존 설정하기 위한 환경변수 추가
ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Asia/Seoul

# 기본 의존성 설치
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    unzip \
    python3 \
    python3-pip \
    xvfb \
    chromium-browser=114.0.5735.90 \
    chromium-chromedriver=114.0.5735.90 \
    tzdata \
    && apt-get clean

# 환경 변수 설정
ENV DISPLAY=:99
ENV CHROME_BIN=/usr/bin/chromium-browser
ENV CHROMEDRIVER_PATH=/usr/bin/chromedriver

WORKDIR /app
COPY . .
RUN pip3 install --no-cache-dir -r requirements.txt

ENTRYPOINT ["sh", "-c", "Xvfb :99 -screen 0 1920x1080x24 & python3 main.py"]