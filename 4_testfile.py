 # it is not mandatory to use init function


class Person:
    def age(self,current,yob):
        return current-yob
    def email(self,email_id):
        print("the mail is :", email_id)
    def askname(self):
        name=input("tell me your name : ")
        return name
    def yob_ask(self):
        dob=input("enter dob or ypb bro :")
        return dob

andy = Person()
sudh =  Person()
ayu = Person()

# now all func are assebile by these var or objects

andy.email("andy@123")
print(ayu.askname())
print(sudh.yob_ask())

