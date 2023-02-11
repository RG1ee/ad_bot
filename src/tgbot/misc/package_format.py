from tgbot.database.db_sqlite import DataBaseHelper


def package_information_format(package) -> str:
    db = DataBaseHelper()
    data = db.select_package_with_key(package)
    TEXT = \
        f"""
<b>{data[0][0]}</b>
<i>{data[0][1]}</i>
<b>Цена публикации пакета: {str(data[0][2])}₽</b>
"""
    return TEXT