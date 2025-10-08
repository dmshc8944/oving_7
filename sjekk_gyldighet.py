from lig_til_emne import studieplan, studiepoenger


def sjekk_gyldighet(data):
    # Plan er gyldig hvis alle emner er lik 30 poeng
    for semnr in range(1, 7):
        sp_sum = sum(data.emner[k].sp for k in data.plan[semnr])
        if sp_sum != 30:
            return False
    return True

def prompt_sjekk_gyldighet(data):
    print("\n=== 5) Sjekk om studieplanen er gyldig ===")
    if sjekk_gyldighet(data):
        print("Studieplanen er gyldig (alle semestre har 30 sp).")
    else:
        print("Studieplanen er ikke gyldig. (alle semestre har ikke 30 sp)")
