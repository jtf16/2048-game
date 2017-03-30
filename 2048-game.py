def cria_aux(arg):
    return isinstance(arg[0], int) and\
           isinstance(arg[1], int) and\
           arg[0]<5 and arg[0]>0 and\
           arg[1]<5 and arg[1]>0   

def cria_coordenada(l, c):
    '''cria_coordenada : int x int -> coordenada
       cria_coordenada constroi um dado do tipo coordenada'''
    if cria_aux((l, c)):
        return (l, c)
    else:
        raise ValueError ('cria_coordenada: argumentos invalidos')
    
def coordenada_linha(c):
    '''coordenada_linha : coordenada -> int
       coordenada_linha devolve a linha correspondente a coordenada introduzida'''
    return c[0]

def coordenada_coluna(c):
    '''coordenada_coluna : coordenada -> int
       coordenada_coluna devolve a coluna correspondente a coordenada introduzida'''    
    return c[1]

def e_coordenada(arg):
    '''e_coordenada : universal -> bool
       e_coordenada verifica se o argumento introduzido e uma coordenada ou nao'''    
    return isinstance(arg, tuple) and\
           len(arg) == 2 and\
           isinstance(arg[0], int) and\
           isinstance(arg[1], int) and\
           arg[0]<5 and arg[0]>0 and\
           arg[1]<5 and arg[1]>0           

def coordenadas_iguais(c1, c2):
    '''coordenadas_iguais : coordenada x coordenada -> bool
       coordenadas_iguais verifica se as coordenadas introduzidas correspondem a mesma posicao ou nao'''
    return c1==c2


def cria_tabuleiro():
    '''cria_tabuleiro : {} -> tabuleiro
       cria_tabuleiro devolve um tabuleiro com todas as posicoes a zero'''
    return [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], 0]

def tabuleiro_posicao(t, c):
    '''tabuleiro_posicao : tabuleiro x coordenada -> int
       tabuleiro_posicao devolve o valor presente na coordenada do tabuleiro introduzidos'''
    if c == ():
        return 0
    elif e_coordenada(c)==True:
        return t[c[0]-1][c[1]-1]
    else:
        raise ValueError ('tabuleiro_posicao: argumenos invalidos')
    
def tabuleiro_pontuacao(t):
    '''tabuleiro_pontuacao : tabuleiro -> int
       tabuleiro_pontuacao devolve a pontuacao para o tabuleiro introduzido'''
    return t[4]

def tabuleiro_posicoes_vazias(t):
    '''tabuleiro_posicoes_vazias : tabuleiro -> list
       tabuleiro_posicoes_vazias devolve uma lista que contem as coordenadas para as posicoes vazias do tabuleiro introduzido'''
    a = []
    i1 = 0
    while i1 < 4:
        i2 = 0
        while i2 < 4:
            if t[i1][i2]==0:
                a = a + [(i1 + 1, i2 + 1)]
                i2 = i2 + 1
            else:
                i2 = i2 + 1
        i1 = i1 + 1
    return a

def tabuleiro_preenche_posicao(t, c, v):
    '''tabuleiro_preenche_posicao : tabuleiro x coordenada x int -> tabuleiro
       tabuleiro_preenche_posicao modifica o tabuleiro, colocando o valor v na coordenada c'''
    if e_coordenada(c)==True and isinstance(v, int) and v >=0:
        t[c[0]-1][c[1]-1] = v
        return t
    else:
        raise ValueError ('tabuleiro_preenche_posicao: argumentos invalidos')
    
def tabuleiro_actualiza_pontuacao(t, v):
    '''tabuleiro_actualiza_pontuacao : tabuleiro x int -> tabuleiro
       tabuleiro_actualiza_pontuacao modifica o tabuleiro, acrescentando a pontuacao v pontos'''
    if isinstance(v, int) and v >= 0 and v % 4 == 0:
        t[4] = t[4] + v
        return t
    else:
        raise ValueError ('tabuleiro_actualiza_pontuacao: argumentos invalidos')
     
