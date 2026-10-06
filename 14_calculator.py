a=float(input("the 1st number ="))
b=float(input("the 2nd number="))

choice=(input("enter if you want to div,add, multiply ,sub :"))

if choice=="add":
  print(a+b)
elif choice=="div":

  if b!=0:
    print(a/b)
  else:
    print("cannot be divided")
elif choice=="multiply":
      print(a*b)
else:
    print(a-b)