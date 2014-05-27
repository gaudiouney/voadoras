__author__ = 'gaudiouney'
FACE = 'http://misslittlecherry.files.wordpress.com/2009/12/1213276673857798001xo0.jpg'
CH = CV = 50
FACEBOTAO = 'http://cdns2.freepik.com/fotos-gratis/clip-art-botao-vermelho_429468.jpg'
HH = HV = 30
class Botao:
    def __init__(self, html, deque, tela):
        bt = self.e_botao = html.IMG(src=FACEBOTAO, width=HH, heigth=HV)
        bt.onclick = deque.voa
        bt.style.position = "relative"
        tela <= bt

class Carta:
    def __init__(self, html, xy, deque):
        x, y = self.pos = xy
        self.deque = deque
        ct = self.e_carta = html.IMG(src=FACE, width=CH, heigth=CV)
        ct.style.position = "absolute"
        ct.style.left, ct.style.top = xy
        x = x / 5
        ct.style.transition = "left 1s linear %fs, top 1s linear %fs" % (x, x)
        deque <= ct
        #ct.onclick = self.voa
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
        self.deque = [Carta(html, (x*4, 10), self) for x in range(10)]

    def voa(self, ev=0):
        [carta.voar((100, 100)) for carta in self.deque]
    def __le__(self, other):
        self.tela <= other

def main(html, doc):
     tela = doc["main"]
     #html = gui.html
     splash = html.DIV()
     cartas = html.DIV()
     tela <= splash
     tela <= cartas
     #tabuleiro(tela, html)
     #embaralha(tela, html)
     #voa(tela, html)
     deque = Deque(html, splash)
     botao = Botao(html, deque, cartas)