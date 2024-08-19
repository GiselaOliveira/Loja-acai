# Apresentar mensagem de boas-vindas com nome
print("-"*2, "Boas-vindas a sorveteria da Gisela Oliveira ", "-"*2)
# Apresentar menu com opções de tamanho e sabor
print("-"*20, "Cardápio", "-"*20)
print("-"*50)
print("-" * 5, "|", "TAMANHO", "|", "CUPUAÇU (CP)",
      "|", "AÇAÍ (AC)", "|", "-" * 5)
print("-" * 5, "|", " " * 2, "P", " " * 2,  "|", " " * 1,
      "R$ 9,00", " " * 2, "|",  "R$ 11,00", " |", "-" * 5)
print("-" * 5, "|", " " * 2, "M", " " * 2,  "|", " " * 1,
      "R$ 14,00", " " * 1, "|",  "R$ 16,00", "" * 1, "|", "-" * 5)
print("-" * 5, "|", " " * 2, "G", " " * 2,  "|", " " * 1,
      "R$ 18,00", " " * 1, "|",  "R$ 20,00", "" * 1, "|", "-" * 5)
print("-" * 50)
# Acumulador para somar valores totais dos pedidos
valor_total = 0
# Apresentar variaveis para armazenar os valores dos produtos
cp_p = 9
cp_m = 14
cp_g = 18

ac_p = 11
ac_m = 16
ac_g = 20
while True:
    while True:
        # Apresentar um input perguntado o sabor desejado
        sabor = input("Entre com o sabor desejado (CP/AC):").upper()
        # Se o sabor escolhido for CP, solicitar o tamanho
        if sabor == 'CP':
            # Perguntar o tamanho ao cliente, P = pequeno, M = medio, G = grande
            tamanho = input("Informe o tamanho desejado (P / M / G): ").upper()

            # Se tamanho for P
            if tamanho == "P":
                print(f"Cupuaçu tamanho {tamanho}: R$ {cp_p: .2f}")
                # somar valor do pedido ao valor total
                valor_total += cp_p
                print()
                break

                # SE tamanho for M
            elif tamanho == "M":
                print(f"Cupuaçu tamanho {tamanho}: R$ {cp_m: .2f}")
                # somar valor ao total
                valor_total += cp_m
                print()
                break

                # Se tamanho for G
            elif tamanho == "G":
                print(f"Cupuaçu tamaho {tamanho}: R$ {cp_g: .2f}")
                # somar valor ao valor total
                valor_total += cp_g
                print()
                # Sair do loop para prosseguir ao pedido adicional
                break
            # Se tamanho invalido, apresentar mensagem e voltar ao loop
            else:
                print("Tamanho invalido. Tente novamente")
                print()
                continue

        # Se a escolhar for AC, entra na condição para perguntar o tamanho
        elif sabor == 'AC':
            # Perguntar o tamanho ao cliente P = pequeno M = medio G = grande
            tamanho = input("Informe o tamanho desejado (P / M / G): ").upper()

            # Se tamanho for P
            if tamanho == "P":
                print(f"Açaí tamanho {tamanho}: R$ {ac_p: .2f}")
                # somar valor do pedido ao valor total
                valor_total += ac_p
                print()
                break

                # Se tamanho for M
            elif tamanho == "M":
                print(f"Açai tamanho {tamanho}: R$ {ac_m: .2f}")
                # somar valor ao total
                valor_total += ac_m
                print()
                break

                # Se tamanho for G
            elif tamanho == "G":
                print(f"Açai tamanho {tamanho}: R$ {ac_g: .2f}")
                # somar valor ao valor total
                valor_total += ac_g
                print()
                # Sair do loop para prosseguir ao pedido adicional
                break

            # Se tamanho invalido, apresentar mensagem e voltar ao loop
            else:
                print("Tamanho invalido. Tente novamente")
                print()
                continue
        # Se sabor for invalido, apresentar mensagem e voltar ao loop
        else:
            print("Sabor invalido. Tente novamente")
            print()
            continue
    # Perguntar se o cliente deseja algo mais
    adicional = input(
        ("Deseja pedir mais alguma coisa? (S / N): \n")).upper()
    # Se a resposta for S, voltar ao loop
    if adicional == "S":
        continue
# Se a resposta for N, encerrar a compra
    else:
        break
# Apresentar valor total da compra
print(f"Valor total R$ {valor_total: .2f}")
