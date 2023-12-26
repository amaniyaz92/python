class User:
    def __init__(self, name, mail, age, phone):
        self.name = name
        self.mail = mail
        self.age = age
        self.phone = phone
    def change_username(self, new_name):
        self.name = new_name
    def change_number(self, new_phone):
        self.phone = new_phone
    def change_mail(self, new_mail):
        self.mail = new_mail

user_name = input('Введите имя: ')
user_mail = input('Введите почту: ')
user_age = input('Введите возраст: ')
user_phone = input('Введите номер телефона: ')
user1 = User(name = user_name, mail = user_mail, age = user_age, phone = user_phone)

while True:
    action = input('Что хотите сделать? ')
    if action.lower() == 'изменить имя':
        new_name = input('Введите новое имя: ')
        user1.change_username(new_name)
        print('Успешно!')
    elif action.lower() == 'изменить номер':
        new_number = input('Введите новый номер: ')
        user1.change_number(new_number)
        print('Успешно!')
    elif action.lower() == 'изменить почту':
        new_mail = input('Введите новую почту: ')
        user1.change_username(new_mail)
        print('Успешно!')
    elif action.lower() == 'инфо':
        print(user1.name, user1.mail, user1.age, user1.phone)
    else:
        print('Неизвестная операция!')
