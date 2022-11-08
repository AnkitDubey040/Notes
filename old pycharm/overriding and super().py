class A:
    var1="class var in class A"
    def __init__(self):
        self.variable1 = "I am inside class A const"
        self.var1="instance variable in class A"  # if this line was not here the upper var1 would be printed
        self.spl ="I am special in A"
class B(A):
    var2="In class B"
    var1="in b"  # still instance var in const of A will be printed
    def __init__(self):  # method overriiding
        super().__init__() # to override
        self.variable1="inside b const"
        self.var1="insside b "

a=A()
b=B()
print(a.var1)
print(b.var1)
#if i want class A const to run eve if ot is overrided
print(b.spl)
print(b.variable1)
