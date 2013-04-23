#-*- coding: cp860
# coding: iso-8859-1 -*-
import pygame, sys, random, os
from pygame.locals import *
from TelaJogo import *
from TelaCreditos import *
from TelaInstrucoes import *
from TelaNome import*
import pygame.mixer



class Menu:
	def __init__(self, tela):
		self.tela = tela

	
		
	
	def inicioMenu(self):
		musicaInicio = pygame.mixer.music.load("img/loop.ogg")
		#pygame.mixer.music.play(-1)
		
		os.environ["SDL_VIDEO_CENTERED"] = "1" 
		pygame.init()
		texto_titulo = pygame.font.Font("img/Yahoo.ttf", 25)
		texto_menu = pygame.font.Font("img/Yahoo.ttf", 15)
		pygame.display.set_caption("PyQuimica! - V 0.1 - ")
		self.tela = pygame.display.set_mode((1024, 600))
		fundo = pygame.image.load("img/gfx/tela_inicial_FINAL.png").convert()
		titulo = pygame.image.load("img/gfx/tela_inicial_TITULO-PY.png")
		botaoNovoJogo = pygame.image.load("img/gfx/NOVOJOGO.png")
		botaoComoJogar = pygame.image.load("img/gfx/COMOJOGAR.png")
		botaoSair = pygame.image.load("img/gfx/SAIR.png")		
		executando = True	
		
		
		while executando:
					
			self.tela.fill((240, 255, 255))
						
			novoJogoRect = botaoNovoJogo.get_rect().move(350,170)
			novoJogoRect.move
			
			comoJogarRect = botaoComoJogar.get_rect().move(350,230)
			comoJogarRect.move
			
			sairRect = botaoSair.get_rect().move(350,290)
			sairRect.move
			
			
						
			for e in pygame.event.get():
				if e.type == QUIT:
					sys.exit(0)	
				
			if (novoJogoRect.collidepoint(pygame.mouse.get_pos())):
					if(pygame.mouse.get_pressed()[0]):
						jogo = TelaJogo(self.tela)
						jogo.inicio()
						
					
			if (comoJogarRect.collidepoint(pygame.mouse.get_pos())):
					if(pygame.mouse.get_pressed()[0]):
						jogo = TelaCreditos(self.tela)
						jogo.inicio()
									
			if (sairRect.collidepoint(pygame.mouse.get_pos())):
					if(pygame.mouse.get_pressed()[0]):
						sys.exit()
					
			
			
			self.tela.blit(fundo,(0,0))
			self.tela.blit(titulo,(180,10))
			self.tela.blit(botaoNovoJogo,(350,170))
			self.tela.blit(botaoComoJogar,(350,230))
			self.tela.blit(botaoSair,(350,290))
						
			pygame.display.flip() 
			
	

