class ineuron:
    def student(self):
        print("The details of all the students")
    def achiever(self):
        print("List of all achievers")
    def hall_of_fame(self):
        print("List of students in hall of fame")

class Ineuron_Vision(ineuron):
    def student(self): # we are overwriting Student method Of parent classs
        print("These are the filtered stidents from the list")


stu = Ineuron_Vision()
stu.student()    # student method of child class printed
#this is called METHOD OVERRIDING


