import random

class BankAccount:

    def __init__(self, money=0):
        self.money = int(money)

    def withdraw(self, amount):
        self.amount = int(amount)
        self.money = self.money - self.amount

    def deposit(self, amount):
        self.amount = int(amount)
        self.money = self.money + self.amount

    def balance(self):
        return float(self.money)

    def __repr__(self):
        return 'BankAccount('+str(float(self.money))+')'


class PingPong:

    def __init__(self):
        self.state = 'PING'

    def next(self):
        if self.state == 'PING':
            self.state = 'PONG'
            return self.state
        else:
            self.state = 'PING'
            return self.state
        
        
