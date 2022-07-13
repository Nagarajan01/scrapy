#1)     Write a script to list out all the prime numbers and composite numbers between 1 to 100.
#       For composite numbers you have to print their multiples also.
# python program to print prime number from 1 to 100
'''
prime_number=[]
composite_number=[]
for i in range(2, 101):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count += 1
    if count == 2:
        prime_number.append(i)
    else:
        composite_number.append(i)
print("prime_number",prime_number)
print("composite_number",composite_number)'''
