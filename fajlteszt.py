verseny_adatok = []

try:
    with open("F1-2024dec.csv" ,encoding="utf-8") as fajl:
        verseny_adatok = fajl.readlines()
        
except Exception as ex:
    print(f"Halihóóóó! : Hiba oka: {ex}")
except FileNotFoundError:
    print("Hiba a fájl megnyitása közben!")

print(verseny_adatok)


""""
    1. [] Megszámolás
    2. [] Eldöntés 1
       [] Eldöntés 2
    3. [] Kiválasztás
    4. [] Keresés
    5. [] Sorozatszámítás, összegzés 
    6. [] Minimum/maximum kiválasztás
    7. [] Másolás
    8. [] Kiválogatás
    9. [] Szétválogatás
    10 [] Metszet
    11.[] Unió 
    12. Rendezés
        [] Egyszerű cserés rendezés
        [] Buborékos
        [] Minimum kiválasztásos
"""

#----------------------------------------------------------
# 1. Hány versenyző nem szerzett még pontot?
db = 0

for i in range(1, len(verseny_adatok)):
    if(int(verseny_adatok[i].split(',')[1]) == 0):
        db = db + 1

print(f"{db} versenyző nem szerzett mép pontot.\n")

#----------------------------------------------------------
#2. Van-e Fernando nevű versenyző?

i = 0
while (i<len(verseny_adatok) and "Fernando" not in verseny_adatok[i]):
    i+=1
if (i<len(verseny_adatok)):
    print("Van fernando nevű versenyző")
else:
    print("Nincs Fernando nevű versenyző")

# 2.B Mindenki szerzett-e már 90 pontot?
i=0
while (i<len(verseny_adatok and int(verseny_adatok[i].split(";")[1]))>=90):
    i+=1
if i<len(verseny_adatok):










print("Itt a program vége")