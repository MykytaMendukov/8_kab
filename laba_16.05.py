#1
class InvalidUsernameError(Exception):
    def __init__(self, username):
        self.username = username
def register_user(username):
    if len(username) < 5:
        raise InvalidUsernameError(username)
    else:
        print('Вас зареєстровано!')
try:
    username = input("Введіть ім'я: ")
    register_user(username)
except InvalidUsernameError as e:
    print(f"Неправильне ім'я {e.username}, мін 5 символів")