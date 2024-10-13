import numpy as np
import pandas as pd
import tensorflow as tf
from typing import Tuple

def predecir_siguiente_nota(notas: np.ndarray, modelo_keras: tf.keras.Model, 
                            temperatura: float) -> Tuple[int,float,float]:
    """Genera una predicción de notas utilizando un modelo de secuencia entrenado.

    Args:
        notas (np.ndarray): Un array de notas (pitch) que se utilizarán como entrada
                           para el modelo.
        modelo_keras (tf.keras.Model): El modelo Keras entrenado que se utilizará 
                                       para hacer las predicciones.
        temperatura (float): Controla la aleatoriedad de las predicciones. 
                             Un valor más bajo resultará en predicciones más conservadoras,
                             mientras que un valor más alto generará predicciones más 
                             variadas y creativas.

    Returns:
        tuple: Un tuple que contiene:
            - int: ID de la nota predicha (pitch).
            - float: Valor del paso (step).
            - float: Duración de la nota.
    """
    
    assert temperatura > 0, "La temperatura debe ser un valor positivo."

    # Añadir una dimensión de lote
    entradas = tf.expand_dims(notas, 0)

    # Realizar la predicción utilizando el modelo
    predicciones = modelo_keras.predict(entradas)
    logits_pitch = predicciones['pitch']
    paso = predicciones['step']
    duracion = predicciones['duration']

    # Ajustar los logits de pitch con la temperatura
    logits_pitch /= temperatura
    
    # Realizar la predicción de pitch de manera aleatoria
    pitch = tf.random.categorical(logits_pitch, num_samples=1)
    pitch = tf.squeeze(pitch, axis=-1)

    # Obtener valores de paso y duración
    duracion = tf.squeeze(duracion, axis=-1)
    paso = tf.squeeze(paso, axis=-1)

    # Asegurar que el paso y la duración no sean negativos
    paso = tf.maximum(0, paso)
    duracion = tf.maximum(0, duracion)

    return int(pitch), float(paso), float(duracion)


def generar_notas(model: tf.keras.Model, filter_df: pd.DataFrame, 
                  temperature: float = 2.0, num_predictions: int = 120, 
                  seq_length: int = 25, vocab_size: int = 128) -> pd.DataFrame:
    """Genera notas musicales utilizando un modelo LSTM a partir de un DataFrame de notas.

    Args:
        model (tf.keras.Model): El modelo LSTM entrenado utilizado para predecir las notas.
        filter_df (pd.DataFrame): DataFrame que contiene las notas de entrada.
        temperature (float, opcional): Parámetro que controla la aleatoriedad de las predicciones. 
            Un valor mayor genera más diversidad. (default: 2.0)
        num_predictions (int, opcional): Número de notas a generar. (default: 120)
        seq_length (int, opcional): Longitud de la secuencia de notas de entrada. (default: 25)
        vocab_size (int, opcional): Tamaño del vocabulario para normalizar el pitch. (default: 128)

    Returns:
        pd.DataFrame: Un DataFrame que contiene las notas generadas, incluyendo pitch, step, duration, start y end.
    """
    # Orden de las claves para extraer las notas
    key_order = ['pitch', 'step', 'duration']
    
    # Apilar las notas de entrada en una matriz
    sample_notes = np.stack([filter_df[key] for key in key_order], axis=1)
    # Normalizar las notas de entrada
    input_notes = sample_notes[:seq_length] / np.array([vocab_size, 1, 1])

    generated_notes = []
    prev_start = 0

    # Generar notas utilizando el modelo
    for _ in range(num_predictions):
        pitch, step, duration = predecir_siguiente_nota(input_notes, model, temperature)
        start = prev_start + step
        end = start + duration
        input_note = (pitch, step, duration)
        
        # Almacenar la nota generada
        generated_notes.append((*input_note, start, end))
        
        # Actualizar las notas de entrada para la siguiente predicción
        input_notes = np.delete(input_notes, 0, axis=0)
        input_notes = np.append(input_notes, np.expand_dims(input_note, 0), axis=0)
        
        # Actualizar el tiempo de inicio
        prev_start = start

    # Convertir las notas generadas a un DataFrame
    generated_notes_df = pd.DataFrame(generated_notes, columns=(*key_order, 'start', 'end'))

    return generated_notes_df
