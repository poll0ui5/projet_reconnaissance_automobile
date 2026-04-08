from pathlib import Path

# On définit le chemin du dossier à scanner
chemin_dossier = Path("og_VMMRdb_model/Mercedes-Benz")

# On récupère uniquement les dossiers (is_dir) 
# et on extrait leur nom (.name)
liste_sous_dossiers = [f.name for f in chemin_dossier.iterdir() if f.is_dir()]

# On affiche le résultat
print(f"Sous-dossiers trouvés ({len(liste_sous_dossiers)}) :")
for nom in liste_sous_dossiers:
    print(f"- {nom}")