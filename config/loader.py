from dataclasses import dataclass
from typing import Optional

from environs import Env

from config.api_config import (
    RunConfig,
    ApiPrefix
)
from config.db_config import DbConfig


@dataclass
class Config:
    db: DbConfig
    run_api: RunConfig
    api_prefix: ApiPrefix


def load_config(path: Optional[str] = None) -> "Config":
    env = Env()
    env.read_env(path)

    db_config = DbConfig.from_env(env)
    run_api_config = RunConfig.from_env(env)
    api_prefix = ApiPrefix()

    return Config(
        db=db_config,
        run_api=run_api_config,
        api_prefix=api_prefix,
    )
