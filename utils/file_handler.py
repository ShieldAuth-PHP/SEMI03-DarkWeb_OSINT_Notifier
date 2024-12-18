import os
import time


def create_directory_if_not_exists(directory):
    """지정된 디렉토리가 없으면 생성."""
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Directory created: {directory}")


def save_screenshot(driver, directory="./logs/darkweb"):
    """스크린샷을 저장하고 파일 경로를 반환."""
    create_directory_if_not_exists(directory)
    timestamp = int(time.time())
    file_path = os.path.join(directory, f"screenshot_{timestamp}.png")
    driver.save_screenshot(file_path)
    print(f"Screenshot saved to: {file_path}")
    return file_path


def delete_file(file_path):
    """지정된 파일을 삭제."""
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"File deleted: {file_path}")
    else:
        print(f"File not found: {file_path}")
