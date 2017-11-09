import re # do w wyrazen regularnych
lines = []

try:
    file = open("PoliMorf-0.6.7.tab", "r", encoding="UTF-8")
except IOError:
    print("Nie ma takiego pliku")
lines = file.readlines()
mapa={}

#r.match("przeszukiwany string")
#r.search("przeszukiwany string")
r=re.compile("^kopark")
r2=re.compile(":pl")
for i in lines:
    mapa[i.split("\t")[0]]=i.split("\t")[2]    
try:
    for key in mapa:
        if(r.search(key)and r2.search(mapa[key]) ):
            print(key)
except KeyError:
    print("Nie ma takiego slowa. ")
        
    #print(key, mapa[key])
#while 1:
#    try:
#        var = input("Podaj se cos: ")
        #print(r.search(mapa
#        print(mapa[var])
#    except KeyError:
#        print("Nie ma takiego slowa")
#"ala" - gdziekolwiek slowo ala
#"^ala" - na poczatku stringa ala
#"ala$" - na koncu stringa ala
#"[ae]la" - dopasuje ela i ala, ale nie ula
#"[^ae]la" - dopasuje ula, ale nie ela i ala
#"([A-Z]([0-9])" - dopasuje A9, B6, ale nie 99, AA,
#"(al)*" - 0 lub wiecej -  dopasuje alalalal, dopasuje " ", "al", ale nie "bl", "zf"
#"(al)+" - 1 lub więcej wystapień "al"
#"(al)?" - 0 lub 1 wystapienie "al"
#a=r"\\" - wylaczenie obslugi znakow specjalnych
