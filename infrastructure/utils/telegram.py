def create_telegram_message(**kwargs):
    return f"""
{kwargs['name']}

{kwargs['description']}

Балкон: {kwargs['balcony']}
Состояние: {kwargs['condition']}
Район: {kwargs['district']}
Комнат: {kwargs['room']}
Этаж: {kwargs['floor']}
Этажность: {kwargs['storey']}
Тип: {kwargs['type']}
Цена: {kwargs['price']}
Номер риелтора: {kwargs['manager_phone']}
Номер риелтора: {kwargs['realtor_phone']}
"""
