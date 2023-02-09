class Cliente():
    
    __slots__ = ['_nome', '_sobrenome', '_cpf']

    def __init__(self, nome, sobrenome, cpf):
        self._nome = nome
        self._sobrenome = sobrenome
        self._cpf = cpf

    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, n):
        self._nome = n
    
    @property
    def sobrenome(self):
        return self._sobrenome
    @sobrenome.setter
    def sobrenome(self, s):
        self._sobrenome = s

    @property
    def cpf(self):
        return self._cpf
    @cpf.setter
    def cpf(self, c):
        self._cpf = c
