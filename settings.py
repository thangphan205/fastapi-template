from pydantic import BaseSettings
import secrets


class DevSettings(BaseSettings):
    API_V1_STR: str = "/api"

    SECRET_KEY: str = secrets.token_urlsafe(32)
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 600
    SQLALCHEMY_DATABASE_URL = "./db/app_database.db"
    # Email Settings
    SMTP_USE_TLS = True
    SMTP_SERVER = ""
    SMTP_PORT_SSL = ""
    SMTP_SENDER = ""
    SMTP_PASSWORD = ""

    EMAIL_SENDER = ""
    EMAIL_SUPPORTER = ""

    LOGGING_FILE = "logs/fastapi.log"


settings = DevSettings()
