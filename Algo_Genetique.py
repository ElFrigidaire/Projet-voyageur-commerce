from population import Population
from Chemin import Chemin
import random


class AlgorithmeGenetique:
    # constructeur
    def __init__(self, population, nb_enfants):
        self.population = population
        self.liste_villes = population.liste_villes
        self.nb_individus = population.nb_individus
        self.nb_enfants = nb_enfants

    # evolution sur generation
    def evolution(self, nb_generation):
        compteur = 0
        while compteur < nb_generation:
            parents = self.selection()  # Sélectionne les meilleurs chemins (parents)
            self.population.liste_chemins = parents
            enfants = self.recombinaison(parents)
            enfants = self.mutation(enfants)
            self.population.addChemins(enfants)
            compteur += 1

    # selection
    def selection(self):
        nb_chemins = self.nb_individus - self.nb_enfants
        chemins_tries = sorted(
            self.population.liste_chemins, key=lambda chemin: chemin.calculer_score()
        )

        meileurs_chemins = chemins_tries[:nb_chemins]
        return meileurs_chemins

    # recombinaison
    def recombinaison(self, parents):

        enfants = []

        while len(enfants) < self.nb_enfants:
            # Choisir 2 parents aléatoirement
            parent1, parent2 = random.sample(parents, 2)

            # Déterminer un point de coupure dans le chemin du premier parent
            cut1 = random.randint(1, len(parent1.liste_villes) - 2)
            cut2 = random.randint(cut1, len(parent1.liste_villes))

            enfant = [-1] * len(parent1)
            enfant[cut1:cut2] = parent1.liste_villes[cut1:cut2]

            equivalence = {
                parent1.liste_villes[i]: parent2.liste_villes[i]
                for i in range(cut1, cut2)
            }

            for i in range(len(enfant)):

                if i >= cut1 and i < cut2:
                    continue

                ville = parent2.liste_villes[i]
                while ville in enfant:
                    ville = equivalence[ville]

                enfant[i] = ville

            # Créer un objet Chemin avec ce nouveau chemin et l'ajouter à la liste des enfants
            enfants.append(Chemin(liste_villes=enfant))

        return enfants

    def mutation(self, enfants, taux_mutation=0.05):
        for chemin in enfants:
            print(len(chemin))
            if random.random() <= taux_mutation:
                pos1, pos2 = random.randint(
                    0, len(chemin.liste_villes) - 1
                ), random.randint(0, len(chemin.liste_villes) - 1)
                chemin.liste_villes[pos1], chemin.liste_villes[pos2] = (
                    chemin.liste_villes[pos2],
                    chemin.liste_villes[pos1],
                )
        return enfants
