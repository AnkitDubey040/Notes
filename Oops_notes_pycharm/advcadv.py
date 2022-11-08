'''my_string = "this is My First Python programming class and i am learNING python string and its function"
1 . Try to extract data from index one to index 300 with a jump of 3
2. Try to reverse a string without using reverse function
3. Try to split a string after conversion of entire string in uppercase
4. try to convert the whole string into lower case
5 . Try to capitalize the whole string
6 . Write a diference between isalnum() and isalpha()
7. Try to give an example of expand tab
8 . Give an example of strip , lstrip and rstrip
9.  Replace a string charecter by another charector by taking your own example
"sudhanshu"
10 . Try  to give a defination of string center function with and exmple
11 . Write your own definition of compiler and interpretor without copy paste form internet in your own language
12 . Python is a interpreted of compiled language give a clear ans with your understanding
13 . Try to write a usecase of python with your understanding .'''

import logging
logging.basicConfig(filename="task1_oops.log",level=logging.DEBUG,format='%(levelname)s : %(name)s : %(asctime)s : %(message)s')

class strings_task():
    def __init__(self,my_string):
        logging.info("The string Constructor is called --------")
        self.mystring = my_string

    def jumping_3(self):
        try:
            logging.info("enter into the three jummping")
            val = self.mystring[0:300:3]
            logging.info("the jumpping of 3 steps -->: {}".format(val))
            return val
        except Exception as e:
            logging.exception(e)

    def reverse_string(self):
        try:
            logging.info("This function tell you the reverse the string :")
            rev = self.mystring[::-1]
            logging.info("The reversed value of the given string is {}".format(rev))
            return rev
        except Exception as e:
            logging.exception(e)

    def split_with_upper(self):
        try:
            logging.info("This will change all the string into upper case and split the string")
            val = self.mystring.upper().split(' ')
            logging.info("This the value after uppering the string and spliting it  {}".format(val))
            return val
        except Exception as e:
            logging.exception(e)

    def entire_string_lowercse(self):
        logging.info("This function tells you the lowercase letter of all strings")
        try:
            logging.info("Total string into Lowercase letters")
            val = self.mystring.lower()
            logging.info("After converting the string into ------> {}".format(val))
            return val
        except Exception as e:
            logging.exception(e)

    def captilize_string(self):
        logging.info("This function tells you the captilize the strings")
        try:
            logging.info("Total string into captilize")
            val = self.mystring.capitalize()
            logging.info("After converting the string into ------> {}".format(val))
            return val
        except Exception as e:
            logging.exception(e)

    def diff_btw_isaplha_isalnum(self):
        logging.info("This function tells you the difference between isalpha and isalnum the strings")
        try:
            logging.info("check the string isalpha -")
            val = self.mystring.isalpha()
            if val == True:
                logging.info("This is having an only alphabetical values WOW")
            else:
                logging.info("This is having the numerical values like ! and spaces as well")
        except Exception as e:
            logging.exception(e)

    def expand_tab_mystring(self):
        logging.info('This function tells you the expand tabs like slash t white spaces the strings')
        try:
            logging.info("check the string is having the expand tab or not if yes it will print the output")
            val = self.mystring.expandtabs()
            logging.info("This tells you the string to expand tabs {}".format(val))
            return val
        except Exception as e:
            logging.exception(e)

    def trim(self):
        logging.info('This function tells you the non spaces between the words in the string')
        try:
            logging.info("check the string is having the strip")
            val = self.mystring.strip(" ")
            logging.info("This leaves you the space string value :{}".format(val))
            return val
        except Exception as e:
            logging.exception(e)

    def leftstrip_(self):
        logging.info('This function tells you the leave the spaces(one tab space) into left side strings')
        try:
            logging.info("check the string is having the lstrip")
            val = self.mystring.lstrip()
            logging.info("This leaves you the space in the left side of the string value :{}".format(val))
            return val
        except Exception as e:
            logging.exception(e)

    def rightstrip_(self):
        logging.info('This function tells you the leave the spaces(one tab space) into right side strings')
        try:
            logging.info("check the string is having the rstrip")
            val = self.mystring.rstrip()
            logging.info("This leaves you the space in the right side of the string value :{}".format(val))
            return val
        except Exception as e:
            logging.exception(e)

    def replace_the_string(self):
        logging.info("This function tells you the replace the value")
        try:
            logging.info("This changes the strings to the name")
            val = self.mystring.replace("Python","Pandas").replace("python","sklearn")
            logging.info("This will tells you the replace value in the string  : {}".format(val))
            return val
        except Exception as e:
            logging.exception(e)

    def function_center(self):
        logging.info("This function tells you the center function")
        try:
            logging.info(" ")
            val = self.mystring.center(20,"*")
            logging.info(": {}".format(val))
            return val
        except Exception as e:
            logging.exception(e)

