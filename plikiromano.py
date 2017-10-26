lines = []

try:
    file = open("PoliMorf-0.6.7.tab", "r", encoding="UTF-8")
except IOError:
    print("Nie ma takiego pliku")
lines = file.readlines()
mapa={}
for i in lines:
    mapa[i.split("\t")[0]]=i.split("\t")[1]
try:
    var = input("Podaj se cos")
    print(mapa[var])
except KeyError:
    print("Nie ma takiego slowa")
