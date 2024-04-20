from pydantic_settings import BaseSettings


class DBconfig(BaseSettings):
    host: str
    port: int
    user: str
    password: str
    name: str

    class Config:
        env_prefix = "DB_"

    @property
    def dsn(self):
        return f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.name}"


class Settings(BaseSettings):
    db: DBconfig


def get_settings():
    return Settings(db=DBconfig())
