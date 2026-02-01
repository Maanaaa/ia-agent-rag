import ollama
import os # Permet de manipuler les chemins de fichiers

def test_ollama():
    print("Test de la connexion à GEMMA 3")

    prompt = "Réponds moi connexion réussie à GEMMA 3"

    try:
        response = ollama.chat(model="gemma3:4b", messages=[{"role": "user", "content": prompt}])
        print(f"Réponse : {response['message']['content']}")

    except Exception as e:
        print(f"Erreur GEMMA 3 : {e}")

if __name__ == "__main__":
    test_ollama()