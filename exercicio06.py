# Desafio

# Criar um programa para calcular o valor da gorjeta baseado no valor total da compra e da porcentagem desejada.

def calculando_gorjeta (valor_conta, porcentagem_gorjeta):
    gorgeta = valor_conta * (porcentagem_gorjeta)
    return round(gorgeta, 2)

total_conta = 100.00
porcentagem = 15
gorjeta = calculando_gorjeta(total_conta, porcentagem)
print(f"Para uma conta de R$:{total_conta: .2f}, a gorjeta de {porcentagem}% é R$:{gorjeta}")