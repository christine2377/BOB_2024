import warnings
warnings.filterwarnings('ignore')

import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="BOB 2024 - Par secteur d'activités",
    page_icon="🧊",
    layout="wide")

st.markdown("# Par Secteur d'activités")
st.sidebar.markdown("# Par Secteur d'activités")

# Quelles sont les raisons de votre engagement bénévole aujourd'hui dans cette cette association ?
df = pd.DataFrame({
                   "Social": ["91%","54%","33%","31%","13%","14%","10%","12%"],
                   "Santé": ["87%","61%","41%","29%","20%","13%","10%","7%"],
                   "Solidarité\ninternationale": ["84%","63%","26%","24%","14%","16%","12%","7%"],
                   "Sport": ["85%","24%","47%","44%","16%","17%","24%","9%"],
                   "Culture": ["70%", "48%","47%","38%","13%","9%","19%","12%"],
                   "Loisirs": ["79%","15%","47%","44%","17%","12%","21%","10%"],
                   "Formation,\nemploi,\néconomie": ["86%","47%","31%","32%","17%","14%","18%","8%"],
                   "Jeunesse,\néducation populaire": ["88%","50%","46%","30%","25%","15%","18%","8%"],
                   "Environnement": ["82%","88%","34%","22%","24%","12%","10%","5%"]},
                    index = (["Le souhait d'être utile et d'agir pour les autres",
                        "La cause défendue",
                        "Un épanouissement personel",
                        "Le souhait d'appartenir à une équipe",
                        "L'aquisition de compétences",
                        "La reconnaissance sociale et\nla valorisation de mon bénévolat",
                        "Le désir d'exercer une responsabilité",
                        "J'avais simplement du temps libre"]))


#Vous diriez, à propos de votre engagement dans cette association, qu'il est synonyme, avant tout, de :
df1 = pd.DataFrame({"Social": ["45%","39%","7%","4%","5%","100%"],
                    "Santé": ["36%","47%","7%","5%","5%","100%"],
                    "Solidarité internationale": ["34%","44%","10%","3%","8%","100%"],
                    "Sport": ["50%","27%","13%","6%","4%","100%"],
                    "Culture": ["52%","29%","12%","2%","5%","100%"],
                    "Loisirs": ["57%","23%","9%","","11%","100%"],
                    "Formation, emploi, économie": ["51%","36%","7%","3%","4%","100%"],
                    "Jeunesse,éducation populaire": ["39%","46%","9%","4%","3%","100%"],
                    "Environnement": ["42%","35%","10%","6%","7%","100%"]},
                   ["Plaisir",
                   "Epanouissement",
                   "Inquitude",
                    "Désillusion",
                    "Non réponse",
                    "Total"])



#Vous avez le sentiment que votre activité bénévole, vous permet : Plusieurs réponses possible
df2 = pd.DataFrame({"Social": ["83%","51%","24%","15%","18%","19%","21%","11%"],
                    "Santé": ["88%","49%","35%","23%","15%","31%","19%","7%"],
                    "Solidarité internationale": ["72%","55%","30%","19%","27%","24%","24%","11%"],
                    "Sport": ["71%","68%","36%","30%","22%","21%","26%","7%"],
                    "Culture": ["55%","72%","32%","23%","35%","15%","22%","8%"],
                    "Loisirs": ["67%","73%","25%","23%","31%","17%","18%","12"],
                    "Formation, emploi, économie": ["79%","57%","28%","14%","26%","26%","19%","9%"],
                    "Jeunesse, éducation populaire": ["78%","65%","40%","30%","29%","30%","29%","13%"],
                    "Environnement": ["53%","58%","42%","27%","27%","23%","19%","8%"]},
                ["D'être à l'écoute et attentif aux autres",
                         "De mener des projets en équipe",
                         "De renforcer mes compétences",
                         "D'être à l'aise dans la prise de parole",
                         "De développer mon esprit créatif",
                         "De mieux affronter des situations compliquées",
                         "D'être autonome, de prendre des initiatives",
                         "De mieux organiser mon temps"])



#Si vous éprouvez des déceptions, sur quels thèmes portent-elles ? Plusieurs réponses possibles

