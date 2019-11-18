
media_amostral=float(input('insira a média amostral(x): '))
var=int(input('Se a população for conhecida digite: 1, se for desconhecida: 2 '))
if var==1:
    tamanho_populacao=float(input('insira o número de elementos da população(N): '))
else:
    tamanho_populacao=1
tamanho_amostra=float(input('insira o  número de elementos da amostra(n): '))
desvio_padrao_normal=float(input('insira o desvio padrão normal(z): '))
desvio_padrao_amostral=float(input('insira o desvio padrão amostral(sx): '))

estimativa_pontual=media_amostral

if tamanho_amostra*100/tamanho_populacao>5 and var==1:
    erro_de_estimacao = (((tamanho_populacao-tamanho_amostra)/(tamanho_populacao-1))**(1/2))*desvio_padrao_normal*desvio_padrao_amostral/(tamanho_amostra**(1/2))
    print('bbb')
else:
    erro_de_estimacao = desvio_padrao_normal*(desvio_padrao_amostral/(tamanho_amostra**(1/2)))
    print('aaa')

estimativa_intervalar_0 = media_amostral - erro_de_estimacao
estimativa_intervalar_1 = media_amostral + erro_de_estimacao

print('Estimativa Pontual:',estimativa_pontual)
print('Estimativa Intervalar:',estimativa_intervalar_0,'até',estimativa_intervalar_1)
print('Erro:',erro_de_estimacao)
