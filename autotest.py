import unittest
from random import randint
import os
import sys

from main import serialize, deserialize

class SerisalizeTestCase(unittest.TestCase):
    numbers_test_amounts = [50, 100, 500, 1000]
    numbers_test_sizes = [(1, 9), (10,99), (100, 999)]
    # функция, которая проверит, как формируется приветствие
    def test_volume(self):
        print("_"*40)
        print("Volume test")
        amounts = SerisalizeTestCase.numbers_test_amounts
        sizes = SerisalizeTestCase.numbers_test_sizes
        test_path_file = r".\data.txt"
        for amount in amounts:
            for size in sizes:
                to_serialize = [randint(*size) for _ in range(amount)]
                with self.subTest():
                    print('_'*40)
                    print(f"Numbers amount = {size}, size = {len(str(size[0]))} digits")
                    serialize(to_serialize, test_path_file)
                    list_size = sum([sys.getsizeof(i) for i in to_serialize])+sys.getsizeof(to_serialize)
                    file_size = os.stat(test_path_file).st_size
                    print(f"File size = {file_size}, list size = {list_size}")
                    self.assertGreater(list_size, file_size*2)
    def test_correct_deserializion(self):
        print("_"*40)
        print("Correct deserializion test")
        amounts = SerisalizeTestCase.numbers_test_amounts
        sizes = SerisalizeTestCase.numbers_test_sizes
        test_path_file = r".\data.txt"
        for amount in amounts:
            for size in sizes:
                to_serialize = [randint(*size) for _ in range(amount)]
                with self.subTest(msg=f"Numbers amount = {size}, size = {len(str(size[0]))} digits"):
                    print('_'*40)
                    print(f"Numbers amount = {size}, size = {len(str(size[0]))} digits")
                    serialize(to_serialize, test_path_file)
                    deserialized = deserialize(path=test_path_file)
                    self.assertEqual(deserialized, to_serialize)

# запускаем тестирование
if __name__ == '__main__':
    unittest.main() 