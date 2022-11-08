#lambda function (one linear functions ) also called Anonymous Func.
minus=lambda x, y: x-y #we write the below sub func in one line using lambda

def subtract(m,n):# does same as lambda it's just lengthy
    return m-n
print(minus(8,2))
print(subtract(9,5))

#now using sort func (another example)
#def a_first(a):
 #   return a[1]

a=[[1,4], [2,6], [6,3]]
#a.sort(key=a_first)
a.sort(key=lambda x: x[1])
print(a)
