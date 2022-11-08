class Dad:
    basketball=1
class Son(Dad):
    dance=1
    basketball=9
    def isDance(self):
        return f"Yes I like to dance so what {self.dance}"
class Grandson(Son):
    dance=6
    def isDance(self): # was already there but since new copy is made so it will be applied
      return f"I dance better {self.dance}"

Ankit=Dad()
Ayush=Son()
Sagar=Grandson()
print(Sagar.isDance()) # prints grandson method if grandson's method was commented out
# then son's method would have ran
print(Sagar.basketball) # prints son's baketbaal first if it was
# not there then dad's basketball would have printed
#


# public,protected and private

#for public simply write variables name
#for protectectd start name with underscore e.g. - _Ankit    class can access it i.r base and derived can acces it but not other
# for private we use double underscore __Ankit cannnot be used outside class i.e. only in base and child and is accessed with first class name e.g. Employee__Ankit (it is called name angling)
