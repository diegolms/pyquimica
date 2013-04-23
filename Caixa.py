# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *

class Caixa(pygame.sprite.Sprite):
	def __init__(self, pos, img):
		pygame.sprite.Sprite.__init__(self, self.containers)
		self.x = pos[0]
		self.y = pos[1]
		self.image = img
		self.rect = self.image.get_rect() #faz um retangulo na imagem
		self._rect = Rect(self.rect)
		self.rect.move_ip((self.x, self.y))
		self.substancia = ""
	
	def adicionaElementosTemporario(self, s):
		self.substancia += s
		
#	def update(self):
#		if pygame.mouse.get_pressed()[0]:
#			if self.rect.collidepoint(pygame.mouse.get_pos()):
#			    print("caixa")     