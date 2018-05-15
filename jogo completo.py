#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
# Módulos
import sys, pygame
from pygame.locals import *
from tkinter.constants import FALSE


#Variaveis
WIDTH = 900
HEIGHT = 500
MposX = 300
MposY = 240

cont=6   #Contador de imagens para ir trocando imagens
direc=True
i, j = 0, 0

xixf={}#X inicial e x final
Rxixf={}
#Os sprites e o verificador:
atak = {}
giro=False

parabola={}
salto = False
#Para Salto andando.?
salto_Par=False

#===========================================================
#=================IMAGEN====================================
 
#def Imagem pega a imagem e exige um segundo algumento como True para faze-la transparente 
def imagen(filename, transparent=False):
        try: image = pygame.image.load(filename)
        except pygame.error(message):
                raise SystemExit(message)
        #AS imagens serão convertidas para um modo interior do python
        image = image.convert()
        if transparent:
                #Pega a cor da posição 0,0 e passa o RLEACCEL para tranparência 
                color = image.get_at((0,0))
                image.set_colorkey(color, RLEACCEL)
        return image
#================================================================
#=========================TECLADO================================
def Teclado():

    global MposX
    global cont, direc, salto, salto_Par, giro
    
    #Key refere-se ao teclado, e get_pressed a alguma tecla precionada
    Teclado = pygame.key.get_pressed()

    #Se as teclas para, pular e andar, não forem precionadas, salto_Par é True
    if Teclado[K_q] and Teclado[K_d] and salto_Par==False:
        salto_Par=True

    elif Teclado[K_e]:
        giro=True
        cont+=1

    elif Teclado[K_q] and Teclado[K_a] and salto_Par==False:
        salto_Par=True

    #Aqui o cont só é alterado dentro dessa função
    elif Teclado[K_d] and salto==False and salto_Par==False:
        MposX+=4
        #Cont está somando +1 a cada ciclo do loop 
        cont+=1 #Contador de imagens para ir trocando imagens
        direc=True  #Para direita a direção será True, ou esqueda False.
    #Se LEFT for clicado e o resto for False:
    elif Teclado[K_a] and salto==False and salto_Par==False:
        MposX-=4
#Decide a velocidade, se cont for igual 6 a atualização da tela chega mais rápido, somei só +1 para não ficar acelerado de mais
        cont+=1
        direc=False

    elif Teclado[K_q] and salto==False and salto_Par==False:
        salto=True


    else:
        cont=6
        
        
    return

#========================SPRITE=====================================
#===================================================================
def sprite():
    global cont
    #Terá que recordar, primeiras duas são onde inicia e as duas 
    #ultimas onde terminan os pixels; vertical inicio, horizontal inicio
    #xixf[7]=(472,273,659,374) #imagen("Kyoko parada/menina01.png")           
    
    xixf[0]=(0,0,185,105)
    xixf[1]=(185,0,185,105)
    xixf[2]=(375,0,185,105)
    xixf[3]=(566,0,185,105)
    xixf[4]=(762,0,185,105)
    xixf[5]=(963,0,185,105)
    xixf[6]=(1160,0,185,105)
    xixf[7]=(1160,0,185,105)

##Se tentar passar uma imagem(nome da pasta/imagem) Dá erro porquê [] só recebe um dicionario como parâmetro   
    Rxixf[7]=(0,0,192,105)
    Rxixf[6]=(192,0,192,105)
    Rxixf[5]=(386,0,192,105)
    Rxixf[4]=(584,0,192,105)
    Rxixf[3]=(786,0,192,125)
    Rxixf[2]=(983,0,192,105)
    Rxixf[1]=(1174,0,192,105)
    Rxixf[0]=(1363,0,172,105)
    #Sprites do ataque giratório
    #atak[0]=(7,6,332,534)
    #atak[1]=(534,6,332,534)
    '''atak[2]=(87,6,332,534)
    atak[3]=(526,6,332,534)
    atak[4]=(156,6,332,534)
    atak[5]=(460,6,332,534)
    atak[6]=(138,6,332,534)
    atak[7]=(490,6,332,534)
    #atak[8]=()
'''



    p=6         #P define a velocidade da animação. atrasando-a am mais loops
    global i, j
    if cont==p:
        i, j = 0, 0
    #Image 0
    if cont==p*2:
        i, j = 1, 1
    # Image1
    elif cont==p*3:
        i, j = 2, 2
    #Image2
    elif cont==p*4:
        i, j = 3, 3
    #Image 3
    elif cont==p*5:
        i, j = 4, 4
    #Image 4
    elif cont==p*6:
        i, j = 5, 5
    #Image 5
    elif cont==p*7:
        i, j = 6, 6
    #Image 6
    elif cont==p*8 :
        j = 7
        cont = 0
    #Usamos o return para que a verificação volte desdo if primeiro! Senão ele tranca do i = 0
    return


