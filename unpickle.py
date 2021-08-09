# Эта программа расконсервирует законсервированные в
# программе cellphone_test.py данные.

import cellphone
import pickle

# Константа для имени файла.
FILENAME = 'cellphones.dat'


def main():
    # Для обозначения конца файла.
    end_of_file = False

    # Открыть файл для чтения.
    input_file = open(FILENAME, 'rb')

    # Прочитать файл до конца.
    while not end_of_file:
        try:
            # Расконсервировать следующий объект.
            phone = pickle.load(input_file)

            # Показать данные о телефоне.
            display_data(phone)
        except EOFError:
            # Установить флаг, чтобы обозначить, что
            # был достигнут конец файла.
            end_of_file = True

    # Закрыть файл.
    input_file.close()


# Функция display_data показывает данные
# из объекта CellPhone, переданнoго в качестве аргумента.
def display_data(phone):
    print('Производитель: ', phone.get_manufact())
    print('Номер модели: ', phone.get_model())
    print('Розничная цена: ', format(phone.get_retail_price(), '.2f'), sep='')
    print('-' * 25)


main()
