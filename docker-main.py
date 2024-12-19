import os
import requests
from dotenv import load_dotenv
from fetcher.darkweb_fetcher import fetch_darkweb_data
from utils.logger import setup_logger

# Tor 프록시 환경 변수 설정
TOR_PROXY = os.getenv("TOR_PROXY", "socks5h://127.0.0.1:9050")


def fetch_darkweb_data(url):
    try:
        # Tor 프록시 설정
        proxies = {
            "http": TOR_PROXY,
            "https": TOR_PROXY
        }
        print(f"Fetching data from {url} using Tor proxy {TOR_PROXY}...")
        
        # .onion URL 요청
        response = requests.get(url, proxies=proxies, timeout=30)
        response.raise_for_status()  # HTTP 에러 발생 시 예외 발생
        
        print(f"Response received: {response.status_code}")
        return response.text
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None


def main():
    # 환경 변수 로드
    load_dotenv()

    # 로거 설정
    logger = setup_logger()

    # 환경 변수에서 URL 가져오기
    url = os.getenv("DARKWEB_URL")
    if not url:
        logger.error("DARKWEB_URL is not set in the environment variables.")
        return

    try:
        logger.info(f"Starting darkweb data fetch for URL: {url}")
        data = fetch_darkweb_data(url)
        if data:
            logger.info(f"Fetched data: {data[:200]}")  # 첫 200자 출력
        else:
            logger.error("Failed to fetch data.")
    except Exception as e:
        logger.error(f"Error occurred: {e}")


if __name__ == "__main__":
    main()

