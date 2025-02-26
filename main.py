class City:
    def __init__(self, x, y):
         # Initialise une ville avec ses coordonnées x et y.
        self.x = x
        self.y = y

    def distance(self, city):
        # Calcule la distance entre la ville actuelle et une autre ville
        return np.hypot(self.x - city.x, self.y - city.y)

    def __repr__(self):
        # Retourne une représentation textuelle de la ville.
        return f"({self.x},{self.y})"