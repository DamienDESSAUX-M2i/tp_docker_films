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

Deux images `tp_docker_films/read` et `tp_docker_films/write`, un network `app_network` et un volume `movies` seront créées.

## Commandes pour exécuter les conteneurs.

Une fois les conteneurs `read` et `write` construits, vous pouvez éxécutez les conteneurs avec la commande :

```bash
docker exec -it read python main.py
docker exec -it write python main.py
```

## Utilisation des applications

### Conteneur `read`

Fonctionnalités :
- Chercher un film par titre
- Chercher un film par age limite
- Chercher un film par genre
- Chercher un film par année de production
- Quitter

### Conteneur `write`

Fonctionnalités :
- Ajouter un film
- Modifier un film
- Supprimer un film
- Quitter