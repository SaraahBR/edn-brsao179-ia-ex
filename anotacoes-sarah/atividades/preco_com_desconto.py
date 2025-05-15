preco = float(input("Digite o preço do seu produto: R$ "))
desconto = float(input("Digite agora o percentual de desconto (%): "))

# Calcula o valor do desconto
valor_desconto = preco * (desconto / 100)
preco_final = preco - valor_desconto

print(f"Desconto: R$ {valor_desconto:.2f}")
print(f"Preço final com desconto: R$ {preco_final:.2f}")