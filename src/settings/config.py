from settings import const
from settings.data import Config, TgBot


def load_config() -> Config:
    return Config(
        tg_bot=TgBot(
            token=const.TOKEN,
            admin_ids=const.ADMIN_IDS
        )
    )
