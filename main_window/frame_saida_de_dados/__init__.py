from customtkinter import CTk, CTkFrame
from .label import Label

class FrameSaidaDeDados(CTkFrame):
    def __init__(
        self,
        window: CTk,
    ):
        super().__init__(
            window,
            corner_radius=0,
            width=450,
            height=250
        )

        self.grid_propagate(False)

        self.grid_columnconfigure(
            0,
            weight=1
        )

        self.__labels = []
        self.__analises_da_frase = {}

    def setAnalisesDaFrase(
        self,
        analises_da_frase = {}
    ):
        if self.__analises_da_frase != analises_da_frase:
            self.__analises_da_frase = analises_da_frase

            self.__labels.clear()
            
            if len(analises_da_frase) > 0:
                for key, value in self.__analises_da_frase.items():
                    frase = f"{key}: {value}"

                    self.__labels.append(
                        Label(
                            self,
                            frase
                        )
                    )

                for count in range(0, len(self.__labels)):
                    self.grid_rowconfigure(count, weight=1)

                    if count < len(self.__labels) - 1:
                        self.__labels[count].grid(
                            row=count,
                            column=0
                        )
                    else:
                        self.__labels[count].grid(
                            row=count,
                            column=0,
                            pady=(
                                0, 15
                            )
                        )