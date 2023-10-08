################################
# Autor: Theodore Kala Noubissi
################################
import pandas as pd
import openpyxl

gaesteListe = pd.DataFrame(columns=["Name"])
gaesteListe = pd.read_excel("gaeste_liste.xlsx")

while True:
    print("----------------------")
    print("Gäste verwalten")
    print("----------------------")
    print("1. Gast hinzufügen")
    print("2. Liste anzeigen")
    print("3. Gast löschen")
    print("4. Gästliste in Excel speichert")
    print("5. Programm beenden")
    
    auswahl = int(input("bitte ihre Auswahl: "))
    
    
    if auswahl == 1:
        gast = input("Name bitte eingeben: ")
        # Créez un DataFrame pour le nouveau nom et concaténez-le avec le DataFrame principal
        new_row = pd.DataFrame({"Name": [gast]})
        gaesteListe = pd.concat([gaesteListe, new_row], ignore_index=True)
        print(f"Neuer Gast: {gast}")

        # Sauvegardez le DataFrame dans un fichier Excel
        gaesteListe.to_excel("gaeste_liste.xlsx", index=False)
    elif auswahl == 2:
        print("------------ Aufgabe ----------")
        if len(gaesteListe) == 0:
            print("Die Liste ist Leer!!")
        else:
            for i, gast in enumerate(gaesteListe["Name"], start=1):
                print(f"{i}. {gast}")
        print("-------------------------------")
    elif auswahl == 3:
        number = int(input("bitte gaste Nummer eingeben: "))
        if number >= 1 and number <= len(gaesteListe):
            delete_gaste = gaesteListe.pop(number - 1)
            print(f"{delete_gaste} wurde gelöscht")
    elif auswahl == 4:
        df = pd.DataFrame(gaesteListe)
        df.to_excel("gaestliste.xlsx", index=False)
    elif auswahl == 5:
        print("Aufwiedersehen")
        break        
    