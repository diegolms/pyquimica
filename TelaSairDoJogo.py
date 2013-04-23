# -*- coding: utf-8 -*-

import pygame, sys, random, os
from pygame.locals import *


class TelaSairDoJogo:
		
	@staticmethod
	def getAcabou():
		return acabou
	
	
	
	def __init__(self, tela, nomeJogador, pontos):
			self.tela = tela
			self.nomeJogador = nomeJogador
			self.pontos = pontos
			
			


	def inicio(self):
		
		os.environ["SDL_VIDEO_CENTERED"] = "1" #centralizar
		pygame.init()
	
		texto_menu = pygame.font.Font("img/zerotwos.ttf", 30)
		texto_sair = pygame.font.Font("img/zerotwos.ttf", 50)
		pygame.display.set_caption("PyQuímica!           - V 0.1 - ")
		self.tela = pygame.display.set_mode((1024, 600))
		executando = True
		fim = pygame.Surface((0,0))
		fim2 = pygame.Surface((0,0))
		
		menu = pygame.Surface((0,0))
		
		
		sair = texto_sair.render(" Sair do Jogo? " , True, (255,255,255))
		
		sim = texto_menu.render(" Sim " , True, (255,255,255))
		simRect = sim.get_rect().move((550,400))
		simRect.move
			
		nao = texto_menu.render(" Não " , True, (255,255,255))
		naoRect = nao.get_rect().move((650,400))
		naoRect.move
		
		textoMenu = False
		
		
		global acabou
		acabou = False
		
		while executando:
									
			if textoMenu==True:
				menu = texto_menu.render("Menu Inicial", True, (255,255,255))
				menuRect = menu.get_rect().move((550,600))
				menuRect.move
				if (menuRect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]):			
					executando = False
					global acabou
					acabou = True
				
			
			for e in pygame.event.get():
				if e.type == QUIT:
					sys.exit(0)	
										
			
			if (naoRect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]):
					executando = False
					
					
			if (simRect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]):
					sair = pygame.Surface((0,0))
					sim = pygame.Surface((0,0))
					nao = pygame.Surface((0,0))
					fim = texto_sair.render("Parabens " +str(self.nomeJogador.upper()), True, (255,255,255))
					fim2 = texto_sair.render("Voce fez  " +str(self.pontos)+ " Pontos", True, (255,255,255))
					textoMenu = True
			
			
			self.tela.fill((0, 0, 0))
			self.tela.blit(sair, (450,300))
			self.tela.blit(sim, (550,400))
			self.tela.blit(nao, (650,400))
			self.tela.blit(fim, (430,300))
			self.tela.blit(fim2, (410,400))
			self.tela.blit(menu, (550,600))
			
			
	
			

			
			
			
			
			pygame.display.flip() #se tem mt movimento/animacao
