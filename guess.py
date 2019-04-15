import random

nummer= int(100*random.random()) #random nummer tussen 0-100
gok = int(input("Gok het nummer tussen de 0 en de 100: ")) #input van user vragen
pogingen = 1 #altijd 1 poging!

while gok != nummer: #als de gok niet goed is, doorgaan
    pogingen = pogingen+1 #een extra poging gedaan
    if gok > nummer:
        print("Je zit te hoog!")
    elif gok < nummer:
        print("Je zit te laag!")
    
    gok=int(input("Wat denk je dat het nummer is?")) #nog een keer vragen

if pogingen != 1: #niet in 1x goed?
    print("Goed geraden, na " + str(pogingen) +" pogingen! Het nummer was inderdaad "+str(nummer)+"!")
else:
    print("Wauw, in 1x goed!")
