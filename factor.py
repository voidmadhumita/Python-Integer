n=int(input("enter a number: :"))
print("factor of:",n,"is:",)
for i in range(1,n):
    if( (n%i)==0):
        print(i,",",end=' ')
