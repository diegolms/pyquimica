# -*- coding: utf-8 -*-
import pygame,sys,os
import pygame.font
from pygame.locals import *
from pygame import*
from Menu import *
import pygame.font
import pygame.mixer





def main():
		
		os.environ["SDL_VIDEO_CENTERED"] = "1"
		pygame.init()
		tela = pygame.display.set_mode((1024, 600))
		musicaInicio = pygame.mixer.music.load("img/loop.ogg")
		pygame.mixer.music.play(-1)
		menu = Menu(tela)
		menu.inicioMenu()
		

if __name__ == "__main__":
		main()	
