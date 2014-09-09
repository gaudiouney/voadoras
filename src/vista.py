__author__ = 'gaudiouney'
TAL = TAC = 500
FACE = 'http://wallpaper.ultradownloads.com.br/114690_Papel-de-Parede-Paisagem-de-primavera_1600x1200.jpg' #, 'http://www.baixaki.com.br/imagens/wpapers/BXK15424_paisagem_tropical800.jpg','http://www.sopapeldeparede.com.br/wp-content/uploads/2009/09/paisagem_001.jpg']
#CARTAS = FACE*3*3
CH = CV = 200
FACEBOTAO = 'http://img.vivaolinux.com.br/imagens/dicas/comunidade/pms-ms.png'
HH = HV = 50

class Botao:
    def __init__(self, html, deque, tela):
        bt = self.e_botao = html.IMG(src=FACEBOTAO, width=HH, heigth=HV)
        bt.onclick = deque.voa
        bt.style.position = "relative"
        bt.style.marginLeft = '10px'
        tela <= bt

class Carta:
    def __init__(self, html, xy, deque):
        x, y = self.pos = xy
        self.deque = deque
        ct = self.e_carta = html.IMG(src=FACE, width=CH, heigth=CV)
        ct.style.position = "absolute"
        ct.style.left, ct.style.top = xy
        x = x / 5
        ct.style.transition = "left 0.5s linear %fs, top 0.5s linear %fs" % (x, x)
        deque <= ct
    def voa(self, evento):
        self.deque.voa()
    def voar(self, delta):
        dx, dy = delta
        x, y = self.pos
        xy = self.pos = x + dx, y + dy
        ct = self.e_carta
        ct.style.left, ct.style.top = xy

class Deque:
    def __init__(self, html, tela):
        self.tela = tela
        self.deque = [Carta(html, (x*4, 100), self) for x in range(10)]
    def voa(self, ev=0):
        [carta.voar((200, 200)) for carta in self.deque]
    def __le__(self, other):
        self.tela <= other

def main(html, doc):
    tela2 = doc["menu2"]
    tela = doc["main"]
    splash = html.DIV()
    cartas = html.DIV()
    tela <= splash
    tela <= cartas
    tela<=tela2
    deque = Deque(html, splash)
    botao = Botao(html, deque, cartas)