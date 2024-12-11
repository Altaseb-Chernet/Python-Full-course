class Account:

    def __init__(self,owner,balance):
        self.owner=owner
        self.__balance=balance

    def deposit(self,amount):
        if amount > 0:
            self.__balance +=amount
            print(f'add amount of {amount}')

        else:
            print('please enter apropriate value')

    def get_balance(self):
        return self.__balance
access=Account('Altaseb',1000)
access.deposit(200)
print(access.get_balance())

class Person:
    def __init__(self,name):
        self.name=name
  


p=Person('altaseb')
p.name