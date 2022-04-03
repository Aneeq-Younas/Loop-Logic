numbers = []

for n in range(1432, 9893323):
    if (n%250==0) and (n%400==0):

        numbers.append(str(n))

print (','.join(numbers))