valid = True
print("Bienvenue au restaurant DALAL JAMM")
commande = int(input("voulez vous faire une commande si oui tapez 1 non tapez 2: "))
if commande == 1:
        print("Merci pour votre choix:")
        choix = int(input("quel plat voulez vous choisir: \n1: Thiébou Djeune\n2: Yassa Poulet\n3: Souppou Kandia\n4: Maffé Viande\n5: Quitter\n"))
        if choix == 1:
                print("vous avez choisi Thiébou Djeune. Votre commande est en cours...")
        if choix == 2:
                print("vous avez choisi Yassa Poulet. Votre commande est en cours...")
        if choix == 3:
                print("vous avez choisi Souppou Kandia. Votre commande est en cours...")
        if choix == 4:
                print("vous avez choisi Maffé Viande. Votre commande est en cours...")
        if choix == 5:
                print("AU REVOIR!")

elif commande == 2:
        print("commande annulée. ")
else: 
        valid = False
        print("choix invalide.")

