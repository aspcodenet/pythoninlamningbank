#allAccounts = {"1212":120, "1215":500, "99123":3 }
allAccounts = {}

kontonummer = input("Ange ditt kontonummer:")
belopp = int(input("Ange belopp att sätta in:"))
if kontonummer in allAccounts:
    allAccounts[kontonummer] = allAccounts[kontonummer] + belopp
else:
    print("Ogiltigt kontonummer")

for kontonummer in allAccounts.keys():
    print(f"{kontonummer} - saldo: {allAccounts[kontonummer]}")

for saldo in allAccounts.values():
    print(f"saldo: {saldo}")

# for key,value in allAccounts.items():
#     print( key, value )


while True:
    print("1. Lista alla konton")
    print("2. Skriv ut hur många konton")
    print("3. Lägg till konto")
    print("4. Ta bort konto")
    print("5. Söka")
    action = input("Ange val:")
    if action == "2":
        print(f"Antal konton:{len(allAccounts)}")
    elif action == "1":
        for namn in allAccounts:
            print(namn)
    elif action == "3":
        namn = input("Ange namn på nya kontot")
        allAccounts.append(namn)
    elif action == "4":
        for index in range(0, len(allAccounts)):
            print(f"{index+1} {allAccounts[index]}")

        index = int(input("Ange nummer på kontot som ska tas bort:"))
        index = index -1
        del allAccounts[index]

    elif action == "5":
        searchQuery = input("Sök efter:").lower()
        for namn in allAccounts:
            lowerCaseNamn = namn.lower()
            index = lowerCaseNamn.find(searchQuery)
            if index != -1:
                print(namn)

