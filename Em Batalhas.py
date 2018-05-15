# -*- coding: utf-8 -*-
import pygame, sys
from pygame.locals import *
import time
import threading
global segundos, segundos2
segundos, segundos2 = 0, 0
#======================Variaveis das posições na tela======================
largura, altura = 900, 600
posX, posY = 450, 500
fundoX, fundoY = 240, 120
#==========================================================================
velocidade, speed = 3, 1

cont, cont2 = 9, 9
#=====================Variaveis dos Sprites==========================
#Para o player:
xixf, xixR, xixY, xixX, golpe_1 = {}, {}, {}, {}, {}
#Para o inimigo:
spritx, spritf, Eleft, Eright, Ecostas = {},{}, {},{},{}
#====================================================================
i, j = 0, 0
#posicao receberá de 1 a 4 para verificar qua direção será ativa na hora de andar. 
posicao, PosEnemy = 1, 0
# Para Inimigos:
X, Y = 400, 100
golpe, golpeEnemy, lutar = False, False, False

ataqueEnemy =  6
vidaEnemy = 500
N_Ememy = 'Selvagem'
#=====================Estatus do Personagem==================
Ataque, Vida, regenerar, Nome = 18, 500, 5, 'Valkíria'

AtaqueBase = True
""""
def crono():
    #Função para contar o tempo de carregamento das skills
    #Conta até cinco Mas não está funcionando
    global segundos2
    segundos2 = int(segundos2)
    hora = threading.Thread(target=crono, args=())
    hora.start()
    cronometro = fonteTime.render(segundos2,1)
    if segundos2 == 6:
        segundos2 = 0
        #return crono()
        if cronometro == 0:
            AtaqueBase = True
    else:
        print(segundos2)
        segundos2 += 1
        time.sleep(1)
    
        return crono()"""

def imagem(filename, transparent=False):
    '''Se queres por tranparent o fundo da imagem passada, coloque dois argumentos
    ,um é a imagem e outro é True, com vírgula assim:("image.png",True)'''
    try: image = pygame.image.load(filename)
    except pygame.error(message):
        raise SystemExit(message)

    image = image.convert()
    if transparent:
        color = image.get_at((0,0))#O RLEACCEL pegará a cor e retorna como transparent
        image.set_colorkey(color, RLEACCEL)
    return image
def fontes():
    pass
def Teclado():
    global posX, posY, cont, Poder, posicao, golpe, AtaqueBase
    teclado = pygame.key.get_pressed()

    
    if  pygame.KEYDOWN:
        # Para duas teclas pressionada
        if teclado[K_w] and teclado[K_a]:
            posY -= velocidade
            posX -= velocidade
            cont+=1
            posicao = 3
        if teclado[K_w] and teclado[K_d]:
            posY -= velocidade
            posX += velocidade
            cont += 1
            posicao = 4
        if teclado[K_a] and teclado[K_s]:
            posX -= velocidade
            posY += velocidade
            cont += 1
            posicao = 3
        if teclado[K_s] and teclado[K_d]:
            posX += velocidade
            posY += velocidade
            cont += 1
            posicao = 4
        
        else:
            
            if teclado[K_4]:
                golpe = True
                    #crono()
            #Quando duas teclas são clicadas está adicionando a soma do cont mais de uma vez, então
            #É importante verificar e corrigir para que ele não ultrapasse o limite para as verificações
            elif cont > 27:
                cont = 9
                
            elif teclado[K_a]:
                posX -= velocidade
                cont+=1
                posicao = 3
            elif teclado[K_d]:
                posX += velocidade
                cont+=1
                posicao = 4
            elif teclado[K_w]:
                posY -= velocidade
                cont+=1
                posicao = 1
            elif teclado[K_s]:
                posY += velocidade
                cont+=1
                posicao = 2

    #Retornar para efetuar uma só operação por loop
    return

def Sprite():
    global cont, cont2, j
    #No momento que coloca a posição inicial, dali pra frente cota-se os pixels X,Y a partir de zero novamente
    #anda para baixo
    xixf[0] = (8,0,40,52)
    xixf[1] = (60,0,40,52)
    xixf[2] = (115,0,40,52)
    #anda pra cima
    xixR[0] = (9,0,46,53)
    xixR[1] = (62,0,44,53)
    xixR[2] = (118,0,44,53)
    #Anda para esquerda
    xixY[0] = (8,0,42,53)
    xixY[1] = (67,0,44,53)
    xixY[2] = (119,0,44,53)
    #Anda para direita
    xixX[0] = (7,0,40,53)
    xixX[1] = (62,0,45,53)
    xixX[2] = (117,0,45,53)
    #Golpe de espada
    golpe_1[0]=(0,0,47,53)
    golpe_1[1]=(48,0,57,53)
    golpe_1[2]=(108,0,47,53)
