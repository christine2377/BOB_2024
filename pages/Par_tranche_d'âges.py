import warnings
warnings.filterwarnings('ignore')

import pandas as pd
import openpyxl
import streamlit as st

st.markdown("# Par tranche d'âges")
st.sidebar.markdown("# Par tranche d'âges")

fichier = "Tranche age.xlsx"

# Quelles sont les raisons de votre engagement bénévole aujourd'hui dans cette cette association ?
table = pd.read_excel( fichier, sheet_name = "Feuil2" ,skiprows=3,nrows= 8, index_col =0, dtype = "object")
table = table.applymap(lambda x: f'{x * 100:.0f}%')


#Vous diriez, à propos de votre engagement dans cette association, qu'il est synonyme, avant tout, de :
table1 = pd.read_excel( fichier, sheet_name = "Feuil2" ,skiprows=17,nrows= 6, index_col =0, dtype = "object")
table1 = table1.applymap(lambda x: f'{x * 100:.0f}%')


#Vous avez le sentiment que votre activité bénévole, vous permet : Plusieurs réponses possible
table2 = pd.read_excel( fichier, sheet_name = "Feuil2" ,skiprows=30,nrows= 8, index_col =0, dtype = "object")
table2 = table2.applymap(lambda x: f'{x * 100:.0f}%')


#Si vous éprouvez des déceptions, sur quels thèmes portent-elles ? Plusieurs réponses possibles
table3 = pd.read_excel( fichier, sheet_name = "Feuil2" ,skiprows=46,nrows= 8, index_col =0, dtype = "object")
table3 = table3.applymap(lambda x: f'{x * 100:.0f}%')


#Quelles seraient vos attentes pour bien vivre votre activité bénévole ? Plusieurs réponses possibles
table4 = pd.read_excel( fichier, sheet_name = "Feuil2" ,skiprows=60,nrows= 9, index_col =0, dtype = "object")
table4 = table4.applymap(lambda x: f'{x * 100:.0f}%')


# Attendez-vous de votre association qu'elle vous aide à développer ces savoir-être ?
table5 = pd.read_excel( fichier, sheet_name = "Feuil2" ,skiprows=78,nrows= 6, index_col =0, dtype = "object")
table5 = table5.applymap(lambda x: f'{x * 100:.0f}%')


styled_table = table.style.set_properties(**{'text-align': 'center'})
styled_table1 = table1.style.set_properties(**{'text-align': 'center'})
styled_table2 = table2.style.set_properties(**{'text-align': 'center'})
styled_table3 = table3.style.set_properties(**{'text-align': 'center'})
styled_table4 = table4.style.set_properties(**{'text-align': 'center'})
styled_table5 = table5.style.set_properties(**{'text-align': 'center'})


"**Quelles sont les raisons de votre engagement bénévole aujourd'hui dans cette cette association ?** *Plusieurs réponses possibles*"
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

