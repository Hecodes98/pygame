#Modulos
import pygame, sys, random
from pygame.locals import *

#Constantes.
SIZE=WIDTH,HEIGHT=400,225
BLANCO=(255,255,255)
NEGRO=(0,0,0)
ROJO=(255,0,0)
VERDE=(0,255,0)
AZUL=(0,0,255)
AMARILLO=(246,255,51)
AGUAMARINA=(51,255,199)

jugadores=pygame.sprite.Group()
rivales=pygame.sprite.Group()
todos=pygame.sprite.Group()

#Clases y Funciones.
class Jugador(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.Surface([50,50])
		self.image.fill(BLANCO)
		self.rect=self.image.get_rect()
		self.rect.x=110
		self.rect.y=0
		self.vel_posX=0
		self.vel_posY=0
		self.gravity=0.4
		self.salto=False

	def gravedad(self):
		if self.vel_posY == 0:
			self.vel_posY=1
		else:
			self.vel_posY+=self.gravity

	def update(self):
		self.gravedad()
		self.rect.x+=self.vel_posX
		self.rect.y+=self.vel_posY

		if self.rect.y >= (HEIGHT-self.rect.height):
			self.vel_posY=0
			self.rect.y=HEIGHT-self.rect.height

class Rival(pygame.sprite.Sprite):
	def __init__(self,pos):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.Surface([50,50])
		self.image.fill(ROJO)
		self.rect=self.image.get_rect()
		self.rect.x=pos[0]
		self.rect.y=pos[1]
		self.xini=pos[0]
		self.posx_fondo=0

	def update(self):
		print self.posx_fondo, self.xini, self.rect.x
		self.rect.x = self.posx_fondo + self.xini

def Recorte(imagenSprite,corteX,corteY,cantidadX,cantidadY):
	matriz=[]
	for y in range(cantidadY):
		matriz.append([])
		for x in range(cantidadX):
			cuadro=imagenSprite.subsurface((x*corteX),(y*corteY),corteX,corteY)
			matriz[y].append(cuadro)
	return matriz

def main():
    #Inicializacion
	pygame.init()
	pantalla=pygame.display.set_mode((SIZE))
	fondoJuego=pygame.image.load("imagenes/fondoJuego.png")
	pygame.display.set_caption("StreetFightherII")
	jugador=Jugador()
	jugadores.add(jugador)
	rival=Rival((600,0))
	rival1=Rival((900,0))
	rivales.add(rival,rival1)
	todos.add(jugadores,rivales)
	reloj=pygame.time.Clock()
	posFondoX,posFondoY=0,0
	velx=-5
	#Ciclo del juego
	while True:
		for evento in pygame.event.get():
			if evento.type == QUIT:
				pygame.quit()
				sys.exit()
		if evento.type == KEYDOWN:
			if evento.key == K_LEFT:
				jugador.vel_posX=-5
			if evento.key == K_RIGHT:
				jugador.vel_posX=5
			if evento.key == K_UP:
				jugador.salto=True
		if evento.type == KEYUP:
			jugador.vel_posX=0

		#logica

		if jugador.salto:
			jugador.vel_posY=-10
			jugador.salto=False

		if jugador.rect.x >= WIDTH-100 and jugador.vel_posX>0.:
			jugador.rect.x=WIDTH-100
			posFondoX+=velx
			for r in rivales:
				r.posx_fondo=posFondoX

		if jugador.rect.x <= 50 and jugador.vel_posX<0.:
			jugador.rect.x=50
			posFondoX-=velx
			for r in rivales:
				r.posx_fondo=posFondoX

		#Actualizacion
		pantalla.fill(NEGRO)
		pantalla.blit(fondoJuego,[posFondoX,posFondoY])
		todos.update()
		todos.draw(pantalla)
		pygame.display.flip()
		reloj.tick(100)

if __name__ == "__main__":
	main()
