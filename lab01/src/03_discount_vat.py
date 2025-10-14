pip=float(input('prise(₽) '))
pop=float(input('discount(%) '))
popka=float(input('vat(%)-вещественные '))
base=pip * (1 - pop/100)
vat_amount=base * (popka/100)
total=base + vat_amount
print(base)
print(vat_amount)
print(total)