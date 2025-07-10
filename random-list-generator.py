from random import randint
ana_liste = []    
cift_sayilar = []
tekrar_edenler = []

while len(ana_liste) < 10:
    sayi = randint(1, 5)
    ana_liste.append(sayi)

for sayi in ana_liste:
    if sayi % 2 == 0:
        cift_sayilar.append(sayi)
    if ana_liste.count(sayi) > 1 and sayi not in tekrar_edenler:
        tekrar_edenler.append(sayi)

print(f"Liste: {ana_liste}")
print(f"Çift sayılar: {cift_sayilar}")
print(f"Tekrar eden sayılar: {tekrar_edenler}")
