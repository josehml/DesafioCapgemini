def escada(n):
    asterisco = 1 # A função deve começar com "1" pois a escada começa com 1 "*"

    for asterisco in range(asterisco, n+1): # Varia a quantidade dos elementos nas linhas
        espaço = n - asterisco
        print(espaço * ' ' + asterisco * '*'); 

while True: # Loop para o algoritmo rodar indefinidamente
    n = int(input('Escolha o número de degraus da escada: ')) # Valor de entrada
    escada(n)