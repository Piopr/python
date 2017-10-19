tydzien=["poniedzialek","wtorek","sroda","czwartek","piatek","sobota","niedziela"]
plik = open("pliczek.txt", "w")

for x in tydzien:
   plik.write(x+"\n")    
plik.close()
plik2 = open("pliczek.txt", "r")

file = open("pliczek.txt", "r")
print(file.read())

             

