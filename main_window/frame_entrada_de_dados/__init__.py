from customtkinter import CTkFrame, CTk
from .label import Label
from .entry import Entry
from .button import Button
from .functions_button import getAtivado, setAtivado
from .analisar_frase import AnalisarFrase

class FrameEntradaDeDados(CTkFrame):
    def __init__(
        self,
        window: CTk
    ):
        super().__init__(
            window,
            corner_radius = 0    
        )

        for count in range(0, 3):
           self.grid_rowconfigure(count, weight=1)

        self.grid_columnconfigure(0, weight=1)

        self.__frase_analisada = {}

        self.__label_01 =  Label(self)

        self.__label_01.grid(
            row=0,
            column=0, 
            padx=(
                0, 250
            ),
            pady=(
                10, 0
            )
        )

        self.__entry_01 = Entry(self)

        self.__entry_01.grid(
            row=1,
            column=0,
            padx=(
                25, 25
            ),
            pady=(
                0, 15
            )
        )

        self.__button_01 = Button(self)

        self.__button_01.grid(
            row=2,
            column=0,
            pady=(
                0, 15
            )
        )

        self.__verificarFrame()

    def __verificarFrame(self):
        ativado = getAtivado()

        if ativado:
            if self.__entry_01.get() != "":
                frase = self.__entry_01.get()

                analisador_de_frase = AnalisarFrase(frase)

                self.__frase_analisada = analisador_de_frase.getAnaliseDaFrase()

            else:
                self.__frase_analisada = {}
                
            setAtivado(False)


        self.after(
            1,
            self.__verificarFrame
        )

    def getFraseAnalisada(self):
        return self.__frase_analisada