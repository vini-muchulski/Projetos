class Programa:
        def __init__(self, nome, ano):
            self._nome = nome.title()
            self.ano = ano
            self._likes = 0

        @property
        def likes(self):
            return self._likes

        def curtida(self):
            self._likes += 1

        @property
        def nome(self):
            return self._nome

        @nome.setter
        def nome(self, novo_nome):
            self._nome = novo_nome.title()

        def imprime(self):
            print("Nome: {} - Ano: {} - Curtidas {}".format(self._nome ,self.ano ,self.likes))

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome,ano)
        self.duracao = duracao

    def imprime(self):
        print("Nome: {} - Ano: {} - Duração: {} min - Curtidas {} ".format(self._nome, self.ano, self.duracao, self.likes))

class Documentario(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome,ano)
        self.temporadas = temporadas

    def imprime(self):
        print("Nome: {} - Ano: {} - Temporadas: {} - Curtidas {} ".format(self._nome, self.ano, self.temporadas, self.likes))

class Serie(Programa):
    def __init__(self,nome ,ano ,temporadas):
        super().__init__(nome,ano)
        self.temporadas = temporadas

    def imprime(self):
        print("Nome: {} - Ano: {} - Temporadas: {} - Curtidas {} ".format(self._nome, self.ano, self.temporadas, self.likes))

class playlist:
    def __init__(self,nome,programas):
        self.nome = nome
        self.__programas = programas

    @property
    def listagem(self):
        return self.__programas

    @property
    def __len__(self):
        return len(self.__programas)

    def __getitem__(self, item):
        return self.__programas[item]


twd = Serie("the walking dead", 2010,11,)
topgun2 = Filme("top gun: maverick", 2022, 137)
doc = Documentario("One Strange Rock", 2018, 2)
FaM = Serie("For All Mankind",2019,3)

topgun2.curtida()
topgun2.curtida()
FaM.curtida()
twd.curtida()
twd.curtida()

filmes_series = [topgun2, doc, FaM, twd]
playlist_folga = (playlist("Fim de semana", filmes_series).listagem)

print ("Tamanho da playlist: {} programas".format(len(playlist_folga)))

print("--------------------------------")

print(topgun2 in playlist_folga)

for programa in playlist_folga:
    programa.imprime()