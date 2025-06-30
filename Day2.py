# 1.Write a program to check if a number is even or odd.

num=int(input("enter a number: "))
if num%2==0:
    print("the number is even")
else:
    print("the number is odd")


# 2.Write a program to find the largest of three numbers.

num1=int(input("enter 1st number: "))
num2=int(input("enter 2nd number: "))
num3=int(input("enter 3rd number: "))

if num1>num2 and num1>num3:
    print("1st number is greatest")
elif num2>num1 and num2>num3:
    print("2nd number is greatest")
else:
    print("3rd number is greatest")


# 3.Check whether the number is a positive or negative integer.

num=int(input("enter a number: "))
if num>0:
    print("Positive integer")
elif num<0:
    print("Negative integer")
else:
    print("zero")


# 4.Check whether a number is a prime number.

num=int(input("enter a number: "))

if num==0 or num==1:
    print("it is not a prime number")
elif num>1:
    for i in range(2,num):
        if num%i==0:
            print(" the number is not a prime")
            break
    else:
        print("the number is a prime")
else:
    print("not a prime number")
    
        
            
# 5.Find the factorial of a given number.

num=int(input("enter a number: "))
fact=1
for i in range (1,num+1):
        fact=fact*i
print(fact)