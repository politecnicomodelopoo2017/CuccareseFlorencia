from .Personas import Personas
class Pasajero(object,Personas):
    vip=None
    necesidadesespeciales=None

    def setvip(self,v):
        self.vip=v

    def setnecesidades(self,n):
        self.necesidadesespeciales=n
