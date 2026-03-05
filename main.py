import streamlit as st
from supabase import create_client

Connexion sécurisée à Supabase
url = st.secrets["SUPABASE_URL"]
key = st.secrets["SUPABASE_KEY"]
supabase = create_client(url, key)

st.set_page_config(page_title="Institut - Inscription", layout="centered")

st.title("🎓 Inscription des Étudiants")
st.write("Veuillez remplir le formulaire ci-dessous pour créer votre compte.")

Formulaire d'inscription
with st.form("form_inscription", clear_on_submit=True):
nom = st.text_input("Nom")
prenom = st.text_input("Prénom")
date_n = st.date_input("Date de naissance")
lieu_n = st.text_input("Lieu de naissance")
profession = st.text_input("Profession")
ville = st.text_input("Ville")
email = st.text_input("Email (votre identifiant)")
password = st.text_input("Mot de passe", type="password")

if valider:
if not email or not password:
st.error("L'email et le mot de passe sont obligatoires !")
else:
# On prépare les données
infos_etudiant = {
"nom": nom,
"prenom": prenom,
"date_naissance": str(date_n),
"lieu_naissance": lieu_n,
"profession": profession,
"ville": ville,
"email": email,
"mot_de_passe": password
}
