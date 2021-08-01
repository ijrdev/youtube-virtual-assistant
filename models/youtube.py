class Youtube():
    def __init__(self, term) -> None:
        self.__term = term
    
    @property
    def term(self):
        return self.__term
    
    @term.setter
    def term(self, value):
        self.__term = value