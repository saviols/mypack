def try_me(volume, preco):
    preco_final = (preco * volume) / 1000

    return preco_final

print('*** Preço por Kilo ***')
gramas = input(float('gramas: '))
preco = input(float('preço: '))

try_me(gramas, preco)