#2)     Write a function to get two integer inputs from the user
#       and find their gcd(greatest common divisor) using euclidean algorithm
# Python program to find GCD of two numbers

'''
def gcd(a, b):
    result = min(a, b)
    while result:
        if a % result == 0 and b % result == 0:
            break
        result -= 1
    return result
a = int(input("enter the no.",))
b = int(input("enter the no.",))
print(f" GCD ( {a} , {b} ) {gcd(a, b)}")'''