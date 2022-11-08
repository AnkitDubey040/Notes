""""
def func(a,b,c):
    print(a,b,c)
func("Ankit","Sagar","Ayush")  # this is for three users what is there are many users
"""
def func(*args):
    for item in args:
        print(item)
abc=["Ankit","Sagar","Ayush","rakshit","Supratim","Ankur"]
func(*abc)#remember if you want any other argument then it s\hould be used befor args parametr
          #eg- func(normal,*kwargs,*args)