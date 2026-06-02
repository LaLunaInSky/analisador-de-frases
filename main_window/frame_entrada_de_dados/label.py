from customtkinter import CTkLabel, CTkFrame

class Label(CTkLabel):
    def __init__(
        self,
        frame: CTkFrame
    ):
        super().__init__(
            frame,
            text="DIGITE O QUE QUISER",
            font=(
                "Arial",
                12,
                "bold"
            )
        )