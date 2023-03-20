from firebase import firebase
import tokens

# Подключение к БД
firebase = firebase.FirebaseApplication(tokens.firebase, None)

# Функция создания прдемета
def new_item(name, count):
    # Данные предмета
    data = {
        'Nams': name,
        'Count': count
    }
    # Отправка запроса а БД
    firebase.post(tokens.firebasedatabase + "Items/", data)