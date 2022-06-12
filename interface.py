
import control

print('Вас приветствует телефонный справочник ')
power_on = True
func_select = control.function_select()
while power_on:
    if func_select == 1:
        get_data = control.get_card()
        if get_data == 1:
            while True:
                search_select = control.search_select()
        # elif get_data == 2:
        #     while True:
        #         search_select = control.search_select()
        # elif get_data == 3:          
    else:
        print('Спасибо, что пользуетесь нашим приложением. До свидания ')
        print()
        power_on = False


def search_select():
    search_select = int(input('Выберите режим поиска:\
    1. Поиск по имени\
    2. Поиск по номеру телефона'))
    return search_select

def get_card():
    get_data = int(input('Найти номер телефона или карточку абонента?\
        1. Номер телефона\
        2. Карточку абонента '))
    return get_data

