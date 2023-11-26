#=====> GPT PROMPT <=====#
'''
scrivi un programma python per un calcolatore statistico. 
il programma deve avere un menu testuale che chiede all'utente 
di inserire i dati necessari per calcolare le seguenti grandezze : 
media, mediana e moda. il programma deve inoltre plottare i risultati 
facendo scegliere tra i seguenti formati : grafico a barre, 
circolare o a torta, cartesiano e istogramma
'''

import statistics
import matplotlib.pyplot as plt

def calcola_media(dati):
    return statistics.mean(dati)

def calcola_mediana(dati):
    return statistics.median(dati)

def calcola_moda(dati):
    try:
        return statistics.mode(dati)
    except statistics.StatisticsError:
        return "Nessuna moda"

def genera_fibonacci(n):
    fibonacci = [0, 1]
    while len(fibonacci) < n:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    print("Sequenza Fibonacci: " + str(fibonacci))    
    return fibonacci

def genera_numeri_primi(n):
    numeri_primi = []
    numero_corrente = 2

    while len(numeri_primi) < n:
        if all(numero_corrente % primo != 0 for primo in numeri_primi):
            numeri_primi.append(numero_corrente)
        numero_corrente += 1
    print("Sequenza Numeri Primi: " + str(numeri_primi))
    return numeri_primi

def genera_sequenza_esponenziale(base, n):
    sequenza_esponenziale = [base ** i for i in range(n)]
    return sequenza_esponenziale

def mostra_grafico(dati, formato, opzione):
    plt.figure(figsize=(8, 6))

    if opzione == "dati_input" or opzione == "0":
        if formato == "barre" or formato == "1":
            plt.bar(range(len(dati)), dati, color='blue')
            plt.xlabel('Elementi')
            plt.ylabel('Frequenza')
            plt.title('Grafico a Barre dei Dati di Input')
        elif formato == "circolare" or formato == "2":
            plt.pie(dati, labels=range(len(dati)), autopct='%1.1f%%', startangle=140)
            plt.axis('equal')
            plt.title('Grafico Circolare dei Dati di Input')
        elif formato == "cartesiano" or formato == "3":
            plt.plot(dati, marker='o')
            plt.xlabel('Elementi')
            plt.ylabel('Valori')
            plt.title('Grafico Cartesiano dei Dati di Input')
        elif formato == "istogramma" or formato == "4":
            plt.hist(dati, bins=len(dati), color='green', edgecolor='black')
            plt.xlabel('Valori')
            plt.ylabel('Frequenza')
            plt.title('Istogramma dei Dati di Input')
    elif opzione == "media" or opzione == "1":
        # Aggiungi il codice per il grafico basato sulla media
        media = calcola_media(dati)
        plt.axhline(y=media, color='red', linestyle='--', label=f'Media: {media:.2f}')
        plt.plot(dati, marker='o', label='Dati di Input')
        plt.legend()
        plt.xlabel('Elementi')
        plt.ylabel('Valori')
        plt.title('Grafico della Media')
    elif opzione == "mediana" or opzione == "2":
        # Aggiungi il codice per il grafico basato sulla mediana
        mediana = calcola_mediana(dati)
        plt.axhline(y=mediana, color='green', linestyle='--', label=f'Mediana: {mediana:.2f}')
        plt.plot(dati, marker='o', label='Dati di Input')
        plt.legend()
        plt.xlabel('Elementi')
        plt.ylabel('Valori')
        plt.title('Grafico della Mediana')
    elif opzione == "moda" or opzione == "3":
        # Aggiungi il codice per il grafico basato sulla moda
        moda = calcola_moda(dati)
        plt.bar(moda.keys(), moda.values(), color='orange', label='Moda')
        plt.plot(dati, marker='o', label='Dati di Input')
        plt.legend()
        plt.xlabel('Elementi')
        plt.ylabel('Frequenza')
        plt.title('Grafico della Moda')
    elif opzione == "fibonacci" or opzione == "4":
        # Aggiungi il codice per generare e visualizzare la sequenza di Fibonacci
        n = int(input("Inserisci il numero massimo di elementi per la sequenza di Fibonacci: "))
        fibonacci_sequence = genera_fibonacci(n)
        plt.plot(fibonacci_sequence, marker='o', label='Sequenza di Fibonacci')
        for i, valore in enumerate(fibonacci_sequence):
            plt.text(i, valore, str(valore), ha='center', va='bottom')
        plt.legend()
        plt.xlabel('Indice')
        plt.ylabel('Valore')
        plt.title('Sequenza di Fibonacci')     
    elif opzione == "primi":
        # Aggiungi il codice per generare e visualizzare la sequenza di numeri primi
        n = int(input("Inserisci il numero massimo di elementi per la sequenza di numeri primi: "))
        numeri_primi_sequence = genera_numeri_primi(n)
        plt.plot(numeri_primi_sequence, marker='o', label='Numeri Primi')
        for i, valore in enumerate(numeri_primi_sequence):
            plt.text(i, valore, str(valore), ha='center', va='bottom')
        plt.legend()
        plt.xlabel('Indice')
        plt.ylabel('Valore')
        plt.title('Sequenza di Numeri Primi')     
    elif opzione == "esponenziale":
        # Aggiungi il codice per generare e visualizzare la sequenza esponenziale
        base = float(input("Inserisci la base della sequenza esponenziale: "))
        n = int(input("Inserisci il numero massimo di elementi per la sequenza esponenziale: "))       
        sequenza_esponenziale = genera_sequenza_esponenziale(base, n)   
        plt.plot(sequenza_esponenziale, marker='o', label='Sequenza Esponenziale')
        for i, valore in enumerate(sequenza_esponenziale):
            plt.text(i, valore, f"{base}^{i} - {valore}", ha='center', va='bottom')
        plt.legend()
        plt.xlabel('Indice')
        plt.ylabel('Valore')
        plt.title('Sequenza Esponenziale')

    else:
        print("Scelta non valida per l'opzione del grafico.")


    plt.show()

