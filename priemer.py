def priemer(pocet):
    sucet = 0
    for i in range(0, pocet):
        num = int(input("Zadaj číslo: "))
        sucet = sucet + num              
    priemer = int(sucet / pocet)

    return priemer

pocet = int(input("Koľko čísel chceš zadať: "))
print(priemer(pocet))
