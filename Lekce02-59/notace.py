# Generátorová notace 

# vytvoření seznamu čtvercůp čísel od 0 do 9
squares = [x**2 for x in range(10)] 
print(f"Čtverce čísel od 0 do 9: {squares}")

mocnina = []
for x in range(10):
    mocnina.append(x**2)
    print(x, x**2)

words = ['Python', 'is', 'awesome']
uppercase_words = [word.upper() for word in words]
print(f"Slova převedená na velká písmena: {uppercase_words}")