from random import randint

number = randint(1, 7)

print('Угадайте число от 1 до 7')

while True:
    guess = int(input('Ввведите число: '))

    if guess < number:
        print('Ваше число меньше того, что загадано.')
    elif guess > number:
        print('Ваше число больше того, что загадано.')
    elif guess == number:
        break

# Test.

print('Отличная интуиция! Вы угадали число :)')