import pygame as pg


def isnumber(value):
    try:
        float(value)
        return True
    except:
        return False


def get_key(val, dici):
    for key, value in dici.items():
        if val == value:
            return key

    return "There is no such Key"


def first_letter_upper(string):
    array = list(string)
    return f'{array[0].upper()}{"".join(array[1:]).lower()}'


def duas_casas(num):
    if num // 1 == num / 1:
        return f'{num}.00'
    return num


class Caixa:

    def __init__(self, x, y, w, h, tela, tamanho=16, text='', color_text=(0, 0, 0), color_box=(0, 0, 0)):
        self.rect = pg.Rect(x, y, w, h)
        self.text = text
        self.tamanho = tamanho
        self.tela = tela
        self.cor_txt = color_text
        self.cor_box = color_box
        self.active = False
        self.font = pg.font.Font(None, self.tamanho)
        self.txt_surp = self.font.render(self.text, True, self.cor_txt)

    def escrever(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = True
            else:
                self.active = False

        elif event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.txt_surp = self.font.render(self.text, True, self.cor_txt)

    def clicar(self, event, atalho=None):
        if atalho is not None:
            if event.type == pg.KEYDOWN:
                if event.key == atalho:
                    return True
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return True
        else:
            return False

    def update(self,  centralizar_caixa=False):
        width = max(self.rect.w, self.txt_surp.get_width() + 15)
        self.rect.w = width
        self.txt_surp = self.font.render(self.text, True, self.cor_txt)

        if centralizar_caixa:
            self.rect.x = self.tela.get_width() / 2 - width / 2

        if self.active:
            pg.draw.line(self.tela, self.cor_txt, (self.rect.x + self.txt_surp.get_width() + 5, self.rect.y + 3),
                         (self.rect.x + self.txt_surp.get_width() + 5, self.rect.y + self.rect.h - 3))

    def draw(self, centralizar_letra=False):
        if centralizar_letra:
            self.tela.blit(self.txt_surp, (self.rect.x + (self.rect.w / 2 - self.txt_surp.get_width() / 2),
                                           self.rect.y + (self.rect.h / 2 - self.tamanho / 3)))
        else:
            self.tela.blit(self.txt_surp, (self.rect.x+5, self.rect.y + (self.rect.h / 2 - self.tamanho / 3)))
        pg.draw.rect(self.tela, self.cor_box, self.rect, 2)
