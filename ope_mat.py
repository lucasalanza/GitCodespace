# Recebe dois números do usuário
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Recebe a operação desejada
operacao = input("Digite a operação (+, -, *, /): ")

# Realiza a operação e armazena o resultado
if operacao == '+':
    resultado = numero1 + numero2
elif operacao == '-':
    resultado = numero1 - numero2
elif operacao == '*':
    resultado = numero1 * numero2
elif operacao == '/':
    if numero2 != 0:
        resultado = numero1 / numero2
    else:
        resultado = "Erro: Divisão por zero"
else:
    resultado = "Operação inválida"

# Exibe o resultado
print("Resultado: ", resultado)
