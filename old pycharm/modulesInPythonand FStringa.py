import random
ran_no=random.randint(2,20)
print(ran_no)
rand=random.random()
print(rand)
#f string
me="Ankit"
a1=2
a="This is %s %s"%(me,a1)
print(a)
#another exazmple
list=["ankit","Ayush","Sagar"]
for item in list:
    print(f"Hi {item}") #use of f string
