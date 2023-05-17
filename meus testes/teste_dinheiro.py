valor = float(input("Custo do produto: " ))
quantidade = int(input("Quantidade de produto: "))
valorTotal = valor * quantidade 

if valorTotal >= 400:
    print("Um desconto de 40% sera aplicado")
    print("O total foi de", valorTotal * 0.6, "reais!")
elif valorTotal >= 300 and valorTotal <= 399:
    print("Um desconto de 30% sera aplicado")
    print("O total foi de", valorTotal * 0.7, "reais!")
elif valorTotal >= 200 and valorTotal <= 299:
    print("Um desconto de 20% sera aplicado")
    print("O total foi de", valorTotal * 0.8, "reais!")
elif valorTotal >= 100 and valorTotal <= 199:
    print("Um desconto de 10% sera aplicado")
    print("O total foi de", valorTotal * 0.9, "reais!")
else:
    print("Sem desconto disponivel")
    
    