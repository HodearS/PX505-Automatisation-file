import os
#Programme intermédiaire pour la mise en forme à utiliser en troisième
# répertoire contenant les fichiers d'entrée
repertoire_entree = r"E:\PX505\Attaque_Trier\testtraitement\sortie"

# Chemin vers le répertoire de sortie
repertoire_sortie = r"E:\PX505\Attaque_Trier\testtraitement\sortie\Testas"

# Parcourir tous les fichiers dans le répertoire d'entrée
for fichier in os.listdir(repertoire_entree):
    chemin_fichier = os.path.join(repertoire_entree, fichier)
    if os.path.isfile(chemin_fichier):
        with open(chemin_fichier, 'r') as file:
            lignes = file.readlines()

        # Variables pour stocker temporairement les données modifiées
        donnees_modifiees = []

        # Parcourir chaque ligne du fichier
        for i, ligne in enumerate(lignes):
            # Vérifier si la ligne contient "ns" à la fin
            if ligne.strip().endswith("ns"):
                # Intervertir le temps et le nom du registre
                donnees_modifiees.append(lignes[i + 1])  # Ajouter le temps
                donnees_modifiees.append(lignes[i])  # Ajouter le nom du registre
            else:
                donnees_modifiees.append(ligne)  # Ajouter les autres lignes inchangées

        # Enregistrer les données modifiées dans un fichier de sortie
        donnees_modifiees = ''.join(donnees_modifiees)
        chemin_fichier_sortie = os.path.join(repertoire_sortie, fichier)

        with open(chemin_fichier_sortie, 'w') as file:
            file.write(donnees_modifiees)
