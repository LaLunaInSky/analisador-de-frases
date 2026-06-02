from customtkinter import CTkEntry, CTkFrame

class Entry(CTkEntry):
    def __init__(
        self,
        frame: CTkFrame
    ):
        super().__init__(
            frame,
            placeholder_text="Pode conter números ou caracteres",
            width=400,
            height=40,
            font=(
                "Arial",
                15
            )
        )