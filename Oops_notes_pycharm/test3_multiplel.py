class Bank():

    def transaction(self):
        print("total transaction value:: ")
    def acc_opening(self):
        print("To show ypur acc open status")
    def deposit(self):
        print("it shows your deposittted amount")


class Hdfc():   # THIS time it is an independent class
    def hdfc_to_icici(self):
        print(" transfer from hdfc to icici")


class Icici(Bank , Hdfc):  # we have called Both above Classes as Parent Class here
    pass
obj =Icici()
obj.deposit()
obj.transaction()
obj.acc_opening()
obj.hdfc_to_icici()