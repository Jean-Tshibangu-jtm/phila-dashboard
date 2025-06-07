import streamlit as st
from pyecharts import options as opts
from pyecharts.charts import Bar, Line
from streamlit_echarts import st_pyecharts

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

# Sélection du mois
mois = st.selectbox("Choisir un mois :", ["Mars", "Avril", "Mai"])
graphique = st.selectbox("Type de graphique :", ["Barres", "Courbes"])

# Récupération des données
if mois == "Mars":
    jeudi, dimanche = mars_jeudi, mars_dimanche
elif mois == "Avril":
    jeudi, dimanche = avril_jeudi, avril_dimanche
elif mois == "Mai":
    jeudi, dimanche = mai_jeudi, mai_dimanche

# Affichage
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