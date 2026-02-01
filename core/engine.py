import ollama
import os

def get_estimation(user_query):
    # Chemin dynamique
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path = os.path.join(base_dir, "data", "data.txt")
    
    with open(path, "r", encoding="utf-8") as file:
        referentiel = file.read()

    instruction_agent = f"""Tu es l'Expert Estimateur de Nexalys.
    Utilise EXCLUSIVEMENT ce référentiel : {referentiel}

    ALGORITHME À SUIVRE :
    1. Décomposition en briques UTA (ex: STRUC_BASE, PAGE_STD).
    2. Détermination du Coefficient de Complexité (C).
    3. Calcul du Temps Technique (T) avec la marge de 20%.
    4. Calcul de la Gestion (G) (20% de T).
    5. Ajout des Forfaits.
    6. Calcul du total TTC arrondi.

    Sois rigoureux sur chaque ligne de calcul."""

    response = ollama.generate(
        model="gemma3:4b",
        system=instruction_agent,
        prompt=user_query,
    )
    return response['response']