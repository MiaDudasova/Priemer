def priemer():
    num1 = int(input("Zadaj prvé číslo: "))
    num2 = int(input("Zadaj druhé číslo: "))
    num3 = int(input("Zadaj tretie číslo: "))
    priemer = int((num1 + num2 + num3) / 3)

    return priemer

print(priemer())
