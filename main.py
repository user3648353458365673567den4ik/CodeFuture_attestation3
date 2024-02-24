import numpy as np


class Generator:  # создаем класс-генератор
    def __init__(self, size_x: int, size_y: int):
        """
        Магический метод init
        Parameters
        ----------
        size_x: Длинна одного массива
        size_y  Количество массивов
        """
        self.generated_list = np.random.rand(size_y, size_x)

    def return_sorted(self, reverse: bool = False):  # создаем метод для сортировки сгененированного массива
        """
        Метод сортировки массивов
        Parameters
        ----------
        reverse
        Если True, массив сортируется в обратную сторону. По умолчанию False
        Returns
        -------
        Массив numpy
        """
        return np.sort(self.generated_list) if reverse else np.sort(self.generated_list, -1)


def main():  # создаем главную функцию для выаполнения кода
    generator = Generator(4, 5)

    print(f'Созданный массив: {generator.generated_list}')
    print(f'Отсортированный массив: {generator.return_sorted()}')
    print(f'Отсортированный в обратную сторону массив: {generator.return_sorted(reverse=True)}')

    
if __name__ == '__main__':  # если файл запущен как главный, запускаем программу
    main()
