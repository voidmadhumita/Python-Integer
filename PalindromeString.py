txt = input("Enter The Text")
print(txt)
back=txt
a=txt[::-1]
if a == back:
    print("The text is Palindrome")
else:
    print("The text is Not Palindrome")
