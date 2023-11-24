# GC DASHBOARD Modulo principale
from modules import gc_pianocartesiano_turtle_01, gc_pianocartesiano_tk, gc_pianocartesiano_dash

def menu():
    while True:
        print("\nDASHBOARD")
        print("1. Piano cartesiano turtle")
        print("2. Piano cartesiano tkinter")
        print("3. Piano cartesiano dash")
        print("X. Esci")

        scelta = input("Seleziona un modulo o digita 'X' per uscire: ").upper()

        if scelta == "1":
            pass
            #gc_pianocartesiano_turtle_01.disegna_cartesiano(x=0, y=0, lunghezza_assi=300, colore_assi="black", spessore_assi=2, dimensione_griglia=20)
        elif scelta == "2":
            gc_pianocartesiano_tk.disegna_cartesiano(0, 0, 500, "black", 2, 10)
        elif scelta == "3":
            gc_pianocartesiano_dash.app.run_server(debug=True)
        elif scelta == "X":
            break
        else:
            print("Opzione non valida. Riprova.")

if __name__ == "__main__":
    menu()
