from getpass import getpass
from hashlib import sha224

def mkusr():
    user = input("Имя нового пользователя: ")
    password = getpass("Пароль нового пользователя (PS: Вводимые символы отображаться не будут): ")
    with open ("system/utils/users.txt", "a") as f:
        password = sha224(bytes(password, encoding="UTF-8")).hexdigest()
        f.write(f"{user}:{password}\n")
