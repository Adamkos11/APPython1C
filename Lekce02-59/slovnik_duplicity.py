cisla_list = [1, 2, 4, 5, 6, 7, 8, 9, 1, 2, 4, 5]
unikatni_cisla = set(cisla_list)
print("Unikátní čísla:", unikatni_cisla)
print("Původní seznam čísel:", cisla_list)
print("Počet unikátních čísel:", len(unikatni_cisla))

prazdna_mnozina = set()
prazdna_mnozina.add(340)
prazdna_mnozina.add(2000)
print("Množina po přidání prvků:", prazdna_mnozina)

if 2120 in prazdna_mnozina:
    print("2120 je v množině.")
else:
    print("2120 není v množině.")

if 3 in unikatni_cisla:
    print("Číslo 3 je v množině unikátních čísel.")
else:
    print("Číslo 3 Není v množině unikátních čísel.")