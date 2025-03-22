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
            ordre_aleatoire = self.randomVilles(self.liste_villes.copy())

            chemin.setListeVilles(ordre_aleatoire)
            liste_objet_chemin.append(chemin)

        return liste_objet_chemin

    def randomVilles(self, liste_villes):
        random.shuffle(liste_villes)
        return liste_villes

    def addChemins(self, liste_Chemin_new):
        for chemin in liste_Chemin_new:
            if isinstance(chemin, Chemin):
                self.liste_chemins.append(chemin)
            else:
                print(f"Erreur : {chemin} n'est pas un objet Chemin")

    def __str__(self):
        chemin_str = [str(chemin) for chemin in self.liste_chemins]
        return "\n".join(chemin_str) + "\n"

    def trier_par_score(self):
        self.liste_chemins.sort(key=lambda chemin: chemin.calculer_score())

    def __len__(self):
        return len(self.liste_chemins)
