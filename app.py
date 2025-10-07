# app.py
from nytt_emne import lag_nytt_emne 
#from 2 import leg_til_emne_i_stidueplan

def vis_meny():
    print("\n=== Studieplan-meny ===")
    print("1. Lag et nytt emne")
    print("2. Legg til et emne i studieplanen")
    print("3. Skriv ut alle emner")
    print("4. Skriv ut studieplanen")
    print("5. Sjekk om studieplanen er gyldig")
    print("6. Lagre til fil")
    print("7. Les fra fil")
    print("8. Avslutt")

def run():
    while True:
        vis_meny()
        valg = input("Velg (1-8): ").strip()
        if valg == "1":
            lag_nytt_emne()
        elif valg == "2":
            leg_til_emne_i_stidueplan()
        elif valg == "8":
            print("Ha det!")
            break
        else:
            continue


if __name__ == "__main__":
    run()