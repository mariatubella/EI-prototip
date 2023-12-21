import streamlit as st
from PIL import Image
import pandas as pd
import altair as alt

st.sidebar.markdown("# Log in")

def main():

    # Add a sidebar with page selection
    role = st.sidebar.selectbox("Quin és el teu rol?", ["", "Administració", "Personal sanitari"])
    zona = st.sidebar.selectbox("A quina regió treballes?", ["", "Metropolitana Sud", "Metropolitana Nord", "Barcelona",
                                                             "Girona", "Catalunya central", "LLeida", "Alt pirineu - Aran",
                                                             "Tarragona", "Terres de l'Ebre"])
    username = st.sidebar.text_input("Usuari")
    contra = st.sidebar.text_input("Contrasenya", type="password")

    if contra == "maria":
        st.write(f"### Hola {username}!")
        st.write(f"### Aquestes son les alertes a la zona {zona}:")

        alertes(zona)

        utis = st.sidebar.selectbox("Serveis", ["","Mapa", "Historial", "Anàlisi sanitari", "Anàlisi ambiental", "Informes", "Compte"])
        if utis == "Mapa":
            mapa(zona)
        elif utis == "Historial":
            historial(zona)
        elif utis == "Anàlisi sanitari":
            analisi(zona)
        elif utis == "Informes":
            informes(zona)
        elif utis == "Anàlisi ambiental":
            analisi_ambiental(zona)
        elif utis == "Compte":
            compte(username, role)
    
    elif contra != "maria" and contra != "":
        st.markdown("<span style='color:red'>Credencials incorrectes</span>", unsafe_allow_html=True)



def alertes(zona):
    if zona == "Metropolitana Sud":
        st.markdown("<div style='background-color:red; padding:10px; color:white; font-size:18px;'><b>Alta incidència prevista a Torrelles de Llobregat fins 17/12/2023</b></div>", unsafe_allow_html=True)
    elif zona == "Girona":
        st.markdown("<div style='background-color:red; padding:10px; color:white; font-size:18px;'><b>Alta incidència prevista a Banyoles fins 22/12/2023</b></div>", unsafe_allow_html=True)
    else:
        st.markdown("<div style='background-color:red; padding:10px; color:white; font-size:18px;'><b>No hi ha cap alerta a la teva zona</b></div>", unsafe_allow_html=True)


def historial(zona):
    st.write(f"### Historial de la regió sanitària {zona}")
    if zona == "Metropolitana Sud":
        st.markdown("<div style='background-color:pink; padding:10px; color:black; font-size:18px;'><b>Alta incidència a Castelldefels fins 17/11/2023</b></div>", unsafe_allow_html=True)
        st.markdown("<div style='background-color:pink; padding:10px; color:black; font-size:18px;'><b>Alta incidència al Prat de Llobregat fins 5/11/2023</b></div>", unsafe_allow_html=True)
        st.markdown("<div style='background-color:pink; padding:10px; color:black; font-size:18px;'><b>Alta incidència a Begues fins 30/10/2023</b></div>", unsafe_allow_html=True)

    elif zona == "Girona":
        st.markdown("<div style='background-color:pink; padding:10px; color:black; font-size:18px;'><b>Alta incidència a Figueres fins 22/11/2023</b></div>", unsafe_allow_html=True)
        st.markdown("<div style='background-color:pink; padding:10px; color:black; font-size:18px;'><b>Alta incidència a Girona fins 11/11/2023</b></div>", unsafe_allow_html=True)
        st.markdown("<div style='background-color:pink; padding:10px; color:black; font-size:18px;'><b>Alta incidència a Santa Coloma de Farners fins 2/11/2023</b></div>", unsafe_allow_html=True)

    else:
        st.markdown("<div style='background-color:pink; padding:10px; color:black; font-size:18px;'><b>No hi ha cap alerta a la teva zona</b></div>", unsafe_allow_html=True)

