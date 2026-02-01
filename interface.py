import streamlit as st
from core.engine import get_estimation

# Titre de la page
st.set_page_config(page_title="Estimation de projets web", page_icon=":computer:")

def load_data():
    with open("data/data.txt", "r", encoding="utf-8") as file:
        return file.read()


# Design
st.title("Assistant - Estimation de tarfis de projets web")
st.markdown("""Décivrez vos besoins, et obtenez une estimation de tarifs personnalisée en quelques secondes.""")

user_input = st.text_input("Votre demande :", placeholder="Exemple : Je veux un site vitrine avec 3 pages et un formulaire de contact")

if st.button("Lancer l'estimation"):
    if user_input.strip():
        with st.spinner("Calcul en cours..."):
            try:
                resultat = get_estimation(user_input)
                st.markdown("---")
                st.markdown(resultat)
            except Exception as e:
                st.error(f"Erreur technique : {e}")
    else:
        st.warning("Veuillez entrer une description de projet.")

st.sidebar.info("Application par Théo Manya, dans le but de tester l'intégration de l'IA dans un projet web.")