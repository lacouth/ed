class Aluno:
    def __init__(self, matricula, nome, notas = []):
        self.__matricula = matricula
        self.__nome = nome
        self.__notas = notas


    def get_nome(self):
        return self.__nome
    def get_matricula(self):
        return (f'A matrícula de {self.__nome} é {self.__matricula}')

    def media(self):
        return sum(self.__notas)/len(self.__notas)
    
    def adiciona_nota(self, n):
        self.__notas.append(n)
    
    def __add__ (self, nota):
        self.__notas.append(nota)
        return self

if __name__ == "__main__":
    fulano = Aluno(1234,"Fulano de tal")
    
    fulano+=100
    fulano+=80

    fulano = fulano +  70


    print(f'A média é {fulano.media()}')

