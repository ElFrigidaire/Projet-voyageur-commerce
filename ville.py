class Ville:

    # constructeur
    def __init__(self, nom, x, y):
        self.nom = nom
        self.x = x
        self.y = y

    # afficher la ville
    def __str__(self):
        return f"{self.nom, self.x, self.y}"
