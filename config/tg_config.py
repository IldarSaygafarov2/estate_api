from environs import Env
from dataclasses import dataclass


@dataclass
class TgConfig:
    token: str
    channel_username: str

    @property
    def send_message_endpoint(self):
        return f"https://api.telegram.org/bot{self.token}/sendMessage"

    @staticmethod
    def from_env(env: Env) -> "TgConfig":
        return TgConfig(
            token=env.str("BOT_TOKEN"),
            channel_username=env.str("CHANNEL_USERNAME"),
        )
