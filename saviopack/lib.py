def try_me(volume, preco):
    preco_final = (1000 * preco) / volume

    return (f'Preço por kg: R${preco_final:.2f}')

print('*** Preço por Kilo ***')
gramas = float(input('gramas: '))
preco = float(input('preço: '))

print(try_me(gramas, preco))
