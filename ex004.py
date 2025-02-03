# Este programa solicita que o usuário digite uma entrada e verifica várias propriedades dessa string,
# como tipo, se é um número, se contém apenas letras, se está em maiúsculas, minúsculas, etc.

# Solicita ao usuário que digite algo e armazena na variável 'a'
a = input('Digite algo: ')

# Exibe o tipo do valor inserido
print('O tipo primitivo desse valor é', type(a))

# Verifica se a string contém apenas espaços
print('Só tem espaços?', a.isspace())

# Verifica se a string é um número
print('É um número?', a.isnumeric())

# Verifica se a string é alfabética
print('É alfabético?', a.isalpha())

# Verifica se a string é alfanumérica
print('É alfanumérico?', a.isalnum())

# Verifica se a string está em maiúsculas
print('Está em maiúscula?', a.isupper())

# Verifica se a string está em minúsculas
print('Está em minúscula?', a.islower())

# Verifica se a string está capitalizada
print('Está capitalizada?', a.istitle())
