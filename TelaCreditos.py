# coding: iso-8859-1 -*-

import pygame, sys, random, os
from pygame.locals import *
from Menu import*

class TelaCreditos:
	
	def __init__(self, tela):
			self.tela = tela


	def inicio(self):
		
		os.environ["SDL_VIDEO_CENTERED"] = "1" #centralizar
		pygame.init()
	
		texto = pygame.font.Font("img/Archive.otf", 35)
		fundo = pygame.image.load("img/gfx/telajogo_instrucoes_FUNDO.png").convert()
		tubo = pygame.image.load("img/gfx/telajogo_instrucoes_PLAY.png").convert_alpha()
		pygame.display.set_caption("PyQuimica! - V 0.1 - ")
		self.tela = pygame.display.set_mode((1024, 600))
		executando = True
		
		while executando:
									
                        linha1 = texto.render("1 - Observe o desafio pedido",True, (0,130,238))
                        linha2 = texto.render("2 - Coloque no tubo de ensaio os elementos que" ,True, (0,130,238))
                        linha3 = texto.render("formam a nomenclatura pedida" ,True, (0,130,238))
                        linha4 = texto.render("3- Clique no botão misturar",True, (0,130,238))
                        linha5 = texto.render("4 - Caso erre a mistura, remova os elementos do", True, (0,130,238))
                        linha6 = texto.render("tubo de ensaio através do botão limpar e tente", True, (0,130,238))
                        linha7 = texto.render("novamente ou passe para o próximo desafio", True, (0,130,238))
                                      
                        tuboRect = tubo.get_rect().move(390, 420)
			tuboRect.move           
			
			
			for e in pygame.event.get():
				if e.type == QUIT:
					sys.exit(0)
			
										
			if (tuboRect.collidepoint(pygame.mouse.get_pos())):
					if(pygame.mouse.get_pressed()[0]):
						jogo = TelaJogo(self.tela)
						jogo.inicio()
			
			
			
			self.tela.blit(fundo, (0, 0))
			self.tela.blit(linha1, (10,50))
			self.tela.blit(linha2, (10,150))
			self.tela.blit(linha3, (10,180))
			self.tela.blit(linha4, (10,280))
			self.tela.blit(linha5, (10,380))
			self.tela.blit(linha6, (10,410))
			self.tela.blit(linha7, (10,440))
			self.tela.blit(tubo, (390, 420))
				
			
			pygame.display.flip() #se tem mt movimento/animacao
