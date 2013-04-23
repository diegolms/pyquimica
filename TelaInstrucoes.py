# -*- coding: utf-8 -*-
 
 
import pygame, sys, random, os
from pygame.locals import *
from Menu import*
from TelaJogo import*


class TelaInstrucoes:
	def __init__(self, tela):
			self.tela = tela


	def inicio(self):
		
		os.environ["SDL_VIDEO_CENTERED"] = "1" #centralizar
		pygame.init()
	
		texto_menu = pygame.font.Font("img/Billd.ttf", 40)
		fundo = pygame.image.load("img" + os.sep + "FundoInstruções.png").convert()
		pygame.display.set_caption(" - PyQuimica! -  v-0.1")
		self.tela = pygame.display.set_mode((1024, 600))
		executando = True
		while executando:
									
			nomeMenu = texto_menu.render("Menu", True, (0,0,0))
			menuRect = nomeMenu.get_rect().move(580,620)
			menuRect.move
			
			
			for e in pygame.event.get():
				if e.type == QUIT:
					sys.exit(0)	
										
			
			if (menuRect.collidepoint(pygame.mouse.get_pos())):
				nomeMenu = texto_menu.render("Menu", True, (255,255,10))
				if(pygame.mouse.get_pressed()[0]):
					executando = False
					#print("Novo Jogo") 
			
			
			
			self.tela.blit(fundo, (0, 0))
			self.tela.blit(nomeMenu, (580,620))
			

			
			
			
			
			pygame.display.flip() #se tem mt movimento/animacao
