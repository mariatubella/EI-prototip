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
        if col5.button("Anàlisi sanitària", type="primary") or st.session_state['curr_page'] == "an_san":
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
    alerta1, alerta2 = st.empty(), st.empty()
    if zona == "Metropolitana Sud":
        alerta1.markdown("<div style='background-color:red; padding:10px; color:white; font-size:18px;'><b>El Prat de Llobregat: alta incidència d'asma prevista fins el 29/12/2023</b></div>", unsafe_allow_html=True)
        alerta2.markdown("<div style='background-color:red; padding:10px; color:white; font-size:18px;'><b>El Prat de Llobregat: nivell moderat de contaminació els dies 28 i 29 de desembre</b></div>", unsafe_allow_html=True)

    elif zona == "Girona":
        alerta1.markdown("<div style='background-color:red; padding:10px; color:white; font-size:18px;'><b>Alta incidència prevista a Banyoles fins 22/12/2023</b></div>", unsafe_allow_html=True)
    else:
        alerta1.markdown("<div style='background-color:red; padding:10px; color:white; font-size:18px;'><b>No hi ha cap alerta a la teva zona</b></div>", unsafe_allow_html=True)
    return [alerta1, alerta2]


def historial(zona):
    el1, el2, el3, el4 = st.empty(), st.empty(), st.empty(), st.empty()
    el1.write(f"### Historial de la regió sanitària {zona}")
    
    if zona == "Metropolitana Sud":
        el2.markdown("<div style='background-color:pink; padding:10px; color:black; font-size:18px;'><b>Alta incidència d'asma a Castelldefels del 9/11/2023 fins el 17/11/2023</b></div>", unsafe_allow_html=True)
        el3.markdown("<div style='background-color:pink; padding:10px; color:black; font-size:18px;'><b>Alta incidència d'asma al Prat de Llobregat del 30/10/2023 fins el 5/11/2023</b></div>", unsafe_allow_html=True)
        el4.markdown("<div style='background-color:pink; padding:10px; color:black; font-size:18px;'><b>Nivell moderat de contaminació a Begues del 24/10/2023 fins el 30/10/2023</b></div>", unsafe_allow_html=True)

    elif zona == "Girona":
        el2.markdown("<div style='background-color:pink; padding:10px; color:black; font-size:18px;'><b>Alta incidència de bronquitis a Figueres del 18/11/2023 fins el 22/11/2023</b></div>", unsafe_allow_html=True)
        el3.markdown("<div style='background-color:pink; padding:10px; color:black; font-size:18px;'><b>Nivell moderat de contaminació a Girona del 2/11/2023 fins el 10/11/2023</b></div>", unsafe_allow_html=True)
        el4.markdown("<div style='background-color:pink; padding:10px; color:black; font-size:18px;'><b>Alta incidència d'asma a Santa Coloma de Farners del 18/11/2023 fins el 2/11/2023</b></div>", unsafe_allow_html=True)

    else:
        el2.markdown("<div style='background-color:pink; padding:10px; color:black; font-size:18px;'><b>No hi ha cap alerta a la teva zona</b></div>", unsafe_allow_html=True)
    
    return [el1, el2, el3, el4]

def analisi(zona):
    elements = [st.empty() for _ in range(6)]

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
    data4 = pd.read_csv("dades4.csv")
    data5 = pd.read_csv("grafic4.csv")

    if poblacio != "" and mes != "":
        st.sidebar.write("### Informació del municipi: El Prat de LLobregat")
        st.sidebar.write("PROVÍNCIA: Barcelona")
        st.sidebar.write("COMARCA: El Baix Llobregat")
        st.sidebar.write("NOMBRE D'HABITANTS: 65.609  habitants (a 1 de gener de 2023)")
        st.sidebar.write("SUPERFÍCIE: 32,23 km2")
        st.sidebar.write("ALTITUD MÀXIMA: 5m (a la plaça de la vila)")
        st.sidebar.write("TEMPERATURA MITJANA ANUAL: 15,6 ºC")

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
    
        elements[3].write("## Predicció de l'impacte en el mes de març")

        col1, col2 = elements[4].columns(2)
        with col1:
            chart4 = (alt.Chart(data4).mark_line(point=True).encode(
                x=alt.X("Dia:N", axis=alt.Axis(labelAngle=0)), 
                y="Consultes:Q", 
                color="Mes:N")
                ).properties(width=600,height=300, title="Comparació del nombre de consultes del febrer amb les previstes al març")
            chart4
        
        with col2:
            st.write(" ")
            st.write(" ")
            st.write("Nombre de consultes al mes de febrer: n")
            st.write("Nombre de consultes previstes pel mes de març: m")
            st.write("Increment de casos: x %")
        
        chart5 = alt.Chart(data5).mark_bar().encode(
        x=alt.X('Prob:Q', axis=alt.Axis(labelAngle=45), scale=alt.Scale(domain=[0,1])),  
        y='Malaltia:N',
        tooltip=['Malaltia:N', 'Prob:N', 'Qualitat:N']).properties(width=400,height=300, title="Probabilitat d'hospitalització de malalties respiratòries")

        elements[5].altair_chart(chart5)


    return elements

