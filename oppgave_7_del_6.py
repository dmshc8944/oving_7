emnekoder = ['DAT120','MAT100','KJE101','FYS120','DAT130']
tiden= ['høst','høst','høst','høst','vår']
studiepoenger = [10,10,5,5,10]

def lagre_studieplan(fillnavn = "studieplan.txt"): 
    with open(fillnavn, "w", encoding="utf-8") as f:
        pass
    for i in range (len(emnekoder)):
        f.write(f"{emnekoder[i], {tiden[i], {studiepoenger[i]}}}")