__author__ = 'gaudiouney'
TABULEIRO = 'http://mosaicosmarinella.com.br/product_images/r/003/azulejo_colorido_amarelo__68802_zoom.jpg?wmode=opaque'
TAL = TAC = 500
FACE = 'http://wallpaper.ultradownloads.com.br/114690_Papel-de-Parede-Paisagem-de-primavera_1600x1200.jpg' #, 'http://www.baixaki.com.br/imagens/wpapers/BXK15424_paisagem_tropical800.jpg','http://www.sopapeldeparede.com.br/wp-content/uploads/2009/09/paisagem_001.jpg']
#CARTAS = FACE*3*3
CH = CV = 200
FACEBOTAO = 'http://img.vivaolinux.com.br/imagens/dicas/comunidade/pms-ms.png'
HH = HV = 50
TELAFUNDO = 'http://www.flaviense.com.br/media/catalog/product/cache/1/image/1200x1200/9df78eab33525d08d6e5fb8d27136e95/f/o/formica-lousa-l-113-verde-oficial.gif'
TC = TL = 1415

class Botao:
    def __init__(self, html, deque, e_tela, e_botao):
        self.e_tela = e_tela
        bt = self.e_botao = e_botao
        bt.onclick = deque.voa
        bt.style.position = "absolute"
        bt.style.left = '10px'
        e_tela <= bt
        e_botao<=bt

class Carta:
    def __init__(self, html, xy, deque):
        x, y = self.pos = xy
        self.deque = deque
        ct = self.e_carta
        ct.style.position = "absolute"
        ct.style.left, ct.style.top = xy
        x = x/10
        ct.style.transition = "left 1s linear %fs, top 1s linear %fs" % (x, x)
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

class Tabuleiroamarelo:
    def __init__(self, html, e_tela):
        self.e_tela = e_tela
        tb = self.e_tabuleiroamarelo
        tb.style.position = "absolute"
        tb.style.marginLeft = '150px'
        e_tela<= tb

def main(html, doc):
    e_botao = html.DIV()
    e_botao = html.IMG(src=FACEBOTAO, width=HH, heigth=HV)
    e_botao.style.position = "absolute"
    e_botao.style.marginLeft = '0px'
    tela = doc["main"]
    cartas = html.DIV()
    cartas = html.IMG(src= FACE , width=CH, heigth=CV)
    cartas.style.position = "absolute"
    cartas.style.marginLeft = '440px'
    e_tela = html.IMG(src=TELAFUNDO, width=TC, heigth=TL)
    e_tela.style.position = "absolute"
    e_tela.style.marginLeft = '0px'
    tela <= e_tela
    e_tabuleiroamarelo = html.DIV()
    e_tabuleiroamarelo = html.IMG(src=TABULEIRO, width=TAC, heigth=TAL)
    e_tabuleiroamarelo.style.position = "absolute"
    e_tabuleiroamarelo.style.marginLeft = '420px'
    splash = html.DIV()
    tela<= e_tabuleiroamarelo
    tela <= cartas
    tela<= e_botao
    tela <= splash
    e_tabuleiroamarelo = Tabuleiroamarelo(html,e_tabuleiroamarelo)
    deque = Deque(html, splash)
    e_botao = Botao(html, deque, cartas)