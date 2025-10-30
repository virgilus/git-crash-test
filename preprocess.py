import csv

# Nom du fichier de sortie
filename = "dataset.csv"

# Données d'exemple
data = [
    ["id", "name", "age", "city", "salary"],
    [1, "Amine", 28, "Marseille", 3200],
    [2, "Sara", 25, "Paris", 2900],
    [3, "Youssef", 32, "Lyon", 4100],
    [4, "Lina", 29, "Toulouse", 3500],
    [5, "Hassan", 35, "Bordeaux", 4700],
]

# Écriture du CSV
with open(filename, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f"✅ Fichier '{filename}' généré avec succès !")
