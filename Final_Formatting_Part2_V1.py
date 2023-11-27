import os

#Programme à utiliser en 4ème
def supprimer_doublons(nom_fichier):
    lignes_modifiees = []

    with open(nom_fichier, 'r') as fichier:
        lignes = fichier.readlines()
        lignes_modifiees.append(lignes[0])  # Ajoute la première ligne

        for i in range(1, len(lignes)):
            if lignes[i] != lignes[0]:  # Vérifie si la ligne actuelle est différente de la première ligne
                lignes_modifiees.append(lignes[i])

    with open(nom_fichier, 'w') as fichier:
        fichier.writelines(lignes_modifiees)

def ajouter_sauts(nom_fichier):
    lignes_modifiees = []

    with open(nom_fichier, 'r') as fichier:
        lignes = fichier.readlines()

        for i in range(len(lignes) - 1):
            lignes_modifiees.append(lignes[i])
            if "ns" in lignes[i + 1] and "Simulation" not in lignes[i + 1]:
                # Si "ns" est présent dans la ligne i+1 et "Simulation" n'est pas présent
                # Vérifie si la ligne suivante contient "ns"
                lignes_modifiees.append('\n')

        lignes_modifiees.append(lignes[-1])  # Ajoute la dernière ligne du fichier

    with open(nom_fichier, 'w') as fichier:
        fichier.writelines(lignes_modifiees)

# Supprime les sauts de ligne consécutifs
def supprimer_sauts_consecutifs(nom_fichier):
    lignes_modifiees = []

    with open(nom_fichier, 'r') as fichier:
        lignes = fichier.readlines()

        # Ajoute la première ligne
        lignes_modifiees.append(lignes[0])

        # Parcours pour supprimer les sauts de ligne consécutifs
        for i in range(1, len(lignes)):
            if lignes[i] != '\n' or lignes[i - 1] != '\n':
                lignes_modifiees.append(lignes[i])

    # Écriture dans le fichier avec les sauts de ligne consécutifs supprimés
    with open(nom_fichier, 'w') as fichier:
        fichier.writelines(lignes_modifiees)

# Chemin vers le répertoire contenant vos fichiers
repertoire = r"E:\PX505\Attaque_Trier\testtraitement\sortie\Testas"  

# Parcourir tous les fichiers dans le répertoire
for fichier in os.listdir(repertoire):
    chemin_fichier = os.path.join(repertoire, fichier)
    if os.path.isfile(chemin_fichier):
        supprimer_doublons(chemin_fichier)
        ajouter_sauts(chemin_fichier)
        supprimer_sauts_consecutifs(chemin_fichier)
