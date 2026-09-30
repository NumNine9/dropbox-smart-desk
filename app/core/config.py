from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    dropbox_app_key: str
    dropbox_app_secret: str
    dropbox_redirect_uri: str
    session_secret: str

    class Config:
        env_file = ".env"


settings = Settings()