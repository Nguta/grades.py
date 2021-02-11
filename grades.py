x= int(input("enter a number "))
y= int(input("enter a number "))
r= int(input("enter a number "))
t= int(input("enter a number "))
p= int(input("enter a number "))
average=float((x+y+r+t+p)/5)

if average>=70 and average<=100:
    print("A")
if average>=60 and average<=69:
    print("B")
if average>=50 and average<=59:
    print("C")
if average>=40 and average<=49:
    print("D")
if average>=0 and average<=39:
    print("FAIL")