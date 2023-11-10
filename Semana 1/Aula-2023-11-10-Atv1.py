import random

pontoMedio = 50

menores = []; maiores = []

for i in range(10):
    pix = random.randint(0, 100) # Limita o interfalo que seré gerado os números
    if(pix < pontoMedio):
        menores.append(pix)
    else:
        maiores.append(pix)

print("Menores: ", menores)
print("Maiores: ", maiores)

'''

';' é interpretado como quebra de linha

para ser interpretado como a mesma linha quando há quebra há duas opções:
() - usar parênteses: ele irá interpretar todo o conteúdo como uma única linha
\ - Usar barra invertida: ao ser inserido uma barra invertida no final da linha, alinha abaixo é interpretada como uma continuação.

'''