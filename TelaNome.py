# -*- coding: utf-8 -*-
import pygame, sys, random, os
from pygame.locals import *
from Menu import*
from TelaJogo import *
from TelaSairDoJogo import*



class TelaNome:
	
	def __init__(self, tela):
			self.tela = tela
			
	


	def inicio(self):
		
		os.environ["SDL_VIDEO_CENTERED"] = "1" #centralizar
		pygame.init()
	
		texto_menu = pygame.font.Font("img/Billd.ttf", 20)
		texto_menuNomeJogador = pygame.font.Font("img/zerotwos.ttf", 50)
		texto_nomeInvalido = pygame.font.Font("img/zerotwos.ttf", 30)
		pygame.display.set_caption("PyQuímica!           - V 0.1 - ")
		self.tela = pygame.display.set_mode((1024, 600))
		executando = True
		nomeDigitado = ""
		digitaNome = True
		entrou = False
		
		while executando:
									
			if entrou == True:
				print(nomeDigitado)
				executando = False
				
				
			
			nomeMenu = texto_menu.render("Menu", True, (0,0,0))
			menuRect = nomeMenu.get_rect().move(530,620)
			menuRect.move
			
			iniciarJogo = texto_menu.render("Iniciar Jogo", True, (0,0,0))
			iniciarJogoRect = iniciarJogo.get_rect().move(680,620)
			iniciarJogoRect.move
			
			nomeJogador = texto_menuNomeJogador.render("Digite seu nome: ", True, (0,0,0))
			nomeJogadorInvalido = pygame.Surface((0,0))
			
	
			
			for e in pygame.event.get():
				if e.type == QUIT:
					sys.exit(0)	
										
				if e.type==pygame.KEYDOWN and digitaNome==True:
					nomeDigitado += e.unicode 
					print(e.unicode)
				
				teclas = pygame.key.get_pressed()
				if teclas[K_BACKSPACE]:
					tamanhoNomeDigitado = len(nomeDigitado)
					novoNome = nomeDigitado[0:tamanhoNomeDigitado-2]
					digitaNome = True
					nomeDigitado = novoNome
					
				if teclas[K_RETURN]:
					tamanhoNomeDigitado = len(nomeDigitado)
					novoNome = nomeDigitado[0:tamanhoNomeDigitado-1]
					nomeDigitado = novoNome
					
				if len(nomeDigitado)==7:
					digitaNome=False
				
				nomeNaTela = texto_nomeInvalido.render(nomeDigitado.upper() + "", True, (250,16,3))
			
			if (menuRect.collidepoint(pygame.mouse.get_pos())):
				nomeMenu = texto_menu.render("Menu", True, (255,255,10))
				if(pygame.mouse.get_pressed()[0]):
					executando = False
					print("novo jogo") 
			
			
			if (iniciarJogoRect.collidepoint(pygame.mouse.get_pos())):
				iniciarJogo = texto_menu.render("Iniciar Jogo", True, (255,255,10))
				if(pygame.mouse.get_pressed()[0]) and len(nomeDigitado) >=1:
					jogo = TelaJogo(self.tela, nomeDigitado)
					jogo.inicio()
					entrou = True
					print("novo jogo")
					
				if len(nomeDigitado) < 1:
					nomeJogadorInvalido = texto_nomeInvalido.render("DIGITE SEU NOME ", True, (0,0,0)) 
				
					
			
			
			self.tela.fill((255,255,255))
			#self.tela.blit(fundo, (0, 0))
			self.tela.blit(nomeNaTela, (610,250))
			self.tela.blit(nomeMenu, (530,620))
			self.tela.blit(iniciarJogo, (680,620))
			self.tela.blit(nomeJogador, (450,200))
			self.tela.blit(nomeJogadorInvalido, (550,250))
			
			

			
			
			
			
			pygame.display.flip() #se tem mt movimento/animacao
			


