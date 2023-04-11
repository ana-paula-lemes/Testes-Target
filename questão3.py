import json

#abre o arquivo 
with open("dados.json", encoding='utf-8') as my_json:
    dados = json.load(my_json)
    
#variaveis
valores = []
total = 0
cont = 0
dias = 0 

for i in dados: #coloco os valores dos faturamentos em um vetor e ja calculo o total juntamento com os dias 
    if i['valor'] != 0: # o faturamento foi maior que 0 
        valores.append(i['valor'])
        total = total + i['valor']
        cont = cont + 1

media_mensal = total/cont  #calculo da media 


for i in range(cont):
   
    if valores[i] > media_mensal:    #vejo quantos dias foram superiores a media mensal 
        dias = dias + 1

    if i == 0:        #indentificando o maior e menor faturamento
        maior = valores[i]
        menor = valores[i]
    if maior < valores[i]:
        maior = valores[i]
    if menor > valores[i]:
        menor = valores[i]
    
    
print(f'O menor valor de faturamento ocorrido em um dia do mês foi: R${menor}.')
print(f'O maior valor de faturamento ocorrido em um dia do mês foi: R${maior}.')
print(f'O mes teve {dias} dias com o faturamento diario maior que a media mensal.')
