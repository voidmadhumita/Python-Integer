nterms=int(input("how many terms?"))
n1,n2=0,1
count=0
if nterms<=0:
    print("please enter a possitive integer")
elif nterms==1:
    print("fibonacci squence upto",nterms,":")
    print(n1)
else:
    print("fibonacci sequence:")
    while count<nterms:
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        count+=1
