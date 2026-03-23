from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "Painel Whatsapp"
    secret_key: str
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 60
    database_url: str
    wasender_api_key: str
    wasender_api_url: str

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings() # type: ignore
