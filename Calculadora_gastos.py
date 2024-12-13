#Obtenção do salário

while True:
    try:
        Salário = float(input("Me informe o seu recebimento deste mês: "))
        if Salário < 1 or Salário > 200000:
            print("Salário invalido")
            continue
        break
    except ValueError:
        print("Numero invalido!")

#Gastos

while True:
    try:
        numero_de_vezes = int(input("Quantas vezes foi gasto o seu salário? "))
        if numero_de_vezes < 1 or numero_de_vezes > 200000:
            print("Numero invalido")
        break
    except ValueError:
        print("Numero invalido!")


total_gasto = 0

for i in range(numero_de_vezes):
    try:

         Valor_gasto = float(input(f"Valor gasto {i + 1}: "))
         total_gasto += Valor_gasto
    except ValueError:
        print("Valor inválido! Digite um número.")

#salario restante
        
salario_restante = Salário - total_gasto

#final

print(f"O seu salário restante é de {salario_restante:.2f}")
print(f"O seu gasto foi de {total_gasto:.2f}")

