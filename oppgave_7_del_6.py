emnekoder = ['DAT120','MAT100','KJE101','FYS120','DAT130']
tiden= ['høst','høst','høst','høst','vår']
studiepoenger = [10,10,5,5,10]

studieplan = [[] for _ in range(6)]

def lagre_studieplan_til_fil(filnavn="studieplan.txt"):
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

def lese_studieplan_til_fill (fillnavn = "studieplan.txt"):
     with open(fillnavn, "r", encoding="utf-8") as f:
          print(f.read())
          return f.read()
     
