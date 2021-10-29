filepath = "valaszok.txt"
fileobject = open(filepath, "r")
helyes = fileobject.readline()
a = []
for i in range(303):
    a.append(str(fileobject.readline()))
fileobject.close()
print(len(a))
print("1. feladat: Az adatok beolvasása.")
print("2. feladat: A versenyen", len(a), "versenyző indult.")
az = input("3.feladat: Kérem adja meg a versenyző azonosítóját: ")
szam = 0
id = ""
x=0
sz=0
h=0
for i in a:
    id = a[x]
    if az == id[0: 5]:
        print(az)
        h=x
        sz=1
    x+=1
if sz==0:
    print("Nem indult ilyen számmal versenyző")
elif sz>0:
    id=a[h]
    print(id[6:20])
print("4. feladat: A helyes megoldás:")
print(helyes)
veg=""
if(sz>0):
    id=a[h]
    for i in range(14):
        akt = 6 + i
        if helyes[i]==id[akt]:
            veg+="+"
        else:
            veg += " "

elif sz==0:
    id = a[0]
    for i in range(14):
        akt = 6 + i
        if helyes[i] == id[akt]:
            veg += "+"
        else:
            veg += " "
print(veg)
jo=0
osz=0

fs = int(input("5. feladat: Kérem adja meg a feladat sorszámát: "))
print(fs)
x=0

id=a[x]
szam = id[6:20]
for i in a:
    id=a[x]
    szam = id[6:20]
    if helyes[fs]==szam[fs]:
        jo+=1
        osz+=1
    else:
        osz+=1
    x+=1
print("A feladatra ",jo," fő, a versenyzők", round(jo/osz*100),"%-a adott helyes választ.")

print("6. feladat: A versenyzők pontszámának meghatározása.")
er=[]
ner=[]
x=0
y= 0
vsz=0
szam=""
for i in a:
    id=a[x]
    szam=id[6:20]
    for j in range(12):
        if (helyes[y] == szam[y] and y >= 0 and y <= 4):
            vsz += 3
        if (helyes[y] == szam[y] and y >= 5 and y <= 9):
            vsz += 4
        if (helyes[y] == szam[y] and y >= 10 and y <= 12):
            vsz += 5
        if (helyes[y] == szam[y] and y == 13):
            vsz += 6
        y+=1
    er.append(vsz)
    x+=1
z=0
for i in er:
    ner.append(a[z])
    ner.append(er[z])
    z+=1
j=0
el=0
mas=0
harm=0
max=0
g=0
for i in range (3):
    for i in ner:
        if  j%2==1 and ner[j]>max and ner[j]!=el and ner[j]!=mas:
            max=ner[j]
    if g==0:
        el=max
    if g==1:
        mas=max
    if g==2:
        harm=max
    g+=1
l=0
for i in ner:
    if ner[l]==el:
        print("1. díj (",el ,"pont): ",ner[l-1])
    if ner[l]==el:
        print("2. díj (",mas ,"pont): ",ner[l-1])
    if ner[l]==el:
        print("1. díj (",harm,"pont): ",ner[l-1])
    l+=1
