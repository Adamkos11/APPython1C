for i in range(2, 10):
    for x in range(2, i):
        print(f"Kontroluji číslo {i} dělené {x}")
        if i % x == 0:
            break
    else:
        print(f"{i} ============ je PRVOČÍSLO ==========")