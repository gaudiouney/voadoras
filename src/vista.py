__author__ = 'gaudiouney'
TAL = TAC = 500
FACE = 'http://www.skatecuriosidade.com/wp-content/uploads/2013/03/king.jpg'
CH = CV = 180
FACEBOTAO = 'http://img.vivaolinux.com.br/imagens/dicas/comunidade/pms-ms.png'
HH = HV = 50
TELAA2 = 'http://cerebromasculino.com/wp-content/uploads/2013/09/moldura_quadro03.gif'
HC = HV = 500

class Botao:
    def __init__(self, html, deque, tela):
        bt = self.e_botao = html.IMG(src=FACEBOTAO, width=HH, heigth=HV)
        bt.onclick = deque.voa
        bt.style.position = "relative"
        bt.style.marginLeft = '10px'
        tela <= bt

class Retorno:
    def __init__(self, html, deque, tela):
        bt = self.e_botao = html.IMG(src=FACEBOTAO, width=HH, heigth=HV)
        bt.onclick = deque.voltar
        bt.style.position = "relative"
        bt.style.marginLeft = '30px'
        tela <= bt

class Carta:
    def __init__(self, html, xy, deque):
        x, y = self.pos = xy
        self.deque = deque
        ct = self.e_carta = html.IMG(src=FACE, width=CH, heigth=CV)
        ct.style.position = "absolute"
        ct.style.left, ct.style.top = xy
        ct.style.marginLeft = '140px'
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
        self.deque = [Carta(html, (x*4, 128), self) for x in range(10)]
    def voa(self, ev=0):
        [carta.voar((800, 200)) for carta in self.deque]
    def voltar(self, ev):
        [carta.voar((-800, -200)) for carta in self.deque]
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
    tela2 <= html.IMG(src=TELAA2, width=HC, heigth=HV);
    deque = Deque(html, splash)
    botao = Botao(html, deque, cartas)
    retorno = Retorno(html, deque, cartas)