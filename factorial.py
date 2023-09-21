num=int(input("enter the number"))
factorial=1
if num<0:
    print("sorry,factorial does not exit for negetive number")
elif num==0:
    print("the factorial of 0 is 1")
else:
    for i in range(1,num+1):
        factorial=factorial*i
    print("the factorial of is:",factorial)
