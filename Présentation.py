import warnings
warnings.filterwarnings('ignore')

import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="BOB 2024",
    page_icon="🧊",
    layout="wide")

st.image('RSIEDH.png',width = 500)

st.markdown("# Baromètre d'Opinion des Bénévoles 2024")
st.sidebar.markdown("# Présentation")

("Baromètre d'Opinion des Bénévoles, en ligne du 15 février au 22 avril 2024, auprès de 3 717 bénévoles de profils et d'horizons diversifiés. "
 "Cet échantillon robuste permet de réaliser des analyses croisées et de tenir compte de la diversité des situations et des formes d'engement.")

("Les résultats téléchargeables ici, par secteur d’activités et par tranche d’âge, viennent en complément de ceux présentés dans La France bénévole "
 "2024, en ligne sur www.recherches-solidarites.org")

("D’autres résultats sont disponibles, sur demande, auprès de [Marie](mailto:marie.duros@recherches-solidarites.org).")

("")
("")
("")

("*Cette enquête du Baromètre d’Opinion des Bénévoles de Recherches & Solidarités est réalisée, cette année, en coopération avec l’Institut Européen "
 "de Développement Humain. Elle a bénéficié d’une large diffusion grâce à la mobilisation des partenaires suivants :*")


st.image("BandeauTempo2024.png", width = 900)
