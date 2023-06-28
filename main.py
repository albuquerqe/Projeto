import pygame 
import os 
import pickle
from tkinter import simpledialog
import sys


pygame.init()

largura = 800
altura = 500
tamanho = (largura, altura)
pygame.display.set_caption("SPACE MARKER DA ANA e Luiz")
gameDisplay = pygame.display.set_mode(tamanho)
meteoroSound = pygame.mixer.Sound("Space_Machine.mp3")
clock = pygame.time.Clock()

try: 
    pygame.mixer.music.load("Space_Machine.mp3")
    pygame.mixer.music.play(-1)
except pygame.error:
    print("Erro no audio")

icone_path = "space.png"
icone = pygame.image.load(icone_path)
pygame.display.set_icon(icone)    

save_file = "marcacoes.pickle"

def salvar_marcacoes(marcacoes):
    with open(save_file, "wb") as file:
        pickle.dump(marcacoes, file)

def carregar_marcacoes():
    if os.path.exists(save_file):
        with open(save_file, "rb") as file:
            return pickle.load(file)
    else:
        return {}
    
def excluir_marcacoes():
    if os.path.exists(save_file):
        os.remove(save_file)

estrela = carregar_marcacoes()

fonte = pygame.font.Font(None, 24)

try:
    fundo = pygame.image.load("bg.jpg")
    fundo = pygame.transform.scale(fundo, tamanho)
    fundo = fundo.convert()
except pygame.error:
    fundo = pygame.Surface(tamanho)
    fundo.fill((0,0,0))

white = (255,255,255)
black = (0,0,0)

rodando = True
while rodando:  
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            salvar_marcacoes(estrela)
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            item = simpledialog.askstring("Space","Nome da estrela:")
            if item is None:
                item = "desconhecido" + str(pos)
            estrela[item] = pos     
        elif evento.type == pygame.KEYUP:
            if evento.key == pygame.K_F10:
                salvar_marcacoes(estrela)
                print("Marcacoes salvas")
            elif evento.key == pygame.K_F11:
                estrela = carregar_marcacoes()
                print("Marcacoes carregadas")
            elif evento.key == pygame.K_F12:
                excluir_marcacoes()
                estrela = {}
                print("Marcacoes excluidas") 
            elif evento.key == pygame.K_ESCAPE:
                salvar_marcacoes(estrela)     
                pygame.quit()    
                sys.exit()   
    gameDisplay.blit(fundo,(0,0))

    for nome, posicao in estrela.items():
        pygame.draw.circle(gameDisplay, white, posicao, 10)
        texto = fonte.render(nome, True, white)
        gameDisplay.blit(texto, (posicao[0] + 15, posicao[1] - 10))
    pontos = list(estrela.values())  
    if len(pontos) >=2:
        for i in range(len(pontos)-1):
            pygame.draw.line(gameDisplay, white, pontos[i], pontos[i + 1], 2)   

    texto_salvar = fonte.render("Pressione F10 para salvar", True, white)
    texto_carregar = fonte.render("Pressione F11 para carregar", True, white)
    texto_excluir = fonte.render("Pressione F12 para excluir", True, white)
    gameDisplay.blit(texto_salvar, (10,10))
    gameDisplay.blit(texto_carregar, (10, 40))
    gameDisplay.blit(texto_excluir, (10, 70))
    pygame.display.update()

pygame.quit()        