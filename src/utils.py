# Módulo de funciones auxiliares para limpieza y transformación de datos
# Este módulo proporciona utilidades para:
# - Limpieza y conversión de valores específicos por tipo de campo
# - Transformación de datos procesados a estructura pandas DataFrame
# - Aplicación de tipos de datos apropiados según el contenido
# - Guardado de resultados en formato CSV

import re
import pandas as pd
from typing import Any, List, Dict

def clean_value(header: str, value: str) -> Any:
    """
    Limpia y convierte valores según el tipo de campo específico.
    
    Esta función aplica transformaciones específicas basadas en el nombre del campo:
    - Identifier: conversión a entero si es numérico
    - Date of Publication: extracción del año usando regex
    - Flickr URL: validación de protocolo HTTP
    - Otros campos: limpieza de espacios en blanco
    
    Args:
        header (str): Nombre del campo/columna
        value (str): Valor a limpiar y convertir
        
    Returns:
        Any: Valor limpio y convertido al tipo apropiado, o None si es inválido
    """
    # Manejar valores vacíos o nulos
    if not value or value == 'nan':
        return None
    
    # Aplicar limpieza específica según el tipo de campo
    if header == 'Identifier':
        # Convertir a entero solo si contiene únicamente dígitos
        return int(value) if value.isdigit() else None
    elif header == 'Date of Publication':
        # Extraer año de 4 dígitos de formatos como [1892] o 1892-05-15
        year_match = re.search(r'(\d{4})', value)
        return year_match.group(1) if year_match else None
    elif header == 'Flickr URL':
        # Validar que la URL comience con protocolo HTTP
        return value if value.startswith('http') else None
    else:
        # Para otros campos, solo limpiar espacios en blanco
        return value.strip()

def create_dataframe(headers: List[str], data: List[Dict]) -> pd.DataFrame:
    """
    Convierte los datos procesados a un DataFrame de pandas con tipos correctos.
    
    Esta función:
    - Crea un DataFrame a partir de la lista de diccionarios
    - Aplica conversiones de tipo apropiadas para cada columna
    - Maneja valores nulos de manera adecuada
    - Asegura tipos de datos consistentes para análisis posterior
    
    Args:
        headers (List[str]): Lista de nombres de columnas
        data (List[Dict]): Lista de diccionarios, uno por cada fila de datos
        
    Returns:
        pd.DataFrame: DataFrame con datos limpios y tipos apropiados
    """
    # Crear DataFrame inicial con todos los datos
    df = pd.DataFrame(data, columns=headers)
    
    # Aplicar conversiones de tipo específicas
    # Identifier: convertir a numérico, permitir NaN para valores inválidos
    df['Identifier'] = pd.to_numeric(df['Identifier'], errors='coerce')
    
    # Date of Publication: convertir años a enteros, usar Int64 para manejar NaN
    df['Date of Publication'] = pd.to_numeric(
        df['Date of Publication'], 
        errors='coerce'
    ).astype('Int64')  # Int64 permite valores nulos en columnas de enteros
    
    return df

def save_results(df: pd.DataFrame, output_path: str):
    """
    Guarda el DataFrame procesado en un archivo CSV.
    
    Args:
        df (pd.DataFrame): DataFrame con datos procesados
        output_path (str): Ruta donde guardar el archivo CSV resultante
    """
    # Guardar sin incluir el índice de pandas en el archivo
    df.to_csv(output_path, index=False)