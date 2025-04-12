from estatisticas import leitor, analise

caminho = input ("Digite o caminho do csv: ")

dados = leitor.ler_csv(caminho)

print(f"Os campos dos CSV são: {[coluna for coluna in dados[0].keys()]}")

campo = input ("Qual campo voce deseja: ")

stats = analise.estatistica(dados, campo)

for chave, valor in stats.items():
    print(f"{chave}:{valor}")