def analisi(zona):
    if zona == "Metropolitana Sud":
        poblacio = st.selectbox("Població", ["", "Argençola", "Bellprat", "el Bruc", "Cabrera d'Anoia", "Capellades", "Carme", 
                                             "Castellolí", "El Prat de Llobregat", "els Hostalets de Pierola", "Igualada", "Masquefa", "Montmaneu",
                                               "Òdena", "Piera", "Santa Margarida de Montbui", "Vilanova del Camí", "Avinyonet del Penedès", 
                                               "Gelida", "Mediona", "Olèrdola", "Sant Pere de Riudebitlles", "..." ])
    elif zona == "Girona":
        poblacio = st.selectbox("Població", ["", "Aiguaviva", "Anglès", "Begur", "Besalú", "la Bisbal d'Empordà", "Castelló d'Empúries", 
                                             "Cassà de la Selva", "Figueres", "Llagostera", "Planoles", "Ribes de Freser",
                                               "Ripoll", "Rupià", "Sant Feliu de Guíxols", "Santa Cristina d'Aro", "Sant Hilari Sacalm", 
                                               "Sant Joan de les Abadesses", "Sant Llorenç de la Muga", " Sant Miquel de Campmajor", "Terrades", "..." ])
    else:
        st.markdown("<div style='background-color:pink; padding:10px; color:black; font-size:18px;'><b>No hi ha informació disponible de la teva zona</b></div>", unsafe_allow_html=True)


    mes = st.selectbox("Mes", ["", "Gener", "Febrer", "Març", "Abril", "Maig", "Juny", 
                                             "Juliol", "Agost", "Setembre", "Octubre", "Novembre",
                                               "Desembre"])

    data = pd.read_csv("dades2.csv")
    data2 = pd.read_csv("dades3.csv")

    if poblacio != "" and mes != "":
        data['Dia'] = pd.to_datetime(data['Dia'], format='%d-%m').apply(lambda x: x.replace(year=2023))
        data['Dia'] = data['Dia'].dt.strftime('%Y-%m-%d')

        chart = alt.Chart(data).mark_line(point=True).encode(
        x=alt.X('Dia:T', axis=alt.Axis(labelAngle=45)),  
        y='Consultes:Q',
        tooltip=['Dia:T', 'Consultes:Q']).properties(width=600,height=300, title=f"Consultes al Cap de {poblacio} el mes de {mes}")


        chart2 = alt.Chart(data2).mark_arc(innerRadius=50).encode(
        theta="Consultes",
        color="Diagnòstic:N",).properties(title=f"Diagnòstics al Cap de {poblacio} el mes de {mes}")

        chart | chart2
    

        municipi, municipi2 = st.columns(2)

        with municipi:
            st.write(f"## {poblacio}")
            st.markdown("<span style='color:blue'>Dades extretes la pàgina web de l'ajuntament.</span>", unsafe_allow_html=True)
            st.write("PROVÍNCIA: Barcelona")
            st.write("COMARCA: El Baix Llobregat")
            st.write("NOMBRE D'HABITANTS: 65.609  habitants (a 1 de gener de 2023, segons el padró d'habitants municipal)")
            st.write("SUPERFÍCIE: 32,23 km2")
            st.write("ALTITUD MÀXIMA: 5m (a la plaça de la vila)")

            st.write("### Ciutats germanes")
            st.write("Garrovillas de Alconétar (Cáceres), Gibara (Cuba), Kukra Hill (Nicaragua), Fingal (Irlanda)")

        with municipi2:
            st.write("### El clima")
            st.write("El clima del Prat és el característic del domini marítim mediterrani, amb estius calorosos i hiverns temperats i relativament humits.")
            st.write("TEMPERATURA MITJANA ANUAL: 15,6 ºC")
            st.write("TEMPERATURA MITJANA ANUAL MÍNIMA: 11,3 ºC")
            st.write("TEMPERATURA MITJANA ANUAL MÀXIMA: 19,8 ºC")
            st.write("PRECIPITACIÓ MITJANA ANUAL: Al voltant dels 600mm, però amb oscil·lacions notables.")

