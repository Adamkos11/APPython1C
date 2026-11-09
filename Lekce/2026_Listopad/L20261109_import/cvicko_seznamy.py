import math
Jmeno = "Petr"
Věk = 30
print(f"Jméno: {Jmeno}, Věk: {Věk}")
numbers = [1, 2, 3, 4, 5]

numbers.append(6)
numbers.sort()
print(f"Seznam čísel: {numbers}")
print(f"První prvek seznamu: {numbers[0]}")
print(f"Poslední prvek seznamu: {numbers[-1]}")
# Slovníky a množiny

student = {
    "Jméno": "Bohdan",
    "Věk": 25,
    "Předměty": ["Matematika", "Fyzika"]

}

student ["Věk"] = 20
student ["Jméno"] = "Petr"
student ["Předměty"] = ["Matematika", "Fyzika", "Informatika"]
print("Student:", student)

data = [3,3,3,4,4,4,5,1,1,6,2,7,8,8,9,9,9]
unique_data = set(data)
print(f"Unikátní hodnoty: {unique_data}")

for i in range(1, 11):
    if i % 3 == 0:         # Číslo dělitelné 3
        print("Fizz")
    elif i % 5 == 0:       # Číslo dělitelné 5
        print("Buzz")
    else:
        print(i)

def vypocet_obvodu_telesa(delka, sirka=None):
    if sirka is None:
        sirka = delka
    return 2 * (delka + sirka)

delka = 5
sirka = 3
print(f"Obvod trojúhelníku s délkou {delka} a šířkou {sirka} je: {vypocet_obvodu_telesa(delka, sirka)}")

# Odmocnina 
odmocnina = math.sqrt(256)
print(f"Odmocnina z 256 je: {odmocnina}")

print(dir(math))