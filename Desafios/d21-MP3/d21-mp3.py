'''  Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.'''
import pygame
# iniciando o mixer
pygame.mixer.init()

# iniciando o pygame
pygame.init()


pygame.mixer.music.load('musica.mp3')
pygame.mixer.music.play(loops=0, start=0.0)
pygame.event.wait()


