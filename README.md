# TP Docker Films

TP de la formation Concepteur Développeur en Science des Données de M2I.

## Récupération du projet

Le projet est hébergé sur GitHub. Pour récupérer le projet, placez-vous dans le répertoire de votre choix puis éxécutez la commande :

```bash
git clone https://github.com/DamienDESSAUX-M2i/tp_docker_films.git
```

## Lancement du projet sous Docker

Pour lancer le projet sous docker, placez-vous dans le répertoire `tp_docker_films/` puis éxécutez la commande :

```bash
docker compose up -d
```

Deux images `tp_docker_films/read` et `tp_docker_films/write`, un network `app_network` et trois volumes `movies`, `utils` et `exceptions` seront créées.

## Commandes pour exécuter les conteneurs.

Une fois les conteneurs `read` et `write` construits, vous pouvez éxécutez les conteneurs avec les commandes :

```bash
docker exec -it read python main.py
docker exec -it write python main.py
```

## Utilisation des applications

### Application `read`

Fonctionnalités :
- Chercher un film par titre. Renvoie la liste des films ayant contenant les mots saisis.
- Chercher un film par age limite. Renvoie la liste des films ayant un limite d'âge supérieure ou égale à l'âge saisi. La saisi doit être un nombre entier positif.
- Chercher un film par genre. Renvoie la liste des films ayant le genre saisi. La saisie doit être l'un des mots suivant : Drame, Crime, Action, Avanture, Animation, Comédie, Biograhie, Famille.
- Chercher un film par année de production. Renvoie la liste des films dont l'année de production est entre deux années saisie. Les saisies sont deux nombres entiers positifs sont demandés. Le second nombre doit être inférieur ou égal au premier.
- Quitter. Mettre fin à l'application.

### Application `write`

Fonctionnalités :
- Ajouter un film. L'utilisateur devra saisir le titre, l'année de production qui est un entier positif, le genre qui doit être l'un des mots Drame, Crime, Action, Avanture, Animation, Comédie, Biograhie ou Famille et l'age limite qui est un entier positif.
- Modifier un film. L'utilisateur devra saisir, l'id du film, le titre, l'année de production qui est un entier positif, le genre qui doit être l'un des mots Drame, Crime, Action, Avanture, Animation, Comédie, Biograhie ou Famille et l'age limite qui est un entier positif.
- Supprimer un film. L'utilisateur devra saisir l'id du film.
- Quitter. Mettre fin à l'application.