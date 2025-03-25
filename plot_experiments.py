import matplotlib.pyplot as plt


def plot_all_experiments(file_path="distances_experiments.txt"):
    try:
        with open(file_path, "r") as f:
            lines = f.readlines()

        experiments = []
        distances = []

        # Parse the file
        for line in lines:
            if line.startswith("Experiment with"):
                experiments.append(line.strip())  # Save experiment details
            elif line.strip():  # Non-empty line with distances
                distances.append(list(map(float, line.strip().split(", "))))

        # Plot all experiments
        plt.figure(figsize=(10, 6))
        for i, distance_list in enumerate(distances):
            plt.plot(
                range(1, len(distance_list) + 1),
                distance_list,
                label=experiments[i],  # Use experiment details as legend
            )

        plt.title("Évolution des distances pour tous les expériences")
        plt.xlabel("Nombre de générations")
        plt.ylabel("Distance parcourue")
        plt.legend(fontsize="small", loc="upper right")
        plt.tight_layout()
        plt.show()

    except FileNotFoundError:
        print(f"Le fichier {file_path} est introuvable.")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")


plot_all_experiments()
