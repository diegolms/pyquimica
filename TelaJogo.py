# coding: iso-8859-1 -*-
import pygame, sys, random, os
from pygame.locals import *
from Botao import*
from Elemento import *
from Caixa import *
from Mistura import *
from TextoRender import*
from TelaFinal import*
from TelaSairDoJogo import*

#from pygame.mixer import Sound
import pygame.mixer

import ConfigParser
import string

listaMistura = []



def read_listINI_(fileINI):
    config = ConfigParser.ConfigParser()
    config.read(fileINI)
    for valor in config.options("misturas"):
        listaMistura.append(eval(config.get('misturas', valor)))
    return listaMistura


class TelaJogo:
	
	
	#def __init__(self, tela, nomeJogador):
	#		self.tela = tela
	#		self.nomeJogador = nomeJogador
			
	def __init__(self, tela):
			self.tela = tela
			self.nomeJogador = ""		



	def inicio(self):
		
		
		pygame.mixer.music.stop()
		
		
		os.environ["SDL_VIDEO_CENTERED"] = "1" #centralizar
		pygame.init()
		inicio = pygame.mixer.music.load("img/music_back.ogg")
		#pygame.mixer.music.play(-1)
					
		
		texto_arial = pygame.font.Font("./img/zerotwos.ttf", 25)
		texto_desafio = pygame.font.Font("Archive.otf", 40)
		texto_info = pygame.font.Font("Archive.otf", 30)
		texto_misturas = pygame.font.Font("arial.ttf", 20)
		texto_respostas = pygame.font.Font("./img/arial.ttf", 30)
		texto_dicas = pygame.font.Font("./img/arial.ttf", 15)
	
		
		listaAux = []
		listaMistura = (read_listINI_("Mistura.ini"))
		

		pergunta = pygame.Surface((0,0))
		resposta = pygame.Surface((0,0))
		nomeSubstancia = pygame.Surface((0,0))
		misturaFinal = pygame.Surface((0,0))
		rendered_text = pygame.Surface((0,0))
		rendered_textDica = pygame.Surface((0,0))
		

		
		
		respostaCerta = pygame.mixer.Sound("img/Palmas.wav")
		respostaErrada =  pygame.mixer.Sound("img/error.wav")
		
		
		
		pygame.display.set_caption("PyQuímica! - V 0.1 - ")
		
		
		
		self.tela = pygame.display.set_mode((1024, 600)) #, pygame.FULLSCREEN)
		
		
		
		#LayeredUpdates para poder modificar a ordem do blit do elemento

		fundo = pygame.image.load("img/gfx/screen.png").convert()
		fundoBancada = pygame.image.load("img/gfx/cenario.png")

		grupo = pygame.sprite.LayeredUpdates() 
		grupo2 = pygame.sprite.LayeredUpdates()
		grupo3 = pygame.sprite.LayeredUpdates()
		Elementos.containers = grupo #todos os elementos da classe pertence ao mesmo grupo de renderizacao
		Botao.containers = grupo3
		Caixa.containers = grupo2
		Mistura.containers = grupo3
		
		
		#Hidrogenio = Elementos("Hidrogênio", "H", (280, 5), pygame.image.load("./img" + os.sep + "Hidrogenio.png").convert_alpha())
		Hidrogenio = Elementos("Hidrogênio", "H", (153, 5), pygame.image.load("./img/gfx/elementos/Hidrogenio.png").convert_alpha())
		Litio = Elementos("Lítio", "Li", (153,45), pygame.image.load("./img/gfx/elementos/Litio.png").convert_alpha())
		Sodio = Elementos("Sódio","Na", (153, 85), pygame.image.load("./img/gfx/elementos/Sodio.png").convert_alpha())
		Potassio = Elementos("Potássio", "K",(153, 125), pygame.image.load("./img/gfx/elementos/Potassio.png").convert_alpha())
		Rubidio = Elementos("Rubídio", "Rb", (153, 165), pygame.image.load("./img/gfx/elementos/Rubidio.png").convert_alpha())
		Cesio = Elementos("Césio", "Cs",(153, 205), pygame.image.load("./img/gfx/elementos/Cesio.png").convert_alpha())
		Francio = Elementos("Frâncio","Fr",(153, 245), pygame.image.load("./img/gfx/elementos/Francio.png").convert_alpha())
		Berilio = Elementos("Berílio","Be",(193, 45), pygame.image.load("./img/gfx/elementos/Berilio.png").convert_alpha())
		Magnesio = Elementos("Magnésio","Mg",(193, 85), pygame.image.load("./img/gfx/elementos/Magnesio.png").convert_alpha())
		Calcio = Elementos("Cálcio","Ca",(193, 125), pygame.image.load("./img/gfx/elementos/Calcio.png").convert_alpha())
		Estroncio = Elementos("Estrôncio","Sr",(193, 165), pygame.image.load("./img/gfx/elementos/Estroncio.png").convert_alpha())
		Bario = Elementos("Bário","Ba",(193, 205), pygame.image.load("./img/gfx/elementos/Bario.png").convert_alpha())
		Radio = Elementos("Rádio","Ra",(193, 245), pygame.image.load("./img/gfx/elementos/Radio.png").convert_alpha())
		Escandio = Elementos("Escândio","Sc",(233, 125), pygame.image.load("./img/gfx/elementos/Escandio.png").convert_alpha())
		Itrio = Elementos("Ítrio","Y",(233, 165), pygame.image.load("./img/gfx/elementos/Itrio.png").convert_alpha())
		Titanio = Elementos("Titânio","Ti",(273, 125), pygame.image.load("./img/gfx/elementos/Titanio.png").convert_alpha())
		Zirconio = Elementos("Zircônio","Zr",(273, 165), pygame.image.load("./img/gfx/elementos/Zirconio.png").convert_alpha())
		Hafnio = Elementos("Háfnio","Hf",(273, 205), pygame.image.load("./img/gfx/elementos/Hafnio.png").convert_alpha())
		Rutherfordio = Elementos("Rutherfórdio","Rf",(273, 245), pygame.image.load("./img/gfx/elementos/Rutherfodio.png").convert_alpha())
		Vanadio = Elementos("Vanádio","V",(313, 125), pygame.image.load("./img/gfx/elementos/Vanadio.png").convert_alpha())
		Niobio = Elementos("Nióbio","Nb",(313, 165), pygame.image.load("./img/gfx/elementos/Niobio.png").convert_alpha())
		Tantalo = Elementos("Tântalo","Ta",(313, 205), pygame.image.load("./img/gfx/elementos/Tantalo.png").convert_alpha())
		Dubnio = Elementos("Dúbnio","Db",(313, 245), pygame.image.load("./img/gfx/elementos/Dubnio.png").convert_alpha())
		Cromio = Elementos("Crômio","Cr",(353, 125), pygame.image.load("./img/gfx/elementos/Cromio.png").convert_alpha())
		Molibdenio = Elementos("Molibdênio","Mo",(353, 165), pygame.image.load("./img/gfx/elementos/Molibdenio.png").convert_alpha())
		Tungstenio = Elementos("Tungstênio","W",(353, 205), pygame.image.load("./img/gfx/elementos/Tungstenio.png").convert_alpha())
		Seaborgio = Elementos("Seabórgio","Sg",(353, 245), pygame.image.load("./img/gfx/elementos/Seaborgio.png").convert_alpha())
		Manganes = Elementos("Manganês","Mn",(393, 125), pygame.image.load("./img/gfx/elementos/Manganes.png").convert_alpha())
		Tecnecio = Elementos("Tecnécio","Tc",(393, 165), pygame.image.load("./img/gfx/elementos/Tecnecio.png").convert_alpha())
		Renio = Elementos("Rênio","Re",(393, 205), pygame.image.load("./img/gfx/elementos/Renio.png").convert_alpha())
		Borio = Elementos("Bório","Bh",(393, 245), pygame.image.load("./img/gfx/elementos/Borio.png").convert_alpha())
		Ferro = Elementos("Ferro","Fe",(433, 125), pygame.image.load("./img/gfx/elementos/Ferro.png").convert_alpha())
		Rutenio= Elementos("Rutênio","Ru",(433, 165), pygame.image.load("./img/gfx/elementos/Rutenio.png").convert_alpha())
		Osmio = Elementos("Ósmio","Os",(433, 205), pygame.image.load("./img/gfx/elementos/Osmio.png").convert_alpha())
		Hassio = Elementos("Hássio","Hs",(433, 245), pygame.image.load("./img/gfx/elementos/Hassio.png").convert_alpha())
		Cobalto = Elementos("Cobalto","Co",(473, 125), pygame.image.load("./img/gfx/elementos/Cobalto.png").convert_alpha())
		Rodio = Elementos("Ródio","Rh",(473, 165), pygame.image.load("./img/gfx/elementos/Rodio.png").convert_alpha())
		Iridio = Elementos("Irídio","Ir",(473, 205), pygame.image.load("./img/gfx/elementos/Iridio.png").convert_alpha())
		Meitnerio = Elementos("Meitnério","Mt",(473, 245), pygame.image.load("./img/gfx/elementos/Meitnerio.png").convert_alpha())
		Niquel = Elementos("Níquel","Ni",(513, 125), pygame.image.load("./img/gfx/elementos/Niquel.png").convert_alpha())
		Paladio = Elementos("Paládio","Pd",(513, 165), pygame.image.load("./img/gfx/elementos/Paladio.png").convert_alpha())
		Platina = Elementos("Platina","Pt",(513, 205), pygame.image.load("./img/gfx/elementos/Platina.png").convert_alpha())
		Darmstadio = Elementos("Darmstádio","Ds",(513, 245), pygame.image.load("./img/gfx/elementos/Darmstadio.png").convert_alpha())
		Cobre = Elementos("Cobre","Cu",(553, 125), pygame.image.load("./img/gfx/elementos/Cobre.png").convert_alpha())
		Prata = Elementos("Prata","Ag",(553, 165), pygame.image.load("./img/gfx/elementos/Prata.png").convert_alpha())
		Ouro = Elementos("Ouro","Au",(553, 205), pygame.image.load("./img/gfx/elementos/Ouro.png").convert_alpha())
		Roentgenio = Elementos("Roentgênio","Rg",(553, 245), pygame.image.load("./img/gfx/elementos/Roentgenio.png").convert_alpha())
		Zinco = Elementos("Zinco","Zn",(593, 125), pygame.image.load("./img/gfx/elementos/Zinco.png").convert_alpha())
		Cadmio = Elementos("Cádmio","Cd",(593, 165), pygame.image.load("./img/gfx/elementos/Cadmio.png").convert_alpha())
		Mercurio = Elementos("Mercúrio","Hg",(593, 205), pygame.image.load("./img/gfx/elementos/Mercurio.png").convert_alpha())
		Copernicio = Elementos("Copernício","Cn",(593, 245), pygame.image.load("./img/gfx/elementos/Copernicio.png").convert_alpha())
		Boro = Elementos("Boro","B",(633, 45), pygame.image.load("./img/gfx/elementos/Boro.png").convert_alpha())
		Aluminio = Elementos("Alumínio","Al",(633, 85), pygame.image.load("./img/gfx/elementos/Aluminio.png").convert_alpha())
		Galio = Elementos("Gálio","Ga",(633, 125), pygame.image.load("./img/gfx/elementos/Galio.png").convert_alpha())
		Indio = Elementos("Índio","In",(633, 165), pygame.image.load("./img/gfx/elementos/Indio.png").convert_alpha())
		Talio = Elementos("Tálio","Ti",(633, 205), pygame.image.load("./img/gfx/elementos/Talio.png").convert_alpha())
		Carbono = Elementos("Carbono","C",(673, 45), pygame.image.load("./img/gfx/elementos/Carbono.png").convert_alpha())
		Silicio = Elementos("Silício","Si",(673, 85), pygame.image.load("./img/gfx/elementos/Silicio.png").convert_alpha())
		Germanio = Elementos("Germânio","Ge",(673, 125), pygame.image.load("./img/gfx/elementos/Germanio.png").convert_alpha())
		Estanho = Elementos("Estanho","Sn",(673, 165), pygame.image.load("./img/gfx/elementos/Estanho.png").convert_alpha())
		Chumbo = Elementos("Chumbo","Pb",(673, 205), pygame.image.load("./img/gfx/elementos/Chumbo.png").convert_alpha())
		Nitrogenio = Elementos("Nitrogênio","N",(713, 45), pygame.image.load("./img/gfx/elementos/Nitrogenio.png").convert_alpha())
		Fosforo = Elementos("Fósforo","P",(713, 85), pygame.image.load("./img/gfx/elementos/Fosforo.png").convert_alpha())
		Arsenio = Elementos("Arsênio","As",(713, 125), pygame.image.load("./img/gfx/elementos/Arsenio.png").convert_alpha())
		Antimonio = Elementos("Antimônio","Sb",(713, 165), pygame.image.load("./img/gfx/elementos/Antimonio.png").convert_alpha())
		Bismuto = Elementos("Bismuto","Bi",(713, 205), pygame.image.load("./img/gfx/elementos/Bismuto.png").convert_alpha())
		Oxigenio = Elementos("Oxigênio", "O",(753, 45), pygame.image.load("./img/gfx/elementos/Oxigenio.png").convert_alpha())
		Enxofre = Elementos("Enxofre","S",(753, 85), pygame.image.load("./img/gfx/elementos/Enxofre.png").convert_alpha())
		Selenio = Elementos("Selênio","Se",(753, 125), pygame.image.load("./img/gfx/elementos/Selenio.png").convert_alpha())
		Telurio = Elementos("Telúrio","Te",(753, 165), pygame.image.load("./img/gfx/elementos/Telurio.png").convert_alpha())
		Polonio = Elementos("Polônio","Po",(753, 205), pygame.image.load("./img/gfx/elementos/Polonio.png").convert_alpha())
		Fluor = Elementos("Flúor","F",(793, 45), pygame.image.load("./img/gfx/elementos/Fluor.png").convert_alpha())
		Cloro = Elementos("Cloro","Cl",(793, 85), pygame.image.load("./img/gfx/elementos/Cloro.png").convert_alpha())
		Bromo = Elementos("Bromo","Br",(793, 125), pygame.image.load("./img/gfx/elementos/Bromo.png").convert_alpha())
		Iodo = Elementos("Iodo","I",(793, 165), pygame.image.load("./img/gfx/elementos/Iodo.png").convert_alpha())
		Astato = Elementos("Astato","At",(793, 205), pygame.image.load("./img/gfx/elementos/Astato.png").convert_alpha())
		Helio = Elementos("Hélio","He",(833, 5), pygame.image.load("./img/gfx/elementos/Helio.png").convert_alpha())
		Neon = Elementos("Néon","Ne",(833, 45), pygame.image.load("./img/gfx/elementos/Neon.png").convert_alpha())
		Argonio = Elementos("Argônio","Ar",(833, 85), pygame.image.load("./img/gfx/elementos/Argonio.png").convert_alpha())
		Criptonio = Elementos("Criptônio","Kr",(833, 125), pygame.image.load("./img/gfx/elementos/Criptonio.png").convert_alpha())
		Xenonio = Elementos("Xenônio","Xe",(833, 165), pygame.image.load("./img/gfx/elementos/Xenonio.png").convert_alpha())
		Radonio = Elementos("Radônio","Rn",(833, 205), pygame.image.load("./img/gfx/elementos/Radonio.png").convert_alpha())
		Lantanio = Elementos("Lantânio","La",(233, 300), pygame.image.load("./img/gfx/elementos/Lantanio.png").convert_alpha())
		Cerio = Elementos("Cério","Ce",(273, 300), pygame.image.load("./img/gfx/elementos/Cerio.png").convert_alpha())
		Praseodimio= Elementos("Praseodímio","Pr",(313, 300), pygame.image.load("./img/gfx/elementos/Praseodimio.png").convert_alpha())
		Neodimio = Elementos("Neodímio","Nd",(353, 300), pygame.image.load("./img/gfx/elementos/Neodimio.png").convert_alpha())
		Promecio = Elementos("Promécio","Pm",(393, 300), pygame.image.load("./img/gfx/elementos/Promecio.png").convert_alpha())
		Samario = Elementos("Samário","Sm",(433, 300), pygame.image.load("./img/gfx/elementos/Samario.png").convert_alpha())
		Europio = Elementos("Európio","Eu",(473, 300), pygame.image.load("./img/gfx/elementos/Europio.png").convert_alpha())
		Gadolinio = Elementos("Gadolínio","Gd",(513, 300), pygame.image.load("./img/gfx/elementos/Gadolinio.png").convert_alpha())
		Terbio = Elementos("Térbio","Tb",(553, 300), pygame.image.load("./img/gfx/elementos/Terbio.png").convert_alpha())
		Disprosio = Elementos("Disprósio","Dy",(593, 300), pygame.image.load("./img/gfx/elementos/Disprosio.png").convert_alpha())
		Holmio = Elementos("Hólmio","Ho",(633, 300), pygame.image.load("./img/gfx/elementos/Holmio.png").convert_alpha())
		Erbio = Elementos("Érbio","Er",(673, 300), pygame.image.load("./img/gfx/elementos/Erbio.png").convert_alpha())
		Tulio = Elementos("Túlio","Tm",(713, 300), pygame.image.load("./img/gfx/elementos/Tulio.png").convert_alpha())
		Iterbio = Elementos("Itérbio","Yb",(753, 300), pygame.image.load("./img/gfx/elementos/Iterbio.png").convert_alpha())
		Lutecio = Elementos("Lutécio","Lu",(793, 300), pygame.image.load("./img/gfx/elementos/Lutecio.png").convert_alpha())
		Actinio = Elementos("Actínio","Ac",(233, 340), pygame.image.load("./img/gfx/elementos/Actinio.png").convert_alpha())
		Torio = Elementos("Tório","Th",(273, 340), pygame.image.load("./img/gfx/elementos/Torio.png").convert_alpha())
		Protactinio = Elementos("Protactínio","Pa",(313, 340), pygame.image.load("./img/gfx/elementos/Protactinio.png").convert_alpha())
		Uranio = Elementos("Urânio","U",(353, 340), pygame.image.load("./img/gfx/elementos/Uranio.png").convert_alpha())
		Neptunio = Elementos("Neptúnio","Np",(393, 340), pygame.image.load("./img/gfx/elementos/Neptunio.png").convert_alpha())
		Plutonio = Elementos("Plutônio","Pu",(433, 340), pygame.image.load("./img/gfx/elementos/Plutonio.png").convert_alpha())
		Americio = Elementos("Amerício","Am",(473, 340), pygame.image.load("./img/gfx/elementos/Americio.png").convert_alpha())
		Curio = Elementos("Cúrio","Cm",(513, 340), pygame.image.load("./img/gfx/elementos/Curio.png").convert_alpha())
		Berquelio = Elementos("Berquélio","Bk",(553, 340), pygame.image.load("./img/gfx/elementos/Berquelio.png").convert_alpha())
		Californio = Elementos("Califórnio","Cf",(593,340), pygame.image.load("./img/gfx/elementos/Californio.png").convert_alpha())
		Einstenio = Elementos("Einstênio","Es",(633, 340), pygame.image.load("./img/gfx/elementos/Einstenio.png").convert_alpha())
		Fermio= Elementos("Férmio","Fr",(673, 340), pygame.image.load("./img/gfx/elementos/Fermio.png").convert_alpha())
		Mendelevio= Elementos("Mendelévio","Md",(713, 340), pygame.image.load("./img/gfx/elementos/Mendelevio.png").convert_alpha())
		Nobelio = Elementos("Nobélio","No",(753, 340), pygame.image.load("./img/gfx/elementos/Nobelio.png").convert_alpha())
		Laurencio = Elementos("Laurêncio","Lr",(793, 340), pygame.image.load("./img/gfx/elementos/Laurencio.png").convert_alpha())
		

		
	
		#botaoLimpar = Botao((375, 485), pygame.image.load("img/gfx/telajogo_cenario_MENU_LIMPAR.png").convert_alpha())
		botaoLimpar = Botao((375, 485), pygame.image.load("img" + os.sep + "transparente.png").convert_alpha())
                #botaoMisturar = Botao((535, 485), pygame.image.load("img/gfx/telajogo_cenario_MENU_MISTURAR.png").convert_alpha())
                botaoMisturar = Botao((535, 485), pygame.image.load("img" + os.sep + "transparente.png").convert_alpha())
		botaoSair = Botao((938, 630), pygame.image.load("img" + os.sep + "botaoSair.png").convert_alpha())
		botaoProximo = Botao((378, 545), pygame.image.load("img/gfx/telajogo_cenario_MENU_PROX.png").convert_alpha())
				
		
		caixa = Caixa((440,405), pygame.image.load("img/gfx/FRASCO-PRINCIPAL.png").convert_alpha())
		suporte = Elementos("","", (517,505), pygame.image.load("img" + os.sep + "transparente.png").convert_alpha())

                quimicos = pygame.image.load("img/gfx/quimicos.png").convert_alpha()
                quimico = quimicos.subsurface((0, 0), (170, 220))
                
                bolha = pygame.image.load("img" + os.sep + "transparente.png").convert_alpha()
                #bolha = pygame.image.load("img/gfx/bolhasDicaCopia.png").convert_alpha()
                bolhaDica = bolha.subsurface((0, 0), (0, 0))
                rectBolhaDica = bolhaDica.get_rect().move(875, 0)
		rectBolhaDica.move

                balaoRespostaErrada = Botao((55, 0), pygame.image.load("img" + os.sep + "transparente.png").convert_alpha())
                
                #rectBalaoRespostaErrada = balaoRespostaErrada.get_rect().move(55, 0)
                #rectBalaoRespostaErrada.move
                
		
		quimicoEsq= pygame.image.load("img" + os.sep + "quimico.png").convert()
		rectQuimicoEsq = quimicoEsq.get_rect().move(60, 565)
		rectQuimicoEsq.move
		
		quimicoDir = pygame.image.load("img" + os.sep + "quimico.png").convert()
		rectQuimicoDir = quimicoDir.get_rect().move(1100, 565)
		rectQuimicoDir.move
	
					
		clock = pygame.time.Clock()
		
		
		arrastando = False 
		auxiliar = ""	
		Limpar = True
		dentroDaCaixa = False
		clicaBotao = False
		gerou=False
		imgBotaoProximo = False
		imgBotaoObterResposta = False
		totalPontos = 0
		errou = False
		respostasErrada = 0
		
		
		#
		gerou = True
		
		mist = listaMistura[random.randint(0, len(listaMistura) - 1)]
		mist2 = ""
		listaAux.append(mist)
		pergunta = texto_misturas.render(mist.nome , True, (0, 0, 0))
		
		suporte.image = pygame.Surface((0,0))
		resposta = pygame.Surface((0,0))
		misturaJogador = pygame.Surface((0,0))
		block = False
		Limpar = True
		
		iniciar = False
		#
		nomenclaturaFinalGerada = ""
		primeiroSimbolo = ""
		segundoSimbolo = ""
		terceiroSimbolo = ""
		contLetras = ""
		contParaSimbolos = 0
		novaLetraCorrespondenteAoCont = ""
		contTotalLetras = 0
		acabou=0
		nomeTotal=""
		entrou = 1
		executando = True
		pediuDica = False
		obteveResposta = False
		#
				
		tempoParaAnimarQuimico = 7
                
		tentouSairDoJogo = False
		
		while executando:
			clock.tick(60)
                        tempoAtual = int(round(pygame.time.get_ticks()/1000))
                        #animacao do quimico
                        if(tempoAtual == tempoParaAnimarQuimico):
                            tempoParaAnimarQuimico+=7
                            #quimico = quimicos.subsurface((170, 0), (170, 220))
                            #quimico = quimicos.subsurface((340, 0), (170, 220)) 
			if tentouSairDoJogo==True:
				if (TelaSairDoJogo.getAcabou()):
					executando = False
					pygame.mixer.music.stop()
					
				#if (TelaSairDoJogo.getAcabou()):
				#	executando  = False
			
			if totalPontos >= 0:
				pontos = texto_arial.render("Pontos: " +str(totalPontos), True, (0,0,0))
			else:
				pontos = texto_arial.render("Pontos: " +str(totalPontos), True, (255,0,6))
			nomeJogador = texto_arial.render("Jogador: " +self.nomeJogador.upper(), True, (0,0,0))
			#compostoQuimico = texto_info.render("Composto Químico", True, (0,0,0))
			formulaQuimica = texto_info.render("Fórmula", True, (0,130,238))
			elemento = texto_info.render("Elemento ", True, (0,130,238))
			#textoDica = texto_info.render("Dica", True, (0,0,0))
			textoInfo = texto_desafio.render("Desafio "+str(len(listaAux))+"/7" , True, (255,0,0))
			
			
			
			pygame.init()

			

					
			
			for e in pygame.event.get():
				if e.type == QUIT:
					sys.exit(0)	
										
			for s in grupo:
				
				if s.rect.collidepoint(pygame.mouse.get_pos()) and gerou==True:
					nomeSubstancia = texto_misturas.render(s.substancia, True, (0,0,0))
									
						
				if pygame.mouse.get_pressed()[0] and gerou==True:
                                        if(s.simbolo=="Zr"):
                                            print ""
					if s.rect.collidepoint(pygame.mouse.get_pos()):
						if(not arrastando):
							clicaBotao = False
							auxiliar = s
							print("arrastando" , auxiliar.substancia)
							arrastando = s.drag = True # ativa o arrastandoo para o quadrado
							grupo.move_to_front(s) # manda o quadrado pra frente dos outros
							
					 
							
				else:
					if arrastando:
						if auxiliar.rect.colliderect(caixa.rect):
							print("dentro da caixa")
							clicaBotao = True
							primeiroSimbolo = auxiliar.simbolo
							contLetras += auxiliar.simbolo
							botaoMisturar = Botao((535, 485), pygame.image.load("img/gfx/telajogo_cenario_MENU_MISTURAR.png").convert_alpha())
							botaoLimpar = Botao((375, 485), pygame.image.load("img/gfx/telajogo_cenario_MENU_LIMPAR.png").convert_alpha())
							if (primeiroSimbolo != segundoSimbolo):
									segundoSimbolo = primeiroSimbolo
									nomenclaturaFinalGerada += auxiliar.simbolo
									entrou=1
									contParaSimbolos=1
			
							else:
									contParaSimbolos+=1
									entrou+=1
									novaLetra = str(contParaSimbolos)
									if(entrou == 2):
										nomenclaturaFinalGerada +=novaLetra;

									else:
										tamanhoMisturaJogador = len(nomenclaturaFinalGerada)
										novaNomenclatura= nomenclaturaFinalGerada[0:tamanhoMisturaJogador-1]
										nomenclaturaFinalGerada = novaNomenclatura
										nomenclaturaFinalGerada+=novaLetra;
														
							dentroDaCaixa = True
							misturaFinal = texto_misturas.render(nomenclaturaFinalGerada, True, (0, 0, 0))
							suporte.image = auxiliar.image
							auxiliar.restaurarElemento()
						else:
							auxiliar.restaurarElemento()
					arrastando = s.drag = False # desativa o arrasto dos quadrados
					
			for s in grupo:
				s.update()
				
			for s in grupo2:
				s.update()
		
			
						
	
			if(botaoMisturar.clickBotao() and block==False and dentroDaCaixa==True and clicaBotao==True):
				block = False
				imgBotaoProximo = True
				if imgBotaoProximo == True:
                                        #botaoProximo = Botao((378, 545), pygame.image.load("img/gfx/telajogo_cenario_MENU_PROX.png").convert_alpha())
                                        print ""
				
				if mist.simbolo == contLetras:
						totalPontos += mist.pontos
						respostaCerta.play()
						Limpar = False
						gerou = False
						block = True
						dentroDaCaixa = False
						#resposta = texto_respostas.render("Reposta Certa", True, (0,0,0))
						#botaoMisturar = Botao((378, 545), pygame.image.load("img/gfx/telajogo_cenario_MENU_MISTURAR.png").convert_alpha()) 
						errou = False
						mist2 = ""
						my_string = mist.info
						my_font = pygame.font.Font(None, 22)
						#my_rect = pygame.Rect((0, 0, 205, 238))
						my_rect = pygame.Rect((100, 100, 272, 212))
						rendered_text = render_textrect(my_string, my_font, my_rect, (0, 0, 0), (255, 255, 255), 0)
						balaoRespostaErrada = Botao((55, 0), pygame.image.load("img/gfx/telajogo_cenario_balao.png").convert_alpha())

						
									
				else:
						balaoRespostaErrada = Botao((55, 0), pygame.image.load("img/gfx/telajogo_cenario_balaoRepostaErrada.png").convert_alpha())
						respostaErrada.play()
						respostasErrada += 1
						#resposta = texto_respostas.render("Resposta Errada", True, (0,0,0))
						#botaoMisturar = Botao((378, 545), pygame.image.load("img/gfx/telajogo_cenario_MENU_MISTURAR.png").convert_alpha()) 
						imgBotaoObterResposta = True
						if (imgBotaoObterResposta == True and respostasErrada >=3):
							botaoObterResposta = Botao((818, 630), pygame.image.load("img" + os.sep + "botaoObterResposta.png").convert_alpha())
						mist2 = mist
						errou = True
						block = True
						Limpar = True
						gerou = False
						totalPontos -= 10
						bolha = pygame.image.load("img/gfx/bolhasDicaCopia.png").convert_alpha()
						bolhaDica = bolha.subsurface((0, 0), (160, 200))
                                                rectBolhaDica = bolhaDica.get_rect().move(875, 0)
                                    		rectBolhaDica.move
                                   
				
				
			if imgBotaoProximo == True:
				#botaoProximo = Botao((378, 545), pygame.image.load("img/gfx/telajogo_cenario_MENU_PROX.png").convert_alpha())

				if(botaoProximo.clickBotao()):
                                        botaoMisturar.kill()
					botaoLimpar.kill()
					balaoRespostaErrada.kill()
					if len(listaAux) == 7:
						tentouSairDoJogo = True
						jogo = TelaFinal(self.tela, self.nomeJogador, totalPontos)
						jogo.inicio()
						
					
					#botaoMisturar = Botao((378, 545), pygame.image.load("img/gfx/telajogo_cenario_MENU_MISTURAR.png").convert_alpha())
					if errou == True:
						listaAux.remove(mist)
					JaExiste = True
					while JaExiste == True:
						mist = listaMistura[random.randint(0, len(listaMistura) - 1)]
						if mist in listaAux or mist == mist2:
							JaExiste = True
						else:
							JaExiste = False
							listaAux.append(mist)	
					respostaCerta.stop()
					respostaErrada.stop()
					#botaof = Botao((378, 545), pygame.image.load("img/gfx/telajogo_cenario_MENU_PROX.png").convert_alpha())
					#botaoObterResposta = Botao((818, 630), pygame.image.load("img/botaoProximoAux.png").convert_alpha())
					
					gerou = True
					pergunta = texto_misturas.render(mist.nome , True, (0, 0, 0))
					suporte.image = pygame.Surface((0,0))
					resposta = pygame.Surface((0,0))
					misturaFinal = pygame.Surface((0,0))
					block = False
					Limpar = True
					clicaBotao = False
					nomenclaturaFinalGerada = ""
					contParaSimbolos = 1
					entrou = 1
					#botaoProximo = suporte
					imgBotaoProximo=False
					imgBotaoObterResposta = False
					primeiroSimbolo = ""
					segundoSimbolo = ""
					nomeTotal = ""
					contLetras = ""
					novaLetraCorrespondenteAoCont = ""
					nomenclaturaFinalGerada = ""
					pediuDica = False
					respostasErrada = 0
					obteveResposta = False
					dica1 = pygame.Surface((0,0))
					dica2 = pygame.Surface((0,0))
					dica3 = pygame.Surface((0,0))
					rendered_text = pygame.Surface((0,0))
					rendered_textDica = pygame.Surface((0,0))
					bolhaDica = bolha.subsurface((0, 0), (0, 0))
					
					
						
			
			
			if(botaoLimpar.clickBotao()and Limpar==True and clicaBotao==True):
                                botaoMisturar.kill()
				botaoLimpar.kill()
				balaoRespostaErrada.kill()
				bolha = pygame.image.load("img" + os.sep + "transparente.png").convert_alpha()
				suporte.image = pygame.Surface((0,0))
				resposta = pygame.Surface((0,0))
				misturaFinal = pygame.Surface((0,0))
				nomenclaturaFinalGerada = ""
				dentroDaCaixa = False
				block = False
				contParaSimbolos = 0
				contLetras = ""
				nomeTotal = ""
				nomenclaturaFinalGerada = ""
				auxiliar = ""
				imgBotaoProximo = False
				primeiroSimbolo = ""
				segundoSimbolo = ""
				terceiroSimbolo = ""
				nomeTotal = ""
				novaLetraCorrespondenteAoCont = ""
        			arrastando = False 
				auxiliar = ""	
				imgBotaoProximo = False
				contTotalLetras = 0
				acabou=0
				entrou = 1
				arrastando = False 
				auxiliar = ""	
				Limpar = True
				gerou = True
				rendered_text = pygame.Surface((0,0))
				rendered_textDica = pygame.Surface((0,0))
				
				
				
			if (botaoSair.clickBotao() and arrastando==False):
				tentouSairDoJogo = True
				jogo = TelaSairDoJogo(self.tela, self.nomeJogador, totalPontos)
				jogo.inicio()
			
			
			if imgBotaoObterResposta == True and respostasErrada >=3:
				botaoObterResposta = Botao((818, 630), pygame.image.load("img" + os.sep + "botaoObterResposta.png").convert_alpha())
				if (botaoObterResposta.clickBotao() and arrastando==False and obteveResposta==False):
					obteveResposta = True
					totalPontos -= mist.pontos/2
					misturaFinal = pygame.Surface((0,0))
					resposta = pygame.Surface((0,0))
					misturaFinal = texto_misturas.render(mist.resposta, True, (0, 0, 0))
					
				
			
			
			
			if(rectBolhaDica.collidepoint(pygame.mouse.get_pos()) and pediuDica==False):
								if pygame.mouse.get_pressed()[0]:
                                                                        bolhaDica = pygame.Surface((0,0))
									pediuDica = True
									totalPontos -= 5
									my_string = mist.dica
									print my_string
									my_font = pygame.font.Font(None, 22)
									my_rect = pygame.Rect((0, 0, 272, 112))
                        						rendered_textDica = render_textrect(my_string, my_font, my_rect, (0, 0, 0), (255, 255, 255), 0)
                                                    			balaoRespostaErrada = Botao((55, 0), pygame.image.load("img/gfx/telajogo_cenario_balaoo.png").convert_alpha())
								
			

                    
                        
                        if(balaoRespostaErrada.clickBotao()):
                            balaoRespostaErrada.kill()
                            
			
			self.tela.fill((240, 255, 255))
			self.tela.blit(fundo,(0,0))
			self.tela.blit(fundoBancada,(0,0))
			self.tela.blit(quimico, (0, 250))
			self.tela.blit(bolhaDica, (875, 0))
			grupo2.draw(self.tela)
			grupo.draw(self.tela)
			grupo3.draw(self.tela)
			pygame.draw.line(self.tela, (0,130,238), (820, 540), (820 ,600),3)
			#pygame.draw.line(self.tela, (0,0,0), (1025,0), (1025,1200), 2)
			#pygame.draw.rect(self.tela, (0,0,0), (1130,380,135,38), 2)
			#pygame.draw.rect(self.tela, (0,0,0), (1050,440,217,36), 2)
			#pygame.draw.rect(self.tela, (0,0,0), (1050,500,217,36), 2)
			#pygame.draw.rect(self.tela, (0,0,0), (1040,200,225,150), 2)
			#pygame.draw.rect(self.tela, (0,0,0), (255,600,217,80), 2)
			#pygame.draw.rect(self.tela, (0,0,0), (808,600,217,80), 2)
			#pygame.draw.rect(self.tela, (0,0,0), (10,150,225,250), 2)
			#self.tela.blit(pontos, (1070, 10))
			#self.tela.blit(textoDica, (1050, 185))
			#self.tela.blit(compostoQuimico, (10, 10))
			self.tela.blit(formulaQuimica, (827, 540))
			self.tela.blit(textoInfo, (10, 530))
			self.tela.blit(elemento, (660, 540))
			#self.tela.blit(nomeJogador, (10, 10))
			self.tela.blit(pergunta, (12, 570))
			#self.tela.blit(resposta, (500, 460))
			self.tela.blit(nomeSubstancia,(640, 570))
			self.tela.blit(misturaFinal,(827, 570))
			#self.tela.blit(quimicoEsq, (60,565))
			#self.tela.blit(balaoRespostaErrada,(55,0))
			#self.tela.blit(quimicoDir, (1100,565))
			self.tela.blit(rendered_text, (85,25))
			self.tela.blit(rendered_textDica, (85,120))
			

			
			
			pygame.display.flip() 
