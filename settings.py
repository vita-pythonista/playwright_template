from pydantic import BaseSettings, HttpUrl
from pathlib import Path

BASE_DIR = Path(__file__).parent


class Settings(BaseSettings):

    # in the future you can add env-variables using dotenv

    TIMEOUT_WAITNG_ELEMENT: int = 30 * 1000
    # SCREEN_RESOLUTION_WIDTH: int = 1920
    # SCREEN_RESOLUTION_HEIGHT: int = 1080
    BASE_URL: HttpUrl = 'https://python.org'


settings = Settings()