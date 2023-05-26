
# 1 -Crie uma lista com os números pares de 1 a 10.

numeros_pares = [n for n in range(1,12) if n % 2 == 0]
print(numeros_pares)

#---------------------------------------------------------------
# 2 -Crie uma lista com os quadrados dos números de 1 a 10.

numeros_quadrados = [q * q for q in range(1,11)]
print(numeros_quadrados)

#------------------------------------------------------------
# 3 -Dada uma lista de palavras, crie uma nova lista contendo o tamanho de cada palavra.

palavras = ['banana','pera','abacaxi']
tamanho_palavras = [len(t) for t in palavras]
print(tamanho_palavras)

# 4 -Dada uma lista de números, crie uma nova lista apenas com os números maiores que 5.

maiores_q_5 = [m for m in range(10) if m > 5]
print(maiores_q_5)

# 5 -Crie uma lista com as letras maiúsculas de uma string.

nome = 'rafael'
letra_maiuscula = [l.upper() for l in nome]
print(*letra_maiuscula)

#6 -Dada uma lista de números, crie uma nova lista contendo apenas os números pares e maiores que 10.

maiores_q_10 = [m for m in range(22) if m % 2 == 0 and m > 10]
print(maiores_q_10)

# 7 -Dada uma lista de nomes, crie uma nova lista apenas com os nomes que começam com a letra "A".

nomes = ['Ana','Bruno','Rodrigo','Afonso','Rafael']
comecam_com_a = [l for l in nomes if l.startswith('A')]
print(comecam_com_a)

# 8 -Dada uma lista de frutas, crie uma nova lista com o comprimento de cada fruta, apenas para as frutas com mais de 5 letras.

frutas = ['acerola','morango','abacate','uva','pera','maçã']
maior_q_5 = [f for f in frutas if len(f) > 5]
print(maior_q_5)

# 9 -Dada uma lista de números, crie uma nova lista com o dobro de cada número, mas apenas se o número for ímpar

numeros_dobro = [n * n for n in range(10) if not n % 2 == 0]
print(numeros_dobro)