import streamlit as st
import pandas as pd
import os
from src.lstm_model import load_lstm
from src.seed import genera_semilla
from src.prediccion import generar_notas
from src.midi_file import dataframe_a_midi, midi_to_wav
from autores import composer_files

# Reconocimiento al autor
st.markdown("""
        ---
        **Página y modelo creados por**: Ariel Flores Santacruz
        """)
st.title("Generador de Música con LSTM 🎶")

# Contenedor para la explicación
with st.container():
    st.header("Generación de Música de Autores Clásicos ✨")
    st.write("""
        Bienvenido a mi aplicación, donde generaremos música basada en compositores clásicos como 
        Beethoven, Debussy, entre otros. Utilizamos una **Red Neuronal de Memoria a Largo Plazo (LSTM)**, que es un 
        tipo de red neuronal recurrente (RNN) diseñada para aprender de secuencias temporales.
    """)

    st.subheader("❓ ¿Qué es una LSTM?")
    st.write("""
        Las LSTM (Long Short-Term Memory) son un tipo de red neuronal diseñada para recordar información a 
        largo plazo y gestionar secuencias de datos, utilizando puertas para decidir qué información conservar 
        o eliminar, lo que las hace ideales para aplicaciones como la generación de música.
    """)

    

st.subheader("Genera Tu Musica")
composers = list(composer_files.keys())  
selected_composer = st.selectbox("Selecciona un compositor:", composers, index=None)

# Verificar si hay un compositor seleccionado
if selected_composer:
    st.write(f"Música generada basada en el estilo de {selected_composer}.")

    # Asegurarse de que la semilla esté en session_state
    if 'semilla' not in st.session_state:
        st.session_state.semilla = pd.DataFrame()

    # Botón para generar la semilla
    if st.button("Generar Semilla"):
        st.session_state.semilla = genera_semilla(selected_composer)
        st.success('Se ha generado una Semilla correctamente', icon="✅")

    # Comprobar si la semilla está vacía
    if st.session_state.semilla.empty:
        st.info('Genere una Semilla', icon="ℹ️")
    else:
        try:
            model = load_lstm()
            st.write("""
                        El valor de la temperatura indica el nivel de creatividad en la generación musical. 
                        Un valor cercano a 1 resulta en composiciones más realistas y coherentes, pero con menos
                        originalidad. A medida que aumentas la temperatura, las composiciones se vuelven más creativas
                        y variadas, aunque pueden alejarse un poco de la realidad musical.
                     """)
            
            # Crear el select_slider para seleccionar la temperatura
            temperatura = st.select_slider(
                "Selecciona La Temperatura",
                options=list(range(1, 6))
            )
            # Botón para generar la predicción
            bandera = False
            if st.button('Generar predicción'):
                with st.spinner('Generando predicciones...'):
                    predicciones = generar_notas(model, st.session_state.semilla, temperatura)
                    dataframe_a_midi(predicciones,'midi/prediccion.mid')
                    midi_to_wav('midi/prediccion.mid','midi/prediccion.wav')
                    bandera = True
                    st.success('Predicciones generadas exitosamente', icon="🎶")

            if bandera:
                st.audio('midi/prediccion.wav', format="audio/wav")

        except Exception as e:
            st.error(f'Ocurrió un error: {e}', icon="⚠️")


    st.markdown("""
        --- 
        **Página y modelo creados por**: Ariel Flores Santacruz
        """)   
    

        

    
