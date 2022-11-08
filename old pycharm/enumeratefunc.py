#ususlyy if we want odd items in the list we do rhe following

"""
l1=["Ankit","Ayush","Sagar","Akshay","Rahul","Ajay"]

i= 1
for item in l1:
    if i%2!=0:
        print(f"please summon {item}") #f string 
    i += 1
"""
#now enumerate function:
l1=["Ankit","Ayush","Sagar","Akshay","Rahul","Ajay"]
for index, item in enumerate(l1):
    if index%2==0:
        print(f"Please summon {item}")
