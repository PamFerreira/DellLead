# Comparação de 5 lojas com a mesma lista de  presentes de casamento disponível.
presentes = {
    'cadeira', 'cafeteira', 'caneca', 'escumadeira',
    'espanador', 'espátula', 'estante', 'faqueiro',
    'frigideira', 'funil', 'halter', 'liquidificador',
    'notebook', 'panela', 'peneira', 'playstation',
    'rádio', 'smartphone', 'sofá', 'tablet', 'teclado',
    'televisão', 'vassoura', 'webcam', 'xbox',
}

loja1 = {
    'cadeira', 'cafeteira', 'caneca', 'escumadeira', 'estante',
    'frigideira', 'funil', 'liquidificador', 'notebook', 'panela',
    'playstation', 'smartphone', 'teclado', 'televisão'}
loja2 = {
    'cafeteira', 'escumadeira', 'espanador', 'frigideira', 'funil',
    'halter', 'peneira', 'playstation', 'sofá', 'tablet', 'televisão',
    'vassoura', 'webcam', 'xbox'}
loja3 = {
    'caneca', 'escumadeira', 'espanador', 'espátula', 'estante',
    'frigideira', 'halter', 'playstation', 'rádio', 'smartphone',
    'sofá', 'teclado', 'televisão', 'vassoura', 'xbox'}
loja4 = {
    'caneca', 'escumadeira', 'espanador', 'espátula', 'estante',
    'frigideira', 'halter', 'playstation', 'rádio', 'smartphone',
    'sofá', 'teclado', 'televisão', 'vassoura', 'xbox'}

total = loja1| loja2 | loja3 |loja4

print((presentes&total))

print((loja1&loja2&loja3&loja4))

print((presentes-total))

print(loja1-loja2-loja3-loja4)
print(loja2-loja1-loja3-loja4)
print(loja3-loja1-loja2-loja4)
print(loja4-loja1-loja2-loja3)

melhor_negocio =[(len(loja1)),(len(loja2)), (len(loja3)),(len(loja4))]
print(melhor_negocio[0:2])
