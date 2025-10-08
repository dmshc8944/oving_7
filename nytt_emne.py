from data import emnekoder, tiden, studiepoenger

def lag_nytt_emne():

    emnekode = input("Skriv inn emnekode f.eks. DAT120: ").upper()
    tid = input("Skriv inn semester tid H(øst)/V(år): ").lower()
    studiepoeng = int(input("Skriv inn studiepoenger: "))


    emnekoder.append(emnekode)
    tiden.append(tid)
    studiepoenger.append(studiepoeng)
    
    print(f'Emne {emnekode} ({tid}, {studiepoeng} studiepoeng) lagt til.\n')

