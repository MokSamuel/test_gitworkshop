#Voorbeelduitwerking 1.4

##Input vragen
a=float(input("Wat is a?"))
b=float(input("Wat is b?"))
c=float(input("Wat is c?"))


##Discriminant bepalen
D = b ** 2 - 4*a*c

##Uitwerken afhankelijk van discriminant
if D > 0:
    nulpunt_1=round((-b + D**0.5)/(2*a),2)
    nulpunt_2=round((-b - D**0.5)/(2*a),2)
    print("Twee nulpunten gevonden, x="+str(nulpunt_1)+" en x="+str(nulpunt_2))
elif D == 0:
    nulpunt=round((-b)/(2*a),2)
    print("1 nulpunt gevonden, x="+str(nulpunt))
else:
    print("Geen nulpunten gevonden")