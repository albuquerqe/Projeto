import pygame 
import os 
import pickle
from tkinter import simpledialog
import sys


pygame.init()

largura = 800
altura = 500
tamanho = (largura, altura)
tela = pygame.display.set_mode(tamanho)
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

try: 
    pygame.mixer.music.load("Space_Machine.mp3")
    pygame.mixer.music.play(-1)
except pygame.error:
    print("Erro no audio")

icone_path = "space.png"
icone = pygame.image.load(icone_path)
pygame.display.set_icon(icone) 

icone_path = "space.png"
icone = pygame.image.load(icone_path)
pygame.display.set_icon(icone)    

save_file = "marcacoes.pickle"

def salvar_marcacoes(marcacoes):
    with open(save_file, "wb") as file:
        pickle.dump(marcacoes, file)


