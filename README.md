# Простая библиотека для учебных целей

Для того чтобы установить библиотеку и использовать в проекте необходимо ввести в терминал:

    pip install unexart_lib

## Что есть в этой библиотеке? ##

- Класс нахождения первых **n** чисел Фибоначчи
- Класс сортировки Пузырьком
- Класс простейшего калькулятора

### Последовательность Фибоначчи ###

Для нахождения первых **n** чисел последовательности необходимо создать экземпляр класса: 
	
	fib = fibonacci(n) # где n - кол-во чисел в последовательности

И применить метод нахождения последовательности:
	
	fib.make() - возвращает список из n чисел Фибоначчи

### Сортировка пузырьком ###

Для сортировки списка необходимо создать экземпляр класса: 
	
	bubble_sort = bubblesort(list) # где list - сортируемый список

И применить метод сортировки:
	
	bubble_sort.sort() - возвращает отсортированный список

### Калькулятор ###

Возможные операции:

- сумма **+**
- разность **-**
- произведение **\***
- частное **/**

Для вычислений необходимо создать экземпляр класса: 
	
	calc = calculator(num1, oper, num2) # где num1 и num2 - числа, а oper - символ операции

И применить метод вычисления ответа:
	
	calc.do() - возвращает ответ вычисления


----------


## Разработчик - UnexarT ##
	