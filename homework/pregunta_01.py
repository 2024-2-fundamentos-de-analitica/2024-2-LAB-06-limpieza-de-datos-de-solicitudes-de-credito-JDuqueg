"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""
import pandas as pd
pd.set_option('display.max_rows', None)

def load_data(input_directory):
    data = pd.read_csv(input_directory, sep=';', header=0, index_col=0)
    
    data = data.dropna().drop_duplicates().reset_index(drop=True)
    return data

def clean_df(df):
    columnas = ['sexo','tipo_de_emprendimiento','idea_negocio','línea_credito','monto_del_credito']
    df.loc[:, columnas] = df.loc[:, columnas].map(lambda x: x.lower().strip())
    for column in columnas:
        df[column]=df[column].str.replace('_',' ').str.replace('-',' ').str.replace(',','').str.replace('$','').str.replace('.00','').str.strip()
    
    
    df['comuna_ciudadano'] = df['comuna_ciudadano'].astype('int')

    df['barrio'] = df["barrio"].str.lower().str.replace('_', ' ').str.replace('-',' ')


    df['fecha_de_beneficio'] = df["fecha_de_beneficio"] = pd.to_datetime(df["fecha_de_beneficio"], format="%d/%m/%Y", errors="coerce").combine_first(pd.to_datetime(df["fecha_de_beneficio"], format="%Y/%m/%d", errors="coerce"))

    df = df.drop_duplicates().reset_index(drop=True)
    df = df.dropna()
    
     

    return df

    

    

def pregunta_01():
    """
    Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
    El archivo tiene problemas como registros duplicados y datos faltantes.
    Tenga en cuenta todas las verificaciones discutidas en clase para
    realizar la limpieza de los datos.

    El archivo limpio debe escribirse en "files/output/solicitudes_de_credito.csv"

    """
    data = load_data('files/input/solicitudes_de_credito.csv')
    df = clean_df(data)
    df.to_csv('files/output/solicitudes_de_credito.csv', sep=';', index=False )

    return df['comuna_ciudadano'].value_counts()

print(pregunta_01())
