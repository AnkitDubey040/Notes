# inheritance type: single, multiple, multilevel, hybrid etc

# MULTILEVEL INHERITANCE:
class Bank():

    def transaction(self):
        print("total transaction value:: ")
    def acc_opening(self):
        print("To show ypur acc open status")
    def deposit(self):
        print("it shows your deposittted amount")


class Hdfc(Bank):
    def hdfc_to_icici(self):
        print(" transfer from hdfc to icici")


class Icici(Hdfc):
    pass

obj = Icici()
obj.hdfc_to_icici()
obj.deposit()
obj.acc_opening()
obj.transaction()



