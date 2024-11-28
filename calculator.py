num1=int(input("enter first number :"))
num2=int(input("enter second number :"))
ope=input("enter operation :")
if ope=='+':
    print("result", num1+num2) 
elif ope=='-':
    print("result", num1-num2)
elif ope=='*':
    print("result", num1*num2) 
elif ope=='/':
    if num2==0:
        print("invalid")
    else:
        print("result",num1/num2)

    
