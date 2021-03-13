from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "Youtube DL"
    BACKEND_CORS_ORIGINS: list = ["*"]
    UPLOAD_FOLDER: str

    class Config:
        env_file = ".env"


settings = Settings()
