# Les dictionnaires sont des listes modifiables (muable) qui fonctionne avec un système de clé-valeur
# On reconnait un dictionnaire par les accolades. Les éléments sont séparés par des virgules.

dico = {
    {
        "prenom": "Matthieu",
        "nom": "Perez",
        "ville": "Villeneuve-lès-Avignon",
    },
    {
        "prenom": "Salvatore",
        "nom": "Moscatiello",
        "ville": "Villeneuve-lès-Avignon",
    },
    {
        "prenom": "Jacques",
        "nom": "Dumitran",
        "ville": "Les Angles",
    },
}

small_dico = {
    "prenom": "Matthieu",
    "nom": "Perez",
    "ville": "Villeneuve-lès-Avignon",
}

# Si test n'existe pas : erreur
prenom = dico[0]["prenom"]

# Vérifier qu'une clé existe
test = dico.get("prénom")  # Retourne None si la clé n'existe pas
test = dico.get("prénom", "La clé n'existe pas")

# Modifier une valeur dans un dictionnaire
dico[0]["prenom"] = "Henri"

# Ajouter une clé
small_dico["naissance"] = "10/01/1983"

# Supprimer une clé
del small_dico["naissance"]

# Supprimer une clé après avoir vérifié qu'elle existait
if "naissance" in small_dico:
    del small_dico["naissance"]

# Boucler sur un dictionnaire
small_dico.keys()  # ==> ["prenom", "nom", "ville", "naissance"]
small_dico.values()  # ==> ["Matthieu", "Perez", "Villeneuve-lès-Avignon", "10/01/1983"]

for cle in small_dico:
    print(cle)  # Retourne par défaut la clé
    print(small_dico[cle])  # Récupérer aussi les valeurs pour chaque clé

for cle, valeur in small_dico.items():
    print(cle, valeur)

