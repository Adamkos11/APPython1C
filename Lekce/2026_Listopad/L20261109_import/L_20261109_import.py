import math

print(f"Číslo PI:{math.pi}")
print(f"Sinus 90 stupnu:{math.sin(math.pi/2)}")

def bezpecne_deleni(a, b):
    try:
        vysledek = a / b
    except ZeroDivisionError as zde:
        print(f"Chyba: {zde}")
        return None
    except Exception as e:
        zprava = f"Neočekávaná chyba{a} / {b}: {e}"
        raise Exception(zprava)
    finally:
        print("Dělení dokončeno")
        print(f"Tento blok se provede vždy.")
    return vysledek

print(bezpecne_deleni(10, 2))
print(bezpecne_deleni(10, 0))