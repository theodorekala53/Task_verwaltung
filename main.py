# Créez une liste vide pour stocker les tâches
liste_de_taches = []

while True:
    # Affichez le menu
    print("Gestionnaire de tâches")
    print("1. Ajouter une tâche")
    print("2. Afficher les tâches")
    print("3. Supprimer une tâche")
    print("4. Quitter")

    choix = input("Choisissez une option : ")

    if choix == "1":
        tache = input("Entrez la description de la tâche : ")
        liste_de_taches.append(tache)
        print("Tâche ajoutée.")

    elif choix == "2":
        print("Liste des tâches :")
        for i, tache in enumerate(liste_de_taches, start=1):
            print(f"{i}. {tache}")

    elif choix == "3":
        if len(liste_de_taches) == 0:
            print("La liste des tâches est vide.")
        else:
            numero = int(input("Entrez le numéro de la tâche à supprimer : "))
            if numero >= 1 and numero <= len(liste_de_taches):
                tache_supprimee = liste_de_taches.pop(numero - 1)
                print(f"Tâche supprimée : {tache_supprimee}")
            else:
                print("Numéro de tâche invalide.")

    elif choix == "4":
        print("Au revoir !")
        break

    else:
        print("Option invalide. Veuillez choisir une option valide.")
