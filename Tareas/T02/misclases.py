class Jugador:
    def __init__(self,id,alias,full_name,club,league,nationality,overall):
        self.id=int(id)
        self.alias=alias
        self.full_name=full_name
        self.club=club
        self.league=league
        self.nationality=nationality
        self.overall=overall

    def __repr__(self):
        salida="{},{},{},".format(str(self.id),self.alias,self.full_name)
        salida+="{},{},{},".format(self.club,self.league,self.nationality)
        salida+="{}".format(self.overall)
        return salida

