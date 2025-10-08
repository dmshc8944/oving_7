from data import emnekoder, tiden, studiepoenger, studieplan, filnavn

def lagre_studieplan_til_fil():
    with open(filnavn, "w", encoding="utf-8") as f:
        f.write("=== Emner ===\n")
        for i in range(len(emnekoder)):
            f.write(f"{emnekoder[i]} ({tiden[i]}) - {studiepoenger[i]} studiepoeng\n")

        f.write("\n=== Studieplan ===\n")
        for semester_index, emner_i_semester in enumerate(studieplan, start=1):
            f.write(f"Semester {semester_index}:\n")
            if emner_i_semester:
                for emne_index in emner_i_semester:
                    f.write(f"  - {emnekoder[emne_index]}\n")
            else:
                f.write("  (ingen emner)\n")
            f.write("\n")
    print(f"Studieplanen er lagret til '{filnavn}'.")

def lese_studieplan_fra_fill ():
     with open(filnavn, "r", encoding="utf-8") as f:
          read = f.read()
          print(read)
          return read




