numero = int(input("Digite um numero: "))

a = 0 
b = 1
soma = 0

while a<numero:
    soma = a + b
    a = b 
    b = soma
if(a == numero):
    print("O numero informado pertence a Sequencia de Fibonacci")
else:
    print("O numero informado não pertence a Sequencia de Fibonacci")
    
