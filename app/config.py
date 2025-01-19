from pydantic import BaseSettings


class Config(BaseSettings):
    HOST: str = "0.0.0.0"
    PORT: int = 8000


config = Config()