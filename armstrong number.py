num=int(input("enter your number:"))

sum=0
back=num
while back>0:
    digit=back%10
    sum+=digit **3
    back=int(back //10)
if(sum==num):
    print(num,"is an Armstrong Number");
else:
    print(num,"is not an Armstrong Number");
