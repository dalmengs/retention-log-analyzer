# 로그 & 접속자 수 분석기
## Log & Retention Analyzer

`docker pull dalmeng/log-retention-analyzer:latest`
`docker run -d -v <YOUR VOLUME>:/usr/src/app -e DB_DIRECTORY="/usr/src/app/log.db" -p 9999:9999 dalmeng/log-retention-analyzer:latest`