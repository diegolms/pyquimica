# -*- coding: utf-8 -*-

import pygame, sys, random, os
from pygame.locals import *


class TelaFinal:
	
	
	
	def __init__(self, tela, nomeJogador, pontos):
			self.tela = tela
			self.nomeJogador = nomeJogador
			self.pontos = pontos


	def inicio(self):
		
		os.environ["SDL_VIDEO_CENTERED"] = "1" #centralizar
		pygame.init()
	
		texto_menu = pygame.font.Font("img/zerotwos.ttf", 40)
		pygame.display.set_caption("PyQuímica!           - V 0.1 - ")
		self.tela = pygame.display.set_mode((1024, 600))
		executando = True
		
			
		
		
		while executando:
									
			
			pontos = texto_menu.render("Pontuação Final :" +str(self.pontos), True, (255,255,255))
			fim1 = texto_menu.render("Parabens " +str(self.nomeJogador)+ " pelo seu ótimo desempenho.", True, (255,255,255))
			fim2 = texto_menu.render(" 'O estudo é a base do sucesso.' ", True, (255,255,255))
			
			
			
			for e in pygame.event.get():
				if e.type == QUIT:
					sys.exit(0)	
										
			
			
			
						
			self.tela.fill((0,0,0))
			self.tela.blit(pontos, (420,20))
			self.tela.blit(fim1, (200,200))
			self.tela.blit(fim2, (290,300))
			
			
			

			
			
			
			
			pygame.display.flip() #se tem mt movimento/animacao
