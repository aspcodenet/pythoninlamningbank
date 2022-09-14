# fstring - var kom den ifrån??? 
age = "20"
print(age+"3")
age = 20
namn = "Stefan"
x = "Hej " + namn + " du är " + str(age) + " år gammal"
#     Hej 23 Stefan du är 20 år gammal    
x = f"Hej {12+11} {namn} du är {age} år gammal"
x = f"om 3 år är du {age+3} år gammal"
print(x)



print("Hej " + namn + " du är " + age + " år gammal")
print(f"Hej {namn} du är {age} år gammal")

for x in range(0,5):
    tal = input("Mata in tal" + x)



print(12+25)

#print("Hej",  namn, " du är ", age, " år gammal")




#telRegister = {"stefan":"070-121212","anna":"121221-12" }
telRegister = {}
while True:
    #0123456
    #stefan 070-121212
    # namnAndTelnr = input("Skriv in namn och telnr")
    # index = namnAndTelnr.find(' ')
    # namn = namnAndTelnr[0:index]
    # telnr = namnAndTelnr[index+1:]
    namn = input("Skriv in namn:")
    if namn in telRegister:
        print("Finns redan")
    else:
        telnr = input(f"Vilket telefonnummer har {namn}?")
        telRegister[namn] = telnr
        
    if len(telRegister) == 5:
        break

print("Telregister lookup")
while True:
    namn = input("Ange namn:")
    if namn in telRegister:
        telnr = telRegister[namn]
        print(f"Telnr:{telnr}")
    else:
        print("Finns ej i registret")  