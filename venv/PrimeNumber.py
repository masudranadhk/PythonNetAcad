def isPrime(num):
    if  (num==2 or num % 2 !=0) and (num==5 or num % 5 !=0)and (num==3 or num % 3 !=0):
        return True
    else:
        return False

for i in range(1, 20):
	if isPrime(i + 1):
			print(i + 1, end=" ")
print()