def analisi_ambiental(zona):
    elements = [st.empty() for _ in range(11)]
    st.sidebar.write("### Llegenda per a la qualitat de l'aire")
    st.sidebar.write("0 - 50: Bona")
    st.sidebar.write("51 - 100: Moderada")
    st.sidebar.write("101 - 150: Moderada grups sensibles")
    st.sidebar.write("151 - 200: Poc saludable")
    st.sidebar.write("201 - 300: Molt poc saludable")
    st.sidebar.write("301 - 500: Perillós per a la salut")

    elements[0].write(f"## Informació de les estacions de contaminació ambiental de la zona {zona}")
    if zona == "Metropolitana Sud":
        poblacio2 = elements[1].selectbox("Població", ["", "Argençola", "Bellprat", "el Bruc", "Cabrera d'Anoia", "Capellades", "Carme", 
                                             "Castellolí", "El Prat de Llobregat", "els Hostalets de Pierola", "Igualada", "Masquefa", "Montmaneu",
                                               "Òdena", "Piera", "Santa Margarida de Montbui", "Vilanova del Camí", "Avinyonet del Penedès", 
                                               "Gelida", "Mediona", "Olèrdola", "Sant Pere de Riudebitlles", "..." ])
    
    else:
        elements[1].markdown("<div style='background-color:pink; padding:10px; color:black; font-size:18px;'><b>No hi ha informació disponible de la teva zona</b></div>", unsafe_allow_html=True)


    if poblacio2 != "":
        col1, col2 = elements[2].columns(2)
        with col1:
            st.write("### El Prat de Llobregat (Sagnier)")
            st.write("NOM DE L'ESTACIÓ: El Prat de LLobregat (Sagnier)")
            st.write("MUNICIPI: El Prat de Llobregat")
            st.write("ADREÇA POSTAL: Carrer de Frederica Montseny, s/n")
            st.write("COORDENADES UTM(m): 41.321774, 2.0821")
            st.write("ALTITUD (m): 7")
            st.write("DATA INSTAL·LACIÓ: 01/02/2011")
            st.write("ZQA: Àrea de Barcelona")

        with col2:
            st.write("### El Prat de Llobregat (Jardins de la Pau)")    
            st.write("NOM DE L'ESTACIÓ: El Prat de LLobregat (Jardins de la Pau)")
            st.write("MUNICIPI: El Prat de Llobregat")
            st.write("ADREÇA POSTAL: Carrer de Tarragona, 16")
            st.write("COORDENADES UTM(m): 41.321487, 2.0977015")
            st.write("ALTITUD (m): 5")
            st.write("DATA INSTAL·LACIÓ: 01/12/2009")
            st.write("ZQA: Àrea de Barcelona")


        elements[3].write("### Dades d'avui a l'estació El Prat de Llobregat (Sagnier)")
        estacio1 = pd.read_csv("estacio1.csv")
        est1 = pd.DataFrame(estacio1)
        elements[4].table(est1)

        elements[5].write("### Dades d'avui a l'estació El Prat de Llobregat (Jardins de la Pau)")
        estacio2 = pd.read_csv("estacio2.csv")
        est2 = pd.DataFrame(estacio2)
        elements[6].table(est2)

        grafic1 = pd.read_csv("grafic1.csv")
        grafic1['Dia'] = pd.to_datetime(grafic1['Dia'], format='%d-%m').apply(lambda x: x.replace(year=2023))
        grafic1['Dia'] = grafic1['Dia'].dt.strftime('%Y-%m-%d')

        chart3 = alt.Chart(grafic1).mark_bar().encode(
        x=alt.X('Dia:T', axis=alt.Axis(labelAngle=45)),  
        y='IQA:Q',
        tooltip=['Dia:T', 'IQA:Q', 'Qualitat:N']).properties(width=300,height=300, title="IQA al Prat setmana del 17 al 23 de desembre")
        
        grafic2 = pd.read_csv("grafic2.csv")
        grafic2['Dia'] = pd.to_datetime(grafic2['Dia'], format='%d-%m').apply(lambda x: x.replace(year=2023))
        grafic2['Dia'] = grafic2['Dia'].dt.strftime('%Y-%m-%d')

        chart4 = alt.Chart(grafic2).mark_bar().encode(
        x=alt.X('Dia:T', axis=alt.Axis(labelAngle=45)),  
        y='O3:Q',
        tooltip=['Dia:T', 'O3:Q', 'Qualitat:N']).properties(width=300,height=300, title="Micrograms/m3 d'O3 al Prat setmana del 17 al 23 de desembre")

        grafic3 = pd.read_csv("grafic3.csv")
        grafic3['Dia'] = pd.to_datetime(grafic3['Dia'], format='%d-%m').apply(lambda x: x.replace(year=2023))
        grafic3['Dia'] = grafic3['Dia'].dt.strftime('%Y-%m-%d')

        chart5 = alt.Chart(grafic3).mark_bar().encode(
        x=alt.X('Dia:T', axis=alt.Axis(labelAngle=45)),  
        y='NO2:Q',
        tooltip=['Dia:T', 'NO2:Q', 'Qualitat:N']).properties(width=300,height=300, title="Micrograms/m3 d'NO2 al Prat setmana del 17 al 23 de desembre")

        
        elements[7].altair_chart(chart3 | chart4 | chart5)

        elements[8].write("### Pronòstic al Prat de Llobregat (predicció setmana 23-29 de desembre)")
        pronostic = pd.read_csv("pronostic.csv")
        pron = pd.DataFrame(pronostic)
        elements[9].table(pron)

        elements[10].markdown("<span style='color:blue'>Dades extretes de https://mediambient.gencat.cat/ca/05_ambits_dactuacio/atmosfera/qualitat_de_laire/vols-saber-que-respires/ i https://www.iqair.com/es/spain/catalunya/barcelona/prat-llobregat-sagnier.</span>", unsafe_allow_html=True)


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
    elements = [st.empty() for _ in range(11)]
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
    elements[10].write("Nombre de llicències contractades: X")

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
