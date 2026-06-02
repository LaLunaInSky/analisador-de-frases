from customtkinter import CTk
from .frame_entrada_de_dados import FrameEntradaDeDados
from .frame_saida_de_dados import FrameSaidaDeDados
from .frame_entrada_de_dados.functions_button import getShowFrame, setShowFrame

class App(CTk):
    def __init__(self):
        super().__init__()

        self.title("Analisador de Frases")

        self.anchor("center")
        
        self.resizable(
            False,
            False
        )

        for count in range(0, 2):
            self.grid_rowconfigure(count, weight=1)

        self.grid_columnconfigure(0, weight=1)

        self.__frame_entrada_de_dados = FrameEntradaDeDados(self)

        self.__frame_saida_de_dados = FrameSaidaDeDados(self)

        self.__frame_entrada_de_dados.grid(
            row=0,
            column=0
        )

        self.__verificarWindow()

    def __verificarWindow(self):
        show_frame = getShowFrame()

        frase_analisada = self.__frame_entrada_de_dados.getFraseAnalisada()

        if len(frase_analisada) > 0:
            self.__frame_saida_de_dados.setAnalisesDaFrase(frase_analisada)

            setShowFrame(True)
        else:
            self.__frame_saida_de_dados.setAnalisesDaFrase()

            setShowFrame(False)

        if show_frame:
            self.__frame_saida_de_dados.grid(
                row=1,
                column=0
            )
        else:
            self.__frame_saida_de_dados.grid_remove()

        self.after(
            1,
            self.__verificarWindow
        )