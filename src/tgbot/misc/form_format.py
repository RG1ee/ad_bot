def format(data):
    FORM = f"""
    <b>{data['company_name']}</b>
<i>{data['company_discription']}</i>

<b>Обязанности:</b>
{data['responsibilities']}

<b>Требования:</b>
{data['requirements']}

<b>Условия работы:</b>
{data['terms']}

<b>Откликнуться:</b> {data['contact_link']}
    """
    return FORM