df3 = pd.DataFrame({"Social": ["37%","38%","23%","18%","18%","12%","11%","12%"],
                    "Santé": ["37%","48%","23%","24%","12%","14%","10%","11%"],
                    "Solidarité internationale": ["41%","41%","26%","23%","13%","13%","8%","6%"],
                    "Sport": ["51%","56%","13%","16%","11%","14%","17%","20%"],
                    "Culture": ["48%","47%","20%","14%","12%","17%","8%","11%"],
                    "Loisirs": ["31%","42%","19%","11%","12%","14%","20%","12%"],
                    "Formation, emploi, écomonie": ["36%","39%","28%","21%","19%","14%","14%","12%"],
                    "Jeunesse, éducation populaire": ["46%","43%","24%","16%","13%","10%","12%","12%"],
                    "Environnement": ["36%","31%","41%","13%","9%","19%","12%","11%"]},
                    index= ["Le manque de moyens matériels et/ou financiers pour mener mes actions",
                        "Le manque de moyens humains dans mon association",
                        "Les effets limités des actions menées par mon association",
                        "Le fonctionnement de mon association",
                        "Les relations entre les bénévoles",
                        "Le manque de dynamisme et d'innovation dans mon association",
                        "Les relations avec les membres de l'association",
                        "La place et la reconnaissance des bénévoles dans mon association"])



#Quelles seraient vos attentes pour bien vivre votre activité bénévole ? Plusieurs réponses possible

df4 = pd.DataFrame({"Social": ["30%","37%","24%","22%","24%","14%","12%","16%","11%"],
                    "Santé": ["40%","45%","30%","25%","17%","14%","12%","18%","7%"],
                    "Solidarité internationale": ["25%","47%","28%","23%","17%","9%","16%","16%","13%"],
                    "Sport": ["22%","56%","42%","24%","7%","7%","10%","21%","7%"],
                    "Culture": ["23%","53%","33%","19%","9%","5%","8%","14%","8%"],
                    "Loisirs": ["21%","61%","28%","20%","7%","4%","8%","15%","4%"],
                    "Formation, emploi, économie": ["30%","35%","30%","27%","19%","8%","10%","20%","7%"],
                    "Jeunesse, éducation populaire": ["32%","35%","35%","20%","19%","10%","10%","14%","15%"],
                    "Environnement": ["46%","29%","30%","19%","23%","20%","10%","11%","10%"]},
                    index = ["De la formation",
                        "L'aide d'autres bénévoles",
                        "La prise en charge des frais occasionnés par mon activité",
                        "Des conseils",
                        "Etre davandage associé aux décisions de mon association",
                        "Plus d'infomations sur les activités de mon association",
                        "Avoir une plus grande liberté d'initiatives",
                        "Une plus grande attention portée à mon activité par les instances dirigeantes",
                        "Une définition plus précise de ma mission"])




styled_df = df.style.set_properties(**{'text-align': 'center'})
styled_df1 = df1.style.set_properties(**{'text-align': 'center'})
styled_df2 = df2.style.set_properties(**{'text-align': 'center'})
styled_df3 = df3.style.set_properties(**{'text-align': 'center'})
styled_df4 = df4.style.set_properties(**{'text-align': 'center'})


"**Quelles sont les raisons de votre engagement bénévole aujourd'hui dans cette cette association ?** *Plusieurs réponses possibles*"
#st.dataframe(df,use_container_width = True)
st.table(styled_df)
"**Vous diriez, à propos de votre engagement dans cette association, qu'il est synonyme, avant tout, de :**"
#st.dataframe(styled_df1,use_container_width = True)
st.table(styled_df1)
"**Vous avez le sentiment que votre activité bénévole, vous permet :** *Plusieurs réponses possibles*"
#st.dataframe(styled_df2,use_container_width = True)
st.table(styled_df2)
"**Si vous éprouvez des déceptions, sur quels thèmes portent-elles ?** *Plusieurs réponses possibles*"
#st.dataframe(styled_df3,use_container_width = True)
st.table(styled_df3)
"**Quelles seraient vos attentes pour bien vivre votre activité bénévole ?** *Plusieurs réponses possibles*"
#st.dataframe(styled_df4,use_container_width = True)
st.table(styled_df4)
"**Attendez-vous de votre association qu'elle vous aide à développer ces savoir-faire et ces savoir-être ?**"