def tabuleiro_reduz(t, d):
    '''tabuleiro_reduz : tabuleiro x string -> tabuleiro
       tabuleiro_reduz modifica o tabuleiro do jogo, reduzindo-o para cima, baixo, esquerda ou direita de acordo com as regras do 2048'''
    x1 = tuple(t[0])
    x2 = tuple(t[1])
    x3 = tuple(t[2])
    x4 = tuple(t[3])
    if d == 'N' or d == 'S' or d == 'W' or d == 'E':
        if d == 'N':
            i1 = 0
            while i1 < 4:
                i2 = 1
                while i2 < 4:
                    if t[i2][i1] != 0:
                        if t[i2-1][i1] == 0:
                            t[i2-1][i1] += t[i2][i1]
                            t[i2][i1] = 0
                            if i2 != 1:
                                i2 -= 2                     
                    i2 += 1
                i1 += 1
            i1 = 0
            while i1 < 4:
                i2 = 1
                while i2 < 4:
                    if t[i2][i1] != 0:
                        if t[i2][i1] == t[i2-1][i1]:
                            t[i2-1][i1] += t[i2][i1]
                            t[i2][i1] = 0
                            tabuleiro_actualiza_pontuacao(t, int(t[i2-1][i1] + t[i2][i1]))
                    i2 += 1
                i1 += 1
            i1 = 0
            while i1 < 4:
                i2 = 1
                while i2 < 4:
                    if t[i2][i1] != 0:
                        if t[i2-1][i1] == 0:
                            t[i2-1][i1] += t[i2][i1]
                            t[i2][i1] = 0
                            if i2 != 1:
                                i2 -= 2                     
                    i2 += 1
                i1 += 1     
            return t
        elif d == 'S':
            i1 = 0
            while i1 < 4:
                i2 = 2
                while i2 >= 0:
                    if t[i2][i1] != 0:
                        if t[i2+1][i1] == 0:
                            t[i2+1][i1] += t[i2][i1]
                            t[i2][i1] = 0
                            if i2 != 2:
                                i2 += 2                     
                    i2 -= 1
                i1 += 1
            i1 = 0
            while i1 < 4:
                i2 = 2
                while i2 >= 0:
                    if t[i2][i1] != 0:
                        if t[i2][i1] == t[i2+1][i1]:
                            t[i2+1][i1] += t[i2][i1]
                            t[i2][i1] = 0
                            tabuleiro_actualiza_pontuacao(t, int(t[i2+1][i1] + t[i2][i1]))
                    i2 -= 1
                i1 += 1
            i1 = 0
            while i1 < 4:
                i2 = 2
                while i2 >= 0:
                    if t[i2][i1] != 0:
                        if t[i2+1][i1] == 0:
                            t[i2+1][i1] += t[i2][i1]
                            t[i2][i1] = 0
                            if i2 != 2:
                                i2 += 2                     
                    i2 -= 1
                i1 += 1        
            return t            
        elif d == 'W':
            i2 = 0
            while i2 < 4:
                i1 = 1
                while i1 < 4:
                    if t[i2][i1] != 0:
                        if t[i2][i1-1] == 0:
                            t[i2][i1-1] += t[i2][i1]
                            t[i2][i1] = 0
                            if i1 != 1:
                                i1 -= 2                     
                    i1 += 1
                i2 += 1
            i2 = 0
            while i2 < 4:
                i1 = 1
                while i1 < 4:
                    if t[i2][i1] != 0:
                        if t[i2][i1] == t[i2][i1-1]:
                            t[i2][i1-1] += t[i2][i1]
                            t[i2][i1] = 0
                            tabuleiro_actualiza_pontuacao(t, int(t[i2][i1-1] + t[i2][i1]))
                    i1 += 1
                i2 += 1
            i2 = 0
            while i2 < 4:
                i1 = 1
                while i1 < 4:
                    if t[i2][i1] != 0:
                        if t[i2][i1-1] == 0:
                            t[i2][i1-1] += t[i2][i1]
                            t[i2][i1] = 0
                            if i1 != 1:
                                i1 -= 2                     
                    i1 += 1
                i2 += 1            
            return t            
        else:
            i2 = 0
            while i2 < 4:
                i1 = 2
                while i1 >= 0:
                    if t[i2][i1] != 0:
                        if t[i2][i1+1] == 0:
                            t[i2][i1+1] += t[i2][i1]
                            t[i2][i1] = 0
                            if i1 != 2:
                                i1 += 2                     
                    i1 -= 1
                i2 += 1
            i2 = 0
            while i2 < 4:
                i1 = 2
                while i1 >= 0:
                    if t[i2][i1] != 0:
                        if t[i2][i1] == t[i2][i1+1]:
                            t[i2][i1+1] += t[i2][i1]
                            t[i2][i1] = 0
                            tabuleiro_actualiza_pontuacao(t, int(t[i2][i1+1] + t[i2][i1]))
                    i1 -= 1
                i2 += 1
            i2 = 0
            while i2 < 4:
                i1 = 2
                while i1 >= 0:
                    if t[i2][i1] != 0:
                        if t[i2][i1+1] == 0:
                            t[i2][i1+1] += t[i2][i1]
                            t[i2][i1] = 0
                            if i1 != 2:
                                i1 += 2                     
                    i1 -= 1
                i2 += 1        
            return t             
    else:
        raise ValueError ('tabuleiro_reduz: argumentos invalidos')

