faturamento = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

total = 0
for estado, valor in faturamento.items():
    total += valor
    
for estado, valor in faturamento.items():
    percentual = (valor / total) * 100 
    print(f"{estado} teve o faturamento de R${valor} que corresponde a {percentual:.2f}% do faturamento total.")