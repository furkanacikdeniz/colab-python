from random import randint
liste1 = []
liste2 = []
liste3 = []
while len(liste1) < 10:

  deger = randint(1,5)
  liste1.append(deger)
  if deger % 2 == 0 :
    liste2.append(deger)
  if liste1.count(deger)>1 in liste1:
    liste3.append(deger)
print(f"Liste: {liste1}")
print(f"Listedeki çift sayıları tutan liste: {liste2}")
print(f"Listedeki tekrar eden sayılar: {liste3}")

