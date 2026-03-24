from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "Painel Whatsapp"
    secret_key: str = "1234567890"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 60
    database_url: str = "sqlite:///database.db"
    wasender_api_key: str = "1234567890"
    wasender_api_url: str = "https://api.wasender.com.br"

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings() 
