from Chemin import Chemin
import random


class Population:

    # constructeur
    def __init__(self, nb_individus, liste_villes):
        self.nb_individus = nb_individus
        self.liste_villes = liste_villes
        self.liste_chemins = self.generer_population_initiale()

    # generer population initiale de manière aléatoire
    def generer_population_initiale(self):
        liste_objet_chemin = []
        for _ in range(self.nb_individus):

            chemin = Chemin(self.liste_villes)
            chemin.randomVilles()
            liste_objet_chemin.append(chemin)

        return liste_objet_chemin

    def addChemins(self, liste_Chemin_new):
        for chemin in liste_Chemin_new:
            if isinstance(chemin, Chemin):
                self.liste_chemins.append(chemin)
            else:
                print(f"Erreur : {chemin} n'est pas un objet Chemin")

    def find_meilleur_distance(self):
        # trouver meilleur distance de la population
        self.liste_chemins.sort(key=lambda chemin: chemin.calculer_score())
        meilleur_chemin = self.liste_chemins[0]
        final_distance = meilleur_chemin.calculer_score()
        return final_distance, meilleur_chemin

    def __str__(self):
        chemin_str = [str(chemin) for chemin in self.liste_chemins]
        return "\n".join(chemin_str) + "\n"

    def trier_par_score(self):
        self.liste_chemins.sort(key=lambda chemin: chemin.calculer_score())

    def __len__(self):
        return len(self.liste_chemins)
