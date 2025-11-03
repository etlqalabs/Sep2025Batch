class BankAccount:
    owner = "EL QA Labs"
    _balance = 5000
    __pin = 1234

    def displayPin(self):
        print(self.__pin)

    def __displayBalance(self):
        print(self._balance)



class SavingsAccount(BankAccount):
    pass

# Create object of BankAccount
ba = BankAccount()
print(ba.owner)
print(ba._balance)
#print(ba.__pin)
ba.displayPin()


# Create object for SavingsAccount
sa = SavingsAccount()
print(sa.owner)
print(sa._balance)
print(sa.__pin)
sa.displayPin()
