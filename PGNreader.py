import os

def read_PGN(filename):
    partida_dict = {}
    with open(filename) as f:
        while True:
            linia = f.readline()
            if(len(linia)==0):
                continue
            if(linia[0]=='['):
                partida_dict[linia.split(' ')[0][1:]] = linia.split('"')[1]
            else:
                linia = f.readlines()
                break
    partida = ''
    for jugades in linia:
        partida= partida + jugades
    partida = partida.replace("\n", " ")
    resultat = partida.split(' ')[-1]
    partida = partida.split('.')
    
    partida.pop(0)
    for i in range(len(partida)):
        jugades = partida[i].split(' ')[1:3]
        if(jugades[-1]== partida_dict["Result"]):
            jugades = jugades[:-1]
        partida_dict[i+1] =  jugades
    return(partida_dict)




if __name__=="__main__":
    dirname = os.path.dirname(__file__)

    name = 'PGN\\1654968224771.pgn'
    filename = os.path.join(dirname,name)
    partida_dict = read_PGN(filename)
    print(partida_dict)