# to see hirearchy see test 3 file in last

import logging
logging.basicConfig(filename="test5.log" ,level= logging.DEBUG ,format='%(levelname)s %(asctime)s %(name)s  %(message)s')

try:      # to open a file
    logging.info("trying to read a file")
    with open("andy.txt" ,'r'):
        #read mode mei error aayega kyonki aisi file exist nhi karti
        logging.info("read the file successfully")
except Exception as e:
    logging.critical("this is critical error msg")
    logging.error(e)     # isme sirf error msg aayega
    logging.exception(e) #isme poora exception aayega details ke saath poori
    logging.error("error ahbddhfbdsjkf")

# we now only has root user but an do logging from diff account i.e. logging streams
