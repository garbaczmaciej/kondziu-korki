numbers = []

a = input()
while a != "":
    numbers.append(int(a))
    a = input()


for number in numbers:
    if number % 2:
        print(number)

print()
