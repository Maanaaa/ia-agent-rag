from core.engine import get_estimation

def main():
    print("Tape 'quitter' pour fermer.\n")
    
    while True:
        query = input("Client : ")
        
        if query.lower() in ["quitter", "exit", "stop"]:
            print("Fin de session.")
            break
            
        if not query.strip():
            continue

        print("\n[Analyse en cours...]")
        try:
            # On appelle la même logique que l'interface Streamlit
            reponse = get_estimation(query)
            print(f"\nIA :\n{reponse}")
            print("\n" + "-"*50 + "\n")
        except Exception as e:
            print(f"Erreur : {e}")

if __name__ == "__main__":
    main()