def e_tabuleiro(arg):
    '''e_tabuleiro : universal -> bool
       e_tabuleiro verifica se o argumento corresponde a um tabuleiro ou nao'''
    if isinstance(arg, list) and len(arg)==5 and isinstance(arg[-1], int):
        l=1
        while l<=4:
            c=1
            while c<=4:
                if isinstance(tabuleiro_posicao(arg, (l, c)), int):
                    c=c+1
                else:
                    return False
            l=l+1
        return True
    return False

def tabuleiro_terminado(t):
    '''tabuleiro_terminado : tabuleiro -> bool
       tabuleiro_terminado verifica se o tabuleiro esta cheio e se estiver, se existem movimentos possiveis para o tabuleiro'''
    l=0
    while l<=3:
        c=0
        while c<=3:
            if t[l][c]==0:
                return False
            c=c+1
        l=l+1
    
    l=0
    while l<=2:
        c=0
        while c<=2:
            if t[l][c] == t[l][c+1]:
                return False
            c=c+1
        l=l+1
    return True
    
def tabuleiros_iguais(t1, t2):
    '''tabuleiros_iguais : tabuleiro x tabuleiro -> bool
       tabuleiros_iguais verifica se os dois tabuleiros introduzidos tem a mesma configuracao e pontuacao'''
    if e_tabuleiro(t1) and e_tabuleiro(t2):
        return t1 == t2

def escreve_tabuleiro(t):
    '''escreve_tabuleiro : tabuleiro -> {}
       escreve_tabuleiro faz a representacao externa do tabuleiro introduzido'''
    if e_tabuleiro(t):
        print('[', tabuleiro_posicao(t, (1,1)), ']', '[', tabuleiro_posicao(t, (1,2)), ']', '[', tabuleiro_posicao(t, (1,3)), ']', '[', tabuleiro_posicao(t, (1,4)), '] \n'+\
              '[', tabuleiro_posicao(t, (2,1)), ']', '[', tabuleiro_posicao(t, (2,2)), ']', '[', tabuleiro_posicao(t, (2,3)), ']', '[', tabuleiro_posicao(t, (2,4)), '] \n'+\
              '[', tabuleiro_posicao(t, (3,1)), ']', '[', tabuleiro_posicao(t, (3,2)), ']', '[', tabuleiro_posicao(t, (3,3)), ']', '[', tabuleiro_posicao(t, (3,4)), '] \n'+\
              '[', tabuleiro_posicao(t, (4,1)), ']', '[', tabuleiro_posicao(t, (4,2)), ']', '[', tabuleiro_posicao(t, (4,3)), ']', '[', tabuleiro_posicao(t, (4,4)), '] \n'+\
              'Pontuacao: ', t[4])
    
    else:
        raise ValueError ('escreve_tabuleiro: argumentos invalidos')
