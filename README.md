# Projet de Groupe : Big Data avec Hadoop et Spark

# Documentation du Projet de Data

## Membres de l'équipe

- **Gabriel LORGET** : Développement de l'interface web.
- **Hugo TRICOIRE** : Configuration et gestion du cluster Hadoop.
- **Alexis JORRÉ** : Développement de l'API et gestion des flux de données.
- **Guillaume BOULBEN** : Assistance à la gestion des flux de données et intégration API.

## Architecture du Système

### 1. **Cluster Hadoop avec HDFS**
Le **cluster Hadoop** est utilisé pour le stockage des données à grande échelle via **HDFS** (Hadoop Distributed File System). Ce système distribué permet de gérer des volumes importants de données avec une haute tolérance aux pannes et une distribution efficace des ressources.

- **HDFS** est configuré pour stocker les fichiers dans des blocs répartis sur plusieurs nœuds du cluster.
- Le **NameNode** gère la structure des fichiers et la répartition des blocs.
- Les **DataNodes** sont responsables de la gestion des blocs de données.

### 2. **Interface Web avec Quarto**
L'interface web a été développée avec **Quarto**, un outil open-source utilisé pour générer des interfaces interactives et des dashboards en combinant du contenu Markdown, Python et JavaScript.

- **Quarto** permet la génération de pages web statiques avec des visualisations interactives et des éléments dynamiques.
- L'interface se connecte à l'API PySpark pour récupérer et afficher les données en provenance du cluster Hadoop.

### 3. **API avec PySpark**
L'API a été développée avec la bibliothèque **PySpark**, qui permet d'interagir avec Hadoop et HDFS à l'aide de **Spark** pour la gestion et le traitement des données en temps réel.

- **PySpark** gère les transformations et les actions sur les RDD (Resilient Distributed Datasets), permettant de manipuler et traiter les données de manière distribuée.
- L'API expose des endpoints pour interagir avec les données du cluster, gérer les flux et assurer la communication avec l'interface web.
- Elle prend en charge des opérations telles que la lecture et l’écriture de données dans HDFS, l'exécution de transformations Spark, et l'agrégation des résultats.

### 4. **Orchestration des Flux de Données**
L'orchestration des flux de données est assurée via l'API. Cette orchestration permet de gérer le passage des données depuis le cluster Hadoop vers l'interface web, avec les étapes suivantes :

- **Entrée des données** : Les données sont stockées dans HDFS.
- **Traitement via PySpark** : L'API PySpark extrait et transforme les données selon les requêtes effectuées par l'interface web.
- **Affichage via Quarto** : Les résultats des transformations sont renvoyés à l'interface web pour être visualisés par l'utilisateur.

## Répartition des Tâches

- **Hugo** a configuré le cluster Hadoop et HDFS, en veillant à optimiser le stockage et la répartition des données.
- **Gabriel** a développé l'interface web en Quarto, en créant des pages interactives pour la visualisation des données.
- **Alexis** a développé l'API avec PySpark, en mettant en place les différentes routes et en assurant la communication entre Hadoop et l'interface web.
- **Guillaume** a travaillé sur la gestion des flux de données et l'intégration des différents composants pour assurer un flux de travail fluide.

## Méthodologie

1. **Mise en place du Cluster Hadoop**  
   - **Hugo** a démarré la configuration du cluster Hadoop en définissant les nœuds et en optimisant le stockage HDFS.
   - Le NameNode et les DataNodes ont été configurés pour assurer une haute disponibilité et une répartition des données optimisée.

2. **Développement de l'API PySpark**  
   - **Alexis** et **Guillaume** ont travaillé sur l'API, en intégrant **PySpark** pour la gestion des flux de données.
   - Ils ont mis en place des tests pour vérifier la bonne communication entre Hadoop et l'API.

3. **Intégration de l'Interface Web**  
   - **Gabriel** a intégré l'interface Quarto une fois que les tests API/Cluster étaient validés.
   - L'interface a été connectée à l'API pour permettre l'affichage des résultats traités en temps réel.

## Instructions de Lancement du Projet

Des commentaires détaillés sont présents dans le code source pour faciliter la compréhension des étapes et de la logique utilisée. Voici les instructions pour lancer le projet :

1. **Installation des prérequis**  
   Avant de démarrer, assurez-vous d'avoir **Docker** et **Docker Compose** installés sur votre machine.

2. **Lancement du projet avec Docker Compose**  
   Exécutez la commande suivante depuis le répertoire racine du projet pour lancer tous les services (Hadoop, PySpark, Interface web) :
   ```bash
   docker-compose up --build
3. Allez sur internet et taper sur un onglet : 
   ```bash
   localhost:3000

## Contexte

Dans le cadre de vos études sur le ***Big Data***, vous allez travailler sur un projet qui utilise ***Hadoop*** pour le stockage de données massives et ***Spark*** pour le traitement de ces données. L'objectif de ce projet est de comprendre et de maîtriser l'utilisation de ces technologies tout en créant une interface graphique pour visualiser les résultats.

## Objectif

