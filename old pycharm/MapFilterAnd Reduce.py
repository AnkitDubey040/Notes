#map function applier one func in whole list
#num=["32","43","453"]
#suppose i want to add 1 to third elenent then i usually do this:
"""
for i in range(len(num)):  #first i convert string to integer
    num[i]=int(num[i])
num[2]=num[2]+5
print(num[2])
"""

#num=list(map(int,num))
 #num[2]=num[2]+5
""""
def sq(a):
    return a*a
num = [2,3,4,1,3,4]
square=list(map(sq,num))
print(square)
"""
def square(a):
    return a*a
def cube(a):
    return a*a*a
func=[square,cube]
for i in range(5):#taking numbers form 0 to 4
    value=list(map(lambda x:x(i),func))
    print(value)
#filter function

list1=[1,2,1,4,2,3,4,2,9,7,6,5,9,12]
def isgreater(num):
    return num>5

list2=list(filter(isgreater,list1)) #tyoecast to list tpo get output
print(list2)

#reduce

from functools import reduce
list3=[1,2,3,4,5,6,7,8,9,0]
#I want to add the list   could have been done by for loop but we can reduce the list using reduce
num=reduce(lambda x,y:x+y, list3)
print(num)