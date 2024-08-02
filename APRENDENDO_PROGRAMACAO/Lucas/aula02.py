competicao = [
    ('Equipe 1', [70, 85, 98, 89]),
    ('Equipe 2', [75, 78, 75, 95]),
    ('Equipe 3', [90, 75, 99, 84])
]

# Converte a lista de tuplas em um dicionário
competicao_dict = dict(competicao)

# Calcula a média dos pontos para cada equipe
medias = [(nome, sum(pontos)/ len(pontos))for nome, pontos in competicao_dict.items()]


# Ordena a lista de médias em ordem decrescente
# O método sort() modifica a lista no local e retorna None
# Portanto, você precisa usar a função sorted() se quiser criar uma nova lista ordenada
oredem_das_medias = sorted(medias, key=lambda x: x[1], reverse=True)

# Exibe a lista ordenada
print(oredem_das_medias)
