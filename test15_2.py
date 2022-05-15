from random import randint

a = 100

def input_random_integer(n=100):
    global a
    a = randint(1, n)

print('Добро пожаловать в числовую угадайку')

def is_valid(num, n):
    return str(num).isdigit() and 0 < int(num) <= int(n)

def play_game(n):
    flag = True
    count = 0

    while flag:
        print(f'Введите число от 1 до {n}:')
        number = input()
        verify = is_valid(number, n)
        count += 1
        if verify == False:
            print(f'А может быть все-таки введем целое число от 1 до {n}?')
            continue
        else:
            number = int(number)
            if number < a:
                print('Ваше число меньше заданного, попробуйте еще разок')
            elif number > a:
                print('Ваше число больше заданного, попробуйте еще разок')
            elif number == a:
                print('Вы угадали, поздравляем!')
                print('Число попыток:', count)
                flag = False

again = True
while again:
    print('Хотите задать правую границу числа? если да, то введите число больше 1 или нет (по умолчанию будет загадано число от 1 до 100):')
    right = input()
    if str(right).isdigit() and int(right) > 1:
        input_random_integer(int(right))
    else:
        right = 100
    print('Число загадано. Игра началась')
    play_game(right)
    print('Начать заного? да или нет:')
    answer = input()
    if answer.lower() != 'да':
        again = False

print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
