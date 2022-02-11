import random

def game_start(a=10):
    n = random.randint(1, a)
    try:
        while True:
            i = input('数字を入力 => ')
            if (n == int(i)):
                print('正解')
                break
            else:
                print('ハズレね')
    except:
        print('数字を入力せい！')
        game_start(a)
        