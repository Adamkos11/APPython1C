import os

script_dir = os.path.dirname(os.path.abspath(__file__))
soubor_cesta = os.path.join(script_dir, 'data.txt')
print(f"Otevírám soubor v adresáři: {soubor_cesta}")

try:
    with open(soubor_cesta, "r", encoding="utf-8") as f:
        line = f.readline()
        while line:
            print(line.strip())
            line = f.readline()
except FileNotFoundError:
    print(f"Soubor {soubor_cesta} nebyl nalezen.")
