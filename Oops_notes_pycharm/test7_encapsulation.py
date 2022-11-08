class Ineuron:
    def __init__(self):
        self.students1 = "data sc"

    def students(self):
        print(self.students1)

class ineuron1:
    def __init__(self):
        self.__students1 = "stu name in ineuron1"
    def students(self):
        print(self.__students1)
    def student_change(self,new_value ):
        #self.__students1="big data stu name changes"
        self.__students1 = new_value
i = Ineuron()
# i.student() # agar same name hai tpo nhi cahlega
i.students()

'''
#overwriting value of variable
i.students1 = "data sc master"
i.students()
'''

i1=ineuron1()
i1.students()

#ovwrwritig value of peivate var
i1.__students1 = "changes ineuron1"
i1.students() # it dont changes the values so fails to overwrite

#actually changing values
#i1.student_change()
#i1.students()
'''
 so for private value we cannot reasiign value using object
 we have to reassign value inside the class only using another method and then use it to change the 
 value of private member 

'''
# now we will give parameter to stu_change method it is also a method to change value
i1.student_change("ankit duby")
i1.students() # now we change value but not directly


# This is example of ENCAPSULTION where we don't allow one component to mix witrh other and no one can change contents
#inside it ...only by opening it... so not directly but thr other way ..no direct access for modification


''' 
diff in absctraction and encapsulation:
in absctraction we are hiding data behind a class .. there we hid data or var behind class aceess is hidden no mentioning
of modification
in encapsulation we are not allowing modification directly
'''
