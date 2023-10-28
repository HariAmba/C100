class Atm:
    def __init__(self,card,pin,balance):
        self.card = card
        self.pin = pin
        self.balance = balance

    def check_balance(self):
        print('Your balance is ',self.balance)

    def cash(self):
       withdraw = int(input('Enter the amount you want to withdraw'))
       self.balance = self.balance - withdraw
       print('Your balance is ', self.balance)

newUser = Atm(2432324,8945,1000)

print(newUser.check_balance())
print(newUser.cash())