#===========================================================
#==================Enemy Sprites============================
    #Virado para tela
    spritf[0]=(9,2,44,52)
    spritf[1]=(60,2,38,52)
    spritf[2]=(114,2,36,52)
    #virado para esquerda
    Eleft[0]=(9,2,31,52)
    Eleft[1]=(61,2,31,52)
    Eleft[2]=(115,2,31,52)
    #DE costas:
    Ecostas[0]=(8,1,36,52)
    Ecostas[1]=(59,0,37,52)
    Ecostas[2]=(113,1,35,53)
    #Para direita:
    Eright[0]=(14,0,32,52)
    Eright[1]=(67,0,33,52)
    Eright[2]=(119,0,36,52)

    #Agora os sprites do ataque:
    spritx[0]=(1,0,40,51)
    spritx[1]=(43,0,52,52)
    spritx[2]=(100,0,39,53)
    spritx[3]=(22,0,74,52)
    

    p=9
    global i
    if cont==p:
        i=0
    if cont==p*2:
        i=1
    if cont==p*3:
        i=2
        cont = 0

    global j
    if cont2==p:
        j=0
    if cont2==p*2:
        j=1
    if cont2==p*3:
        j=2
        cont2 = 0
    if cont2 > p*3:
        cont2 = 0

    return
def inimigos():
    #largura, altura = 900, 600
    global Y, X, j, posY, posX, PosEnemy, largura, altura, cont2, golpeEnemy, speed

    if 1 <= posX - X <= 120 or 1 <= X - posX <= 120 or 1 <= posY - Y <= 120 or 1 <= Y - posY <= 120:
        lutar = True
        if X < largura and posX < largura:
            if X > posX:
                X-=speed
                cont2 += 1
                PosEnemy = 4 #Inimigo para nossa esquerda
            if X < posX:
                X+=speed
                cont2 += 1
                PosEnemy = 3 #Inimigo para nossa direito
        if Y < altura and posY < altura:
            if Y < posY:
                PosEnemy = 1 #Inimigo Virado pra baixo
                Y+=speed
                cont2 += 1
            if Y > posY:
                Y -=speed
                cont2 += 1
                PosEnemy = 2 #Vira inimigo pra cima
    if(not(1 <= posX - X <= 120 or 1 <= X - posX <= 120 or 1 <= posY - Y <= 120 or 1 <= Y - posY <= 120)):  
        if X < 400:
            X += speed
        if X > 400:
            X -= speed
        if Y > 100:
            Y -= speed
        if Y < 100:
            Y += speed

    if golpeEnemy == False:
        #Além da comparação se está a menos de 20 pixel, tive que garantir e verificar que menor que Zero não vale
        if posX == X and posY == Y:
            #Caso o player esteja na mesma posição do inimigo. Inimigo Atacará na posição 2.
            golpeEnemy = True
            PosEnemy = 2
            return
        if 15 < (Y - posY) <= 40 and X == posX: 
            golpeEnemy = True
            PosEnemy = 2
            Y += speed
            return
        elif 15 < (posY - Y) <= 40 and X == posX:
            golpeEnemy = True
            PosEnemy = 1
            Y -= speed
            return
        elif 15 < (X - posX) <= 40 and Y == posY:
            golpeEnemy = True
            PosEnemy = 4
            X += speed
            return
        elif 15 < (posX - X) <= 40 and Y == posY:
            golpeEnemy = True
            PosEnemy = 3
            X -= speed
            return
        else: golpeEnemy = False

    return
def main():
    def crono():
        global segundos
        segundos = int(segundos)
        if segundos == 6:
            segundos = 0
            return crono()
        else:
            segundos += 1
            time.sleep(1)
            return crono()

    global i, xixf, X, Y, posX,posY,posicao,spritx, cont2, PosEnemy
    global golpe, spritf, Eleft, Eright, Ecostas, golpeEnemy, j, Vida
    global ataqueEnemy, Nome, vidaEnemy, segundos

    pygame.init()
    #tamanho da tela
    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("Em batalhas")
    #Visual do mapa    
    fundo = imagem('cenario 01.png')
    fundo = pygame.transform.scale(fundo, (900, 600))
    fundo.blit(fundo, (900,600))

    GU = imagem('girl/frente.png',True)
    GU2 = imagem('girl/costa.png',True)
    GU3 = imagem('girl/esquerda.png',True)
    GU4 = imagem('girl/direita.png',True)

    golpe1 = imagem('girl/atak.png',True)
    golpe1_inverso = pygame.transform.flip(golpe1,True,False);

    #GU = pygame.transform.scale(GU, (220,60))
    #Aqui já inicia com personagem pintado na tela sem precisar de alguma condição
    #tela.blit(GU, (posX,posY))

    Enemy = imagem('enemys/down.png',True)
    Enemy2 = imagem('enemys/right.png',True)
    Enemy3 = imagem('enemys/left.png',True)
    Enemy4 = imagem('enemys/up.png',True)
    E_atak = imagem('enemys/enemyAtak.png',True)
    atakDireita = imagem('enemys/AtakDireita.png',True)
