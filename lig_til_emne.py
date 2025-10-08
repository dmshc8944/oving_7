emnekoder = ['DAT120','MAT100','KJE101','FYS120','DAT130']
tiden= ['høst','høst','høst','høst','vår']
studiepoenger = [10,10,5,5,10]


studieplan = [[] for _ in range(6)]


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
    if total_studiepoeng + studiepoenger[emne_index] > 30:
        print(f'Feil: for mye studiepoeg i semester {semester}, total studiepoeg er {total_studiepoeng}/30 poeg.')
        return False
        

    studieplan[semester_index].append(emne_index)
    print(f'Emne {emnekoder[emne_index]} lagt til i semester {semester}.')
    return True



#test
result1 = leg_til_emne_i_stidueplan(0,1)
print(result1,'\n')
result1 = leg_til_emne_i_stidueplan(4,2)
print(result1,'\n')
result1 = leg_til_emne_i_stidueplan(3,1)
print(result1,'\n')
result1 = leg_til_emne_i_stidueplan(1,2)
print(result1,'\n')
result1 = leg_til_emne_i_stidueplan(0,3)
print(result1,'\n')





#--------------------------------------------------------------------------------------------------------------------------

def lag_nytt_emne(emne, tid, studiepoeng):
    emnekoder.append(emne)
    tiden.append(tid)
    studiepoenger.append(studiepoeng)
    print(f'Emne {emne} lagt til i studieplanen.')


#test
lag_nytt_emne('MAT200', 'vår', '10')
print(f'Nye emner: {emnekoder}')
print(f'Antall emner: {len(emnekoder)}.')



print('\n')
print(leg_til_emne_i_stidueplan(1,1))
print(leg_til_emne_i_stidueplan(2,1))
print(studieplan)
lag_nytt_emne('TN110','høst',5)
print(leg_til_emne_i_stidueplan(6,1))