Le but du projet est de stocker et traiter un grand volume de données en utilisant ***Hadoop*** et ***Spark***, puis de créer une interface graphique permettant d'explorer et de visualiser les données traitées. Vous aurez le choix des frameworks de programmation pour la création de l'interface graphique. De plus, le projet devra être dockerisé pour faciliter le déploiement et l'exécution.

## Description du Projet

1. **Stockage des données avec Hadoop** :
   
   - Installer et configurer un cluster ***Hadoop***.
   
   - Importer un jeu de données volumineux dans le ***HDFS*** (***Hadoop Distributed File System***). Vous pouvez utiliser un jeu de données de votre choix (par exemple, des logs de serveur web, des données de capteurs ***IoT***, des datasets de ***Kaggle***, etc.).
   
   - Les données doivent être structurées de manière appropriée pour le traitement ultérieur avec Spark.

2. **Traitement des données avec Spark** :
   
   - Installer et configurer ***Apache Spark*** sur le cluster ***Hadoop***.
   
   - Écrire des scripts ***Spark*** pour nettoyer, transformer et analyser les données stockées dans ***Hadoop***. 
   
   - Les scripts doivent être capables de répondre à plusieurs questions analytiques pertinentes en fonction des données choisies. Par exemple :
     
     - Analyse des tendances dans les données sur une période donnée.
     
     - Calcul des statistiques descriptives.

3. **Création de l'interface graphique** :
   
   - Développer une interface graphique pour visualiser les résultats des analyses.
   
   - Vous pouvez utiliser n'importe quel framework de votre choix pour l'interface graphique (par exemple, ***Flask/Django*** pour Python, ***Node.js/Express*** pour ***JavaScript***, Java avec ***Spring Boot***, etc.).
   
   - L'interface doit permettre aux utilisateurs de :
     
     - Visualiser des graphiques interactifs et des tableaux de bord.
     
     - Filtrer et explorer les données analysées.
     
     - Télécharger des rapports ou des visualisations au format ***PDF*** ou ***CSV***.

4. **Dockerisation du projet** :
   
   - Créer des ***Dockerfiles*** pour tous les composants du projet (***Hadoop***, ***Spark***, et l'interface graphique).
   
   - Configurer des conteneurs ***Docker*** pour chaque composant afin de faciliter le déploiement et l'exécution.
   
   - Utiliser ***Docker Compose*** pour orchestrer et gérer les différents conteneurs.

## Contraintes

1. **Travail en équipe** :
   
   - Le projet doit être réalisé par des groupes de ***3 à 5*** étudiants.
   
   - Une répartition claire des tâches doit être définie et respectée.

2. **Technologies utilisées** :
   
   - Utilisation obligatoire de ***Hadoop*** pour le stockage des données.
   
   - Utilisation obligatoire de ***Spark*** pour le traitement des données.
   
   - Choix libre du framework de programmation pour l'interface graphique.
   
   - Utilisation obligatoire de ***Docker*** pour la conteneurisation du projet.

3. **Documentation** :
   
   - Le code doit être bien commenté et suivre les meilleures pratiques de développement.
   
   - Une documentation détaillée doit être fournie, expliquant l'architecture du système, les étapes de configuration, et les instructions pour exécuter le projet.


## Livrables

1. **Code Source** :
   
   - Les scripts ***Hadoop*** et ***Spark***.
   
   - Le code de l'interface graphique.
   
   - Les ***Dockerfiles*** pour chaque composant.
   
   - Le fichier ***Docker Compose***.

2. **Documentation** :
   
   - Documentation technique détaillée.
   
   - Guide d'installation et d'exécution du projet.


## Critères d'évaluation

- **Fonctionnalité** : Capacité du système à stocker, traiter et visualiser les données.

- **Qualité du Code** : Propreté, organisation et commentaires du code.

- **Interface Utilisateur** : Facilité d'utilisation, interactivité et esthétique de l'interface graphique.

- **Documentation** : Complétude et clarté de la documentation fournie.

- **Travail d'Équipe** : Collaboration efficace et répartition équitable des tâches.

- **Dockerisation** : Qualité et fonctionnalité des conteneurs ***Docker***.

## Ressources

- Documentation ***Hadoop*** : [https://hadoop.apache.org/](https://hadoop.apache.org/)

- Documentation ***Spark*** : [https://spark.apache.org/docs/latest/](https://spark.apache.org/docs/latest/)

- Documentation ***Docker*** : [https://docs.docker.com/](https://docs.docker.com/)

- Frameworks :

  - Flask : [https://flask.palletsprojects.com/](https://flask.palletsprojects.com/)

  - Django : [https://www.djangoproject.com/](https://www.djangoproject.com/)

  - Node.js/Express : [https://expressjs.com/](https://expressjs.com/)

  - Spring Boot : [https://spring.io/projects/spring-boot](https://spring.io/projects/spring-boot)


### Dépôt du Homework
 
Veuillez déposer vos livrable sur Moodle.

Vous avez jusqu'au ***08/09 avant 23h59*** pour compléter/déposer ce projet. Bonne chance et bon travail en équipe !

