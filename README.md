# SignalDesk BE

Flask RESTful backend for security event operations.

## Architecture

- Backend shape: `module`
- Database: `MariaDB`
- ORM: `Tortoise ORM`
- Runtime: Python Flask with Gunicorn/Waitress, no Node.js backend
- API style: REST only. GraphQL was deliberately removed.

## demo-backend conversion

The source idea from `cyjoon68/demo-backend` is converted from NestJS/GraphQL style auth, user, phone verification, and token hardening into Flask REST endpoints:

- `POST /api/auth/login`
- `POST /api/auth/refresh`
- `GET /api/dashboard`
- `PATCH /api/events/{event_id}/status`

## Resume bullets

- Rebuilt demo-backend authentication semantics as Flask REST with JWT refresh flow.
- Implemented module backend using MariaDB and Tortoise ORM.
- Added OpenAPI, pytest contract tests, Docker Compose, and k6 p95 smoke threshold.
