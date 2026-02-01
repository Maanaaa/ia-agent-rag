# Agent RAG

Ce projet est un agent d'IA spécialisé dans l'estimation de projets digitaux. Il utilise le modèle **Gemma 3** via **Ollama** couplé à une architecture **RAG** pour transformer des besoins clients en devis techniques.

---

## 🚀 Concept : C'est quoi le RAG ?

Le **RAG (Retrieval-Augmented Generation)** est une technique qui permet de "donner des lunettes" à une IA :

1.  **Retrieval (Récupération)** : L'IA va chercher des informations dans un fichier source local (`data/data.txt`).
2.  **Augmented (Augmentée)** : On ajoute ces informations (tarifs, briques de temps) au contexte de la question.
3.  **Generation (Génération)** : L'IA génère une réponse basée sur ces faits réels plutôt que d'inventer des chiffres.

**Résultat :** L'agent ne "hallucine" pas les prix, il applique rigoureusement le référentiel de l'agence.

---

## 🏗️ Architecture du Projet

Le projet est structuré pour séparer la **Logique Métier** de l'**Interface Utilisateur** :

* **`core/engine.py`** : Le cerveau. Il gère l'appel à Ollama, injecte les données du RAG et applique l'algorithme de calcul.
* **`data/data.txt`** : Le référentiel UTA. Contient toutes les briques de temps et les règles tarifaires.
* **`interface.py`** : L'interface Web développée avec **Streamlit**.
* **`app.py`** : Une version console (CLI) pour tester la logique rapidement.
* **`setup.sh`** : Script Bash pour automatiser l'installation et le lancement.

---

## 📊 Modèle de Données Atomique (UTA)

Le projet abandonne les prix forfaitaires flous pour une approche par **Unités de Temps Atomiques** :

1.  **Briques de temps** : Chaque tâche a une valeur horaire (ex: `STRUC_BASE` = 6h).
2.  **Algorithme de calcul** :
    * **T** (Temps Technique) = (Somme UTA) × Complexité × 1.20 (Marge).
    * **G** (Gestion) = 20% de T.
    * **Total** = Somme des coûts + Forfaits (Hébergement, SEO).
3.  **Arrondi** : Le montant final est toujours arrondi à la dizaine supérieure.

---

## 🛠️ Installation

### 1. Prérequis
* **Ollama** installé avec le modèle `gemma3:4b`.
* **Python 3.10** ou plus.

### 2. Lancement automatique (Conseillé)
Utilisez le script fourni pour créer l'environnement et lancer l'application en une commande :
```bash
bash setup.sh
```

### 3. Lancement manuel
# 1. Créer l'environnement virtuel
python -m venv venv

# 2. Activer l'environnement
# Sur Windows (Git Bash) :
source venv/Scripts/activate

# 3. Installer les dépendances
pip install -r requirements.txt

# 4. Lancer l'interface Web
streamlit run interface.py