def main():
    #global i, MposX, xixf
    #Chama todas as classes e módulos do pygame
    pygame.init()    
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Kyoko")
 
    fondo = imagen("mapa05.jpg") 
     
    player = imagen("Menina_Correndo/PraDireita.png",True)#Transforma a imagem para Transparente
    #Criamos variavel que recebe a imagem invertida; pelotransform.True inverte no horizontal, e false vertical 
    #player_inv=pygame.transform.flip(player,True,False);
    player_inv = imagen("Menina_Correndo/PraEsquerda.png",True)
    #player_atak = imagen("atak.png.",True)

    clock = pygame.time.Clock()
    
    global salto_Par
    abaixa=False
    abaixa_Par=False
    # el bucle principal del juego
    while True:
        #definidos o time em 60 segundos/Para que o jogo não va tão rápido
        time = clock.tick(60)
       
        sprite()
        Teclado()
        #Redefinimos o tamanha da imagem do tamanha que queremos
        fondo = pygame.transform.scale(fondo, (1000, 500))
        #blit coloca a imagem na posição 0,0
        screen.blit(fondo, (0, 0))
        

        global MposX, MposY,salto,giro,atak,j
        #Verificamos as duas variaveis boleanas para que não seja pintado duas vezes a imagem
        #Senão essa verificação passaria a imagem para screen e outra verificação a baixo passaria de novo
        if salto==False and salto_Par==False:
            if direc == True and salto==False: #Se direct for True 
                #Vai pintar a boneca das posições definidas em numero [i] de xixf
                screen.blit(player, ( MposX, MposY),(xixf[i]))
            if direc == False and salto==False:#Se direct for False pintaremos o player inverso
                #Vai pintar a boneca das posições definidas em numero [i] de Rxixf
                screen.blit(player_inv, ( MposX, MposY),(Rxixf[i]))

        #Quando acrescentar novo sprite como esse, verificar se todas as variaveis novas estão como globais
       # if giro == True and salto==False:
            #screen.blit(player_atak,(MposX, MposY),(atak[j]))

        #Salto Normal. Caso salto seja True entra na verificação 
        #Se salto ganhou True na função teclado então roda essa condição 
        if salto==True:
            if direc==True:
                screen.blit(player, (MposX, MposY),(xixf[4]))

            #O screen está pintando a imagem por essa verificaçao e de novo pelo if de baixo do salto
            if direc==False:
                screen.blit(player_inv, ( MposX, MposY), (Rxixf[4]))
            '''Na hora de trocar o MposY ou MposX atenção porque o critério de parada é
            MposY == 252, Se fosse 250 a soma de 160 de 4 em 4 não fecharia em 252. 
            Então cuidado ou some antes se a velocidade que MposY será acrencentado feche
            na condição if abaixo com o mesmo valor
            '''
            if abaixa==False:
                MposY-=4
    
            if abaixa==True:
                MposY+=4
            #Se salto for True MposY ira abaichar em +4 frames por loop
            if MposY==160:
                abaixa=True
                
            if MposY == 240:
                abaixa=False
                salto=False
        #===============================

        #SALTO PARA O LADO
        if salto_Par==True and direc==True:
            
            screen.blit(player, ( MposX, MposY),(xixf[4]))
            
            if abaixa_Par==False:
                MposY-=4
                MposX+=4

            if abaixa_Par == True:
                MposY+=4
                MposX+=2

            if MposY==160:
                abaixa_Par=True

            if MposY == 240:
                abaixa_Par=False
                salto_Par=False
        if salto_Par==True and direc==False:

            screen.blit(player_inv, (MposX, MposY),(Rxixf[4]))
            #Leva o pulo para esqueda
            if abaixa_Par==False:
                MposY-=4
                MposX-=4
            #Leva o pulo para direita
            if abaixa_Par==True:
                MposY+=4
                MposX-=4

            if MposY==160:
                abaixa_Par=True
            
            if MposY==240:
            #Tranca a condição salto_Par igual a True,
                abaixa_Par=False
                salto_Par=False
        #Ataques:
        #Para atualizala
        pygame.display.flip()
        
        # Posibles entradas del teclado y mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
   
    return 0
 

if __name__ == '__main__':
    main()
