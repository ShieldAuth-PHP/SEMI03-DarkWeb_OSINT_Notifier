import os

from dotenv import load_dotenv

from fetcher.darkweb_fetcher import fetch_darkweb_data
from utils.logger import setup_logger


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
        darkweb_data = fetch_darkweb_data(url)
        if darkweb_data:
            logger.info(f"Darkweb data fetched successfully: {darkweb_data}")
        else:
            logger.error("Failed to fetch darkweb data.")
    except Exception as e:
        logger.error(f"Error occurred: {e}")

if __name__ == "__main__":
    main()