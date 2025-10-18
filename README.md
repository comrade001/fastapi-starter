# FastAPI Starter

Backend starter project built with FastAPI, Poetry, and a full testing + linting toolchain.
Designed to showcase production-grade patterns: modular routing, async testing, middleware, and validation.

STACK & TOOLING
----------------------------------------------------------------
Framework:        FastAPI + Uvicorn
Environment:      Poetry
Linting/Format:   Ruff, Black, Mypy
Testing:          Pytest, Httpx (async client)
Quality Gates:    Pre-commit hooks, Coverage (pytest-cov)

SETUP
----------------------------------------------------------------
poetry install
poetry run pre-commit install

RUN THE API
----------------------------------------------------------------
poetry run uvicorn hello_python.api.main:app --reload --app-dir src

Docs:  http://127.0.0.1:8000/docs

Endpoints:
 - /ping             -> health check
 - /items/{id}       -> POST with payload validation
 - /users/{id}       -> returns user info
 - /orders/{id}      -> applies VAT, supports ?fail=true

TESTS & COVERAGE
----------------------------------------------------------------
poetry run pytest -q
poetry run pytest --cov=src/hello_python --cov-report=term-missing

All tests run fully in memory via httpx.ASGITransport.
Async tests validated with pytest-asyncio.

STRUCTURE
----------------------------------------------------------------
src/
  hello_python/
    api/
      main.py            -> app + routers + middleware
      users.py           -> /users routes
      orders.py          -> /orders routes
      middleware.py      -> response time header
      exceptions.py      -> custom exception handler
    models/
      user.py            -> User model + validators
tests/
  test_ping.py
  test_items.py
  test_routers.py
  test_user_validation.py
  test_middleware_exceptions.py
  test_async_endpoints.py

HIGHLIGHTS
----------------------------------------------------------------
 - Modular architecture for scalable APIs.
 - Strict validation with Pydantic v2 (field_validator, regex, enums).
 - Custom middleware adding x-process-time header.
 - Centralized exception handling (InvalidOrderException).
 - Fully async test suite (GET + POST endpoints).
 - Coverage consistently >90%.

AUTHOR
----------------------------------------------------------------
Abraham Solis Alvarez - Backend Developer
LinkedIn: https://www.linkedin.com/in/abraham-solis-alvarez
GitHub:   https://github.com/comrade001

----------------------------------------------------------------
"Clean code is not written by chance - it's enforced by tools,
validated by tests, and proven by coverage."
