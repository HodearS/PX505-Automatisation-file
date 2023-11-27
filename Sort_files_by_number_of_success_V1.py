import os
#Dernier programme à utiliser permet d'avoir un txt avec le nombre d'attaque succeed par ordre croissant
def compter_occurrences(fichier):
    # Compte le nombre d'occurrences de "ns" dans les lignes ne comportant pas "Simulation"
    occurrences = 0
    with open(fichier, 'r') as file:
        for ligne in file:
            if "Simulation" not in ligne:
                occurrences += ligne.count("ns")
    return occurrences

def parcourir_registre(chemin_dossier, dossier_sortie):
    # Création du dossier de sortie s'il n'existe pas
    if not os.path.exists(dossier_sortie):
        os.makedirs(dossier_sortie)

    # Chemin du fichier où enregistrer les résultats
    fichier_resultats = os.path.join(dossier_sortie, "resultats_occurrences.txt")

    # Dictionnaire pour stocker les résultats
    occurrences_par_fichier = {}

    for nom_fichier in os.listdir(chemin_dossier):
        chemin_fichier = os.path.join(chemin_dossier, nom_fichier)
        if os.path.isfile(chemin_fichier):
            occurrences = compter_occurrences(chemin_fichier)
            occurrences_par_fichier[nom_fichier] = occurrences

    # Tri des résultats par nombre d'occurrences
    resultats_tries = sorted(occurrences_par_fichier.items(), key=lambda x: x[1])

    # Écriture des résultats dans le fichier de sortie
    with open(fichier_resultats, 'w') as resultats:
        for nom_fichier, occurrences in resultats_tries:
            ligne_resultat = f"Le fichier '{nom_fichier}' contient {occurrences} occurrences de 'ns' sans 'Simulation'.\n"
            resultats.write(ligne_resultat)

# répertoire contenant les fichiers à analyser
dossier_entree = r"E:\PX505\Attaque_Trier\testtraitement\sortie\Testas"

# chemin du répertoire de sortie
dossier_sortie = r"E:\PX505\Attaque_Trier\testtraitement\sortie\Testas\occurence"

# Appelle la fonction pour parcourir le registre et enregistrer les résultats
parcourir_registre(dossier_entree, dossier_sortie)
