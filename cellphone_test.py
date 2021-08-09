# Эта программа тестирует класс CellPhone
# и консервирует(сериализует) объекты CellPhone.

import pickle
import cellphone

# Константа для имени файла.
FILENAME = 'cellphones.dat'


def main():
    # Инициализировать переменную для управления циклом.
    again = 'д'

    # Открыть файл для записи.
    output_file = open(FILENAME, 'wb')

    # Получить данные от пользователя.
    while again == 'д':
        # Получить данные о телефоне.
        man = input('Введите производителя: ')
        mod = input('Введите номер модели: ')
        retail = float(input('Введите розничную цену: '))

        # Создать экземпляр класса CellPhone.
        phone = cellphone.CellPhone(man, mod, retail)

        # Показать введённые данные.

        print('Вот введённые Вами данные:')
        print('Призводитель телефона: ', phone.get_manufact())
        print('Модель телефона: ', phone.get_model())
        print('Розничная цена: ', format(phone.get_retail_price(), '.2f'), sep='')

        # Закончервировать объект и записать его в файл.
        pickle.dump(phone, output_file)

        # Получить ещё один элемент данных?
        again = input('Введите "д", если хотите добавить ещё: ')
    # Закрыть файл.
    output_file.close()


main()
