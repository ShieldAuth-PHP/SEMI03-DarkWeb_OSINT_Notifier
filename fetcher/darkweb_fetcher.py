import time

from core.driver_setup import setup_driver
from core.elasticsearch_handler import insert_data
from utils.file_handler import save_screenshot
from utils.logger import setup_logger


def fetch_darkweb_data(url):
    logger = setup_logger()
    driver = setup_driver()
    try:
        logger.info(f"Fetching data from {url}")
        driver.get(url)

        # 스크린샷 저장
        screenshot_path = save_screenshot(driver)
        logger.info(f"Screenshot saved at: {screenshot_path}")

        return {"url": url, "screenshot_path": screenshot_path, "timestamp": time.time()}
    except Exception as e:
        logger.error(f"Error fetching data from {url}: {e}")
        return None
    finally:
        driver.quit()
