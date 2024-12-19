# Dark Web OSINT Notifier

.onion 사이트 데이터를 크롤링하고 Telegram 알림을 통해 정보를 전달하는 기능을 제공합니다. Docker를 통해 간단히 실행할 수 있습니다.

### 실행 방법
1. 레포지토리 클론

```
git clone https://github.com/ShieldAuth-PHP/SEMI03-DarkWeb_OSINT_Notifier.git
cd SEMI03-DarkWeb_OSINT_Notifier
```

2. 환경 변수 설정
.env.template를 복사하여 .env 파일 생성:

`cp .env.template .env`

.env 파일에서 아래 값을 설정합니다:

```
TELEGRAM_API_KEY=your_telegram_bot_api_key
TELEGRAM_CHAT_ID=your_telegram_chat_id
DARKWEB_URL=http://exampleonion.onion
TOR_PROXY=socks5h://127.0.0.1:9050
```

3. Docker 실행
`docker-compose up --build`

2. 주요 기능
- .onion 사이트 데이터 크롤링
- Telegram 알림 전송

3. 문제 해결
- Tor 프록시 확인:
`curl --socks5-hostname 127.0.0.1:9050 https://check.torproject.org``

- 로그 확인:
`docker logs <container_name>`

