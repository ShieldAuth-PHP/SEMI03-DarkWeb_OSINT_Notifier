import logging
import os


def setup_logger(log_file="./logs/app.log"):
    """로거를 설정하고 반환."""
    # 디렉토리 생성
    log_dir = os.path.dirname(log_file)
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
        print(f"Log directory created: {log_dir}")

    # 로깅 설정
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(log_file),  # 파일로 로그 저장
            logging.StreamHandler()        # 콘솔에 로그 출력
        ]
    )
    logger = logging.getLogger()
    return logger
