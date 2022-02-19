def anagrama(palavra): # Função que encontra os anagramas da palavra escolhida
    substrings = []
        
    for i in range(0, len(palavra)):
        for j in range(1, len(palavra)):
            if palavra[i] == palavra[j] and i < j: # Procura a repetição de letras na palavra 

                if palavra[i] == palavra[i + 1]: # Procura caso as letras iguais estejam em sequência
                    seguida = palavra[i : i + 1]
                    substrings.append([seguida, seguida])

                else:
                    '''
                        Procura as seções da palavra que terminam ou começam com as letras repetidas
                        e as adiciona como um par dentro do array substrings

                        Adiciona, também, a letra em si já que pode ser permutada de lugar, assim
                        gerando mais um par de substrings possível
                    '''

                    letra = palavra[i : i + 1]
                    noInicio = palavra[i : j]
                    noFim = palavra[i + 1 : j + 1]
                    
                    substrings.append([letra, letra])
                    substrings.append([noInicio, noFim])
                    

    print(len(substrings)) # Mostra a quantidade de pares de substrings no terminal
    print(substrings) # Mostra quais são os pares no terminal

while True: # Loop para rodar indefinidamente
    
    palavra = str(input('Escreva uma palavra: ')).lower()
    anagrama(palavra) # 'ovo' ---> 2 [['o', 'o'], ['ov', 'vo']]
    