import doctest

def matriz_identidad(matriz):
    '''
    >>> matriz_identidad([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
    True
    >>> matriz_identidad([[1,0,0,0],[0,1,0,0],[0,0,1,0],[2,0,0,1]])
    False
    >>> matriz_identidad([[1,0,0,0],[2,1,0,0],[0,1,0,0],[0,0,0,0]])
    False
    >>> matriz_identidad([[1,0,0,0],[0,1,0,0],[0,0,1,1],[0,0,0,1]])
    False
    '''
    valor = True
    largo_fil = len(matriz)
    num_fil = 0
    while valor and num_fil < largo_fil:
        sub_matriz = matriz[num_fil]
        can_0 = sub_matriz.count(0)
        if sub_matriz[num_fil] != 1 or can_0 != largo_fil-1:
            valor = False
        num_fil += 1
    return valor

def main():
    print(matriz_identidad([[0,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]))        

if __name__ == '__main__':
    doctest.testmod()
    main()
