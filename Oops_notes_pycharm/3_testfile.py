class Person:
    def __init__(andy,name,srname,email,yob):
        andy.name=name
        andy.srname=srname
        andy.email=email
        andy.yob=yob

    # now suppose we are creating another init:
    # it will consider second beacuse pehle upar wala
    #consideer kar liya to ab baaad wala hua to baad wala
    #ab __init__ hai bhai
    #to hamesha last wala init hoga
    def __init__(andy, name, email):
        andy.name = name
        andy.email=email


#ank_var= Person("ankit"," dubey","ankit@1232141",2001)
#sag_var= Person("saga","naka","s@1232141",1978)
zeb_var= Person("zebestian","weasly@1232141")

#print(ank_var.yob)   #ispe error show kar dega as 5 parameters hai

print(zeb_var.name)




