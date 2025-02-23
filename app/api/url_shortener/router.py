from fastapi import APIRouter

from logger import CustomLogger

router = APIRouter(prefix="/", tags=["url shortener"])
LOGGER = CustomLogger(module_name=__name__).get_logger()
