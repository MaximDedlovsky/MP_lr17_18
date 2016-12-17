import math
numbers = []
enter = input('Enter numbers: ').split()
for s in enter:
    numbers.append(int(s))
evens = []
squares = []
for number in numbers:
    if number % 2 == 0:
        evens.append(number)
    if math.sqrt(number) == int(math.sqrt(number)):
        squares.append(number)
evens = set(evens)
squares = set(squares)
print('Events: ')
print(evens)
print('Squares: ')
print(squares)
print('Intersection: ')
print(evens & squares)
print('Union: ')
print(evens | squares)
print('Difference: ')
print(evens - squares)
print('Symmetric difference: ')
print((evens - squares) | (squares - evens))
