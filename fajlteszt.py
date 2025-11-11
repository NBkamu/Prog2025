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
while i<len(verseny_adatok) and int(verseny_adatok[i].split(",")[1])>=90:
    i+=1
if i==len(verseny_adatok):
    print("Van")
else:
    print("Nem")
    
3.#Melyik istálló pilótája a Yuki Tsunoda?
i=0
while verseny_adatok[i].split(",")[0]!="Yuki Tsunoda":
    i+=1
print("Yuki Tsunoda a",verseny_adatok[i].split(",")[2])

4.#Melyik csapatban volt Pierre Gasly
i=1
while i<=len(verseny_adatok) and "Pierre Gasly" not in verseny_adatok[i]:
    i+=1
if i<len(verseny_adatok):
    print("Pierre Gasly",verseny_adatok[i].split(",")[2].strip(), "csapatban van!")
else:
    print("Nincs ilyen versenyző")

5.#Számolja ki a versenyzők pontszámámak átlagát
S=0
for i in range(1, len(verseny_adatok)):
    S+=int(verseny_adatok[i].split(",")[1])
print(f"a versenyzők pontszámainak átlaga: {S/len(verseny_adatok)-1}") 
    
6.#
maxi=1
max=verseny_adatok[i].split(",")[1]
for i in range(3,len(verseny_adatok)):
    if verseny_adatok[i]>verseny_adatok[maxi]:
        maxi=i
        max=verseny_adatok[i]    
print(max)

7.#Min kiválasztás
mini=1
min=verseny_adatok[i].split(",")[1]
for i in range(2,len(verseny_adatok)):
    if verseny_adatok[i]<verseny_adatok[mini]:
        mini=i
        min=verseny_adatok[i]
print("A legkevesebb ponttal rendelkező versenyző: ", verseny_adatok[mini].split(",")[0])

#8.Kiválógatás (másik listába) ki van mclaren-be
db1=0
masik_lista=[]
for i in range(2,len(verseny_adatok)):
    if verseny_adatok[i].split(",")[2].strip()=="McLaren":
        db1+=1
        masik_lista[db1].append(verseny_adatok[i].split(",")[0])
print("McLaren",masik_lista)
print("Itt a program vége")

#9. Szétválogatás
#kinek nincs pontja?
dby=0
dbx=0
y=[]
x=[]
for i in range(1,len(verseny_adatok)):
    if(int(verseny_adatok[i].split(",")[1])>0):
        dby+=1
        y.append(verseny_adatok[i].split(",")[0])
    else:
        dbx+=1
        x.append(verseny_adatok[i].split(",")[0])
print(f"Van pontja: {y} \n\n , nincs pontja: {x}")

            