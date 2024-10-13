import numpy as np
import pandas as pd


composer_files = {
    'Albéniz': ['alb_esp1.mid', 'alb_esp2.mid', 'alb_esp3.mid', 'alb_esp4.mid', 'alb_esp5.mid', 'alb_esp6.mid',
                'alb_se1.mid', 'alb_se2.mid', 'alb_se3.mid', 'alb_se4.mid', 'alb_se5.mid', 'alb_se6.mid', 
                'alb_se7.mid', 'alb_se8.mid'],
    'Beethoven y Bach': ['beethoven_hammerklavier_1.mid', 'beethoven_hammerklavier_2.mid', 'beethoven_hammerklavier_3.mid',
                  'beethoven_hammerklavier_4.mid', 'beethoven_les_adieux_1.mid', 'beethoven_les_adieux_2.mid',
                  'beethoven_les_adieux_3.mid', 'beethoven_opus10_1.mid', 'beethoven_opus10_2.mid',
                  'beethoven_opus10_3.mid', 'beethoven_opus22_1.mid', 'beethoven_opus22_2.mid',
                  'beethoven_opus22_3.mid', 'beethoven_opus22_4.mid', 'beethoven_opus90_1.mid',
                  'beethoven_opus90_2.mid', 'pathetique_1.mid', 'pathetique_2.mid', 'pathetique_3.mid',
                  'mond_1.mid', 'mond_2.mid', 'mond_3.mid','bach_846.mid', 'bach_847.mid', 'bach_850.mid'],
    'Brahms , Borodin y Burgmüller': ['brahms_opus117_1.mid', 'brahms_opus117_2.mid', 'brahms_opus1_1.mid', 'brahms_opus1_2.mid', 
               'brahms_opus1_3.mid', 'brahms_opus1_4.mid','bor_ps1.mid', 'bor_ps1_format4.mid', 'bor_ps1_format5.mid', 'bor_ps2.mid', 'bor_ps3.mid', 
                'bor_ps4.mid', 'bor_ps5.mid', 'bor_ps6.mid', 'bor_ps7.mid','burg_agitato.mid', 'burg_erwachen.mid', 'burg_geschwindigkeit.mid', 'burg_gewitter.mid', 
                   'burg_perlen.mid', 'burg_quelle.mid', 'burg_spinnerlied.mid', 'burg_sylphen.mid', 
                   'burg_trennung.mid'],
                   
    'Chopin': ['chpn-p1.mid', 'chpn-p2.mid', 'chpn-p3.mid', 'chpn-p4.mid', 'chpn-p5.mid', 'chpn-p6.mid', 'chpn-p7.mid', 
               'chpn-p8.mid', 'chpn-p9.mid', 'chpn-p10.mid', 'chpn-p11.mid', 'chpn-p12.mid', 'chpn-p13.mid', 
               'chpn-p14.mid', 'chpn-p15.mid', 'chpn-p16.mid', 'chpn-p17.mid', 'chpn-p18.mid', 'chpn-p19.mid', 
               'chpn-p20.mid', 'chpn-p21.mid', 'chpn-p22.mid', 'chpn-p23.mid', 'chpn-p24.mid', 'chpn_op10_e01.mid', 
               'chpn_op10_e05.mid', 'chpn_op10_e12.mid', 'chpn_op23.mid', 'chpn_op25_e1.mid', 'chpn_op25_e2.mid', 
               'chpn_op25_e3.mid', 'chpn_op25_e4.mid', 'chpn_op25_e11.mid', 'chpn_op25_e12.mid', 'chpn_op27_1.mid', 
               'chpn_op27_2.mid', 'chpn_op33_2.mid', 'chpn_op33_4.mid', 'chpn_op35_1.mid', 'chpn_op35_2.mid', 
               'chpn_op35_3.mid', 'chpn_op35_4.mid', 'chpn_op53.mid', 'chpn_op66.mid', 'chpn_op7_1 (1).mid', 
               'chpn_op7_1.mid', 'chpn_op7_2.mid', 'chp_op18.mid', 'chp_op31.mid'],

    'Clementi y Haydn': ['clementi_opus36_1_1.mid', 'clementi_opus36_1_2.mid', 'clementi_opus36_1_3.mid', 
                 'clementi_opus36_2_1.mid', 'clementi_opus36_2_2.mid', 'clementi_opus36_2_3.mid', 
                 'clementi_opus36_3_1.mid', 'clementi_opus36_3_2.mid', 'clementi_opus36_3_3.mid', 
                 'clementi_opus36_4_1.mid', 'clementi_opus36_4_2.mid', 'clementi_opus36_4_3.mid', 
                 'clementi_opus36_5_1.mid', 'clementi_opus36_5_2.mid', 'clementi_opus36_5_3.mid', 
                 'clementi_opus36_6_1.mid', 'clementi_opus36_6_2.mid','haydn_33_1.mid', 'haydn_33_2.mid', 'haydn_33_3.mid', 'haydn_35_1.mid', 'haydn_35_2.mid', 'haydn_35_3.mid', 
              'haydn_43_1.mid', 'haydn_43_2.mid', 'haydn_43_3.mid', 'haydn_7_1.mid', 'haydn_7_2.mid', 'haydn_7_3.mid', 
              'haydn_8_1.mid', 'haydn_8_2.mid', 'haydn_8_3.mid', 'haydn_8_4.mid', 'haydn_9_1.mid', 'haydn_9_2.mid', 
              'haydn_9_3.mid', 'hay_40_1.mid', 'hay_40_2.mid'],

    'Debussy': ['debussy_cc_1.mid', 'debussy_cc_2.mid', 'debussy_cc_3.mid', 'debussy_cc_4.mid', 'debussy_cc_5.mid', 
                'debussy_cc_6.mid', 'deb_clai.mid', 'deb_menu.mid', 'deb_pass.mid', 'deb_prel.mid'],

    'Grieg, Liszt y Schumann': ['grieg_album.mid', 'grieg_berceuse.mid', 'grieg_brooklet.mid', 'grieg_butterfly.mid', 'grieg_elfentanz.mid',
              'grieg_halling.mid', 'grieg_kobold.mid', 'grieg_march.mid', 'grieg_once_upon_a_time.mid', 'grieg_spring.mid',
              'grieg_voeglein.mid', 'grieg_waechter.mid', 'grieg_walzer.mid', 'grieg_wanderer.mid', 'grieg_wedding.mid',
              'grieg_zwerge.mid','liz_donjuan.mid', 'liz_et1.mid', 'liz_et2.mid', 'liz_et3.mid', 'liz_et4.mid', 'liz_et5.mid', 'liz_et6.mid', 
              'liz_et_trans4.mid', 'liz_et_trans5.mid', 'liz_et_trans8.mid', 'liz_liebestraum.mid', 'liz_rhap02.mid', 
              'liz_rhap09.mid', 'liz_rhap10.mid', 'liz_rhap12.mid', 'liz_rhap15.mid','sch_ca.mid', 'sch_eti.mid', 'sch_fs.mid', 'sch_kre1.mid', 'sch_kre2.mid', 'sch_kre3.mid', 'sch_kre4.mid', 
                 'sch_kre5.mid', 'sch_kre6.mid', 'sch_walt.mid', 'sch_wood.mid'],

    'Mendelssohn y Scarlatti': ['mendel_op19_1.mid', 'mendel_op19_2.mid', 'mendel_op19_3.mid', 'mendel_op19_4.mid', 'mendel_op19_5.mid', 
                    'mendel_op19_6.mid', 'mendel_op30_1.mid', 'mendel_op30_2.mid', 'mendel_op30_3.mid', 'mendel_op30_4.mid', 
                    'mendel_op30_5.mid', 'mendel_op53_5.mid', 'mendel_op62_3.mid', 'mendel_op62_4.mid', 'mendel_op62_5.mid','scarlatti_e3.mid', 'scarlatti_500.mid'],

    'Mozart': ['mz_311_1.mid', 'mz_311_2.mid', 'mz_311_3.mid', 'mz_330_1.mid', 'mz_330_2.mid', 'mz_330_3.mid', 
               'mz_331_1.mid', 'mz_331_2.mid', 'mz_331_3.mid', 'mz_332_1.mid', 'mz_332_2.mid', 'mz_332_3.mid', 
               'mz_333_1.mid', 'mz_333_2.mid', 'mz_333_3.mid', 'mz_545_1.mid', 'mz_545_2.mid', 'mz_545_3.mid', 
               'mz_570_1.mid', 'mz_570_2.mid', 'mz_570_3.mid', 'mz_570_4.mid', 'mz_279_1.mid', 'mz_279_2.mid', 
               'mz_279_3.mid'],

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
