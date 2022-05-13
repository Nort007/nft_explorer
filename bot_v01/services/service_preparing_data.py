def preparing_callback_data(callback):
    """Подготавливает данные для ответов в собранный вид
    Поскольку колбек данные поставляются в виде a:b:c:d,
    разделяем методом сплита
    """
    callback_to_list = callback.split(':')
