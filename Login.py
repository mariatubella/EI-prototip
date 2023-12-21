import streamlit as st
from PIL import Image
import pandas as pd
import altair as alt

logo = Image.open('Logo.png')


st.set_page_config(
    page_title = "Salut i medi ambient",
    page_icon = logo,
    layout = "wide",
    initial_sidebar_state = "expanded"
)

class PageManager():
    def __init__(self, username, password):
        self.username, self.password = username, password
        self.zona = "Metropolitana Sud"
        self.temporary = []

        if 'curr_page' not in st.session_state:
            st.session_state['curr_page'] = None

    def main_page(self):
        text1 = st.empty()
        text1.write(f"### Hola {self.username}!")
        self.temporary.append(text1)

        text2 = st.empty()
        text2.write(f"### Aquestes son les alertes a la zona {self.zona}:")
        self.temporary.append(text2)

        self.temporary.append(alertes(self.zona))

    def map_page(self):
        self.temporary.append(mapa(self.zona))
    
    def history_page(self):
        for el in historial(self.zona):
            self.temporary.append(el)
    
    def reports_page(self):
        for el in informes(self.zona):
            self.temporary.append(el)
    
    def an_san_page(self):
        for el in analisi(self.zona):
            self.temporary.append(el)
    
    def an_amb_page(self):
        for el in analisi_ambiental(self.zona):
            self.temporary.append(el)
    
    def profile_page(self):
        for el in compte(self.username, "Administració"):
            self.temporary.append(el)

    def reset_page(self):
        for el in self.temporary:
            el.empty()

        self.temporary = []

    def change_to(self, new_page):
        self.reset_page()
        st.session_state['curr_page'] = new_page
        bar = st.empty()
        bar.markdown("---")
        self.temporary.append(bar)
        if new_page == "main":
            self.main_page()
        elif new_page == "map":
            self.map_page()
        elif new_page == "history":
            self.history_page()
        elif new_page == "reports":
            self.reports_page()
        elif new_page == "an_san":
            self.an_san_page()
        elif new_page == "an_amb":
            self.an_amb_page()
        elif new_page == "profile":
            self.profile_page()
        else:
            raise ValueError(f"The page {new_page} doesn't exist.")

def main():

    st.sidebar.image(logo)

    # Add a sidebar with page selection
    # role = st.sidebar.selectbox("Quin és el teu rol?", ["", "Administració", "Personal sanitari"])
    # zona = st.sidebar.selectbox("A quina regió treballes?", ["", "Metropolitana Sud", "Metropolitana Nord", "Barcelona",
    #                                                          "Girona", "Catalunya central", "LLeida", "Alt pirineu - Aran",
    #                                                          "Tarragona", "Terres de l'Ebre"])

    username_input = st.empty()
    pass_input = st.empty()
    username = username_input.text_input("Usuari")
    password = pass_input.text_input("Contrasenya", type="password")

    if password == "maria":
        username_input.empty()
        pass_input.empty()
        
        manager = PageManager(username, password)

        col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
        if col1.button("Pàgina principal", type="primary") or st.session_state['curr_page'] == "main":
            manager.change_to("main")
        if col2.button("Mapa de la zona", type="primary") or st.session_state['curr_page'] == "map":
            manager.change_to("map")
        if col3.button("Historial recent", type="primary") or st.session_state['curr_page'] == "history":
            manager.change_to("history")
        if col4.button("Informes generats", type="primary") or st.session_state['curr_page'] == "reports":
            manager.change_to("reports")
        if col5.button("Anàlisi sanitari", type="primary") or st.session_state['curr_page'] == "an_san":
            manager.change_to("an_san")
        if col6.button("Anàlisi ambiental", type="primary") or st.session_state['curr_page'] == "an_amb":
            manager.change_to("an_amb")
        if col7.button("Perfil d'usuari", type="primary") or st.session_state['curr_page'] == "profile":
            manager.change_to("profile")

        if st.session_state['curr_page'] is None:
            manager.main_page()
    
    elif password != "maria" and password != "":
        st.markdown("<span style='color:red'>Credencials incorrectes</span>", unsafe_allow_html=True)



def alertes(zona):
    alerta = st.empty()
    if zona == "Metropolitana Sud":
        alerta.markdown("<div style='background-color:red; padding:10px; color:white; font-size:18px;'><b>Alta incidència prevista a Torrelles de Llobregat fins 17/12/2023</b></div>", unsafe_allow_html=True)
    elif zona == "Girona":
        alerta.markdown("<div style='background-color:red; padding:10px; color:white; font-size:18px;'><b>Alta incidència prevista a Banyoles fins 22/12/2023</b></div>", unsafe_allow_html=True)
    else:
        alerta.markdown("<div style='background-color:red; padding:10px; color:white; font-size:18px;'><b>No hi ha cap alerta a la teva zona</b></div>", unsafe_allow_html=True)
    return alerta


