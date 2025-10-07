def lag_nytt_emne(emnekoder=list(), tiden=list(), studiepoenger=list()):
    emnekoder.append(input("Skriv inn emnekode f.eks. DAT120: "))
    tiden.append(input("Skriv inn semester tid H(øst)/V(år): "))
    studiepoenger.append(input("Skriv inn studiepoenger: "))
    return emnekoder, tiden, studiepoenger

#print(lag_nytt_emne())