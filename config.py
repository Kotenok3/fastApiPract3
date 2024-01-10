from dotenv import load_dotenv
import os


class Settings:
    POSTGRES_DATABASE_URL: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: str
    POSTGRES_DB: str = 'fastApiPractic3'


load_dotenv()

settings = Settings()
settings.POSTGRES_PORT = os.environ.get('POSTGRES_PORT')
settings.POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD')
settings.POSTGRES_USER = os.environ.get('POSTGRES_USER')
settings.POSTGRES_HOST = os.environ.get('POSTGRES_HOST')
settings.POSTGRES_DATABASE_URL = f"postgresql+asyncpg:" \
                                  f"//{settings.POSTGRES_USER}:" \
                                  f"{settings.POSTGRES_PASSWORD}" \
                                  f"@{settings.POSTGRES_HOST}:" \
                                  f"{settings.POSTGRES_PORT}" \
                                  f"/{settings.POSTGRES_DB}"

