import csv

def ler_csv(caminho):
    with open(caminho, newline="", encoding="utf-8") as file:
        leitor = csv.DictReader(file)
        
        dados = []
        for linha in leitor:
            for chave, valor in linha.items():
                linha[chave] = float(valor) 
            dados.append(linha)
            
    return dados
