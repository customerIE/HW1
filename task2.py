from random import randint

# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу
# и на себя”. Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.


def simple_number():
    i = 2
    counter = 0
    min = 0
    max = 100000
    while True:
        number = int(input('Введите число в диапозоне от 1 до 100000: '))
        if min < number < max:
            while i <= number - 1:
                if number % i == 0:
                    counter += 1
                i += 1
            if counter >= 1:
                print('Число составное')
            else:
                print('Число простое')
            break
        else:
            print('Недопустимое значение:')

simple_number()
