from firebase import firebase
import tokens

# Подключение к БД
firebase = firebase.FirebaseApplication(tokens.firebase, None)

# Функция создания пользователя
def new_player(name, password):
    # Данные пользователя
    data = {
        'Name': name,
        'Password': password
    }
    # Отправка запроса а БД
    firebase.post(tokens.firebasedatabase + "Players/", data)