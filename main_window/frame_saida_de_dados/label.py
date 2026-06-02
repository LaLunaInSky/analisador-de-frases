from customtkinter import CTkFrame, CTkLabel

class Label(CTkLabel):
    def __init__(
        self,
        frame: CTkFrame,
        text_label: str = ""
    ):
        super().__init__(
            frame,
            text=text_label,
            font=(
                "Arial",
                18
            )
        )