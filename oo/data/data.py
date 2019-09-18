class Data:
    def __init__(self,dia,mes,ano):
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano
    
    def set_dia(self,dia):
        if dia > 0 and dia < 32:
            self.__dia = dia
        else:
            self.__dia = 1
    
    def set_mes(self, mes):
        if mes > 0 and mes < 13:
            self.__mes = mes
        else:
            self.__mes = 1

    def set_ano(self, ano):
        if ano > 0:
            self.__ano = ano
        else:
            self.__ano = 1

    def get_ano(self):
        return self.__ano
    
    def get_dia(self):
        return self.__dia

    def get_mes(self):
        return self.__mes

    def __str__(self):
        return(f'{self.__dia}/{self.__mes}/{self.__ano}')

if __name__ == "__main__":
    d = Data(1,1,1990)
    print(d)