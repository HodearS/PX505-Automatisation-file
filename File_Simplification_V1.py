import os
import re
#Simplification des fichiers, à utiliser en premier
def extract_specific_info(input_file, output_dir):
    extracted_info = []
    target_info = []

    # Extraction du temps du nom du fichier source -> utile pour l'automatisation
    filename = os.path.basename(input_file) #permet d'extraire un nom d'un path
    match = re.search(r'(\d+ns)', filename)  # on recherche ici "un entier" et le mot "ns" dans le nom
    if match:
        base_name = match.group(1) #récupère la partie qui match avec la recher
        output_filename = f"{base_name}_simplified.txt" #l'écrit dans le nom du fichier génerer

    with open(input_file, 'r') as file:
        lines = file.readlines()

        for index, line in enumerate(lines):
            print(f"Ligne suivante: {lines[index + 1].strip() if index + 1 < len(lines) else None}") #débug

            if 'at' in line: #on recupere le timing de fin du programme après le Attack success potentiellement pas utile
                print("at OK")
                parts = line.split('at')
                if len(parts) > 1:
                    target = parts[1].split()[0]
                    print(target)
                    if target == 'ed' or target == 'ion': #retire les bugs de mise en page optimiser le code pour y retirer ?
                        target = ''
                    else: #permet d'éviter d'avoir un espace en haut du fichier
                        if index == 0:
                            target_info.append(target)
                            print(f"Target ajoutée: {target}")#débug
                        else:
                            target_info.append('\n' + target)
                            print(f"Target ajoutée: {target}")#débug

            if 'targeting' in line: #on recupere le nom du registre après le core_i utile pour le tri
                print("targeting OK")
                elements = line.split('targeting ')[-1].strip()
                core_i_index = elements.find('/core_i/')
                if core_i_index != -1:
                    target = elements[core_i_index + len('/core_i/'):]
                    target_info.append(target)
                    print(f"Target ajoutée: {target}")#débug

            elif 'Exit valid' in line or 'expected' in line or 'Simulation time' in line: #on traite ici tous les autres ças qui nous interessent (on ne découpe pas on prend la ligne)
                print("'Exit valid'/'expected'/'Simulation time' OK")
                target_info.append(line.strip())
                print(f"Line ajoutée: {line.strip()}")#débug

        if target_info:
            extracted_info.append('\n'.join(target_info))

    #output_filename = "extracted_info2.txt"
    output_path = os.path.join(output_dir, output_filename)

    with open(output_path, 'w') as out_file:
        for index, info in enumerate(extracted_info):
            if index != 0:
                out_file.write('\n')
            out_file.write(info + '\n')

    print(f"Traitement OK fichier sauvegarder a '{output_path}'.")

source_directory = "E:/PX505/Attaque" #repertoire source
output_directory = "E:/PX505/Attaque_Trier" #repertoire de destination

for filename in os.listdir(source_directory): #parcours tous les éléments d'un répertoire
    file_path = os.path.join(source_directory, filename) #permet de crée un chemin complet vers chaque fichier
    if os.path.isfile(file_path): #verifie qu'il s'agit d'un fichier (élément actuelle) et non d'un repertoire
        extract_specific_info(file_path, output_directory) #on passe le fichier à la fonction plust haut
