import os
import shutil

# 1. Chemin vers ton dossier principal (celui qui contient Renault, Peugeot, etc.)
base_path = 'C:/Users/plled/Documents/SN2/PE/VMMRdb'

# 2. On boucle sur chaque dossier de marque
for marque in os.listdir(base_path):
    marque_path = os.path.join(base_path, marque)
    
    # On vérifie que c'est bien un dossier
    if os.path.isdir(marque_path):
        print(f"Traitement de la marque : {marque}")
        
        # 3. On parcourt tous les sous-dossiers de la marque
        for root, dirs, files in os.walk(marque_path):
            # On ignore le dossier de la marque lui-même, on ne veut que ce qui est "dedans"
            if root == marque_path:
                continue
                
            for file in files:
                # On ne prend que les images
                if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                    source = os.path.join(root, file)
                    
                    # 4. On crée un nouveau nom unique : nomdusousdossier_nomdufichier.jpg
                    nouveau_nom = f"{os.path.basename(root)}_{file}"
                    destination = os.path.join(marque_path, nouveau_nom)
                    
                    # 5. On déplace le fichier
                    shutil.move(source, destination)

        # 6. Une fois fini, on supprime les sous-dossiers vides pour faire propre
        for item in os.listdir(marque_path):
            item_path = os.path.join(marque_path, item)
            if os.path.isdir(item_path):
                shutil.rmtree(item_path)

