import random
velikost = 10
pole = [random.randint(1, 100) for i in range(velikost)]
print(f"Neuspořádané pole: {pole}")

for i in range(velikost -1, 0, -1):
    for j in range(0, i):
        if pole[j] > pole[j + 1]:
            pole[j], pole[j + 1] = pole[j + 1], pole[j]
print(f"Uspořádané pole: {pole}")