import logging

logging.basicConfig(filename="TaskLogFile" ,level = logging.DEBUG , format =  ' %(levelname)s :  %(asctime)s :  %(message)s   ' )


class String_func:
    logging.info("We are going to study string functions: ")
    def __init__(self,qstr1):
        self.qstr1=qstr1

    def indexExt(self):
        try:
            logging.info("to extract index wise char from strings with jump of 3 steps")
            a = self.qstr1[0:300:3]
            logging.info("The obtained answer is: %a " , a)
        except Exception as e:
            logging.exception(e)

    def revStr(self):
        try:
            logging.info("to reverse a string without using reverse function")
            a = self.qstr1[::-1]
            logging.info("The reversed string is : %a" ,a)
        except Exception as e:
            logging.exception(e)

    def upSplit(self):
        try:
            logging.info("to covert string in upper case and split it ")
            a = self.qstr1.upper().split(" ")
            logging.info("The obtained string is : %a" ,a)
        except Exception as e:
            logging.exception(e)

    def strLow(self):
        try:
            logging.info("to covert string in lower case ")
            a = self.qstr1.lower()
            logging.info("The lower case string is : %a" ,a)
        except Exception as e:
            logging.exception(e)

    def strCapatilize(self):
        try:
            logging.info("to capitalize the string ")
            a = self.qstr1.capitalize()
            logging.info("The capitalized string is : %a" ,a)
        except Exception as e:
            logging.exception(e)
    def strIsalphaOrIsnum(self):
        try:
            logging.info("to check if string is alphanumeric or alphabetical only")
            a = self.qstr1.isalnum()
            if a == True:
                logging.warning("The string is alpha numeric")
            else:
                logging.warning("The string is alphabetical only")
        except Exception as e:
            logging.exception(e)

    def strStrip(self):
        try:
            logging.info("to use strip,lstip,rstip")
            a = self.qstr1.strip()
            logging.info("The stripped string is: %a",a )
            a=self.qstr1.lstrip()
            logging.info("The left stripped string is : %a" ,a)
            a=self.qstr1.rstrip()                                       # jab mai b,c le rha hoon tab ye kaam nhi kar rha 
            logging.critical("The right stripped string is : %a",a)

        except Exception as e:
            logging.exception(e)


'''    def strExpandTabs(self):
        try:
            logging.info("to expand tabs in the string ")
            l=[]
            for i in qstr:
                l.append(i)
            for i in str(l):
                    
                    
            a = self.qstr1.expandtabs()
            logging.info("The expanded  string is : %a", a)
        except Exception as e:
            logging.Exception(e)
    

'''




qstr="    this is My First Python programming class and i am learNING python string and its function    "
strobj = String_func(qstr)
strobj.indexExt()
strobj.revStr()
strobj.upSplit()
strobj.strLow()
strobj.strCapatilize()
strobj.strIsalphaOrIsnum()
# strobj.strExpandTabs()
strobj.strStrip()






    