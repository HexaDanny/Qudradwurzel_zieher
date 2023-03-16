from math import sqrt

def qudratwurzel_zieher():
    a = input("Bitte geben sie eine Zahl ein, aus der die Quadratwurzel gezogen werden soll.\nBestätigen Sie die Eingabe mit der Enter Taste. :")
    if a == str:
        a = input("Bitte wähle nur aus Dezimal und Ganzzahlen.")
    b = sqrt(float(a))

    if b % 1 == 0:
        print(f"Die Qudaratwurzel aus {a} ist {int(b)}")
    elif b % 1 >= 0:
        i = int(input("Auf wie viel Nachkommastellen soll gerundet werden? "))
        print(f"Die Quadratwurzel aus {a} ist ~ {round(b,i)}")

qudratwurzel_zieher()

