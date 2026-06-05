n = int(input("Enter a number: "))
largest = 1

i = 2
while i <= n:
    while n % i == 0:
        largest = i
        n //= i
    i += 1

print("Largest Prime Factor:", largest)