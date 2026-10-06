#1. Largest of 3 Numbers

#CODE
a=int(input("ENTER FIRST NUMBER: "))
b=int(input("ENTER SECOND NUMBER: "))
c=int(input("ENTER THIRD NUMBER: "))

if(a>b and a>c):
    print(a,"is the largest number")
elif(b>a and b>c):
    print(b, "is the greatest number")
else:
    print(c, "is the greatest number")

#Algorithm

#1.Start

#2.Read three numbers: a, b, and c.

#3.If a > b and a > c, then a is the largest.

#4.Else if b > a and b > c, then b is the largest.

#5.Else, c is the largest.

#6.Print the largest number.

#7.Stop
