import time

class Robot:
    def __init__(self, nom):
        self.nom = nom
        self.allume = False
        self.charge = 0
        self.vitesse = 0

    def allumer(self):
        if not self.allume:
            self.allume = True
            print(f"{self.nom} est allumé.")

    def eteindre(self):
        if self.allume:
            self.allume = False
            print(f"{self.nom} est éteint.")

    def charger_batterie(self):
        if self.allume:
            for _ in range(11):
                time.sleep(1)
                self.charge = _ * 10
            self.charge = 100

    def enregistrer_vitesse(self, vitesse):
        self.vitesse = vitesse

    def obtenir_vitesse(self):
        return self.vitesse

    def arreter_deplacement(self):
        if self.vitesse > 0:
            self.vitesse = 0
            

    def resume_etat(self):
        etat = "allumé" if self.allume else "éteint"
        return f"{self.nom} est {etat} avec une charge de {self.charge}%, se déplace à {self.vitesse} km/h."



"""
    Lorsque je crée mon robot, je veux pouvoir lui attribuer un nom
    Mon robot doit pouvoir s'allumer
    Mon robot doit pouvoir s'éteindre
    Mon robot doit pouvoir charger sa batterie à 100%, allumé ou non
    Le temps de charge ne peut pas être immédiat (10s max)
    Mon robot doit afficher sont % de batterie durant sa charge
    Mon robot doit pouvoir enregistrer une vitesse de déplacement
    Mon robot doit pouvoir me donner sa vitesse de déplacement
    Mon robot doit pouvoir arrêter son déplacement sur commande
    Mon robot doit pouvoir me fournir un résumé de son état global
"""