def historial(zona):
    el1, el2, el3, el4 = st.empty(), st.empty(), st.empty(), st.empty()
    el1.write(f"### Historial de la regió sanitària {zona}")
    
    if zona == "Metropolitana Sud":
        el2.markdown("<div style='background-color:pink; padding:10px; color:black; font-size:18px;'><b>Alta incidència a Castelldefels fins 17/11/2023</b></div>", unsafe_allow_html=True)
        el3.markdown("<div style='background-color:pink; padding:10px; color:black; font-size:18px;'><b>Alta incidència al Prat de Llobregat fins 5/11/2023</b></div>", unsafe_allow_html=True)
        el4.markdown("<div style='background-color:pink; padding:10px; color:black; font-size:18px;'><b>Alta incidència a Begues fins 30/10/2023</b></div>", unsafe_allow_html=True)

    elif zona == "Girona":
        el2.markdown("<div style='background-color:pink; padding:10px; color:black; font-size:18px;'><b>Alta incidència a Figueres fins 22/11/2023</b></div>", unsafe_allow_html=True)
        el3.markdown("<div style='background-color:pink; padding:10px; color:black; font-size:18px;'><b>Alta incidència a Girona fins 11/11/2023</b></div>", unsafe_allow_html=True)
        el4.markdown("<div style='background-color:pink; padding:10px; color:black; font-size:18px;'><b>Alta incidència a Santa Coloma de Farners fins 2/11/2023</b></div>", unsafe_allow_html=True)

    else:
        el2.markdown("<div style='background-color:pink; padding:10px; color:black; font-size:18px;'><b>No hi ha cap alerta a la teva zona</b></div>", unsafe_allow_html=True)
    
    return [el1, el2, el3, el4]

