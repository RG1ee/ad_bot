def cart(data) -> str:
    text = "<b>Корзина</b>\n\n"
    total_price = 0
    for i in data:
        text = text + f"{i[1]} — {i[2]}₽\n"
        total_price += int(i[2])
    text = text + f"\n<b>Итоговая цена: {str(total_price)}₽</b>"
    return text
