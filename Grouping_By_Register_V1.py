import os
#Regroupement par registre, à utiliser en second
# répertoire contenant vos fichiers d'entrée
repertoire_entree = r"E:\PX505\Attaque_Trier\testtraitement"

# Chemin vers le répertoire de sortie
repertoire_sortie = r"E:\PX505\Attaque_Trier\testtraitement\sortie"

# Dictionnaire pour stocker les données regroupées par registre
donnees_par_registre = {}

# Parcourir tous les fichiers dans le répertoire d'entrée
for fichier in os.listdir(repertoire_entree):
    chemin_fichier = os.path.join(repertoire_entree, fichier)
    if os.path.isfile(chemin_fichier):
        with open(chemin_fichier, 'r') as file:
            lignes = file.readlines()

        # Variables pour stocker temporairement les données
        nom_registre = None
        donnees = []

        # Parcourir chaque ligne du fichier
        for i, ligne in enumerate(lignes):
            # Vérifier si la ligne contient "ns" à la fin
            if ligne.strip().endswith("ns") and i + 1 < len(lignes): #verifie que la ligne se termine par "ns" et qu'il y a une ligne après pour récuperer le nom du registre
                # Prendre la ligne suivante comme nom du registre
                nom_registre = lignes[i + 1].strip()
                donnees = lignes[i:i + 2]  #

                # Parcourir les lignes suivantes pour collecter les données du registre
                for j in range(i + 2, len(lignes)):
                    if lignes[j].strip().endswith("ns"):
                        break  # Arrêter si on trouve une nouvelle ligne avec "ns"
                    else:
                        donnees.append(lignes[j])  # Ajouter les données

                # Enregistrer les données pour le registre
                if nom_registre not in donnees_par_registre:
                    donnees_par_registre[nom_registre] = []
                donnees_par_registre[nom_registre].extend(donnees)

# Écrire les données regroupées dans des fichiers par registre dans le répertoire de sortie
for nom_registre, donnees in donnees_par_registre.items():
    nom_fichier_sortie = nom_registre.replace("/", "_") + "_regroupee.txt"
    chemin_fichier_sortie = os.path.join(repertoire_sortie, nom_fichier_sortie)

    with open(chemin_fichier_sortie, 'w') as file:
        file.writelines(donnees)
