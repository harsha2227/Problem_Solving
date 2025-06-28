# 1.adding the digits of a number

num=123
sum=0
while num!=0:
    last_digit=num%10
    sum+=last_digit
    num=num//10
print(sum)


# 2.reversing a given number

num=2345
rev=0
while num!=0:
    last_digit=num%10
    rev=rev*10+last_digit
    num=num//10
print(rev)


# 3.multiply digits in a numbers

num=123
mul=1
while num!=0:
    last_digit=num%10
    mul=mul*last_digit
    num=num//10
print(mul)

# 4. Chech weather its a palindrome or 

num=12321
original_num=num
rev=0
while num!=0:
    last_digit=num%10
    rev=rev*10+last_digit
    num=num//10
if original_num==rev:
        print("the number is palindrom")
else:
        print("it is not a palindrom")