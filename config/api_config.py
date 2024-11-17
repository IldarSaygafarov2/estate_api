from environs import Env
from dataclasses import dataclass, field


@dataclass
class RunConfig:
    api_host: str
    api_port: int

    @staticmethod
    def from_env(env: Env):
        return RunConfig(
            api_host=env.str("API_HOST"),
            api_port=env.int("API_PORT")
        )


@dataclass
class ApiV1Prefix:
    prefix: str = "/v1"
    balconies: str = '/balconies'
    conditions: str = '/conditions'
    districts: str = '/districts'
    floors: str = '/floors'
    rooms: str = '/rooms'
    storeys: str = '/storeys'
    types: str = '/types'
    estates: str = '/estates'


@dataclass
class ApiPrefix:
    prefix: str = "/api"
    v1: ApiV1Prefix = field(default_factory=ApiV1Prefix)