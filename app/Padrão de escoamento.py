import matplotlib.pyplot as graf
import numpy as n

cores = ['#C5E1A5', '#F6AE2D', '#69A3D8', '#6D6875']
padroes = ['Segregado', 'Transição', 'Intermitente', 'Distribuído']

v = [0.0001, 0.01, 0.15, 0.4, 1]
#Função utilizada para gerar o gráfico
def gerargrafico(a1, a2, a3):
    # Chama a função grafico
    #somente algumas retornam pontos, pois esses serão utilizados para preencher as áreas dos gráficos
    p1 = grafico(v[0], v[1], 316, 0.302)  #início de l1
    p2 = grafico(v[1], v[3], 316, 0.302) #final de l1
    grafico(v[1], v[2], 0.000925, -2.4684)  #l2
    grafico(v[1], v[4], 0.1, -1.4516)  #l3
    p4 = grafico(v[3], v[4], 0.5, -6.738)  #l4

    #preenchimento das áreas do gráfico
    #a função preencher recebe os intervalos para cada preenchimento
    preencher(0, v[0], p1[0], 0.1, 1, v[2], p1[1], 0.1, cores[0], 0)
    preencher(1, v[2], p1[1],0.1, 1, 1, p1[1], 0.1, cores[1], 0)
    preencher(1, 1, p1[1], 0.1, 3, v[4], p2[1], p4[1], cores[2], 0)
    preencher(0, v[3], p1[0], p2[1], 3, v[4], p2[1], p4[1], cores[3], 1)

    #etiquetas do gráfico
    graf.xlabel("Hold Up NS")
    graf.ylabel("Número de Froude")
    graf.title("Padrão de escoamento")

    #define a escala logarítmica do gráfico
    graf.xscale('log')
    graf.yscale('log')

    #define os limites do gráfico
    graf.xlim(0.0001, 1)
    graf.ylim(0.1, 1000)

    #plota o ponto com a padrão como legenda
    graf.scatter(a1, a2, color='red')

    #cria a lefgenda do gráfico, usando as cores definidas
    legenda = []
    for i in range(len(cores)):
        legenda.append(
            graf.Line2D([0], [0], marker='s', color='w', markersize=10, markerfacecolor=cores[i], label=padroes[i]))

    graf.legend(handles=legenda, loc='upper left')

    #plota o gráfico
    graf.show()


#Função auxiliar para gerar o gráfico
def grafico(b1, b2, b3, b4):
    ponto = [] #pontos para preencher o as áreas dos gráficos
    y = [] #valores de y (Número de Froude)
    x = n.linspace(b1, b2) #intervalod de x
    tam = len(x)

    #para cada valor de x, haverá uma resultante em y
    for i in range(0, tam):
        aux = b3*(x[i]**b4)
        y.append(aux)

    #para cada chamda da função, gera a linha correspondente
    #algumas retornarão os pontos necessários para preencher o gráfico
    if(b2==0.01):

        #retorna o primeiro e último ponto de y
        #gera l1, no intervalo de 0.0001 a 0.4
        for i in range(0, tam):
            if(i==0 or i==tam-1):
                ponto.append(y[i])
        graf.plot(x, y, color='black')
        return ponto

    elif(b2==0.15):
        #gera l2
        graf.plot(x, y, color='black')
    elif(b2==0.4):

        #retorna o primeiro e último valor de y
        #gera l1, de 0.4 a 1
        for i in range(0, tam):
            if(i==0 or i==tam-1):
                ponto.append(y[i])
        graf.plot(x, y, color='black')
        return ponto

    elif(b2==1 and b1==0.01):
        #gera l3
        graf.plot(x, y, color='black')
    elif(b2==1 and b1==0.4):

        #retorna o primeiro e último ponto de y
        #gera l4
        for i in range(0, tam):
            if(i==0 or i==tam-1):
                ponto.append(y[i])
        graf.plot(x, y, color='black')
        return ponto

    else:
        return 0


