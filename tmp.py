from prettytable import PrettyTable
import os

# Créer un tableau avec les en-têtes des colonnes
table = PrettyTable()
table.field_names = ["Nom du fichier", "Taille (octets)", "Date de modification"]

# Récupérer les informations des fichiers dans un répertoire spécifique
directory = "/home/amon/dev/cyberEngien/"
for filename in os.listdir(directory):
    path = os.path.join(directory, filename)
    if os.path.isfile(path):
        size = os.path.getsize(path)
        mod_time = os.path.getmtime(path)
        table.add_row([filename, size, mod_time])

# Afficher le tableau
print(table)