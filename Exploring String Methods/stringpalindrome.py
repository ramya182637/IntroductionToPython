print("Enter the string")
str = input()
revstr = str[:: -1]
if(str == revstr):
    print("yes its palindrom ",str)
else:
    print("Not a plaindrome")