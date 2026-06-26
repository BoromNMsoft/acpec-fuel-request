# ACPEC Fuel Request

Module Odoo de gestion des demandes de carburant pour une société de distribution d'hydrocarbures.

## Comment lancer le projet

Prérequis : Docker et Docker Compose installés.


git clone https://github.com/BoromNMsoft/acpec-fuel-request.git
cd acpec-fuel-request
docker compose up -d


Le premier démarrage télécharge les images Odoo 17 et PostgreSQL 15, ce qui peut prendre quelques minutes selon la connexion.

Pour arrêter les conteneurs :

docker compose down


Pour arrêter et supprimer aussi les volumes (réinitialisation complète) :

docker compose down -v


## Ports utilisés

 Odoo       | 8069      
 PostgreSQL | 5432     

Accès à l'application : [http://localhost:8069](http://localhost:8069)

## Identifiants de connexion par défaut

À la première connexion sur `http://localhost:8069`, Odoo affiche un écran de création de base de données :

Nom de la base : au choix (ex. `acpec_db`)
Email administrateur : au choix (ex. `amadba999@gmail.com`)
Mot de passe : amadou123
Login PostgreSQL : `odoo`
Mot de passe PostgreSQL : `odoo`

Une fois la base créée, vous êtes automatiquement connecté en tant qu'administrateur avec l'email et le mot de passe choisis à cette étape.

## Comment installer le module depuis l'interface Odoo

1. Aller dans Apps (Applications) depuis le menu principal
2. Cliquer sur Mettre à jour la liste des applications (nécessite le mode développeur, ou utiliser le bouton dédié dans le menu Apps)
3. Retirer le filtre "Apps" dans la barre de recherche pour voir tous les modules
4. Rechercher ACPEC Fuel Request
5. Cliquer sur Installer

Le module ajoute un nouveau menu Carburant > Demandes dans la barre de navigation principale.

Note sur les droits d'accès : l'administrateur du système hérite automatiquement du groupe « Manager Carburant » dès l'installation, et a donc immédiatement accès complet au module sans configuration supplémentaire. Pour tester le profil « Utilisateur », créez un utilisateur dédié et assignez-lui le groupe « Gestion Carburant : Utilisateur ».

## Fonctionnalités implémentées

Modèle `fuel.request` avec numérotation automatique (séquence `FR0001`, `FR0002`, ...)
Calcul automatique du montant total (`quantity × unit_price`), stocké et recalculé dynamiquement
Workflow à 4 états : Brouillon → Soumis → Approuvé / Rejeté → (retour) Brouillon, avec boutons contextuels selon l'état
Vues complètes : liste avec totaux, formulaire avec statusbar, recherche avec filtres par état/client/date et regroupements
Sécurité à deux niveaux :
  - Groupe Utilisateur : accès à ses propres demandes uniquement (record rule)
  - Groupe Manager : accès complet, y compris suppression
Chatter intégré (`mail.thread`, `mail.activity.mixin`) : suivi automatique des changements d'état, messagerie interne, activités planifiées
Rapport PDF imprimable au format QWeb, accessible depuis le menu Imprimer du formulaire

## Choix techniques et dépendances

Version Odoo : 17.0 (image officielle `odoo:17.0`)
Base de données : PostgreSQL 15
Dépendances du module : `base` (fondations Odoo), `mail` (chatter et activités)
Persistance : volumes Docker nommés pour la base de données et les fichiers Odoo, afin de conserver les données entre redémarrages
Code source du module monté en bind mount, permettant le développement local sans reconstruction d'image
