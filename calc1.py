def calculadora(num1, num2, operacao):
    if operacao == 1:
        return num1 + num2
    elif operacao == 2:
        return num1 - num2
    elif operacao == 3:
        return num1 * num2
    elif operacao == 4:
        if num2 != 0:  # Evita divisão por zero
            return num1 / num2
        else:
            return "Divisão por zero não é permitida."
    else:
        return "Essa opção não existe"

while True:
    print("Lista de operações:")
    print("1: Soma")
    print("2: Subtração")
    print("3: Multiplicação")
    print("4: Divisão")
    print("0: Sair")
    
    operacao = int(input("Digite o número da operação: "))
    
    if operacao == 0:
        print("Saindo da calculadora.")
        break
    
    if operacao < 1 or operacao > 4:
        print("Essa opção não existe")
        continue
    
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    
    resultado = calculadora(num1, num2, operacao)
    
    print("Resultado:", resultado)