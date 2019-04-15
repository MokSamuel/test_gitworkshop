#Eerste while-loop: print de getallen 1 t/m 10
getal=1
while getal < 11:
    print(getal)
    getal = getal + 1
   

#Tweede while-loop: 100-a totdat er niks over is
totaal=100
aantal_keer=0
a=int(input("Welk getal?"))
while totaal > 0:
   totaal = totaal - a
   aantal_keer = aantal_keer + 1
   
print("Er is " +str(aantal_keer)+ " keer een loop uitgevoerd.")

