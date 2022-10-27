def is_prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

numbers = []

a = input()
while a != "":
    numbers.append(int(a))
    a = input()


for number in numbers:
    if is_prime(number):
        print(number)
