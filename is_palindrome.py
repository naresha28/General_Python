
n = int(input("enter a number"))
n = str(n)
rev = n[::-1]
print("the reverse number is", int(rev))
if int(n)==int(rev):
    print("the given number is a palindrome")
else:
    print("the given number is not a palindrome")
