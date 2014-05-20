__author__ = 'gaudiouney'

def tabuleio(tela, html):
    tabul = html.DIV()
    tela <= tabul

def embaralha(tela, html):
    pass

def voa(tela, html):
    pass

def main(html, doc):
    tela = doc["main"]
    #html = gui.html
    splash = html.DIV("VOADORAS")
    tela <= splash
    tabuleiro(tela, html)
    embaralha(tela, html)
    voa(tela, html)