from flask import Flask , request , jsonify


'''(def test(a,b):
    return a+b)'''
# we want to execute this function from postman application or any browser say
''''
we are trying to create a kind of communication between the other lang or programs  so that we can 
run our application using those other tools
'''
# print(test(4,5))

# let's first create an object of Flask class named app
app = Flask(__name__)
'''
here we have imported Flask lib which will help comm
we have created object app so we can access all the methods , variables in a class Flask 
now in app.route line :
we know each framework is diff so they are independent and not compatible so we need to use something which does
not depend on any protocol so we use api 

app.rote means we are trying to create a route for object app through /abc bu GET and POST which will help us 
send and receive data and we write it just above the function so that after this route do this function or execute it 

so what if we want to access someones else sys so we need ip add , etc so how can we get inside a folder so we will give path of each folder and then we will be able to access and 
perform action on it . 

so to reach to func test1 we need to reach out to it's path so 
app.route behaves as a decorator here 


GET , POST 
if you go to google and type DATA SCIENCE so you see some result as DATA +SCIENCE 
so data is in diff servers so it creates a query and searches for this file in diff files and fetches the result
and responses so it sends query in backend and give response so we have first sent some data and get data afterwards.

Even in user ID pass we send data and then it authinticates just that we are  not able to see it as it is encrypted all is happening in background 
so we send data through 
1. link , url (google search)
2. Body (gmail)
Therefore 
 GET means POSTING A DATA  via  a URL or browser 
and POST means Posting a data via a  BODY 



'''

# let's create a function here
@app.route('/abc' , methods = ['GET' ,'POST'])
def test1():
    if(request.method=='POST'):     # when we want to oass data from somewhere else
        a = request.json['num1']    # ask to send data in json format
        b = request.json['num2']
        result = a + b
        return jsonify((str(result)))    # to return to the same syatem
# on running after this we see server has been created locally and on a local https link
'''
After server has been created :
open POSTMAN and click on new or click on + button and call POST click on it as the func we have created is being sended thr post it will ask to enter URL so enter the URl 
visible in server 127.0.0.1 and also the port number which is 5000 along with /abc which is the path 
since we have choosen POSt so click on body and then raw choose json as mode now in that give
1. keep it inside double quote "num1" : 20 and then for b and then click on send and we will get the result 
code 200 means success 
and code 400 mean error 

'''
# now write another function
@app.route('/abc1/andy',methods=['GET' , 'POST'])
def test2():
    if (request.method == 'POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a * b
        return jsonify((str(result)))

@app.route('/abc1/andy/test',methods=['GET' , 'POST'])
def test3():
    if (request.method == 'POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a ** b
        return jsonify((str(result)))

@app.route('/abc1/andy/test4', methods=['GET', 'POST'])
def test4():
        if (request.method == 'POST'):
            a = request.json['num1']
            b = request.json['num2']
            result = a - b
            return jsonify((str(result)))


@app.route('/abc1/andy/test5',methods=['GET' , 'POST'])
def test5():
    if (request.method == 'POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a / b
        return jsonify((str(result)))


# instantiating the app thr postman

if __name__=='__main__'  :
    app.run()

