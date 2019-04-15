from datetime import datetime


##Functie

#Functie isprime(nummer), geeft 2 waardes terug: prime (bool) en number (int); het laagste getal waardoor gedeeld kan worden
#Als de waarde 1 is, is het dus prime en is de bool true, anders false

def isprime(testnum):
    
    prime= True
    start=datetime.now() #tijdstip bij begin uitvoeren
    number = 1
    
    for i in range(2,int(testnum**0.5 +1)): #de loop waar wordt getest op priem, hoeft maar t/m wortel van priemgetal
        if testnum % i == 0: #als het deelbaar is door -iets-: geen priem meer!
            prime = False
            number = i
            break
    
    print("Tijd verstreken: " + str(datetime.now()-start)) #tijdstip begin - tijdstip eind = verstreken tijd
    return(prime,number) #geef prime + deelgetal

##Uitvoeren functie    

b, d = isprime(int(input("Welk getal moet ik testen?")))
if b:
    print("Dit nummer is een priemgetal")
else:
    print("Dit is geen priemgetal, het is deelbaar door " + str(d))