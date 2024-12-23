from pathlib import Path

# Manipulation de données d'un fichier
p = Path.home() / "src" / "vla_django" / "templates" / "vla_django" / "index.html"
print(p)
print(dir(p))

print(p.parts) # C:, Users, matth, Documents...
print(p.suffix) # .html
print(p.stem) # index
print(p.parent) # Dossier parent
print(p.is_dir()) # False
print(p.is_file()) # True

# Créer un dossier unique
p = Path.home()
newdir = p / "DossierTest"
newdir.mkdir(exist_ok=True) # Pas d'erreur si le dossier existe déjà

# Créer une architecture de dossiers
p = Path.home()
newdir = p / "DossierTest" / "1" /"2" / "3"
newdir.mkdir(parents=True)

# Supprimer un dossier
olddir = Path.home() / 'DossierTest' / "1" / "2" / "3"

# Si le dossier est vide
olddir.rmdir() # Supprimer le dossier "3"

# Si le dossier n'est pas vide
import shutil
shutil.rmtree(olddir)

# Créer/supprimer un fichier
newfile = p / "readme.md"
newfile.touch() # Créer le fichier
newfile.unlink() # Supprimer le fichier

# Ecrire dans un fichier
p = Path.home() / "Pathlib" / "readme.txt"
p.touch() # Le fichier est vide puisqu'il vient d'être créé
p.write_text("Bonjour") # Ajoute du texte au fichier
p.read_text() # Affiche le contenudu fichier

## Scanner un dossier
p = Path.home().iterdir()

# Afficher les fichiers et dossiers les uns après les autres (même cachés)
for f in p:
    print(f.name)

# Afficher uniquement les dossiers dans le dossier sélectionné
[f for f in p if f.is_dir()]

# Afficher uniquement les fichiers dans le dossier sélectionné
[f for f in p if f.is_file()]

# Afficher tous les fichiers images du 1er niveau
pics = p.glob("*.png")

for f in pics:
    print(f.name)
    
# Afficher tous les fichiers images à tous les niveaux
pics = p.rglob("*.png")

for f in pics:
    print(f.name)


# Formation à terminer sur Udemy