def analisi_ambiental(zona):
    st.write(f"## Informació de les estacions de contaminació ambiental de la zona {zona}")
    if zona == "Metropolitana Sud":
        poblacio2 = st.selectbox("Població", ["", "Argençola", "Bellprat", "el Bruc", "Cabrera d'Anoia", "Capellades", "Carme", 
                                             "Castellolí", "El Prat de Llobregat", "els Hostalets de Pierola", "Igualada", "Masquefa", "Montmaneu",
                                               "Òdena", "Piera", "Santa Margarida de Montbui", "Vilanova del Camí", "Avinyonet del Penedès", 
                                               "Gelida", "Mediona", "Olèrdola", "Sant Pere de Riudebitlles", "..." ])
    elif zona == "Girona":
        poblacio2 = st.selectbox("Població", ["", "Aiguaviva", "Anglès", "Begur", "Besalú", "la Bisbal d'Empordà", "Castelló d'Empúries", 
                                             "Cassà de la Selva", "Figueres", "Llagostera", "Planoles", "Ribes de Freser",
                                               "Ripoll", "Rupià", "Sant Feliu de Guíxols", "Santa Cristina d'Aro", "Sant Hilari Sacalm", 
                                               "Sant Joan de les Abadesses", "Sant Llorenç de la Muga", " Sant Miquel de Campmajor", "Terrades", "..." ])
    else:
        st.markdown("<div style='background-color:pink; padding:10px; color:black; font-size:18px;'><b>No hi ha informació disponible de la teva zona</b></div>", unsafe_allow_html=True)


    if poblacio2 != "":
        col1, col2 = st.columns(2)
        with col1:
            st.write("NOM DE L'ESTACIÓ: El Prat de LLobregat - Sagnier, Barcelona")
        with col2:    
            st.write("UBICACIÓ DE L'ESTACIÓ: Complex Esportiu Municipal Sagnier. Carrer de Frederica Montseny, El Prat De Llobregat. 08820 Barcelona")


        data = {"Nivell de contaminació de l'aire": ["Bo"], "Índex de qualitat de l'aire (IQA)": [17], "Contaminant principal": ["O3"]}
        df_custom = pd.DataFrame(data)

        st.table(df_custom)

def informes(zona):
    st.write("## Informes estàtics")
    st.selectbox("Temporalitat", ["", "Resum mes anterior", "Resum quinzena anterior", "Informe avui", "A 7 dies vista"])
    if zona == "Metropolitana Sud":
        poblacio = st.selectbox("Població", ["", "Argençola", "Bellprat", "el Bruc", "Cabrera d'Anoia", "Capellades", "Carme", 
                                             "Castellolí", "els Hostalets de Pierola", "Igualada", "Masquefa", "Montmaneu",
                                               "Òdena", "Piera", "Santa Margarida de Montbui", "Vilanova del Camí", "Avinyonet del Penedès", 
                                               "Gelida", "Mediona", "Olèrdola", "Sant Pere de Riudebitlles", "..." ])
        st.download_button(f"Informe {poblacio}", data="hola aixo es una prova", file_name="Informe")
    elif zona == "Girona":
        poblacio = st.selectbox("Població", ["", "Aiguaviva", "Anglès", "Begur", "Besalú", "la Bisbal d'Empordà", "Castelló d'Empúries", 
                                             "Cassà de la Selva", "Figueres", "Llagostera", "Planoles", "Ribes de Freser",
                                               "Ripoll", "Rupià", "Sant Feliu de Guíxols", "Santa Cristina d'Aro", "Sant Hilari Sacalm", 
                                               "Sant Joan de les Abadesses", "Sant Llorenç de la Muga", " Sant Miquel de Campmajor", "Terrades", "..." ])
        st.download_button(f"Informe {poblacio}", data= "hola aixo es una prova", file_name="Informe")
    else:
        st.markdown("<div style='background-color:pink; padding:10px; color:black; font-size:18px;'><b>No hi ha informes disponibles a la teva zona</b></div>", unsafe_allow_html=True)

def compte(username, role):
    st.write("## Informació del compte")
    st.write(f"Usuari: {username}")
    st.write(f"Rol: {role}")

    if st.button("Canvi de contrasenya"):
        st.text_input("Contrasenya antiga", type="password")
        st.text_input("Contrasenya nova", type="password")
    
    st.write("### Subscripció")
    st.selectbox("Mètode de descripció", ["Subscripció trimestral completa", "Subscripció trimestral parcial", "Subscripció mensual"])
    st.write("Data d'alta: dd/mm/aaaa")
    st.write("Data d'expiració de subscripció: dd/mm/aaaa")
    st.selectbox("Mètode de pagament", ["VISA", "Apple Pay", "Google Pay"])
    st.write("Targeta vinculada: **** **** **** *123")


def mapa(zona):
    image_sud = Image.open('sud.png')
    if zona == "Metropolitana Sud":
        st.image(image_sud, caption="Alertes zona Metropolitana Sud")
    else:
        st.markdown("<span style='color:red'>Mapa no disponible</span>", unsafe_allow_html=True)


if __name__ == "__main__":
    main()
