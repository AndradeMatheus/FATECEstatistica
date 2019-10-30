import math
import os
import sys
import pandas as pd

valores = []
 
def calcular(valores=None, calculos=None):
    if valores:
        if valores.__class__.__name__ == 'list' and calculos.__class__.__name__ == 'dict':
            def somar(valores):
                soma = 0
                for v in valores:
                    soma += v
                return soma
 
            def media(valores):
                soma = somar(valores)
                qtd_elementos = len(valores)
                media = soma / float(qtd_elementos)
                return media
 
            def variancia(valores):
                _media = media(valores)
                soma = 0
                _variancia = 0
 
                for valor in valores:
                    soma += math.pow( (valor - _media), 2)
                _variancia = soma / float( len(valores) )
                return _variancia
 
            def desvio_padrao(valores):
                return math.sqrt( variancia(valores) )
                 
 
            calculos['soma'] = somar(valores)
            calculos['media'] = media(valores)
            calculos['variancia'] = variancia(valores)
            calculos['desvio_padrao'] = desvio_padrao(valores)
            
def desvioPadrao():
    while(True):
        entrada = input('Entre com os valores, separando-os por virgula\n pressione (Enter) | pressione \'c\' + (Enter) para calcular\n: ')
        if(entrada == 'c'):
            break

        for n in entrada.split(','):
            valores.append(int(n))

    os.system('cls')
    calculos = {}
    calcular(valores, calculos)
    print ('VALORES INFORMADOS: %s' % valores)
    print ('SOMA => %d' % calculos['soma'])
    print ('MÉDIA => %.6f' % calculos['media'])
    print ('VARIÂNCIA => %.6f' % calculos['variancia'])
    print ('DESVIO PADRÃO => %.6f' % calculos['desvio_padrao'])

def dadosAgrupados():
    df = pd.DataFrame(columns=["valor", "quantidade"])
    n = int(input("Entre com o número de agrupamentos: "))

    for _ in range(n):
        vl = input("Entre com o valor: ")
        qt = (int(input("Entre com a quantidade de valores para {}: ".format(vl))))
        df1 = pd.DataFrame(data=[[vl,qt]],columns=["valor", "quantidade"])
        df = pd.concat([df,df1], axis=0)

    df.index = range(len(df.index))
    print(df)

    desvioporgrupo = df.groupby(["valor"]).agg({"quantidade": ["std"]})
    print('Desvio por grupo: \n', desvioporgrupo)

    desvio = df.quantidade.std()
    print('\nDesvio: ', format(desvio))

    media = df.quantidade.mean()
    print('Media: ', format(media))

    dispersao = df.quantidade.skew()
    print('Dispersao: ', dispersao)

    soma = df.quantidade.sum()
    print('Soma: ', soma)

def main():
    while(True):
        menu = int(input('\n\nPara acessar o DesvioPadrao, entre com \'1\' e pressione (enter) \nPara acessar os DadosAgrupados, entre com \'2\': '))
        if(menu == 1):
            os.system('cls')
            desvioPadrao()
        elif(menu == 2):
            os.system('cls')
            dadosAgrupados()
        else:
            os.system('cls')
            print('Tente novamente.\n')
            
main()