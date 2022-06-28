columnes = ['a','b','c','d','e','f','g','h']
files = ['1','2','3','4','5','6','7','8']
peces = ['','T','C','A','D','R']
enroc = ['0-0', '0-0-0']

totes_les_jugades=[]

for peza in peces:
    for fila in files:
        for columna in columnes:
            #Totes les jugades sense menjar
            if peza=='':
                if fila in ['1','8']:
                    for coronacio in peces[1:-1]:
                        totes_les_jugades.append(peza+columna+fila+'='+coronacio)
                else:
                    totes_les_jugades.append(peza+columna+fila)
            else:
                totes_les_jugades.append(peza+columna+fila)
            #Totes les jugades menjant
            if peza=='':
                
                if(columnes.index(columna)==0):
                    columnes_adjacents=['b']
                elif(columnes.index(columna)==7):
                    columnes_adjacents=['g']
                else:
                    columnes_adjacents=[columnes[columnes.index(columna)-1],columnes[columnes.index(columna)+1]]
                

                for columna2 in columnes_adjacents:
                    if fila in ['1','8']:
                        for coronacio in peces[1:-1]:
                            totes_les_jugades.append(peza+columna2+'x'+columna+fila+'='+coronacio)
                    else:
                        totes_les_jugades.append(peza+columna2+'x'+columna+fila)
            else:
                totes_les_jugades.append(peza+'x'+columna+fila)

print(totes_les_jugades)
print(len(totes_les_jugades))