#maak de functie
##Functie
def fibonacci(start, stop):
    
    a = 0 #het 0-de nummer hebben we nodig om te berekenen
    b = 1 #het 1ste nummer hebben we nodig om te rekenen
    f = [a,b]
    
    #eerst alle nummers berekenen tot -stop-+1
    for i in range(2,stop+1):  #(+1 omdat we eigenlijk bij 0 beginnen)
        a, b = b, a+b #nieuwe a en b bepalen
        f.append(b) #nieuwe nummer toevoegen aan lijst


    del f[:start] #de eerste -start- elementen verwijderen uit de lijst
    
    return(f) 

##Programma
#test de functie
fib_number = fibonacci(int(input("Bij welk nummer wil je beginnen?")), int(input("Bij welk nummer wil je stoppen?")))
print(fib_number)