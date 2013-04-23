# -*- coding: utf-8 -*-
import pygame
from pygame.locals import*


class Elementos(pygame.sprite.Sprite):
	def __init__(self, substancia, simbolo, pos, img):
		pygame.sprite.Sprite.__init__(self, self.containers)
		self.substancia = substancia
		self.simbolo = simbolo
		self.x = pos[0]
		self.y = pos[1]
		

		self.image = img
		
		
		
		self.rect = self.image.get_rect() #faz um retangulo na imagem
		self._rect = Rect(self.rect)
		
		self.rect.move_ip((self.x, self.y)) # move o retangulo
		self.drag = False #variavel pra comparar se anda
		
	#def move(self, pos):
		#self.x, self.y = pos
	
	def update(self):
		if(self.drag):
			self._rect = Rect(self.rect)
			self.rect.center = pygame.mouse.get_pos()
			self.rect.clamp_ip((0, 0, 1024, 600)) #nao sair da tela
			
			
			
	def restaurarElemento(self):
		self.rect = self.image.get_rect()
		self.rect.move_ip(self.x, self.y)
        
   
    	
        
        
    
            
        
