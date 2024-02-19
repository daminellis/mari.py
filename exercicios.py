a = 12
b = 1.34
c = 1/5
d = True
e = 'abcd'
f = []  # lista
g = ()  # tupla
h = {}
i = 5 + 1j

print(f'ola {a} e {b}')

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))
print(type(i)) 

# faça um programa  que leia um valor em metros e passe para centimetros e milimetros
metro = float(input('Digite um numero em metros :'))
cent = metro * 100
mm = cent * 100

print (f' Seu numero em metros : {metro}\n  Seu numero em centimetro : {cent} \n  Seu numero em milimetro : {mm}')

=====================================================================================================================================
=====================================================================================================================================

disciplina = input('Digite a disciplina (iot ou banco): ')
pratica = float(input('Digite a nota da prova prática: '))
teorica = float(input('Digite a nota da prova teórica: '))

if disciplina.lower() == 'iot':
    maxpratica = 4
    maxteorica = 6
elif disciplina.lower() == "banco":
    maxpratica = 5
    maxteorica = 5
else:
    print('Disciplina inválida! Tente novamente')
    exit()

if pratica <= 0 or teorica <= 0:
    print('Algum número digitado foi negativo! Tente novamente')
elif pratica > maxpratica or teorica > maxpratica:
    print('Alguma nota digitada foi acima da nota máxima da disciplina! Tente novamente')
else:
    soma = pratica + teorica
    if soma > 10:
        print('Valor de 10 foi ultrapassado (inválida)')
    else:
        print(f'Sua nota na disciplina {disciplina} foi: {soma}')

=====================================================================================================================================
=====================================================================================================================================
