# This program calculates some of the digits of a given number
def sum_digits(n):
    summ = 0
    while (n>0):
        summ += n%10
        n=n//10
    return summ

print(sum_digits(123456))
