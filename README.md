# SignalDesk BE

![Python](https://img.shields.io/badge/Python-3.12-3776ab?logo=python)
![Flask](https://img.shields.io/badge/Flask-REST-000000?logo=flask)
![MariaDB](https://img.shields.io/badge/MariaDB-Tortoise_ORM-003545?logo=mariadb)

보안 이벤트 운영 대시보드를 위한 Flask REST API입니다. 이벤트 조회, 상태 변경, 인증 토큰 갱신, dashboard 데이터를 제공합니다.

## 기능

- `POST /api/auth/login`
- `POST /api/auth/refresh`
- `GET /api/dashboard`
- `PATCH /api/events/{event_id}/status`
- OpenAPI 명세 제공
- k6 smoke script 제공

## 아키텍처

- 구조: module
- Framework: Flask
- ORM: Tortoise ORM
- Database: MariaDB
- Runtime: Gunicorn / Waitress

## 실행

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
pytest
```

## Docker

```bash
docker compose up --build
```

## 환경 변수

```bash
DATABASE_URL=mysql://app:app@localhost:3306/app
```

## 설계 메모

기존 GraphQL 방식 대신 REST API로 인증과 dashboard 계약을 단순화했습니다. FE는 `ky` client를 통해 같은 REST endpoint를 사용합니다.
