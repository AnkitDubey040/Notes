# self keyword nhi hai iskijagah mai kuch aur bhi use kar skta hoon
class Person:
    def __init__(andy,name,srname,email,yob):
        andy.name=name
        andy.srname=srname
        andy.email=email
        andy.yob=yob
    #creating another function to find age
    def age(self,currentyear):
        return currentyear-self.yob
    #here with self.yob wwe get refrence of actual yob
    #pointer is helping to get data from yob



ank_var= Person("ankit"," dubey","ankit@1232141",2001)
sag_var= Person("saga","naka","s@1232141",1978)
zeb_var= Person("zebestian","weasely","weasly@1232141",1974)


print(ank_var.email)
print(ank_var.yob)
print(sag_var.name)
print(sag_var.srname)
print(zeb_var.email)
print(zeb_var.yob)

# concatenate name and sr name for ank_var:
print(ank_var.name + ank_var.srname)

# age find karne ke liye by calling a function:
print(" age is: " ,ank_var.age(2022))
print(" age is: " ,sag_var.age(2022))

# for upper case:
s=str(ank_var)
s.upper()

# if we pass less parameters in object it gives error
# agar hum andy.name=name wale mei 3 hi parameter pass kare bhale hi upar func definition mei 4 ho to jab hum object bna
#ke func ko call karenge 3 parameters ke saath bhi tabhi vo chal jayega par normally nhi chalta agar hum 4 parameter ko
# define karte to
