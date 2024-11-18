from dataclasses import dataclass, field

from environs import Env


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
class AccessTokenConfig:
    token_secret: str
    algorith: str = "HS256"
    token_expire_seconds: int = 3600

    @staticmethod
    def from_env(env: Env):
        return AccessTokenConfig(
            token_secret=env.str("SECRET_KEY"),
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
    auth: str = '/auth'


@dataclass
class ApiPrefix:
    prefix: str = "/api"
    v1: ApiV1Prefix = field(default_factory=ApiV1Prefix)

    @property
    def bearer_token_url(self) -> str:
        parts = (self.prefix, self.v1.prefix, self.v1.auth, "/login")
        path = "".join(parts)
        return path.removeprefix("/")
