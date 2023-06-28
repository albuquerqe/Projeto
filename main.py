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
