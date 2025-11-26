import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import seaborn as sns

from analyse_sentimentsFINAL import nettoyer_texte, sentiment_model

# ==============================
#   TITRE
# ==============================
st.title(" Analyse de Sentiments")


# ==============================
#   CHARGEMENT DATASET
# ==============================
df = pd.read_csv('analyse_sentiments_complete.csv', sep=';')

# Conversion label -> texte
if 'label' in df.columns:
    df['transformer_label'] = df['label'].map({1: "POSITIF", 0: "NEGATIF"})

# ==============================
#   ONGLET : PREDICTION
# ==============================
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    " Prédiction",
    " Aperçu du Dataset",
    " Distribution des Sentiments",
    " Nuage de Mots",
    " Analyse par Mots-Clés"
])

# ------ ONGLET 1 : PREDICTION ------
with tab1:
    texte_input = st.text_area("📝 Saisissez un avis à analyser :", "")

    if st.button("Prédire le sentiment"):
        texte_clean = nettoyer_texte(texte_input)
        resultat = sentiment_model([texte_clean])[0]
        sentiment = "POSITIF" if resultat["label"] == "LABEL_1" else "NÉGATIF"

        # Couleurs selon sentiment
        if sentiment == "POSITIF":
            st.success("🌟 **POSITIF**")
        else:
            st.error("🔴 **NÉGATIF**")

        st.write(f"Confiance : **{resultat['score']*100:.1f}%**")

        # Progress bar colorée selon score
        st.progress(resultat["score"])


# ------ ONGLET 2 : APERÇU DATASET ------
with tab2:
    st.write("###  Aperçu des premières lignes du dataset")
    st.dataframe(df.head())

    st.write("###  Informations")
    st.write(df.describe(include='all'))


# ------ ONGLET 3 : DISTRIBUTION ------
with tab3:
    st.write("###  Distribution des Sentiments")

    fig, ax = plt.subplots()

    couleurs = ['#2ecc71', '#e74c3c']  # vert / rouge
    df['transformer_label'].value_counts().plot(kind='bar', ax=ax, color=couleurs)

    plt.xlabel("Sentiment")
    plt.ylabel("Nombre d'avis")
    plt.title("Répartition des sentiments")

    st.pyplot(fig)


# ------ ONGLET 4 : WORDCLOUD ------
with tab4:
    st.write("###  Nuage de Mots")

    texte_total = " ".join(df['texte_avis'].astype(str))

    wc = WordCloud(
        width=800,
        height=400,
        background_color='white',
        colormap='viridis'   # colormap stylée
    ).generate(texte_total)

    fig, ax = plt.subplots(figsize=(10,5))
    ax.imshow(wc)
    ax.axis("off")
    st.pyplot(fig)


# ------ ONGLET 5 : ANALYSE PAR MOTS-CLÉS ------
with tab5:
    st.write("### Analyse par mot-clé")

    mot = st.text_input("Entrez un mot à rechercher :")

    if mot:
        resultats = df[df['texte_avis'].str.contains(mot, case=False, na=False)]

        st.write(f"### Résultats pour **{mot}** : {len(resultats)} avis")

        # Style couleur sur la colonne sentiment
        resultats_style = resultats.style.apply(
            lambda s: ['background-color: #2ecc7055' if v=='POSITIF' else 'background-color: #e74c3c55' for v in s],
            subset=['transformer_label']
        )

        st.dataframe(resultats_style, use_container_width=True)
