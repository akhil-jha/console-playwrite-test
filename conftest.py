from dataclasses import dataclass

import pytest
from dynaconf import Dynaconf

settings = Dynaconf(
    settings_files=["conf/settings.yaml"],
    environments=True,
    envvar_prefix="DYNACONF",
    load_dotenv=True,
)


@dataclass
class Config:
    base_url: str = settings.base_url
    username: str = settings.username
    password: str = settings.password
    headless: bool = settings.headless


@pytest.fixture(scope="session")
def config() -> Config:
    return Config()
