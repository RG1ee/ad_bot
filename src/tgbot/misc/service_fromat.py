from tgbot.database.db_sqlite import DataBaseHelper


def service_information_format(service) -> str:
    db = DataBaseHelper()
    data = db.select_service_with_key(service)
    TEXT = \
        f"""
<b>{data[0][0]}</b>

<i>{data[0][1]}</i>

{data[0][2]}
Цена публикации в канале: {str(data[0][3] // 100)}₽
"""
    return TEXT
