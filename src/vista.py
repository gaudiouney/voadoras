__author__ = 'gaudiouney'
FACE = 'http://misslittlecherry.files.wordpress.com/2009/12/1213276673857798001xo0.jpg'
CH = CV = 200
#FACEBOTAO = 'http://cdns2.freepik.com/fotos-gratis/clip-art-botao-vermelho_429468.jpg'
#HH = HV = 60

#class Botao:
#    def __init__(self, html, deque, tela):
#        bt = self.e_botao = html.IMG(src=FACEBOTAO, width=HH, heigth=HV)
#        bt.onclick = deque.voa
#        bt.style.position = "absolute"
#        bt.style.marginLeft = '10px'
#        tela <= bt
class Carta:
    def __init__(self, html, xy, ev, mouse_over, drag_start, source, cartas):#, deque):
        x, y = self.pos = xy
        self.m0 = [None,None]
        self.cartas = cartas
        ct = self.e_carta = html.IMG(src=FACE, width=CH, heigth=CV)
        ct.style.position = "absolute"
        ct.style.left, ct.style.top = xy
        x = x / 5
        cartas <= ct
        source.bind('mouseover',mouse_over)
        source.bind('dragstart',drag_start)
    def mouse_over(self, ev):
        print('mouse over ! ')
        ev.target.style.cursor = "pointer"
        self.m0 = [None,None]
    def drag_start(self, ev, ct, x):
        self.m0 = [ev.x-ev.target.left,ev.y-ev.target.top]
        ev.data['text']=ev.target.id
        ev.data.effectAllowed = 'move'
        #ct.style.transition = "left 0.4s linear %fs, top 0.4s linear %fs" % (x, x)
        #cartas <= ct
    #def voa(self, evento):
    #    self.deque.voa()
    #    self.botao.voa()

    #def voar(self, delta):
        #dx, dy = delta
        #x, y = self.pos
        #xy = self.pos = x + dx, y + dy
        #ct = self.e_carta
        #ct.style.left, ct.style.top
#class Deque:
#    def __init__(self, html, tela):
#        self.tela = tela
#        self.deque = [Carta(html, (x*4, 200), self) for x in range(10)]
#
#    def voa(self, ev=0):
#        [carta.voar((200, 200)) for carta in self.deque]
#    def __le__(self, other):
#        self.tela <= other

def main(html, doc):
    tela = doc["main"]
    def drag_over(ev):
        ev.data.dropEffect = 'move'
        ev.preventDefault()
    def drop(ev):
        src_id = ev.data['text']
        elt = [src_id]
        elt.style.left = "%spx" %(ev.x) #-m0[0])
        elt.style.top = "%spx" %(ev.y) #-m0[1])
        elt.draggable = False
        elt.unbind('mouseover')
        elt.style.cursor = "auto"
        ev.preventDefault()

    splash = html.DIV()
    cartas = html.DIV()
    tela <= splash
    tela <= cartas
#     deque = Deque(html, splash)
    cartas = Carta(html, cartas)
    panel = tela
    tela <= panel
    dest = tela
    tela <= dest
    source = doc['Carta']#doc["Botao"]
    source <= cartas #botao
    source.draggable = True
    tela.bind('dragover',drag_over)
    tela.bind('drop',drop)
