# Задание для Laboratory of system technologies

## Как использовать

Можно запустить юнит-тесты с помощью интерпретатора python.exe файл autotest.py для проверки работы серилализации и десириализации на предмет:
 - корректность результатов процесса
 - уменьшение объема данных на не менее 50% от исходного


оба теста запускаются сразу.

Или использовать модуль serializer в своем проекте:

    - функция to_symbolic(number: int, min_length = 0) -> str 
    Переводит число в систему счисления с основанием 94(кол-во печатных символов в ASCII) и использует символы ASCII для записи в str, возвращая постренную строку, переданной длины (добавляя незначующие нули в начале), если она была передана.

    - функция to_int(symbolic: str) -> int
    Обратно преобразует число зашифрованное ASCII в число.

    - функция serialize(l:list[int], path=None) -> str
    Сериализует список чисел в строку, указав первым символом длину последовательности символов представляющую собой число из этого списка. Сериализованную строку печатает в файл, если путь указан. Возвращает  сериализованную строку.

    - функция deserialize(serialized: str=None, path=None) -> list[int]
    Десериализует список чисел из строки полученной в качестве аргумента или из файла по пути. В случае одновременного использования обоих вариантов использует последний.