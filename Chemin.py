import random
import math


class Chemin:

    def __init__(self, liste_villes):
        self.liste_villes = liste_villes

        if liste_villes is not None:
            self.distance_totale = self.calculer_score()
        else:
            self.distance_totale = 0

    def setListeVilles(self, liste_villes):
        if liste_villes is not None:
            self.liste_villes = liste_villes
            self.distance_totale = self.calculer_score()

    def distance(self, ville1, ville2):
        # Calcul de la distance euclidienne entre deux villes
        return math.sqrt((ville1.x - ville2.x) ** 2 + (ville1.y - ville2.y) ** 2)

    def calculer_score(self):
        distance_totale = 0
        for i in range(1, len(self.liste_villes)):
            ville_actuelle = self.liste_villes[i - 1]
            ville_suivante = self.liste_villes[i]  # % len(self.liste_villes)
            distance_totale += self.distance(ville_actuelle, ville_suivante)
            # distance_totale = round(score, 2)
            if distance_totale == 0:
                print(f"erreur, score : 0")
        distance_totale += self.distance(self.liste_villes[-1], self.liste_villes[0])
        return distance_totale

    def randomVilles(self):
        copieville = self.villes[:]
        ville_depart = self.villes[0]
        sous_liste = self.ville[1:]
        random.shuffle(sous_liste)
        nouvelle_liste = [ville_depart] + sous_liste + [ville_depart]
        return nouvelle_liste

    def __str__(self):
        chemin_str = f"Score du chemin : {self.distance_totale}\n"
        for ville in self.liste_villes:
            chemin_str += str(ville) + "\n"
        return chemin_str

    def __len__(self):
        return len(self.liste_villes)