logging.shutdown()

'''List questions:
l = [[1,2,3,4],(2,3,4,5,6),(3,4,5,6,7),set([23,4,5,4,4,5,45,45,4,5]),{"k1":"sudh","k2":"ineuron","k3":kumar,3:6,7:8},["ineuron","data science"]]

try to extract all the list entity
try to extract all the dict entiry
try to extract all the tuples entity
try to extract all the numerical data it may by part of dit key and values
try to give summation of all the numerical data
try to filter out all the odd values out of all the numerical data which is a part of list
try to extract ineuron out of this data
try to find out number of occurances of all the data
try to find out number of keys in dict element
try to filter out all the strings data
try to find out alphanumeric data  ## k1 ,k2,k3
try to find out multiplication of all the individual collection inside dataset
try to unwrape all the collections inside collection and create a flat list'''

class GeneralQuestions():
    def __init__(self,my_list):
        self.my_list = my_list

    def extract_all_list(self):
        '''This function extract all the values with in a list of list'''
        try:
            for i in self.my_list:
                if type(i) == list:
                    logging.info(i)
        except Exception as e:
            logging.exception(e)

    def extract_all_dict(self):
        '''This function tells you all the dictonary values'''
        try:
            for i in self.my_list:
                if type(i) == dict:
                    logging.info(i)
        except Exception as e:
            logging.exception(e)

    def extract_all_tuples(self):
        '''This function tealls you all the tuple values in dict'''
        try:
            for i in self.my_list:
                if type(i) == tuple:
                    logging.info(i)
        except Exception as e:
            logging.exception(e)

    def extract_all_numerical(self):
        '''This function tells you the int type in the given list'''
        numerical_values = []
        try:
            for i in self.my_list:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if type(j) == int:
                            numerical_values.append(j)
                if type(i) == dict:
                    for k,v in i.items():
                        if type(v) == int or type(k) == int:
                            numerical_values.append(v)
                            numerical_values.append(k)
            logging.info(numerical_values)
        except Exception as e:
            logging.exception(e)

    def odd_number_from_numerical_data(self):
        '''This will get all the odd numbers in a given list'''
        numerical_values = []
        odd_numbers = []
        try:
            for i in self.my_list:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if type(j) == int:
                            numerical_values.append(j)
                if type(i) == dict:
                    for k, v in i.items():
                        if type(v) == int or type(k) == int:
                            numerical_values.append(v)
                            numerical_values.append(k)
            for s in numerical_values:
                if(s%2!=0):
                    odd_numbers.append(s)
            logging.info(odd_numbers)

        except Exception as e:
            logging.exception(e)

    def summation_all_numerical_data(self):
        '''This will give you the sum of all the values in a given numerical list'''
        numerical_values = []
        try:
            for i in self.my_list:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if type(j) == int:
                            numerical_values.append(j)
                if type(i) == dict:
                    for k,v in i.items():
                        if type(v) == int or type(k) == int:
                            numerical_values.append(v)
                            numerical_values.append(k)

            logging.info(sum(numerical_values))
        except Exception as e:
            logging.exception(e)


    def extract_ineuron_from_this_data(self):
        '''This will extract all the ineuron string from the given list'''
        extrated_val = []
        try:
            for i in self.my_list:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if j == "ineuron":
                            extrated_val.append(j)
                if type(i) == dict:
                    for k,v in i.items():
                        if k == "ineuron" or v == "ineuron":
                            # extrated_val.append(k)
                            extrated_val.append(v)
            logging.info(extrated_val)
        except Exception as e:
            logging.exception(e)

    def extract_all_data(self):
        '''This will unwrap the list'''
        all_values = []
        try:
            for i in self.my_list:
                if type(i) == list  or type(i) == tuple or type(i) == set:
                    for j in i:
                        all_values.append(j)
                if type(i) == dict:
                    for k,v in i.items():
                        all_values.append(k)
                        all_values.append(v)
            logging.info(all_values)
        except Exception as e:
            logging.exception(e)

    def number_of_time_repeated(self):
        '''Number of times the values in this list is occured'''
        all_values = []
        try:
            for i in self.my_list:
                if type(i) == list  or type(i) == tuple or type(i) == set:
                    for j in i:
                        all_values.append(j)
                if type(i) == dict:
                    for k,v in i.items():
                        all_values.append(k)
                        all_values.append(v)

            for s in set(all_values):
                logging.info(f'{s} -- > {all_values.count(s)}')

        except Exception as e:
            logging.exception(e)

    def number_of_keys(self):
        '''Total number of keys in a dict'''
        dummy_list = []
        try:
            for i in self.my_list:
                if type(i) == dict:
                    for k in i.keys():
                        dummy_list.append(k)
            logging.info(len(dummy_list))
        except Exception as e:
            logging.exception(e)

    def filter_all_string_data(self):
        '''This will filter all the string data'''
        dummy_list_string = []
        try:
            for i in self.my_list:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if type(j) == str:
                            dummy_list_string.append(j)
                if type(i) == dict:
                    for k,v in i.items():
                        if type(k) == str or type(v) == str:
                            dummy_list_string.append(k)
                            dummy_list_string.append(v)
            logging.info(dummy_list_string)
        except Exception as e:
            logging.exception(e)

    def find_alphanumerical_data(self):
        '''This fun tells alpha numerical data like k1'''
        dummy_list = []
        try:
            for i in self.my_list:
                if type(i) == dict:
                    for k,v in i.items():
                        if type(k) == str:
                            if k.isalnum():
                                dummy_list.append(k)
            logging.info(dummy_list)
        except Exception as e:
            logging.exception(e)

