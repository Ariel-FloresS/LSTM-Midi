import numpy as np
import pandas as pd


composer_files = {
    'Beethoven y Brahms': [
        'beethoven_hammerklavier_2.mid',
        'beethoven_les_adieux_2.mid',
        'beethoven_opus10_2.mid',
        'beethoven_opus22_2.mid',
        'beethoven_opus22_3.mid',
        'waldstein_2.mid',
        'brahms_opus117_1.mid',
        'brahms_opus117_2.mid',
        'brahms_opus1_2.mid',
    ],
    'Chopin': [
        'chpn-p1.mid', 'chpn-p2.mid', 'chpn-p3.mid', 'chpn-p4.mid', 'chpn-p5.mid',
        'chpn-p6.mid', 'chpn-p7.mid', 'chpn-p8.mid', 'chpn-p9.mid', 'chpn-p10.mid',
        'chpn-p11.mid', 'chpn-p12.mid', 'chpn-p13.mid', 'chpn-p14.mid', 'chpn-p15.mid',
        'chpn-p16.mid', 'chpn-p17.mid', 'chpn-p18.mid', 'chpn-p19.mid', 'chpn-p20.mid',
        'chpn-p21.mid', 'chpn-p22.mid', 'chpn-p23.mid', 'chpn-p24.mid',
        'chpn_op10_e01.mid', 'chpn_op10_e05.mid', 'chpn_op10_e12.mid',
        'chpn_op25_e2.mid', 'chpn_op25_e3.mid', 'chpn_op25_e4.mid', 'chpn_op27_1.mid',
        'chpn_op7_1 (1).mid', 'chpn_op7_2.mid'
    ],
    'Debussy': [
        'debussy_cc_1.mid',
        'debussy_cc_2.mid',
        'debussy_cc_3.mid',
        'debussy_cc_4.mid',
        'debussy_cc_5.mid',
        'debussy_cc_6.mid',
        'deb_clai.mid',
        'deb_menu.mid',
        'deb_pass.mid',
        'deb_prel.mid'
    ],
    'Grieg': [
        'grieg_album.mid',
        'grieg_berceuse.mid',
        'grieg_brooklet.mid',
        'grieg_butterfly.mid',
        'grieg_elfentanz.mid',
        'grieg_halling.mid',
        'grieg_kobold.mid',
        'grieg_march.mid',
        'grieg_once_upon_a_time.mid',
        'grieg_spring.mid',
        'grieg_voeglein.mid',
        'grieg_waechter.mid',
        'grieg_walzer.mid',
        'grieg_wanderer.mid',
        'grieg_zwerge.mid'
    ],
    'Mozart': [
        'mz_311_2.mid',
        'mz_330_2.mid',
        'mz_332_2.mid',
        'mz_545_2.mid',
        'mz_545_3.mid',
        'mz_570_2.mid',
        'mz_570_3.mid'
    ],
    'Tchaikovsky': [
        'ty_april.mid',
        'ty_februar.mid',
        'ty_januar.mid',
        'ty_juli.mid',
        'ty_juni.mid',
        'ty_maerz.mid',
        'ty_mai.mid',
        'ty_november.mid',
        'ty_oktober.mid',
        'ty_september.mid',
        'pathetique_2.mid',  #
    ],
    'Mendelssohn y Liszt': [
        'schumm-2.mid',
        'schumm-3.mid',
        'schumm-5.mid',
        'schumm-6.mid',
        'liz_et4.mid',
        'liz_et5.mid',
        'liz_liebestraum.mid'
    ],
    
    'Various': [
        'appass_2.mid',
        'br_im2.mid',
        'br_im5.mid',
        'br_im6.mid' 
    ]
}


def get_dataframe()->pd.DataFrame:
    return pd.read_csv('data/notes.csv')



def genera_semilla(autor_name) -> pd.DataFrame:
    """Genera una semilla aleatoria seleccionando un archivo MIDI y su correspondiente DataFrame.

    Returns:
        Tuple[str, pd.DataFrame]: Un tuple que contiene:
            - str: El nombre del archivo MIDI seleccionado aleatoriamente.
            - pd.DataFrame: Un DataFrame filtrado que contiene las notas relacionadas
              con el archivo MIDI seleccionado.
    """
    
    # Cargar el DataFrame desde el archivo CSV
    df = get_dataframe()

    df = df[df['filename'].isin(composer_files[autor_name])]

    
    # Seleccionar aleatoriamente un nombre de archivo
    nombre_archivo_aleatorio = df['filename'].sample(n=1).values[0]
    
    # Filtrar el DataFrame para obtener solo las notas del archivo seleccionado
    df_filtrado = df[df['filename'] == nombre_archivo_aleatorio]

    return  df_filtrado
