def verificar(senha): # Essa função identifica o número de caracteres está faltando

    caractere_faltando = 0 # Pré-definição de que a senha é ideal
    digito_faltando = 0
    minus_faltando = 0
    maius_faltando = 0
    especial_faltando = 0

    tamanho_senha = len(senha)

    if tamanho_senha < 6: # O tamanho é a restrição mais geral, portanto, é a primeira prioridade
        caractere_faltando = 6 - tamanho_senha

    if any(char.isdigit() for char in senha) == False: # Os "if"s são independentes, por isso não são "elif"s
        digito_faltando = 1
    if any(char.islower() for char in senha) == False:
        minus_faltando = 1
    if any(char.isupper() for char in senha) == False:
        maius_faltando = 1
    if any(char in "!@#$%^&*()-+" for char in senha) == False:
        especial_faltando = 1
    
    faltas = digito_faltando + minus_faltando + maius_faltando + especial_faltando # Une o conjunto de restrições específicas

    if faltas > caractere_faltando: # Escolhe a informação mais importante para enviar ao usuário
        print(faltas)
    else:
        print(caractere_faltando)

while True: # Loop para repetir o algoritmo indefinidamente

    palavra = str(input('Escolha uma senha: ')).strip()
    palavra.split()
    ''.join(palavra) # Os três métodos utilizados forçam a senha a não ter espaços por fora e por dentro

    verificar(palavra)