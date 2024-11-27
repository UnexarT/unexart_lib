from unexart_lib import *
import pytest

def test_sort_correct_data():
    data = [64, 34, 25, 12, 22, 11, 90]
    sorter = bubblesort(data)
    assert sorter.sort() == [11, 12, 22, 25, 34, 64, 90]

def test_sort_empty_list():
    data = []
    sorter = bubblesort(data)
    assert sorter.sort() == []

def test_sort_single_element():
    data = [1]
    sorter = bubblesort(data)
    assert sorter.sort() == [1]

def test_sort_already_sorted():
    data = [1, 2, 3, 4, 5]
    sorter = bubblesort(data)
    assert sorter.sort() == [1, 2, 3, 4, 5]

def test_sort_reverse_sorted():
    data = [5, 4, 3, 2, 1]
    sorter = bubblesort(data)
    assert sorter.sort() == [1, 2, 3, 4, 5]

def test_sort_invalid_data():
    data = [1, 'two', 3]
    sorter = bubblesort(data)
    with pytest.raises(TypeError, match="Ошибка: данные должны быть числовыми."):
        sorter.sort()

def test_validate_data_valid():
    data = [1, 2, 3.5]
    sorter = bubblesort(data)
    assert sorter.validate_data() == True

def test_validate_data_invalid():
    data = [1, 'two', 3]
    sorter = bubblesort(data)
    assert sorter.validate_data() == False

def test_addition():
    calc = calculator(1, '+', 2)
    assert calc.do() == 3

def test_subtraction():
    calc = calculator(5, '-', 3)
    assert calc.do() == 2

def test_multiplication():
    calc = calculator(4, '*', 2)
    assert calc.do() == 8

def test_division():
    calc = calculator(10, '/', 2)
    assert calc.do() == 5

def test_division_by_zero():
    calc = calculator(10, '/', 0)
    with pytest.raises(ZeroDivisionError, match="Ошибка: деление на ноль"):
        calc.do()

def test_invalid_operator():
    calc = calculator(10, '^', 2)
    with pytest.raises(ValueError, match="Ошибка: недопустимый оператор"):
        calc.do()

def test_invalid_data():
    calc = calculator(10, '+', 'two')
    with pytest.raises(TypeError, match="Ошибка: данные должны быть числовыми."):
        calc.do()

def test_validate_data_valid():
    calc = calculator(1, '+', 2)
    assert calc.validate_data() == True

def test_validate_data_invalid():
    calc = calculator(1, '+', 'two')
    assert calc.validate_data() == False

def test_fibonacci_correct_length():
    fib = fibonacci(5)
    assert fib.make() == [0, 1, 1, 2, 3]

def test_fibonacci_length_one():
    fib = fibonacci(1)
    assert fib.make() == [0]

def test_fibonacci_invalid_length_string():
    with pytest.raises(TypeError, match="Ошибка: задаваемая длинна должна быть целым числом."):
        fib = fibonacci("five")
        fib.make()

def test_fibonacci_invalid_length_float():
    with pytest.raises(TypeError, match="Ошибка: задаваемая длинна должна быть целым числом."):
        fib = fibonacci(5.5)
        fib.make()
