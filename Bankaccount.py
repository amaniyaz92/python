class Bankaccount:
    def __init__(self, name, balance=0.0):
        self.name = name
        self.balance = balance
    def deposit(self, sum_dep):
        self.balance += sum_dep
    def cash(self, sum_cash):
        self.balance -= sum_cash
    def my_balance(self):
        return self.balance

client_name = input('Введите свое имя ')
client1 = Bankaccount(name=client_name)
while True:
    action = input('Что хотите сделать? ')
    if action.lower()=='депозит':
        sum = float(input('Сумма депозита '))
        client1.deposit(sum)
        print('Операция успешна!')
    elif action.lower() == 'снять наличные':
        sum = float(input('Сумма для снятия '))
        if sum <= client1.balance:
            client1.cash(sum)
            print('Операция успешна!')
        else:
            print('Недостаточно средств!')
    elif action.lower() == 'баланс':
        print(client1.my_balance())
    else:
        print('Неизвестная операция!')
