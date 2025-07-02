# 1. print prime numbers from 1 to 100 by useing functions

def is_prime(num):
    if num<2:
        return False
    for i in range(2,num):
        if num%i==0:
            return False
    return True

for j in range(1,101):
    if is_prime(j):
        print(j, end='')



        
# 2. print next prime of a given number 

num=int(input("enter a number: "))
next_prime_not_found= True
while next_prime_not_found:
    num+=1
    fact=0
    for i in range(2,num):
        if num%i==0:
            fact+=1
            break
    if fact==0:
        print("next prime is: ",num)
        next_prime_not_found=False



    
# 3. print previous prime of a given number

num=int(input("enter a number: "))
previous_prime_not_found=True
while previous_prime_not_found:
    num-=1
    fact=0
    for i in range(2,num):
        if num%i==0:
            fact+=1
            break
    if fact==0:
        print("previous prime is: ",num)
        previous_prime_not_found=False



# 4. check weather a number is an Armstrong or not

num=int(input("enter a number: "))
temp=num
power=len(str(temp))
sum=0

while num!=0:
    digit=num%10
    sum+=digit**power
    num=num//10
    if sum==temp:
        print("given number is Armstrong")
        break
else:
    print("given number is not an armstrong")
        
    

# 5.print Armstrong numbers between 1 to 2000

for num in range(1,2001):
    temp=num
    power=len(str(num))
    sum=0
    
    while num!=0:
        digit=num%10
        sum+=digit**power
        num=num//10
    if sum==temp:
        print(temp,end=' ')
        