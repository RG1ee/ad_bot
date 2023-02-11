from tgbot.database.db_sqlite import DataBaseHelper


def format_from_db(user_id: int) -> str:
    db = DataBaseHelper()
    try:
        data = db.select_form(user_id)[0]
    except Exception:
        TEXT = "\nВы ещё не заполнили анкету\n"
        return TEXT
    TEXT = f"""
```
<b>{data[1]}</b>

<i>{data[2]}</i>

<b>Обязанности:</b>
— {data[3]}

<b>Требования:</b>
— {data[4]}

<b>Условия работы:</b>
— {data[5]}

<b>Откликнуться:</b> {data[6]}
```
    """
    return TEXT
