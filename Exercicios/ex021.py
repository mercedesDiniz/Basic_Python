# Faça um programa em python que abra e reproduza o áudio de um arquivo MP3. (ERRO)

import pygame
pygame.init()
pygame.mixer.music.load('d21.mp3')
pygame.mixer.music.play()
pygame.event.wait()