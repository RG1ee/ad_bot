page = 0


def return_page() -> int:
    return page


def addiction_page() -> None:
    global page
    page += 1
    return


def subtraction_page() -> None:
    global page
    page -= 1
    return


def default_page() -> None:
    global page
    page = 0
    return


help_information = [
    """
<b>Введение</b>

Здравствуйте, я чат-бот для размещения рекламных анкет в телеграм каналах
Я помогу Вам правильно составить анкету, помогу с выбором каналов для размещения, оплатой и отправкой на модерацию.
Далее все просто, Вы сможете увидеть объявление размещенным.
Далее я рекомендую подробно изучить инструкцию по правильной работе со мной.

<b>Страница 1 из 3</b>
    """,
    """
<b>Профиль</b>

В пункте меню "Профиль" Вы сможете посмотреть сохранённые анкеты, перейти в корзину и оплатить выбранные услуги.

<b>Страница 2 из 3</b>
    """,
    """
<b>Анкета</b>

На этой странице Вы узнаете про анкеты:
Для одного профиля Вы можете создать и только одну анкету, далее она будет перезаписываться

При формировании анкеты, в таких пунктах, как Обязанности, Требования и Условия работы
для форматирования используйте перенос строки:
<u>К примеру:</u>

<i>Обязанность 1
Обязанность 2
Обязанность 3</i>

<u>Изменятся в:</u>

<i>— Обязанность 1
— Обязанность 2
— Обязанность 3</i>

Внимательно проверьте, чтобы Ваша анкета имела соответствующий вид, не содержала ненормативной лексики.
Это необходимо для того, чтобы все рекламные сообщения имели общий вид.
Если Вы допустите ошибки при формировании анкеты, то модератор отправит её обратно на исправление ошибок.

<b>Страница 3 из 3</b>
    """
]
