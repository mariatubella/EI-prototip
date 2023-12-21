import streamlit as st
from PIL import Image

logo = Image.open('Logo.png')
st.sidebar.image(logo)

st.sidebar.write("### Mail de contacte")
st.sidebar.write("pad.ai@gmail.com")

st.sidebar.write("### Telèfon de contacte")
st.sidebar.write("+34 111 11 11 11")

st.markdown("# PAD.ai")
st.write("PAD.ai (Pollution and Diseases) és una nova iniciativa que hem tirat endavant cinc estudiants de la UPC especialitzats en Ciència i Enginyeria de Dades. Col·laborem amb ciutadans, serveis mèdics i organismes públics, desenvolupant algoritmes preventius que alerten sobre problemes de salut i contaminació.")

st.markdown("# Sobre aquesta plataforma")
st.write('''Aquesta plataforma té com a principal objectiu mostrar de manera interactiva l'actual situació de certs municipies, tant pel que fa a la qualitat mediambiental
         com per diferents aspectes referents a la incidència en centres de salut. La informació que es dona és proveïda per dos principals fonts: dades mèdiques de l'ICS i 
          dades ambientals aconseguides de diferents estacions metereològiques. D'aquesta manera mostrem certa relació que podria existir entre aquests factors.''')

st.write("### Autors")
st.write("Albert Fugardo, Marc Franquesa, Maria Risques, Maria Tubella i Mauro Filomeno")

if st.button("### Contacta amb nosaltres"):
    st.text_input("Nom")
    st.text_input("Adreça de correu")
    st.text_input("Empresa/Organització")
    st.text_area("Missatge")