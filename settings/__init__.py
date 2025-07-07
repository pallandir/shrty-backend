from decouple import config

TITLE: str = "Shrty"
VERSION: str = "0.0.1"
TIMEZONE: str = "UTC"
DESCRIPTION: str | None = None
DEBUG: bool = True

SERVER_HOST: str = config("HOST", default="0.0.0.0", cast=str)
SERVER_PORT: int = config("PORT", default=8090, cast=int) 
ENVIRONMENT: str = config("ENVIRONMENT", default="dev")
SERVER_WORKERS: int = config("SERVER_WORKERS", default=1, cast=int) 
API_PREFIX: str = "/api/v1"
DOCS_URL: str = f"{API_PREFIX}/docs"
OPENAPI_URL: str = f"{API_PREFIX}/openapi.json"
REDOC_URL: str = f"{API_PREFIX}/redoc"
OPENAPI_PREFIX: str = ""
API_RESPONSE_CHUNK = 5000

DATABASE_URL: str = config("DB_URL", default="")
ALLOWED_ORIGINS: list[str] = [
    "http://localhost:3000",
    "http://0.0.0.0:3000",
    "http://127.0.0.1:3000",
    "http://127.0.0.1:3001",
    "http://localhost:5173",
    "http://0.0.0.0:5173",
    "http://127.0.0.1:5173",
    "http://127.0.0.1:5174",
]
ALLOWED_METHODS: list[str] = ["*"]
ALLOWED_HEADERS: list[str] = ["*"]

LOGGING_LEVEL: str = config("LOG_LEVEL", default="INFO", cast=str)
LOGGERS: tuple[str, str] = ("uvicorn.asgi", "uvicorn.access")