dati = []

def inserisci_dato():
    try:
        dati.extend(map(float, input("Inserisci dati numerici separati da spazio: ").split()))
    except ValueError:
            print("Errore: Inserisci un dato numerico valido.")

def main():
    
    while True:
        print("\n<<<<< GC CALCULATOR >>>>>")
        print("1. Inserisci dati")
        print("2. Calcola media")
        print("3. Calcola mediana")
        print("4. Calcola moda")
        print("5. Mostra grafico")
        print("6. Genera sequenza di Fibonacci")
        print("7. Genera sequenza numeri Primi")
        print("8. Genera sequenza esponenziale")
        print("0. Cancella tutti i dati")
        print("x. Esci")

        scelta = input("Scelta: ")

        if scelta == "1":
            inserisci_dato()
        elif scelta == "2":
            print(f"Media: {calcola_media(dati)}")
        elif scelta == "3":
            print(f"Mediana: {calcola_mediana(dati)}")
        elif scelta == "4":
            print(f"Moda: {calcola_moda(dati)}")
        elif scelta == "5":
            formato = input("Scegli il formato del grafico (barre : 1, circolare : 2, cartesiano : 3, istogramma : 4): ")
            opzione = input("Vuoi visualizzare il grafico dei dati di input o uno dei grafici calcolati? (dati_input :0 , media : 1, mediana : 2, moda : 3): ")
            mostra_grafico(dati, formato, opzione)
        elif scelta == "6":
            mostra_grafico(dati, None, "fibonacci")
        elif scelta == "7":
            mostra_grafico(dati, None, "primi")
        elif scelta == "8":
            mostra_grafico(dati, None, "esponenziale")
        elif scelta == "0":
            conferma = input("Sei sicuro di voler cancellare tutti i dati? (s/n): ")
            if conferma.lower() == "s":
                dati.clear()
                print("Dati cancellati.")
            else:
                print("Operazione annullata.")
        elif scelta == "x" or scelta=="X":
            break
        else:
            print("Scelta non valida. Riprova.")

if __name__ == "__main__":
    main()
