# Déloppement de l'API rest

## Etapes préliminaires

### Créer l'environnement virtuel

Pour ce faire lancer la commande suivante

```bash
python -m venv venv
```

Puis mettre à jour pip et installer les dépendences

```bash
python.exe -m pip install --upgrade pip
pip install -r restApi/requirements.txt
```

### Configuration de la BD

Déplacez-vous dans le dossier du projet et lancez les migrations

```bash
cd restApi
python manage.py makemigrations
python manage.py migrate
```

### Lancement du serveur

```bash
python manage.py runserver
```

puis ouvrir le navigateur à l'adresse [http://127.0.0.1:8000](link)

## Développement

Le module ```catégory``` ayant été définie votre travail consiste créer celui de ```product``` en utilisant les classes génirics:

- ListAPIView
- RetrieveAPIView
- CreateAPIView
- UpdateAPIView
- DestroyAPIView

et definir leurs routes urls

__NB :__ La route qui définira les détails du produit devra utiliser le name="product-detail"
__PS :__ la route de categories que j'ai créé est [http://localhost:8000/api/category/](link)

Version de python __3.13.1__
