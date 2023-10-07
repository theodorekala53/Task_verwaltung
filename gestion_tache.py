################################
# Aufgabe verwalten
# Autor: Theodore Noubissi Kala
# Pogrammiersprache: Python
################################
import pandas as pd
import openpyxl
# eine Liste erstellen um die Aufgabe zu speichern 
aufgabe_liste = []


while True:
    # Menu Anzeigen
    print("-------------------------------")
    print("Aufgabe verwaltung")
    print("-------------------------------")
    print("1. Aufgabe hinzufügen")
    print("2. Aufgabe Anzeigen")
    print("3. Aufgabe löschen")
    print("4. Ergebnise in excelfile speichern")
    print("5. Programm beenden")
    
    auswahl = input("--> Option auswählen:")
    
    if auswahl == "1":
        task = input("aufgabe eingeben: ")
        print(f"Neue Eingabe: {task}")
        entscheidung = input("wollen sie Speichern (y/n)?: ")
        if entscheidung == "y":
            aufgabe_liste.append(task)
            print("Aufgabe gespeichert!!!")
        else:
            continue
    elif auswahl == "2":
        print("------------ Aufgabe ----------")
        if len(aufgabe_liste) == 0:
            print("Die Liste ist leer!!")
        for i, task in enumerate(aufgabe_liste, start=1):
            print(f"{i}. {task}")
        print("-------------------------------")
    elif auswahl == "3":
        if len(aufgabe_liste) == 0:
            print("Die Liste ist leer!!")
        number = int(input("AufgabeNummer eingebenn: "))
        if number >= 1 and number <= len(aufgabe_liste):
            gelöcsht_Auf = aufgabe_liste.pop(number - 1)
            print(f"sie haben {gelöcsht_Auf} gelöscht")
        else:
            print("die ausgewählte Nummer ist falsch")
    elif auswahl == "4":
        df = pd.DataFrame(aufgabe_liste)
        df.to_excel("GästeListe.xlsx")
    elif auswahl == "5":
        print("aufwiedersehen!!")
        break