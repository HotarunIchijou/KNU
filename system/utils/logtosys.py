from getpass import getpass
from hashlib import sha224
from time import sleep

class logintosys:
    def checkLoginInFile(login):
        with open('system/utils/users.txt', 'r') as f:
            users = f.read().splitlines()
            correct_login = False
            for user in users:
                user = user.split(':')[0]
                if user == login:
                    correct_login = True
        if correct_login:
            return True
        else:
            return False

    def checkPassword(login, password):
        with open('system/utils/users.txt', 'r') as f:
            users = f.read().splitlines()
            for user in users:
                if user.split(':')[0] == login:
                    password = sha224(bytes(password, encoding='UTF-8')).hexdigest()
                    if password == user.split(':')[1]:
                        return True
                    else:
                        return False
    while True:
        sleep(1)
        print('''Введите имя и пароль пользователя (Имя пользователя по умолчанию: admin; Пароль пользвателя по умолчанию: admin)''')
        sleep(0.3)
        login = input('Введите имя пользователя: ')
        password = getpass('Введите пароль: ')
        if checkPassword(login, password):
            sleep(0.5)
            print('Добро пожаловать в KolotovkinOS')
            sleep(0.3)
            break
        else:
            sleep(0.5)
            print('Неверный логин или пароль')
            sleep(0.3)
            continue

