# 1.Write a program to print the vowels in the given string

str=input("Type something: ")
vow="a,e,i,o,u,A,E,I,O,U"

for i in str:
    if i in vow:
        print(i)
        
        
# 2.write a program to find character count in a given string 

str=input("enter a string: ")
count=0
for i in str:
    count+=1
print(count)



# 3.print ASCII codes for given string 

str=input("enter a string: ")
for char in str:
    Ascii_value= ord(char)
    print(f"{char}'s ascii vale is {Ascii_value}")




# 4.convert the given string into a list

str=input("enter a string: ")
list=[]

for i in str:
    list.append(i)
print(list)


# 5.convert lowercase characters to uppercase using ASCII

str=input("enter a string: ")
upper_str=""

for char in str:
    if "a"<=char<="z":
        upper_ascii= ord(char)-32
        upper_str+=chr(upper_ascii)
    else:
        upper_str+=char
print(upper_str)

