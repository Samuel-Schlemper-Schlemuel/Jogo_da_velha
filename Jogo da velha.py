import funcoes_uteis as fu


class Jogo:
    valores = {
        'A1': '__',
        'A2': '__',
        'A3': '__',
        'B1': '__',
        'B2': '__',
        'B3': '__',
        'C1': '__',
        'C2': '__',
        'C3': '__'
    }

    def __init__(self):
        print('Escreva o lugar que você quer que seu símbolo apareça')
        self.desenho_atual = '  1  2  3\na __|__|__\nb __|__|__\nc __|__|__'
        print(self.desenho_atual)

    def __desenhar__(self, simbolo, local):
        if self.valores[local] == '__':
            self.valores[local] = simbolo
            self.desenho_atual = f'  1  2  3\na {self.valores["A1"]}|{self.valores["A2"]}|{self.valores["A3"]}' \
                                 f'\nb {self.valores["B1"]}|{self.valores["B2"]}|{self.valores["B3"]}' \
                                 f'\nc {self.valores["C1"]}|{self.valores["C2"]}|{self.valores["C3"]}'
            print(self.desenho_atual)
        else:
            print('Você já escolheu esse local, digite outro')
            rodar()

    def __ganhar__(self, ganhador):
        if self.valores['A1'] == self.valores['A2'] == self.valores['A3'] != '__':
            return f'O {ganhador.nome} ganhou'

        elif self.valores['B1'] == self.valores['B2'] == self.valores['B3'] != '__':
            return f'O {ganhador.nome} ganhou'

        elif self.valores['C1'] == self.valores['C2'] == self.valores['C3'] != '__':
            return f'O {ganhador.nome} ganhou'

        elif self.valores['A1'] == self.valores['B1'] == self.valores['C1'] != '__':
            return f'O {ganhador.nome} ganhou'

        elif self.valores['A2'] == self.valores['B2'] == self.valores['C2'] != '__':
            return f'O {ganhador.nome} ganhou'

        elif self.valores['A3'] == self.valores['B3'] == self.valores['C3'] != '__':
            return f'O {ganhador.nome} ganhou'

        elif self.valores['A1'] == self.valores['B2'] == self.valores['C3'] != '__':
            return f'O {ganhador.nome} ganhou'

        elif self.valores['A3'] == self.valores['B2'] == self.valores['C1'] != '__':
            return f'O {ganhador.nome} ganhou'

        else:
            return 'Ninguém ganhou ainda'

    def __recomecar__(self):
        self.valores = {
            'A1': '__',
            'A2': '__',
            'A3': '__',
            'B1': '__',
            'B2': '__',
            'B3': '__',
            'C1': '__',
            'C2': '__',
            'C3': '__'
        }
        self.__init__()


class Jogador:
    def __init__(self, nome, simbolo):
        self.nome = nome
        self.vitorias = 0
        self.simbolo = simbolo


nome_1 = input('Primeiro jogador, escreva seu nome: ')
nome_2 = input('Segundo jogador, escreva seu nome: ')
jogador1 = Jogador(nome_1, 'X')
jogador2 = Jogador(nome_2, 'O')
jogo = Jogo()
jogador_atual = jogador1
acabou = False

print(f'{jogador1.nome} será o X e o {jogador2.nome} será o O, para escolher o lugar onde quer jogar é só digitar '
      f'o número e a letra que representa o local')


def rodar():
    global jogador_atual, acabou

    while True:
        local = input(f'{jogador_atual.nome} digite onde quer jogar: ')
        correto = False

        for key in jogo.valores.keys():
            if fu.first_letter_upper(local) == key:
                jogo.__desenhar__(jogador_atual.simbolo, fu.first_letter_upper(local))
                correto = True

        if not correto:
            print('Esse lugar não existe, digite algo que encaixe, como A1 para jogar na primeira célula')
            rodar()

        ganhou = jogo.__ganhar__(jogador_atual)

        if ganhou != 'Ninguém ganhou ainda':
            print(ganhou)
            jogador_atual.vitorias += 1
            resposta = input('Vocês querem jogar outra partida (responda não caso queira parar)? ')

            if resposta == 'não':
                acabou = True
            else:
                jogo.__recomecar__()

        jogador_atual = jogador1 if jogador_atual == jogador2 else jogador2

        if acabou:
            print(f'O {jogador1.nome} venceu {jogador1.vitorias} vezes, enquanto {jogador2.nome} venceu'
                  f' {jogador2.vitorias} vezes')
            break


rodar()
