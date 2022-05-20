import funcoes_uteis as fu
import pygame as pg
import time


pg.init()
tamanho = largura, altura = 900, 600
black = 20, 20, 20
blue = 0, 0, 200
tela = pg.display.set_mode(tamanho)
pg.display.set_caption('Jogo da velha')


class Jogo:
    blocos = {
        'A1': fu.Caixa(300, 150, 100, 100, tela, 40, '', blue, blue),
        'A2': fu.Caixa(300, 250, 100, 100, tela, 40, '', blue, blue),
        'A3': fu.Caixa(300, 350, 100, 100, tela, 40, '', blue, blue),
        'B1': fu.Caixa(400, 150, 100, 100, tela, 40, '', blue, blue),
        'B2': fu.Caixa(400, 250, 100, 100, tela, 40, '', blue, blue),
        'B3': fu.Caixa(400, 350, 100, 100, tela, 40, '', blue, blue),
        'C1': fu.Caixa(500, 150, 100, 100, tela, 40, '', blue, blue),
        'C2': fu.Caixa(500, 250, 100, 100, tela, 40, '', blue, blue),
        'C3': fu.Caixa(500, 350, 100, 100, tela, 40, '', blue, blue)
    }

    def __init__(self, jogador1, jogador2):
        self.jogador1 = jogador1
        self.jogador2 = jogador2
        self.explicao = fu.Caixa(50, 50, 100, 60, tela, 40, f'O {jogador1.nome} é o X e o {jogador2.nome} é o O',
                                 blue, blue)
        self.mensagem = fu.Caixa(50, 470, 900, 50, tela, 40, '', blue, black)
        self.jogar_novamente_sim = fu.Caixa(345, 540, 100, 60, tela, 40, 'sim', blue, blue)
        self.jogar_novamente_nao = fu.Caixa(455, 540, 100, 60, tela, 40, 'não', blue, blue)

    def desenhar(self, escrever_mensagem, vitoria=False):
        self.explicao.update(True)
        self.explicao.draw(True)

        for bloco in self.blocos.values():
            bloco.update()
            bloco.draw(True)

        if escrever_mensagem:
            self.mensagem.update(True)
            self.mensagem.draw(True)

        if vitoria:
            self.jogar_novamente_sim.update()
            self.jogar_novamente_sim.draw(True)
            self.jogar_novamente_nao.update()
            self.jogar_novamente_nao.draw(True)

    def ganhar(self):
        if self.blocos['A1'].text == self.blocos['A2'].text == self.blocos['A3'].text != '':
            return True
        elif self.blocos['B1'].text == self.blocos['B2'].text == self.blocos['B3'].text != '':
            return True
        elif self.blocos['C1'].text == self.blocos['C2'].text == self.blocos['C3'].text != '':
            return True
        elif self.blocos['A1'].text == self.blocos['B1'].text == self.blocos['C1'].text != '':
            return True
        elif self.blocos['A2'].text == self.blocos['B2'].text == self.blocos['C2'].text != '':
            return True
        elif self.blocos['A3'].text == self.blocos['B3'].text == self.blocos['C3'].text != '':
            return True
        elif self.blocos['A1'].text == self.blocos['B2'].text == self.blocos['C3'].text != '':
            return True
        elif self.blocos['A3'].text == self.blocos['B2'].text == self.blocos['C1'].text != '':
            return True
        else:
            return False

    def recomecar(self):
        for bloco in self.blocos.values():
            bloco.text = ''


class Jogador:
    def __init__(self, nome, simbolo):
        self.nome = nome
        self.vitorias = 0
        self.simbolo = simbolo


texto_1 = fu.Caixa(50, 50, 200, 40, tela, 32, 'Escrevam seus nomes abaixo', blue, black)
caixa_1 = fu.Caixa(50, 150, 200, 40, tela, 32, '', blue, blue)
caixa_2 = fu.Caixa(50, 250, 200, 40, tela, 32, '', blue, blue)
botao = fu.Caixa(50, 350, 200, 40, tela, 32, 'Clique para enviar', blue, blue)
caixas = [caixa_1, caixa_2]
continuar = True

while continuar:
    tela.fill(black)
    clock = pg.time.Clock()
    texto_1.update(True)
    texto_1.draw()
    botao.update(True)
    botao.draw()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        if botao.clicar(event, pg.K_RETURN):
            continuar = False
            break
        for caixa in caixas:
            caixa.escrever(event)

    for caixa in caixas:
        caixa.update(True)
        caixa.draw()

    pg.display.flip()
    clock.tick(30)


nome_1 = caixa_1.text
nome_2 = caixa_2.text
jogador1 = Jogador(nome_1, 'X')
jogador2 = Jogador(nome_2, 'O')
jogo = Jogo(jogador1, jogador2)
jogador_atual = jogador1
mensagem = False
vitoria = False


def rodar():
    global jogador_atual, mensagem, vitoria

    while True:
        tela.fill(black)
        clock = pg.time.Clock()
        simbolo = jogador1.simbolo if jogador_atual == jogador1 else jogador2.simbolo
        jogo.desenhar(mensagem, vitoria)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if not vitoria:
                for bloco in jogo.blocos.values():
                    if bloco.clicar(event):
                        if bloco.text == '':
                            bloco.text = f'{simbolo}'
                            jogador_atual = jogador1 if jogador_atual == jogador2 else jogador2
                            mensagem = False
                        else:
                            jogo.mensagem.text = 'Esse lugar já foi escolhido, selecione outro'
                            mensagem = True
            if vitoria:
                if jogo.jogar_novamente_sim.clicar(event):
                    jogador_atual = jogador1 if jogador_atual == jogador2 else jogador2
                    jogo.mensagem.text = f'O jogador a começar é {jogador_atual.nome}'
                    mensagem = True
                    jogo.recomecar()
                    vitoria = False
                elif jogo.jogar_novamente_nao.clicar(event):
                    jogo.mensagem.text = f'O jogador {jogador1.nome} ganhou {jogador1.vitorias} vezes e ' \
                                         f'{jogador2.nome} ganhou {jogador2.vitorias} vezes'
                    tela.fill(black)
                    jogo.desenhar(True, True)
                    pg.display.flip()
                    time.sleep(5)
                    pg.quit()
                    exit()
            else:
                if jogo.ganhar():
                    jogador_atual = jogador1 if jogador_atual == jogador2 else jogador2
                    jogo.mensagem.text = f'Parabéns! O {jogador_atual.nome} ganhou, iras jogar de novo?'
                    jogador_atual.vitorias += 1
                    mensagem = True
                    vitoria = True
                else:
                    empate = True
                    for bloco in jogo.blocos.values():
                        if bloco.text == '':
                            empate = False
                            break
                    if empate:
                        jogo.mensagem.text = 'Infelizmente houve um empate, tentem novamente!'
                        mensagem = True
                        jogo.recomecar()

        pg.display.flip()
        clock.tick(30)


rodar()
