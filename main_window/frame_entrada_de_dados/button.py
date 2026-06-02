from customtkinter import CTkFrame, CTkButton
from .functions_button import ativarBotao

class Button(CTkButton):
    def __init__(
        self,
        frame: CTkFrame
    ):
        super().__init__(
            frame,
            text="Analisar a frase",
            height=35,
            corner_radius=18,
            font=(
                "Arial",
                16,
                "bold"
            ),
            command= lambda: ativarBotao()
        )