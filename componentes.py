import pygame
from random import randint


class Jogo:
    def __init__(self):
        self.tela = pygame.display.set_mode((600, 600))
        self.cor_fundo = (0, 0, 0)
        self.clock = pygame.time.Clock()
        self.fonte = pygame.font.SysFont('Arial', 16)
        self.cor_fonte = (255, 255, 0)
        self.cobrinha = None
        self.comida = None
        self.pontuacao = 0

    def tick(self, tick):
        self.clock.tick(tick)

    def adicionar_cobrinha(self, nova_cobrinha):
        self.cobrinha = nova_cobrinha

    def adicionar_comida(self, nova_comida):
        self.comida = nova_comida

    def desenhar_pontuacao(self):
        texto_renderizado = self.fonte.render(f'Pontuação: {self.pontuacao}', False, self.cor_fonte)
        self.tela.blit(texto_renderizado, (0, 0))

    def checar_colisao(self):
        if self.cobrinha.partes[0][0] == self.comida.posicao[0] and self.cobrinha.partes[0][1] == self.comida.posicao[1]:
            self.pontuacao += 1
            self.cobrinha.partes.append([self.cobrinha.partes[-1][0], self.cobrinha.partes[-1][1]])
            self.comida.sortear_posicao()

    def checar_gameover(self):
        colisao_parede = not 0 <= self.cobrinha.partes[0][0] <= 590 or not 0 <= self.cobrinha.partes[0][1] <= 590
        colisao_cobrinha = [self.cobrinha.partes[0][0], self.cobrinha.partes[0][1]] in self.cobrinha.partes[1:]
        if colisao_parede or colisao_cobrinha:
            exit()


    def lidar_eventos(self, eventos):
        for evento in eventos:
            if evento.type == pygame.QUIT:
                exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP and self.cobrinha.direcao != 2:
                    self.cobrinha.direcao = 1
                if evento.key == pygame.K_DOWN and self.cobrinha.direcao != 1:
                    self.cobrinha.direcao = 2
                if evento.key == pygame.K_RIGHT and self.cobrinha.direcao != 4:
                    self.cobrinha.direcao = 3
                if evento.key == pygame.K_LEFT and self.cobrinha.direcao != 3:
                    self.cobrinha.direcao = 4

    def run(self):
        self.cobrinha.mover()
        self.checar_colisao()
        self.checar_gameover()

        self.tela.fill(self.cor_fundo)
        self.desenhar_pontuacao()
        self.comida.desenhar(self.tela)
        self.cobrinha.desenhar(self.tela)

        pygame.display.update()


class Cobrinha:
    def __init__(self):
        self.partes = [[350, 290], [340, 290], [330, 290]]
        self.cor = (255, 255, 255)
        self.direcao = 3

    def desenhar(self, screen):
        for parte in self.partes:
            pygame.draw.rect(screen, self.cor, (parte[0], parte[1], 10, 10))

    def mover(self):
        for i in range(len(self.partes) - 1, 0, -1):
            self.partes[i] = [self.partes[i - 1][0], self.partes[i - 1][1]]

        if self.direcao == 1:
            self.partes[0][1] -= 10
        if self.direcao == 2:
            self.partes[0][1] += 10
        if self.direcao == 3:
            self.partes[0][0] += 10
        if self.direcao == 4:
            self.partes[0][0] -= 10


class Comida:
    def __init__(self):
        self.cor = (255, 0, 0)
        self.tamanho = 10
        self.sortear_posicao()

    def sortear_posicao(self):
        self.posicao = [round(randint(0, 590)/10) * 10, round(randint(0, 590)/10) * 10]

    def desenhar(self, screen):
        pygame.draw.rect(screen, self.cor, (self.posicao[0], self.posicao[1], self.tamanho, self.tamanho))
