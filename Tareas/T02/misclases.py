

class Jugador:
    def __init__(self,id,alias,full_name,_club,league,nationality,overall):
        self.id=int(id)
        self.alias=alias
        self.full_name=full_name
        self.league=league
        self.nationality=nationality
        self.overall=overall

    def __repr__(self):
        salida="{},{},{},".format(str(self.id),self.alias,self.full_name)
        salida+="{},{},{}".format(self.league,self.nationality,self.overall)
        return salida