#===========================FONTES==================================
    pygame.font.init()
    padrao = pygame.font.get_default_font()

    fonteVida = pygame.font.SysFont(padrao,45)
    lifeEnemy = pygame.font.SysFont(padrao,30)

    Name = pygame.font.SysFont(padrao,25)
    
#===================================================================
    clock = pygame.time.Clock()
    cont = 0
#=========================Do Cronometro=====================================
    fonteTime = pygame.font.SysFont("Arial",54,True,False)
    clock = pygame.time.Clock()
    cont = 0
    hora = threading.Thread(target=crono, args=())
    hora.start()
#=====================Jogo em Loop==================================
    while True:

        tempo = clock.tick(60)

        text = fonteVida.render('Hp  %i'%Vida,1,(255,255,255))
        text2 = lifeEnemy.render('Hp Inimigo  %i'%vidaEnemy,1,(255,255,255))
        NomePlayer = Name.render('{}'.format(Nome),1,(255,255,255))

#================Chama==Funções=================================
        Teclado()
        inimigos()
        Sprite()

        tela.blit(fundo, (0,0))
       # pygame.transform.scale((70, 190))
        if golpe == False:
            #Caso não haja ataque ele verifica que posição deve ser pintada
            if posicao == 2:
                tela.blit(GU,(posX, posY),(xixf[i]))
            if posicao == 1:
                tela.blit(GU2,(posX, posY),(xixR[i]))
            if posicao == 3:
                tela.blit(GU3,(posX, posY),(xixY[i]))
            if posicao == 4:
                tela.blit(GU4,(posX, posY),(xixX[i]))
        if golpe == True:
        #Verifica a posição que o golpe será pintado
        #Retornar a variavel golpe para False para que não fique no mesmo sprite
            if posicao == 2:
                tela.blit(golpe1,(posX-7, posY+2),(golpe_1[0]))
                golpe = False
            if posicao == 1:
                tela.blit(golpe1,(posX-1, posY),(golpe_1[2]))
                golpe = False
            if posicao == 3:
                tela.blit(golpe1_inverso,(posX-27, posY),(54,0,57,53))
                golpe = False
            if posicao == 4:
                tela.blit(golpe1,(posX, posY),(golpe_1[1]))
                golpe = False

        #tela.blit(poder, (posX+20, posY+20))
#=======================Para inimigo(s)============================
        if golpeEnemy == False:
            if PosEnemy == 1: #baixo
                tela.blit(Enemy,(X,Y),(spritf[j]))
            elif PosEnemy == 2: #cima
                tela.blit(Enemy4,(X,Y),(Ecostas[j]))
            elif PosEnemy == 3: #direita
                tela.blit(Enemy2,(X,Y),(Eright[j]))
            elif PosEnemy == 4: #esqueda
                tela.blit(Enemy3,(X,Y),(Eleft[j]))
        if golpeEnemy == True:
            #Retornar a variavel golpeEnemy para False para que não fique pressa ao mesmo sprite
            #Por que estava retorando dois spretes? porque um estava fora do if e retornava assim que fosse True
            if PosEnemy == 1:#5< Y - posY < 20: #baixo
                tela.blit(E_atak,(X,Y),(spritx[0]))
                if cont == 40:
                    Vida -= ataqueEnemy
                    cont = 0
                golpeEnemy=False
            if PosEnemy == 2: #cima
                tela.blit(E_atak,(X,Y),(spritx[2]))
                if cont == 40:
                    Vida -= ataqueEnemy
                    cont = 0
                golpeEnemy = False
            if PosEnemy == 3: #direita
                tela.blit(atakDireita,(X,Y),(spritx[3]))
                if cont == 40:
                    Vida -= ataqueEnemy
                    cont = 0
                golpeEnemy=False
            if PosEnemy == 4: #esquerda
                tela.blit(E_atak,(X-20,Y),(spritx[1]))
                if cont == 40:
                    Vida -= ataqueEnemy
                    cont = 0
                golpeEnemy=False
            cont += 1
        #Se Imprimir o texto antes do mapa, o texto ficará escondido atrás do mapa.
#==============================Textos=======================================
        tela.blit(NomePlayer,(posX-12,posY-15))
        tela.blit(text2,(largura-250,altura-580))
        tela.blit(text, (20,20))
#================= Do Cronometro ==========================
    #Pinta o que foi definido para cronometro e ,1 como True e (192,192,192) É a cor.
        cronometro = fonteTime.render(segundos,1,(128,128,255))
        tela.blit(cronometro,(largura/2,15))
        pygame.display.update()
        if cronometro == 0:
            Vida += regenerar

#===========================================================================
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    return 0

if __name__ == '__main__':
    main()
