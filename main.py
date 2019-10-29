import math, os, sys
 
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
 
 
if __name__ == '__main__':
    os.system('clear')
#   valores = range(1, 16)
    valores = [7, 5, 3]
    calculos = {}
    calcular(valores, calculos)
    print ('VALORES INFORMADOS: %s' % valores)
    print ('SOMA => %d' % calculos['soma'])
    print ('MÉDIA => %.2f' % calculos['media'])
    print ('VARIÂNCIA => %.2f' % calculos['variancia'])
    print ('DESVIO PADRÃO => %.2f' % calculos['desvio_padrao'])