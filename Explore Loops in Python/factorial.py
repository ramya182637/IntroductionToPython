print("enter the number to find its factorial: ",end=" ")
n= int(input())
fact = 1
for i in range (1,n+1):
    fact = fact * i
print("Factorial is : ",fact)
