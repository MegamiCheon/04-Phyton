num = int(input('Digite um número inteiro: '))
print('-'*20)
print('{}1{} para {}binário{}'.format('\033[34m', '\033[m', '\033[33m', '\033[m'))
print('{}2{} para {}octal{}'.format('\033[34m', '\033[m', '\033[33m', '\033[m'))
print('{}3{} para {}hexadecimal{}'.format('\033[34m', '\033[m', '\033[33m', '\033[m'))
print('-'*20)
base = int(input('Escolha a base para a conversão: '))
if base == 1:
    bi = bin(num)
    print('o resultado é {}'.format(bi)[2:])
elif base == 2:
    oc = oct(num)
    print('o resultado é {}'.format(oc)[2:])
elif base == 3:
    he = hex(num)
    print('o resultado é {}'.format(he)[2:])
else:
    print('opção inválida')
print('{}adeus...{}'.format('\033[4;31m', '\033[m'))
