# 1.Reverse the given String 

s=input("enter a string: ")

def reverse_string(s):
    rev_str=""
    for char in s:
        rev_str=char+rev_str
    return rev_str
print(reverse_string(s))

# -------------------------------

s=input("enter a string: ")

rev=""
for char in s:
    rev=char+rev
print(rev)



# 2. print weather the given string is a palindrome or not

s=input("enter a string: ")
rev=""
for char in s:
    rev=char+rev
    if s==rev:
        print(f" {s} is a palindrome")
        break
else:
    print(f"{s} is not a palindrome")



# 3.Remove all duplicates from a string

s=input("enter a string: ")
new_s=""
for char in s:
    if char not in new_s:
        new_s+=char
print(new_s)        



# 4.Check if two strings are anagrams of each other.


s1=input("1st string: ")
s2=input("2nd string: ")

is_same=True

if len(s1)!=len(s2):
    print("length differnce, ie., not anagrams")
else:
    for char in s1:
        if s1.count(char)!=s2.count(char):
            is_same=False
            print("both are not anagram")
            break
    if is_same==True:
        print("both are anagrams")
    
    
    
    
# 5.inp:abcdabcaba ---> output:4a3b2c1d

v="abcdabcaba"
res=""
for char in v:
    if char not in res:
        count=v.count(char)
        res+=char+str(count)
print(res)
        











