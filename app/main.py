"""
Application backend entry point
"""

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.responses import ORJSONResponse

from settings import (
    LOGGING_LEVEL,
    API_PREFIX,
    SERVER_HOST,
    SERVER_PORT,
    SERVER_WORKERS,
    DEBUG,
    DOCS_URL,
    TITLE,
    ALLOWED_HEADERS,
    ALLOWED_METHODS,
    API_RESPONSE_CHUNK,
)
from logger import CustomLogger
from app import routers_list

app = FastAPI(
    title=TITLE,
    docs_url=DOCS_URL,
    swagger_ui_parameters={
        "defaultModelsExpandDepth": -1
    },  # Hides Schemas Menu in Docs
    default_response_class=ORJSONResponse,
)


logger = CustomLogger(__name__, LOGGING_LEVEL.upper())

# Middlewares
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=ALLOWED_METHODS,
    allow_headers=ALLOWED_HEADERS,
)
app.add_middleware(
    GZipMiddleware,
    minimum_size=API_RESPONSE_CHUNK,  # Minimum size of the response before it is compressed in bytes
)


for route in routers_list:
    app.include_router(route, prefix=API_PREFIX)


# Health Check
@app.get("/_health", status_code=200, include_in_schema=False)
async def health_check() -> ORJSONResponse:
    """This is the health check endpoint"""
    return ORJSONResponse([{"status": "ok"}])


if __name__ == "__main__":
    logger.app_logger.info(f"running application with {SERVER_WORKERS} workers")
    uvicorn.run(
        app="app.main:app",
        host=SERVER_HOST,
        port=SERVER_PORT,
        reload=DEBUG,
        workers=SERVER_WORKERS,
    )
