#Oefenopgave 1
totaal=0
#let op: 1 t/m 41 range anders sla je een stap over omdat je niet bij 0 begint!
for i in range(1,41): 
    totaal=totaal+i
    
print(totaal)

#Oefenopgave 2
#lege lijst aanmaken
tafel=[]

for j in range(1,21):
    tafel.append(j*21)

print(tafel)

#Oefenopgave 3
#vraag om de input
rijen=int(input("Hoeveel rijen?"))


#begin de loop: iedere rij langslopen, begin bij rij 1, eindig bij rijen+1
for i in range(1, rijen+1): 
    rij=[]                  #maak een legel lijst aan voor deze rij
    for j in range(1,i+1):  #in deze rij: vul met 1,2,3 als het de 3e rij is bv
        rij.append(j)       #append is een lijst-functie om nummer toe tevoegen
    print(rij)              #rij is klaar, laat zien
    
