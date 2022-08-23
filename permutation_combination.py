def factorial(num):                             
    result = 1                              #Fnction defined to get n factorials
    for i in range (1, num+1):
        result = result * i
    return result
def comb(num1, num2):                      #Function defined for nCr
    result = factorial(num1)//(factorial(num2)*factorial(num1 - num2))
    return result
def permut(num1, num2):                    #Function defined for nPr
    result = factorial(num1)//(factorial(num1 - num2))
    return result

def operations():                          #The main menu
    print("Operations:\n1: Factorial\n2: Combination\n3:Permutation\n4:Exit")
    choose = int(input("--"))              #Selecting options
    if choose == 1:
        try:                               #Exception handaling for back to main menu
            print("Press Enter to exit")    
            while True:
                num = int(input("Enter your number: "))
                print(factorial(num))
        except:
            operations()
    elif choose == 2:
        try:                                            #get nCr
            print("Press Enter to exit") 
            while True:
                num1,num2 = map(int,input("Enter n, r value: ").split())
                print(comb(num1, num2))
        except:
            operations()
    elif choose == 3:
        try:
            print("Press Enter to exit") 
            while True:                                 #get nPr
                num1, num2 = map(int, input("Enter n, r value:  ").split())
                print(permut(num1, num2))
        except:
            operations()
    elif choose == 4:
        print("<programme closed>")
    else:
        print("Wrong selection...")        #wrong selection problem solve
        operations()
operations()        #Starting the programme