class AnalisarFrase:
    def __init__(
        self,
        frase: str
    ):
        self.__frase_sem_espaços = self.__removerEspaços(frase)

        self.__analises_da_frase = {
            "Foi digitado": frase,
            "O tipo primitivo é": type(frase),
            "Só possui espaços?": self.__subtituirBoolean(frase.isspace()),
            "É um número?": self.__subtituirBoolean(self.__frase_sem_espaços.isnumeric()),
            "É alfabético?": self.__subtituirBoolean(self.__frase_sem_espaços.isalpha()),
            "É alfanúmerico?": self.__subtituirBoolean(self.__frase_sem_espaços.isalnum()),
            "Está em maiúscula?": self.__subtituirBoolean(frase.isupper()),
            "Está em minúscula?": self.__subtituirBoolean(frase.islower()),
            "Está capitalizada?": self.__subtituirBoolean(frase.istitle())
        }

    def __removerEspaços(
        self,
        frase: str
    ) -> str:
        frase_sem_espaço = frase.replace(" ", "")

        return frase_sem_espaço
    
    def __subtituirBoolean(
        self,
        boolean: bool
    ) -> str:
        if boolean:
            return "Sim"
        else:
            return "Não"

    def getAnaliseDaFrase(self):
        return self.__analises_da_frase