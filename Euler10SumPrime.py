#Getting sum of all prime numbers below a number

def PrimeNo(n):
    i = 3
    count = 1
    prime = 2
    while i <= n:
        for x in range(3, int(i** 0.5)+1, 2):
            if i % x == 0:
                break
        else:
            prime += i
            count += 1
        
        i += 2
    
    return prime

final = PrimeNo(2000000)
print(final)