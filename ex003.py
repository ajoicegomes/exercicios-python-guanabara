# Solicita ao usuário que digite o primeiro número e armazena o valor na variável 'n1'
n1 = int(input('Digite um número: '))

# Solicita ao usuário que digite o segundo número e armazena o valor na variável 'n2'
n2 = int(input('Digite outro número: '))

# Realiza a soma dos números 'n1' e 'n2' e armazena o resultado na variável 's'
s = n1 + n2

# Exibe a soma dos números informados pelo usuário de forma formatada
# A função .format insere os valores de 'n1', 'n2' e 's' dentro da string
print(f'A soma entre {n1} e {n2} resulta em {s}.')


