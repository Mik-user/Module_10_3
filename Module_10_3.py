from threading import Thread, Lock
from random import randint
import time
class Bank():
    lock = Lock()

    def __init__(self):
        super().__init__()
        self.lock.locked()
        self.balance = 0


    def deposit(self):
        #global lock
        for i in range(100):
            pay = randint(50,500)
            self.balance += pay
            print(f'\nПополнение: {pay}. Баланс:{self.balance}')
            time.sleep(0.001)
            if self.balance >=500 and self.lock.locked() == True:
                self.lock.release()


    def take(self):
        for i in range(100):
            removal = randint(50,500)
            print(f'\nЗапрос на: {removal}')
            if removal <= self.balance:
                self.balance -= removal
                print(f'\nСнятие: {removal}. Текущий баланс: {self.balance}')
                time.sleep(0.001)
            else:
                print('Запрос отклонен. Недостаточно средств')
                self.lock.acquire()

bk = Bank()


th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
