persons = [
    {
        "prenom": "Matthieu",
        "nom": "Perez",
        "age": 41,
        "ville": "Villeneuve-lès-Avignon",
    },
    {
        "prenom": "Salvatore",
        "nom": "Moscatiello",
        "age": 65,
        "ville": "Villeneuve-lès-Avignon",
    },
    {
        "prenom": "Jacques",
        "nom": "Dumitran",
        "age": 68,
        "ville": "Les Angles",
    },
    {
        "prenom": "Eric",
        "nom": "Nowak",
        "age": 59,
    },
    {
        "prenom": "Robert",
        "nom": "Farré",
        "age": 0,
        "ville": "Les Angles",
    },
    {
        "prenom": "José",
        "nom": "Perez",
        "age": "inconnu",
        "ville": "Les Angles",
    },
    {
        "prenom": "Emmanuel",
        "nom": "Aurelio",
        "ville": "Pujaut",
    },
]

# Vérification de la ville
for el in persons:
    if "ville" not in el:
        el["ville"] = "à renseigner"

# Vérification que l'âge est correctement renseigné
# Voir toutes les sortes d'erreurs en testant avec des valeurs impossibles
for el in persons:
    try:
        age_ratio = 1 / el["age"]
    except ZeroDivisionError:
        print(f"{el['prenom']} : âge nul.")
    except TypeError:
        print(f"{el['prenom']} : âge défini par une valeur non numérique.")
    except KeyError:
        print(f"{el['prenom']} : âge non renseigné.")
    else:
        print(f"{el['prenom']} a {el['age']} ans.")
    finally:
        print("-----------------------------------------------------")
