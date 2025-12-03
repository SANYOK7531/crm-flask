# app/core/config.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    azure_sql_dsn: str  # mssql+pyodbc://user:pass@server.database.windows.net:1433/db?driver=ODBC+Driver+18+for+SQL+Server
    jwt_secret: str
    jwt_algorithm: str = "HS256"

    model_config = {"env_file": ".env"}

settings = Settings()
