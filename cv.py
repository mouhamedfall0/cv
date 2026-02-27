import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Currculum Vitae ", page_icon="📍", layout="wide")

# Sidebar pour Contacts et Logiciels
st.sidebar.header(" *Contacts*")
st.sidebar.markdown("""
*Email*  
[mouhamedfall261@gmail.com](mouhamedfall261@gmail.com)
**Adresse**  
Dakar, Medina, 
""")
st.sidebar.header(" *Logiciels maîtrisés*")
logiciels = [
    "QGIS / ArcGIS",
    "AutoCAD", 
    "Python",
    "Pix4D",
    "Excel",
    "PowerPoint",
    "Erdas"
]
for logiciel in logiciels:
    st.sidebar.markdown(f"• *{logiciel}*")

st.sidebar.markdown("---")
st.sidebar.markdown("Géomaticien - L2 en cours")

# Main content
st.title(" *Mouhamed Lamine Fall*")
st.markdown("  geographe Géomaticien")

## COMPETENCES
st.header(" *Compétences*")
competences = [
    "topographiques",
    "Cartographie",
    "Utilisation des outils de la geomatique : Niveau, Station totale(manuelle, Drone, GPS",
    "Géo-référencement",
    "Implanter une base de données",
     "Teledetection",
    
]

for comp in competences:
    st.markdown(f"• *{comp}*")

## EXPERIENCES
st.header(" *Expériences*")

st.subheader("*Juin - Septembre 2022*")
st.markdown("*GREDAT – cabinet developpement territorial*")

## Formation
st.header(" *Formation*")

st.markdown("""
*2025 - 2026*  
*Centre d'entrepreneuriat et de développement technique (CEDT) le G15*  
Licence 2 en Géomatique (Formation en cours)

*2024 - 2025*  
*Centre d'entrepreneuriat et de développement technique (CEDT) le G15*  
Licence 1 en Géomatique

*2017 - 2018*  
*UCAD*  
Maitrise en geographie


*2017 - 2018*  
*Meckhe*  
Baccalauréat


""")



    
