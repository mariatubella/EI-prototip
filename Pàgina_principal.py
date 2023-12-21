import streamlit as st
from PIL import Image

def main():
    st.title("PAD.ai : MODELS PREDICTIUS PER A LA GESTIÓ DE RECURSOS MÈDICS")

    logo = Image.open('Logo.png')
    st.image(logo)

if __name__ == "__main__":
    main()