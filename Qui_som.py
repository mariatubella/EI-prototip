import streamlit as st

st.sidebar.write("### Mails de contacte")
st.sidebar.write("albert.fugardo@estudiantat.upc.edu")
st.sidebar.write("marc.franquesa@estudiantat.upc.edu")
st.sidebar.write("maria.risques@estudiantat.upc.edu")
st.sidebar.write("maria.tubella@estudiantat.upc.edu")
st.sidebar.write("mauro.filomeno@estudiantat.upc.edu")

st.sidebar.write("### Telèfon de contacte")
st.sidebar.write("+34 111 11 11 11")

st.markdown("# PAD.ai")
st.write("PAD.ai (Pollution and Diseases) és una nova iniciativa que hem tirat endavant cinc estudiants de la UPC especialitzats en Ciència i Enginyeria de Dades. Col·laborem amb ciutadans, serveis mèdics i organismes públics, desenvolupant algoritmes preventius que alerten sobre problemes de salut i contaminació.")

st.write("### Autors")
st.write("Albert Fugardo, Marc Franquesa, Maria Risques, Maria Tubella i Mauro Filomeno")

if st.button("### Contacta amb nosaltres"):
    st.text_input("Nom")
    st.text_input("Adreça de correu")
    st.text_input("Empresa/Organització")
    st.text_area("Missatge")