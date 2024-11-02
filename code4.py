#write a script that will take two numbers and display the sum of those numbers

try:
    n1=int(input("please enter the first number: "))
    n2=int(input("please enter the second number: "))
    _sum=n1+n2
    print(_sum)
except:
    print("please enter a valid number")