def analisi(zona):
    elements = [st.empty() for _ in range(4)]

    if zona == "Metropolitana Sud":
        poblacio = elements[0].selectbox("Població", ["", "Argençola", "Bellprat", "el Bruc", "Cabrera d'Anoia", "Capellades", "Carme", 
                                             "Castellolí", "El Prat de Llobregat", "els Hostalets de Pierola", "Igualada", "Masquefa", "Montmaneu",
                                               "Òdena", "Piera", "Santa Margarida de Montbui", "Vilanova del Camí", "Avinyonet del Penedès", 
                                               "Gelida", "Mediona", "Olèrdola", "Sant Pere de Riudebitlles", "..." ])
    elif zona == "Girona":
        poblacio = elements[0].selectbox("Població", ["", "Aiguaviva", "Anglès", "Begur", "Besalú", "la Bisbal d'Empordà", "Castelló d'Empúries", 
                                             "Cassà de la Selva", "Figueres", "Llagostera", "Planoles", "Ribes de Freser",
                                               "Ripoll", "Rupià", "Sant Feliu de Guíxols", "Santa Cristina d'Aro", "Sant Hilari Sacalm", 
                                               "Sant Joan de les Abadesses", "Sant Llorenç de la Muga", " Sant Miquel de Campmajor", "Terrades", "..." ])
    else:
        elements[0].markdown("<div style='background-color:pink; padding:10px; color:black; font-size:18px;'><b>No hi ha informació disponible de la teva zona</b></div>", unsafe_allow_html=True)


    mes = elements[1].selectbox("Mes", ["", "Gener", "Febrer", "Març", "Abril", "Maig", "Juny", 
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

        elements[2].altair_chart(chart | chart2)
    

        municipi, municipi2 = elements[3].columns(2)

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

    return elements

def analisi_ambiental(zona):
    elements = [st.empty() for _ in range(4)]

    elements[0].write(f"## Informació de les estacions de contaminació ambiental de la zona {zona}")
    if zona == "Metropolitana Sud":
        poblacio2 = elements[1].selectbox("Població", ["", "Argençola", "Bellprat", "el Bruc", "Cabrera d'Anoia", "Capellades", "Carme", 
                                             "Castellolí", "El Prat de Llobregat", "els Hostalets de Pierola", "Igualada", "Masquefa", "Montmaneu",
                                               "Òdena", "Piera", "Santa Margarida de Montbui", "Vilanova del Camí", "Avinyonet del Penedès", 
                                               "Gelida", "Mediona", "Olèrdola", "Sant Pere de Riudebitlles", "..." ])
    elif zona == "Girona":
        poblacio2 = elements[1].selectbox("Població", ["", "Aiguaviva", "Anglès", "Begur", "Besalú", "la Bisbal d'Empordà", "Castelló d'Empúries", 
                                             "Cassà de la Selva", "Figueres", "Llagostera", "Planoles", "Ribes de Freser",
                                               "Ripoll", "Rupià", "Sant Feliu de Guíxols", "Santa Cristina d'Aro", "Sant Hilari Sacalm", 
                                               "Sant Joan de les Abadesses", "Sant Llorenç de la Muga", " Sant Miquel de Campmajor", "Terrades", "..." ])
    else:
        elements[1].markdown("<div style='background-color:pink; padding:10px; color:black; font-size:18px;'><b>No hi ha informació disponible de la teva zona</b></div>", unsafe_allow_html=True)


    if poblacio2 != "":
        col1, col2 = elements[2].columns(2)
        with col1:
            st.write("NOM DE L'ESTACIÓ: El Prat de LLobregat - Sagnier, Barcelona")
        with col2:    
            st.write("UBICACIÓ DE L'ESTACIÓ: Complex Esportiu Municipal Sagnier. Carrer de Frederica Montseny, El Prat De Llobregat. 08820 Barcelona")


        data = {"Nivell de contaminació de l'aire": ["Bo"], "Índex de qualitat de l'aire (IQA)": [17], "Contaminant principal": ["O3"]}
        df_custom = pd.DataFrame(data)

        elements[3].table(df_custom)

    return elements

def informes(zona):
    elements = [st.empty() for _ in range(4)]
    elements[0].write("## Informes estàtics")
    elements[1].selectbox("Temporalitat", ["", "Resum mes anterior", "Resum quinzena anterior", "Informe avui", "A 7 dies vista"])
    if zona == "Metropolitana Sud":
        poblacio = elements[2].selectbox("Població", ["", "Argençola", "Bellprat", "el Bruc", "Cabrera d'Anoia", "Capellades", "Carme", 
                                             "Castellolí", "els Hostalets de Pierola", "Igualada", "Masquefa", "Montmaneu",
                                               "Òdena", "Piera", "Santa Margarida de Montbui", "Vilanova del Camí", "Avinyonet del Penedès", 
                                               "Gelida", "Mediona", "Olèrdola", "Sant Pere de Riudebitlles", "..." ])
        elements[3].download_button(f"Informe {poblacio}", data="hola aixo es una prova", file_name="Informe")
    elif zona == "Girona":
        poblacio = elements[2].selectbox("Població", ["", "Aiguaviva", "Anglès", "Begur", "Besalú", "la Bisbal d'Empordà", "Castelló d'Empúries", 
                                             "Cassà de la Selva", "Figueres", "Llagostera", "Planoles", "Ribes de Freser",
                                               "Ripoll", "Rupià", "Sant Feliu de Guíxols", "Santa Cristina d'Aro", "Sant Hilari Sacalm", 
                                               "Sant Joan de les Abadesses", "Sant Llorenç de la Muga", " Sant Miquel de Campmajor", "Terrades", "..." ])
        elements[3].download_button(f"Informe {poblacio}", data= "hola aixo es una prova", file_name="Informe")
    else:
        elements[4].markdown("<div style='background-color:pink; padding:10px; color:black; font-size:18px;'><b>No hi ha informes disponibles a la teva zona</b></div>", unsafe_allow_html=True)
    
    return elements

def compte(username, role):
    elements = [st.empty() for _ in range(12)]
    elements[0].write("## Informació del compte")
    elements[1].write(f"Usuari: {username}")
    elements[2].write(f"Rol: {role}")

    if elements[3].button("Canvi de contrasenya"):
        elements[4].text_input("Contrasenya antiga", type="password")
        elements[5].text_input("Contrasenya nova", type="password")
    
    elements[6].write("### Subscripció")
    elements[7].selectbox("Mètode de descripció", ["Subscripció trimestral completa", "Subscripció trimestral parcial", "Subscripció mensual"])
    elements[8].write("Data d'alta: dd/mm/aaaa")
    elements[9].write("Data d'expiració de subscripció: dd/mm/aaaa")
    elements[10].selectbox("Mètode de pagament", ["VISA", "Apple Pay", "Google Pay"])
    elements[11].write("Targeta vinculada: **** **** **** *123")

    return elements


def mapa(zona):
    mapa = st.empty()
    image_sud = Image.open('sud.png')
    if zona == "Metropolitana Sud":
        mapa.image(image_sud, caption="Alertes zona Metropolitana Sud")
    else:
        mapa.markdown("<span style='color:red'>Mapa no disponible</span>", unsafe_allow_html=True)
    
    return mapa


if __name__ == "__main__":
    main()
