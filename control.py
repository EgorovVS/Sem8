
def function_select():
    func_select = int(input('Выберите режим работы:\
    1. Поиск абонента или номера телефона\
    2. Редактор справочника\
    3. Выход '))
    return func_select


def search_select():
    search_select = int(input('Выберите режим поиска:\
    1. Поиск по имени\
    2. Поиск по номеру телефона\
    3. Назад '))
    return search_select

def get_card():
    get_data = int(input('Найти номер телефона или карточку абонента?\
        1. Номер телефона\
        2. Карточку абонента\
        3. Назад '))
    return get_data