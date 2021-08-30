import pygame
from componentes import Jogo, Cobrinha, Comida

pygame.init()

if __name__ == '__main__':
    jogo = Jogo()
    cobrinha = Cobrinha()
    comida = Comida()

    jogo.adicionar_cobrinha(cobrinha)
    jogo.adicionar_comida(comida)

while True:
    jogo.tick(20)
    eventos = pygame.event.get()
    jogo.lidar_eventos(eventos)
    jogo.run()
