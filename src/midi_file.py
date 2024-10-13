import pretty_midi
import numpy as np
import pandas as pd
import soundfile as sf

def dataframe_a_midi(df: pd.DataFrame, output_file: str) -> None:
    """Convierte un DataFrame con columnas 'start', 'end' y 'pitch' a un archivo MIDI.

    Args:
        df (pd.DataFrame): DataFrame que contiene las notas, debe tener las columnas 'start', 'end' y 'pitch'.
        output_file (str): Ruta donde se guardará el archivo MIDI de salida.
        instrument_name (str, opcional): Nombre del instrumento a utilizar. (default: 'Piano acústico')

    Returns:
        None: La función guarda el archivo MIDI en la ruta especificada.
    """
    # Crear un objeto PrettyMIDI
    midi = pretty_midi.PrettyMIDI()

    instrument_program = 2 
    instrument = pretty_midi.Instrument(program=instrument_program)

    # Añadir notas al instrumento
    for _, row in df.iterrows():
        start_time = row['start']
        end_time = row['end']
        pitch = int(row['pitch'])

        # Crear una nota MIDI
        note = pretty_midi.Note(
            velocity=100,  # Velocidad de la nota (0-127)
            pitch=pitch,   # Pitch de la nota
            start=start_time,  # Tiempo de inicio de la nota
            end=end_time  # Tiempo de finalización de la nota
        )

        # Añadir la nota al instrumento
        instrument.notes.append(note)

    # Añadir el instrumento a la pista
    midi.instruments.append(instrument)

    # Guardar el archivo MIDI
    midi.write(output_file)
    
def midi_to_wav(midi_file_path, wav_file_path):
    """Convierte un archivo MIDI a WAV."""
    try:
        # Cargar el archivo MIDI
        midi_data = pretty_midi.PrettyMIDI(midi_file_path)
        
        # Generar el audio a partir del archivo MIDI
        audio_data = midi_data.synthesize()

        # Guardar el audio como un archivo WAV
        sf.write(wav_file_path, audio_data, 22050)
        
        print(f"Conversión exitosa: {midi_file_path} a {wav_file_path}")
    except Exception as e:
        print(f"Ocurrió un error: {e}")