logging.shutdown()

"""#Questions
l = [3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh" , 234:[23,45,656]}]
1 . Try to reverse a list
2. try to access 234 out of this list
3 . try to access 456
4 . Try to extract only a list collection form list l
5 . Try to extract "sudh"
6 . Try to list all the key in dict element avaible in list
7 . Try to extract all the value element form dict available in list
"""

class My_List():
    def __init__(self,lis):
        self.lis = lis

    def reverse_the_list(self):
        '''This wil reverse the list which has dict and tuple as well'''
        try:
            val = self.lis[::-1]
            logging.info(val)
            return val
        except Exception as e:
            logging.exception(e)

    def access_234_in_list(self):
        '''Access 234 in this list'''
        dummy_list = []
        try:
            for i in self.lis:
                if type(i) == list or type(i) == tuple:
                    for j in i:
                        if type(j) == int:
                            if j == 234:
                                dummy_list.append(j)
                if type(i) == dict:
                    for k,v in i.items():
                        if type(k) == int :
                            if k == 234:
                                dummy_list.append(k)
            logging.info(dummy_list)
        except Exception as e:
            logging.exception(e)

    def access_456_in_data(self):
        '''This function access 456'''
        dummy_list = []
        try:
            for i in self.lis:
                if type(i) == list or type(i) == tuple:
                    for j in i:
                        if type(j) == int:
                            if j == 456:
                                dummy_list.append(j)
                if type(i) == dict:
                    for k,v in i.items():
                        if type(k) == int :
                            if k == 456:
                                dummy_list.append(k)
            logging.info(dummy_list)
        except Exception as e:
            logging.exception(e)

    def list_collection_list(self):
        '''This function collects all the list values form the given list'''
        lis = []
        try:
            for i in self.lis:
                if type(i) == list:
                    lis.append(i)
            logging.info(lis)
        except Exception as e:
            logging.exception(e)

    def extract_sudh_from_list(self):
        '''Extract the name sudh '''
        dummy_list = []
        try:
            for i in self.lis:
                if type(i) == list or type(i) == tuple:
                    for j in i:
                        if type(j) != int:
                            if j == 'sudh':
                                dummy_list.append(j)
                if type(i) == dict:
                    for k, v in i.items():
                        if type(k) != int or type(v) != int:
                            if k == 'sudh' or v == "sudh":
                                dummy_list.append(v)

            logging.info(dummy_list)
        except Exception as e:
            logging.exception(e)

    def all_keys_in_list_of_dict(self):
        '''This will get all the keys in a list of keys'''
        p = []
        try:
            for i in self.lis:
                if type(i) == dict:
                    for k,v in i.items():
                        p.append(k)
            logging.info(p)
        except Exception as e:
            logging.exception(e)


    def all_values_in_list_of_dict(self):
        '''This will get all the keys in a list of keys'''
        p = []
        try:
            for i in self.lis:
                if type(i) == dict:
                    for k,v in i.items():
                        p.append(v)
            logging.info(p)
        except Exception as e:
            logging.exception(e)

