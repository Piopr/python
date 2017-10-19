file = open("PoliMorf-0.6.7.tab", "r", encoding="UTF-8")
#print(file.readline())
mapa = {}
for x in file:
    z = x.split("\t")    
    #z = x.readline()  
    mapa = {z[0] : z[1]}
    #print(z[1])
try:
    cz = input("Podaj slowo")
    print(mapa[cz])
except ValueError:
    print("Nie ma takiego slowa")
    #print(z[0])
    #print(z[1])

#with open("PoliMorf.txt", "r") as f:
 #       data = f.readlines()
        #print(data)

  #      for line in data:
   #         words = line.split()
    #        print(words)
    
