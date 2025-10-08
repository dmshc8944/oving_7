from data import emnekoder, tiden, studiepoenger, studieplan


def leg_til_emne_i_stidueplan(emne_index, semester):
    semester_index = semester - 1
    emne_tid = tiden[emne_index]

    for sem in studieplan:
        if emne_index in sem:
            print(f'Feil: emne {emnekoder[emne_index]} er allerede i studieplanen.')
            return False
        
    if emne_tid == 'høst' and semester not in [1,3,5]:
            print(f'Feil: høstemne {emnekoder[emne_index]} kan bare legges til i 1, 3 og 5 semester.')
            return False
    elif emne_tid == 'vår' and semester not in [2,4,6]:
            print(f'Feil: våremne {emnekoder[emne_index]} kan legges bare i 2, 4 og 6. semester.')
            return False
        


    total_studiepoeng = sum(studiepoenger[i] for i in studieplan[semester_index])
    if total_studiepoeng + int(studiepoenger[emne_index]) > 30:
        print(f'Feil: for mye studiepoeg i semester {semester}, total studiepoeg er {total_studiepoeng}/30 poeg.')
        return False
        

    studieplan[semester_index].append(emne_index)
    print(f'Emne {emnekoder[emne_index]} lagt til i semester {semester}.')
    return True



def vis_emner():
    for i, kode in enumerate(emnekoder):
        print(f'{i}: {kode}, {tiden[i]}, {studiepoenger[i]}')



def vis_studieplan():
     print('\nStudieplan:')

     for i, sem in enumerate(studieplan, start=1):
            if sem:
                print(f'\nSemester {i}:')
                total_studiepoenger = sum(studiepoenger[idx] for idx in sem)
                for idx in sem:
                    print(f' - {emnekoder[idx]} ({tiden[idx]}, {studiepoenger[idx]} studiepoenger)')
                print(f'Total: {total_studiepoenger} studiepoeng') 
        
            else:
                 print(f'\nSemester {i}: ingen emner')