#Função utilizada para calcular as linhas
def calcularl(c1, c2, c3):
    l = c1*(c3**c2)
    return l


def preencher(d1, d2, d3, d4, d5, d6, d7, d8, d9, d10):

    if(d10 == 0):

        # serão definidas duas retas, e preenchida a área entre elas
        # as retas são geradas por meio dos intervalos informados como argumentos da função
        x_curva1 = n.array([v[d1], d2])
        y_curva1 = n.array([d3, d4])
        x_curva2 = n.array([v[d5], d6])
        y_curva2 = n.array([d7, d8])

        # são concatenados os vaores, para se obter x e y
        x_total = n.concatenate((x_curva1, x_curva2[::-1]))
        y_total = n.concatenate((y_curva1, y_curva2[::-1]))
        #por meio da função fill, as áreas definidas são preenchidas
        graf.fill(x_total, y_total, color=d9)

    else:
        # serão definidas três retas, e preenchida a área entre elas
        # as retas são geradas por meio dos intervalos informados como argumentos da função
        x_curva3 = n.array([v[d1], d6])
        y_curva3 = n.array([1000, 1000])
        x_curva1 = n.array([v[d1], d2])
        y_curva1 = n.array([d3, d4])
        x_curva2 = n.array([v[d5], d6])
        y_curva2 = n.array([d7, d8])

        # são concatenados os valores, para se obter x e y
        x_total = n.concatenate((x_curva1, x_curva2, x_curva3[::-1]))
        y_total = n.concatenate((y_curva1, y_curva2, y_curva3[::-1]))

        graf.fill_between(x_total, y_total, max(y_total), color=d9)


def definirpadrao(e1, e2, e3, e4, e5, e6):

    #a função define o padrão ao definir em qual área do gráfico o par se encontra
    if (e5 >= 0.0001):
        if (e6 > 0.1):

            if (e5 <= 0.01 and e6 < e1):
                pad = padroes[0]
            elif (e5 > 0.01 and e5 <= 0.4):

                if (e6 <= e2):
                    pad = padroes[0]
                elif (e6 > l2 and e6 <= e3):
                    pad = padroes[1]
                elif (e6 > e3 and e6 <= e1):
                    pad = padroes[2]
                else:
                    pad = padroes[3]

            elif (e5 > 0.4):

                if (e6 <= e3):
                    pad = padroes[1]
                elif (e6 > e3 and e6 <= e4):
                    if (e5 <= 1):
                        pad = padroes[2]
                    else:
                        pad = 'Fora do intervalo'
                else:
                    pad = padroes[3]

            else:
                pad = padroes[3]
        else:
            pad = 'Fora do intervalo'
    else:
        pad = 'Fora do intervalo'

    return pad


#Código
g = 9.81
print("____________________Bem-Vindo____________________\n")
print("INFORMAÇÕES DOS FLUIDOS:")

#vazões
qo = float(input("Vazão de óleo: "))
qg = float(input("Vazão de gás: "))

#Diâmetro
print("\nINFORMAÇÕES DO DUTO:")
D = float(input("Diâmetro: "))

#Área
A = n.pi*(D**2)/4

#Velocidades
vo = qo / A
vg = qg / A
vm = vo + vg

#HoldUp NS / Número de Froude
HuNS = (vo/(vo+vg))
fr = ((vm**2)/(g*D))
fr2 = fr**2

#Linhas
l1 = calcularl(316, 0.302, HuNS)
l2 = calcularl(0.000925, -2.4684, HuNS)
l3 = calcularl(0.1, -1.4516, HuNS)
l4 = calcularl(0.5, -6.738, HuNS)

#Função que define o padrão de escoamento
padrao = definirpadrao(l1, l2, l3, l4, HuNS, fr2)

print(padrao)
print("__________________________________________________")

#Gerando o gráfico
gerargrafico(HuNS, fr2, padrao)