# check if the given number is a prime or not

def Is_Prime(num):
    if num <= 1:
        return False
    for i in range (2,num):
        if num%i ==0:
            return False
    return True


print(Is_Prime(19))
