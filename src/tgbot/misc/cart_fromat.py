def cart(data) -> str:
    text = "<b>Корзина</b>\n\n"
    total_price = 0
    for i in data:
        text = text + f"{i[2]} — {i[3]}₽\n"
        total_price += int(i[3])
    text = text + f"\n<b>Итоговая цена: {str(total_price)}₽</b>"
    return text
