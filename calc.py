def calculadora(num1, num2, operacao):
    operacoes = {
        1: num1 + num2,
        2: num1 - num2,
        3: num1 * num2,
        4: num1 / num2 if num2 != 0 else "Divisão por zero não é permitida."
    }
    
    return operacoes.get(operacao, 0)

# Entrada de dados
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = int(input("Digite o número da operação (1:Soma, 2:Subtração, 3:Multiplicação, 4:Divisão): "))

resultado = calculadora(num1, num2, operacao)

print("Resultado:", resultado)