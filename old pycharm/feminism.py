print("To test if you are a feminist or not")
print("Is modern feminism a cancer ?")
print("enter 'y' for yes and 'n' for no")
ch = str(input())
if(ch=='y'):
    print("congrats! you are not a feminits")
elif(ch=='n'):
        print("Do you consider yourself a feminist")
        ch1=str(input("Enter y/n"))
        if(ch1=='y'):
            print("You are a feminist and a pathetic human being")
        elif(ch1=='n'):
                print("congo you are not a feminist but let's understand your reason for not calling feminism a cancer")
                print("Have you watched Jordan petersonon videos?")
                ch2=str(input())
                if(ch2=='y'):
                    print("Then you should have been clear on that so ypu are a feminist just don't wanna show it")
                elif(ch2=='n'): print("Go watch jordan peterson's videoes and then again take the quiz ")
                else: print("Wrong input")
        else: print("wrong input")
else:
    print("Wrong input")
