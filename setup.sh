#!/bin/bash

echo "SETUP SCRIPT"

# 1. Nettoyage
if [ -d "venv" ]; then
    echo "Suppression de l'ancien venv..."
    rm -rf venv
fi

# Création du venv
echo "Création du venv..."
python -m venv venv

# Installation (on utilise le chemin Windows pour l'exécutable dans le venv)
echo "Installation des dépendances..."
./venv/Scripts/python -m pip install --upgrade pip
./venv/Scripts/pip install ollama streamlit

# Lancement
echo "Lancement de l'interface..."
./venv/Scripts/streamlit run interface.py