#Voorbeelduitwerking opgave 1.2

##Constantes definieeren om mee te vergelijken & rekenen
Zichtbaarlicht_onder=390
Violet = 450
Blauw = 495
Groen = 570
Geel = 590
Oranje = 620
Rood = 750
Zichtbaarlicht_boven=750

h = 6.62607004* (10 ** -34)
c = 299792458

##Input vragen
golflengte = float(input("Welke golflengte heeft de straling?"))

##Berekenen freq en energie
f = c/golflengte
E = h*f

print("De frequentie van deze straling is "+str(f)+" Hz")
print("De energie van deze straling is "+str(E)+" J")

##Indelen golflengte in kleur

if golflengte < Zichtbaarlicht_onder:
    print("Deze straling is niet zichtbaar (te lage golflengte)")
elif golflengte < Violet:
    print("Dit licht is violet")
elif golflengte < Blauw:
    print("Dit licht is blauw")
elif golflengte < Groen:
    print("Dit licht is groen")
elif golflengte < Geel:
    print("Dit licht is geel")
elif golflengte < Oranje:
    print("Dit licht is oranje")
elif golflengte < Rood:
    print("Dit licht is rood")
else:
    print("Deze straling is niet zichtbaar (te hoge golflengte)")