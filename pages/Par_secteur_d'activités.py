import warnings
warnings.filterwarnings('ignore')

import pandas as pd
import streamlit as st
import openpyxl
import xlsxwriter
from io import BytesIO

st.set_page_config(
    page_title="BOB 2024 - Par secteur d'activités",
    page_icon="🧊",
    layout="wide")

st.markdown("# Résultats par secteur d'activités")
st.sidebar.markdown("# Par secteur d'activités")

fichier = "BOB2024-Dashboard.xlsx"
sheet = "Secteur_activités"
# Quelles sont les raisons de votre engagement bénévole aujourd'hui dans cette cette association ?
table = pd.read_excel( fichier, sheet_name = sheet ,skiprows=4,nrows= 8, index_col =0, dtype = "object")
table = table.applymap(lambda x: f'{x * 100:.0f}%')


#Vous diriez, à propos de votre engagement dans cette association, qu'il est synonyme, avant tout, de :
table1 = pd.read_excel( fichier, sheet_name = sheet ,skiprows=19, nrows= 6, index_col =0, dtype = "object")
table1 = table1.applymap(lambda x: f'{x * 100:.0f}%')


#Vous avez le sentiment que votre activité bénévole, vous permet : Plusieurs réponses possible
table2 = pd.read_excel( fichier, sheet_name = sheet ,skiprows=32,nrows= 8, index_col =0, dtype = "object")
table2 = table2.applymap(lambda x: f'{x * 100:.0f}%')


#Si vous éprouvez des déceptions, sur quels thèmes portent-elles ? Plusieurs réponses possibles
table3 = pd.read_excel( fichier, sheet_name = sheet ,skiprows=45,nrows= 8, index_col =0, dtype = "object")
table3 = table3.applymap(lambda x: f'{x * 100:.0f}%')


#Quelles seraient vos attentes pour bien vivre votre activité bénévole ? Plusieurs réponses possibles
table4 = pd.read_excel( fichier, sheet_name = sheet ,skiprows=60,nrows= 9, index_col =0, dtype = "object")
table4 = table4.applymap(lambda x: f'{x * 100:.0f}%')


# Attendez-vous de votre association qu'elle vous aide à développer ces savoir-être ?
table5 = pd.read_excel( fichier, sheet_name = sheet ,skiprows=77,nrows= 6, index_col =0, dtype = "object")
table5 = table5.applymap(lambda x: f'{x * 100:.0f}%')

questions = ["Quelles sont les raisons de votre engagement bénévole aujourd'hui dans cette association ? Plusieurs réponses possible",
             "Vous diriez, à propos de votre engagement dans cette association, qu'il est synonyme, avant tout, de :",
             "Vous avez le sentiment que votre activité bénévole, vous permet : Plusieurs réponses possibles",
             "Attendez-vous de votre association qu'elle vous aide à développer ces savoir-faire et ces savoir-être ?",
             "Si vous éprouvez des déceptions, sur quels thèmes portent-elles ? Plusieurs réponses possibles",
             "Quelles seraient vos attentes pour bien vivre votre activité bénévole ? Plusieurs réponses possibles"
             ]

styled_table = table.style.set_properties(**{'text-align': 'center'})
styled_table1 = table1.style.set_properties(**{'text-align': 'center'})
styled_table2 = table2.style.set_properties(**{'text-align': 'center'})
styled_table3 = table3.style.set_properties(**{'text-align': 'center'})
styled_table4 = table4.style.set_properties(**{'text-align': 'center'})
styled_table5 = table5.style.set_properties(**{'text-align': 'center'})


"**Quelles sont les raisons de votre engagement bénévole aujourd'hui dans cette association ?** *Plusieurs réponses possibles*"
#st.dataframe(df,use_container_width = True)
st.table(styled_table)
"**Vous diriez, à propos de votre engagement dans cette association, qu'il est synonyme, avant tout, de :**"
#st.dataframe(styled_df1,use_container_width = True)
st.table(styled_table1)
"**Vous avez le sentiment que votre activité bénévole, vous permet :** *Plusieurs réponses possibles*"
#st.dataframe(styled_df2,use_container_width = True) ajout dernier
st.table(styled_table2)
"**Attendez-vous de votre association qu'elle vous aide à développer ces savoir-faire et ces savoir-être ?**"
st.table(styled_table5)
"**Si vous éprouvez des déceptions, sur quels thèmes portent-elles ?** *Plusieurs réponses possibles*"
#st.dataframe(styled_df3,use_container_width = True)
st.table(styled_table3)
"**Quelles seraient vos attentes pour bien vivre votre activité bénévole ?** *Plusieurs réponses possibles*"
#st.dataframe(styled_df4,use_container_width = True)
st.table(styled_table4)

###########################################################

# Liste des tables
tables = [table,table1,table2,table5,table3,table4]


# Fonction pour créer un fichier Excel avec les questions et les tables
def to_excel(tables, questions):
    output = BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        workbook = writer.book

        # Formats
        bold_format = workbook.add_format({'bold': True, 'text_wrap': True})
        border_format = workbook.add_format({'border': 1, 'text_wrap': True})

        for table, question, sheet_name in zip(tables, questions,
                                               ["Tableau1", "Tableau2", "Tableau3", "Tableau4", "Tableau5",
                                                "Tableau6"]):
            # Créer une feuille
            worksheet = workbook.add_worksheet(sheet_name)

            # Écrire la question en gras
            worksheet.write(0, 0, question, bold_format)

            # Laisser une ligne vide entre la question et le tableau
            empty_row = 1

            # Écrire les index et les noms des colonnes en gras avec bordures
            worksheet.write(empty_row + 1, 0, table.index.name if table.index.name else "", bold_format)
            for idx, col in enumerate(table.columns):
                worksheet.write(empty_row + 1, idx + 1, col, bold_format)
                worksheet.set_column(idx + 1, idx + 1, 20)  # Ajuster la largeur de la colonne

            # Ajuster la largeur de la colonne pour les index
            worksheet.set_column(0, 0, 50)

            # Écrire les données du tableau avec bordures et retour à la ligne pour l'index
            for row_idx, (index, row) in enumerate(table.iterrows()):
                worksheet.write(row_idx + empty_row + 2, 0, index, bold_format)
                for col_idx, value in enumerate(row):
                    worksheet.write(row_idx + empty_row + 2, col_idx + 1, value, border_format)

    return output.getvalue()


# Bouton de téléchargement
excel_data = to_excel(tables, questions)
st.download_button(label="Télécharger les données", data=excel_data, file_name="BOB_2024-par_tranches_ages.xlsx", mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                   help="Cliquez ici pour télécharger les données au format XLSX")
