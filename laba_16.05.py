#1
class InvalidUsernameError(Exception):
    def __init__(self, username):
        self.username = username

class InvalidCharacterError(Exception):
    def __init__(self, character):
        self.character = character
#InvalidWordError
#DublicateUsernameError

def register_user(username):
    if len(username) < 5:
        raise InvalidUsernameError(username)
    elif '@' or ' ' or '!' or '&' or '*' in username:
        raise InvalidCharacterError(username)
    else:
        print('Вас зареєстровано!')
try:
    username = input("Введіть ім'я: ")
    register_user(username)
except InvalidUsernameError as e:
    print(f"Неправильне ім'я '{e.username}', мін 5 символів")
except InvalidCharacterError as e1:
    print(f"Неправильне ім'я '{e1.character}', має у собі забаронені символи")
    #зроби список з юзерів і перевірь

#2
class InvalidPasswordError(Exception):
    def __init__(self, password):
        self.password = password
class InvalidNumberQuantityError(Exception):
    def __init__(self, number):
        self.number = number
def register_password(password):
    if len(password) < 8:
        raise InvalidPasswordError(password)
    elif password.isnumeric() == 0:
        raise InvalidNumberQuantityError(password)
    else:
        print('Вас зареєстровано!')
try:
    password = input("Введіть пароль: ")
    register_password(password)
except InvalidPasswordError as i:
    print(f"Неправильний пароль '{i.password}', мін 8 символів")
except InvalidNumberQuantityError as i1:
    print(f"Неправильний пароль '{i1.number}', не має в собі числел")

#3
class InvalidFileFormatError(Exception):
    def __init__(self, f):
        self.f = f
#FileNotFoundError
#UnsuppertedFormatError

def read_file(f):
    try:
        with open(f, 'r') as file:
            content = file.read()
            print('File content', content)
    except IOError:
        raise InvalidFileFormatError(f)
try:
    read_file(input('File name: '))
except InvalidFileFormatError as e2:
    print(f'Невідомий формат файлу {e2.f}, функція підтримає тільки текстові файли')