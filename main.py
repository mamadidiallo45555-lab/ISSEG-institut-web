import streamlit as st

# 1. CONFIGURATION DU SITE
st.set_page_config(page_title="Réseau Social Institut", layout="centered")

# 2. MENU DE NAVIGATION (BARRE À GAUCHE)
st.sidebar.title("Navigation")
page = st.sidebar.radio("Aller vers :", ["Connexion", "Inscription"])

# 3. FONCTION POUR LA PAGE D'INSCRIPTION
def afficher_inscription():
st.title("🎓 Inscription à l'Institut")
st.subheader("Créez votre compte")
with st.form("inscription_form"):
col1, col2 = st.columns(2)
with col1:
nom = st.text_input("Nom")
prenom = st.text_input("Prénom")
date_nays = st.date_input("Date de naissance")
lieu_nays = st.text_input("Lieu de naissance")
with col2:
profession = st.text_input("Profession")
ville = st.text_input("Ville")
email = st.text_input("Email")
password = st.text_input("Mot de passe", type="password")
st.write("---")
st.write("📸 Ma Photo de Profil")
photo_profil = st.file_uploader("Choisir une image", type=['png', 'jpg', 'jpeg'])
if photo_profil is not None:
st.image(photo_profil, width=150)
submit_button = st.form_submit_button("S'inscrire")
if submit_button:
if nom and prenom and email and password:
st.success(f"Bienvenue {prenom} ! Compte créé.")
else:
st.error("Veuillez remplir les champs obligatoires.")

# 4. FONCTION POUR LA PAGE DE CONNEXION
def afficher_connexion():
st.title("🔑 Connexion")
st.subheader("Entrez vos identifiants")
with st.form("form_connexion"):
email_log = st.text_input("Email")
pass_log = st.text_input("Mot de passe", type="password")
bouton_log = st.form_submit_button("Se connecter")
if bouton_log:
if email_log and pass_log:
st.success("Connexion réussie !")
else:
st.error("Veuillez remplir les champs.")

# 5. LOGIQUE POUR AFFICHER LA BONNE PAGE
if page == "Inscription":
afficher_inscription()
else:
afficher_connexion()
