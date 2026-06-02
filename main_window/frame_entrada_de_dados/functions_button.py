ativado = False
show_frame = False

def ativarBotao():
    setAtivado(True)

def getAtivado() -> bool:
    global ativado

    return ativado

def setAtivado(
    off_on: bool
):
    global ativado

    ativado = off_on

def getShowFrame() -> bool:
    global show_frame

    return show_frame

def setShowFrame(
    off_on: bool
):
    global show_frame

    show_frame = off_on