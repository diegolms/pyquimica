# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *

class Botao(pygame.sprite.Sprite):
	def __init__(self, pos, img):
		pygame.sprite.Sprite.__init__(self, self.containers)
		
		self.x, self.y = pos
		self.image = img
		self.rect = self.image.get_rect()
		self.rect.move_ip(self.x, self.y)
		self._rect = self.rect
		
	def clickBotao(self):
		if(pygame.mouse.get_pressed()[0]):
			if(self.rect.collidepoint(pygame.mouse.get_pos())):
				return True;
				
		return False