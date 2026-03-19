from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
  ANTHROPIC_API_KEY: str = ""
  OPENAI_API_KEY: str = ""

  model_config = SettingsConfigDict(env_file=".env")

settings = Settings()