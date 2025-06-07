import streamlit as st
from pyecharts import options as opts
from pyecharts.charts import Bar, Line
from streamlit_echarts import st_pyecharts

st.set_page_config(page_title="Participation Hebdomadaire", layout="centered")

st.markdown(
    "<h2 style='text-align: center;'>Tableau de bord : Participation Hebdomadaire</h2>",
    unsafe_allow_html=True
)

# Données hebdomadaires par mois
semaines = ["Semaine 1", "Semaine 2", "Semaine 3", "Semaine 4"]

# Mars
mars_jeudi = [20, 30, 33, 22]
mars_dimanche = [50, 65, 80, 60]

# Avril
avril_jeudi = [25, 28, 35, 30]
avril_dimanche = [55, 60, 78, 70]

# Mai
mai_jeudi = [18, 22, 27, 25]
mai_dimanche = [45, 58, 65, 55]

# Interface utilisateur
st.write("")
col1, col2 = st.columns(2)
mois = col1.selectbox("Choisir un mois :", ["Mars", "Avril", "Mai"])
graphique = col2.selectbox("Type de graphique :", ["Barres", "Courbes"])

# Sélection des données
if mois == "Mars":
    jeudi, dimanche = mars_jeudi, mars_dimanche
elif mois == "Avril":
    jeudi, dimanche = avril_jeudi, avril_dimanche
elif mois == "Mai":
    jeudi, dimanche = mai_jeudi, mai_dimanche

# Construction du graphique
if graphique == "Barres":
    chart = (
        Bar()
        .add_xaxis(semaines)
        .add_yaxis("Jeudi", jeudi, label_opts=opts.LabelOpts(is_show=True, formatter="{c} participants"))
        .add_yaxis("Dimanche", dimanche, label_opts=opts.LabelOpts(is_show=True, formatter="{c} participants"))
        .set_global_opts(title_opts=opts.TitleOpts(title=f"Participation – {mois}"))
    )
else:
    chart = (
        Line()
        .add_xaxis(semaines)
        .add_yaxis("Jeudi", jeudi, is_smooth=True)
        .add_yaxis("Dimanche", dimanche, is_smooth=True)
        .set_global_opts(title_opts=opts.TitleOpts(title=f"Évolution – {mois}"))
    )

# Affichage dans Streamlit
st_pyecharts(chart)