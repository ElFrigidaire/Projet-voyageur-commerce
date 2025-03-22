from Algo_Genetique import AlgorithmeGenetique
from ville import Ville
from population import Population
from Chemin import Chemin
import random
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np
import json

with open("./cities.json", "r") as f:
    cities = json.load(f)
    nom_ville = [v["label"] for v in cities["cities"]]


def plot_route(chemin, liste_distances):
    _, axes = plt.subplots(2, figsize=(10, 8))

    x = [city.x for city in chemin.liste_villes]
    y = [city.y for city in chemin.liste_villes]
    axes[0].plot(x, y, "mo-", label="Chemin")
    axes[0].plot([x[0], x[-1]], [y[0], y[-1]], "mo-")
    axes[0].scatter(x[0], y[0], c="red", marker="*", s=150, label="Départ/Arrivée")
    axes[0].set_title(f"Meilleur Chemin : {liste_distances[-1]}")
    axes[0].set_xlabel("Coordonnée X")
    axes[0].set_ylabel("Coordonnée Y")
    axes[0].legend()

    axes[1].plot(np.arange(1, len(liste_distances) + 1), liste_distances, "r-")
    axes[1].set_title("Évolution de la distance du meilleur chemin")
    axes[1].set_xlabel("Nombre de générations")
    axes[1].set_ylabel("Distance parcourue")

    plt.tight_layout()
    plt.show()


def run_genetic_algorithm():
    try:
        # Récupérer les valeurs saisies par l'utilisateur
        # num_cities = int(entry_num_cities.get())
        # Initialisation
        nb_villes = int(entry_num_cities.get())

        # nom_ville = "abcdefghijklmnopqrstuvwxyz"

        nb_individus = int(entry_population_size.get())

        nb_generations = int(entry_num_generations.get())

        nb_enfants = int(entry_child_size.get())

        taux_mutation = float(entry_mutation_rate.get())

        if nb_enfants > nb_individus:
            messagebox.showerror(
                f"Nombre d'enfants doit être plus petit que : {nb_individus}"
            )  # doit être plus petit que le nombre d'individus

        # Taille du plan
        h = 200
        l = 200

        liste_villes = []
        for i in range(nb_villes):
            ville = Ville(nom_ville[i], random.randint(0, l), random.randint(0, h))
            liste_villes.append(ville)

        v_depart = liste_villes[0]  # ville de départ

        population = Population(
            nb_individus, liste_villes
        )  # liste de solutions. Taille : définie par user.

        algo_genetique = AlgorithmeGenetique(population, nb_enfants, taux_mutation)
        algo_genetique.evolution(nb_generations)
        print(algo_genetique.liste_distances)

        # Afficher les distances dans une fenêtre graphique
        # show_distances(chemin.initial_distance, final_distance)
        final_distance, meilleur_chemin = population.find_meilleur_distance()
        print(final_distance)
        plot_route(meilleur_chemin, algo_genetique.liste_distances)

    except ValueError as e:
        messagebox.showerror("Erreur", str(e))


def generate_random_population_size():
    entry_population_size.delete(0, tk.END)
    entry_population_size.insert(0, str(random.randint(10, 100)))


def generate_random_child_size():
    entry_child_size.delete(0, tk.END)
    entry_child_size.insert(0, str(random.randint(1, 10)))


def generate_random_mutation_rate():
    entry_mutation_rate.delete(0, tk.END)
    entry_mutation_rate.insert(0, str(round(random.uniform(0.01, 1), 2)))


def generate_random_num_generations():
    entry_num_generations.delete(0, tk.END)
    entry_num_generations.insert(0, str(random.randint(200, 20000)))


# Créer la fenêtre principale
root = tk.Tk()
root.title("Interface Utilisateur pour TSP")

# Ajouter des étiquettes et des champs de saisie pour les paramètres
tk.Label(root, text="Nombre de Villes :").grid(row=0, column=0)
entry_num_cities = tk.Entry(root)
entry_num_cities.grid(row=0, column=1)

tk.Label(root, text="Taille de la Population :").grid(row=1, column=0)
entry_population_size = tk.Entry(root)
entry_population_size.grid(row=1, column=1)
button_population_size = tk.Button(
    root, text="Aléatoire", command=generate_random_population_size
)
button_population_size.grid(row=1, column=2)

tk.Label(root, text="Nombre de nouveaux enfants par génération :").grid(row=2, column=0)
entry_child_size = tk.Entry(root)
entry_child_size.grid(row=2, column=1)
button_child_size = tk.Button(
    root, text="Aléatoire", command=generate_random_child_size
)
button_child_size.grid(row=2, column=2)

tk.Label(root, text="Fréquence de Mutation :").grid(row=3, column=0)
entry_mutation_rate = tk.Entry(root)
entry_mutation_rate.grid(row=3, column=1)
button_mutation_rate = tk.Button(
    root, text="Aléatoire", command=generate_random_mutation_rate
)
button_mutation_rate.grid(row=3, column=2)

tk.Label(root, text="Nombre de Générations :").grid(row=4, column=0)
entry_num_generations = tk.Entry(root)
entry_num_generations.grid(row=4, column=1)
button_num_generations = tk.Button(
    root, text="Aléatoire", command=generate_random_num_generations
)
button_num_generations.grid(row=4, column=2)

# Ajouter un bouton pour exécuter l'algorithme génétique
button_run = tk.Button(
    root, text="Exécuter Algorithme Génétique", command=run_genetic_algorithm
)
button_run.grid(row=5, column=0, columnspan=2)

# Exécuter la boucle principale de l'interface graphique
root.mainloop()
