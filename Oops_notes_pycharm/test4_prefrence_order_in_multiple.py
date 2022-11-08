class Bank():

    def transaction(self):
        print("total transaction value:: ")
    def acc_opening(self):
        print("To show ypur acc open status")
    def deposit(self):
        print("it shows your deposittted amount")
    def test(self):
        print("this is test method from Bank")


class Hdfc():
    def hdfc_to_icici(self):
        print(" transfer from hdfc to icici")

    def test(self):   # same name as test func of Bank class
        print("This is test method from hdfc class")

class Ineuron():
    def acc_ineuron(self):
        print("it is acc_neuron method")



class Icici(Hdfc , Bank,Ineuron):
    pass


obj =Icici()
obj.deposit()
obj.transaction()
obj.acc_opening()
obj.hdfc_to_icici()
obj.test() # test method from Bank class works

# Now reverse prefrence of inheritance in Icici class matlab pehle ab Hdfc inherit karo fir Bank aur ab
# test method Hdfc wala Chalega

obj.acc_ineuron()
