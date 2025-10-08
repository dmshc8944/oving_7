# app.py
from nytt_emne import lag_nytt_emne
from lig_til_emne import leg_til_emne_i_stidueplan, vis_studieplan, vis_emner, sjekk_studiepoeng
from oppgave_7_del_6 import lagre_studieplan_til_fil, lese_studieplan_fra_fill




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
            print('Lag nye emner:')

            while True:
                lag_nytt_emne()
                svar = input("Skriv 'videre' for å gå tilbake til menyen, eller trykk Enter for å legge til et nytt emne: ").lower().strip()
                if svar == "videre":
                    break

        elif valg == "2":
            vis_emner()
            while True:
                emne_index = int(input('Velg emne med nummer: '))
                semester = int(input('Velg semester(1-6): '))
                leg_til_emne_i_stidueplan(emne_index, semester)

                svar = input("Skriv 'videre' for å gå tilbake til menyen, eller trykk Enter for å legge til et emne i studieplan: ").lower().strip()
                if svar == "videre":
                    break
        
        elif valg == '3':
            vis_emner()
        elif valg == '4':
            vis_studieplan()
        elif valg == '5':
            sjekk_studiepoeng(emne_index, semester)
        elif valg == '6':
            lagre_studieplan_til_fil()
        elif valg == '7':
            lese_studieplan_fra_fill()        
        elif valg == "8":
            print("Ha det!")
            break
        else:
            continue


if __name__ == "__main__":
    run()