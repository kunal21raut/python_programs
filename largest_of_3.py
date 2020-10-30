a=float(input("Enter the value of a:"))
b=float(input("Enter the value of b:"))
c=float(input("Enter the value of c:"))
print("a=",a,"b=",b,"c=",c)
if a>b and a>c:
    print("a is greater than b and c")
elif b>a and b>c:
    print("b is greater than a and c")
elif c>a and c>b:
    print("c is greater than a and b")
else:
    if a==b:
        print("a is equal to b")
    elif a==c:
        print("a ia equal to c")
    elif b==c:
        print("b is equal to c")

print("\n=====Program to  calculate grade of student marks======\n")
marks=int(input("Enter the Marks of Student :"))
if marks>=81 and marks<=100:
    print("Congrats! you have passed with \'+A\' Grade.\nYou got :",marks,"marks")
elif marks>=74 and marks<81:
    print("Congrats ! you have passed with \'A\' Grade.\nYou got :",marks,"marks")
elif marks>=64 and marks<74:
    print("Congrats ! you have passed with \'+B\' Grade.\nYou got :",marks,"marks")
elif marks>=56 and marks<64:
    print("Congrats ! you have passed with \'B\' Grade.\nYou got :",marks,"marks")
elif marks>=48 and marks<56:
    print("Congrats ! you have passed with \'C\' Grade.\nYou got :",marks,"marks")
elif marks>=40 and marks<48:
    print("Congrats ! you have passed with \'D\' Grade.\nYou got :",marks,"marks")
else:
    print("You have Failed. \nYou got :",marks,"marks \n Better Luck Next Time !") 