logging.shutdown()

class My_Tuples():
    def __init__(self,my_tuple):
        self.my_tuple = my_tuple

    def extract_tuples_from_list(self):
        l = []
        try:
            for i in self.my_tuple:
                if type(i) == tuple:
                    l.append(i)
            logging.info(l)
        except Exception as e:
            logging.exception(e)

logging.shutdown()


my_string = "this is My First Python programming class and i am learNING python string and its function"

my_list = [[1,2,3,4] , (2,3,4,5,6) , (3,4,5,6,7) , set([23,4,5,45,4,4,5,45,45,4,5]) ,
     {'k1' : "sudh", 'k2' : "ineuron", 'k3' : "kumar", 3:6, 7:8} , ['ineuron', 'data science']]

li_1 = [3, 4, 5, 6, 7, [23, 456, 67, 8, 78, 78], [345, 56, 87, 8, 98, 9], (234, 6657, 6),
     {"key1": "sudh", 234: [23, 45, 656]}]

t = l = [3, 4, 5, 6, 7, [23, 456, 67, 8, 78, 78], [345, 56, 87, 8, 98, 9], (234, 6657, 6),
     {"key1": "sudh", 234: [23, 45, 656]}]

# my_string = "banana"
s = strings_task(my_string)
s.jumping_3()
s.reverse_string()
s.split_with_upper()
s.entire_string_lowercse()
s.captilize_string()
s.diff_btw_isaplha_isalnum()
s.expand_tab_mystring()
s.leftstrip_()
s.rightstrip_()
s.trim()
s.replace_the_string()
s.function_center()

logging.info("-"*150)

l = GeneralQuestions(my_list)
l.extract_all_list()
l.extract_all_dict()
l.extract_all_tuples()
l.extract_all_numerical()
l.odd_number_from_numerical_data()
l.summation_all_numerical_data()
l.extract_ineuron_from_this_data()
l.extract_all_data()
l.number_of_time_repeated()
l.number_of_keys()
l.filter_all_string_data()
l.find_alphanumerical_data()

logging.info("-"*150)

li = My_List(li_1)
li.reverse_the_list()
li.access_234_in_list()
li.access_456_in_data()
li.list_collection_list()
li.extract_sudh_from_list()
li.all_keys_in_list_of_dict()
li.all_values_in_list_of_dict()

logging.info("-"*150)

tu = My_Tuples(t)
tu.extract_tuples_from_list()