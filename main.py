from Algo_Genetique import AlgorithmeGenetique
from ville import Ville
from population import Population
from Chemin import Chemin
import math
import random

# Initialisation
nb_villes = 5  # Nombre de ville,
nom_ville = "abcdefghijklmnopqrstuvwxyz"
nb_individus = 10

nb_enfants = 5  # doit être plus petit que le nombre d'individus

nb_generations = 20

# Taille du plan
h = 100
l = 100

liste_villes = []
for i in range(nb_villes):
    ville = Ville(nom_ville[i], random.randint(0, l), random.randint(0, h))
    liste_villes.append(ville)

v_depart = liste_villes[0]  # ville de départ

# fonction_distance = lambda x1, x2, y1, y2: math.sqrt((y2 - y1) ** 2 + (kix2 - x1) ** 2)


population = Population(
    nb_individus, liste_villes
)  # liste de solutions. Taille : définie par user.

algo_genetique = AlgorithmeGenetique(population, nb_enfants)
algo_genetique.evolution(nb_generations)
population.liste_chemins.sort(key=lambda chemin: chemin.calculer_score())
meilleur_chemin = population.liste_chemins[0]
print(meilleur_chemin)


# nombre_iteration = 0  # nombre de fois qu’est effectuée la boucle

# k = 0  # nombre d’élites dans la pop. Nombre pair

# p = 0  # probabilité de mutation (faible)
