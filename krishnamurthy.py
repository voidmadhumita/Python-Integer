Number=int(input("enter the number to check krisumhnamurthy Number= "))
Sum=0
Temp=Number

while Temp > 0:
    fact = 1
    i = 1
    rem = Temp % 10
    
    while i <=rem:
        fact = fact * i
        i = i + 1
    print('Factorial of %d = %d'%(rem, fact))
    Sum = Sum + fact
    Temp = Temp // 10
print("The Sum of the Digits factorials = %d" %Sum)
if Sum == Number:
    print("\n%d is a Krishnamuthy Number." %Number)
else:
    print("%d is not a Krishnamurhy  Number." %Number)
