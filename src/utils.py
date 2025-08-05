# Funciones auxiliares
import re
import pandas as pd
from typing import Any

def clean_value(header: str, value: str) -> Any:
    """Limpia y convierte valores según el campo"""
    if not value or value == 'nan':
        return None
    
    if header == 'Identifier':
        return int(value) if value.isdigit() else None
    elif header == 'Date of Publication':
        # Extraer año de formatos como [1892] o 1892-05-15
        year_match = re.search(r'(\d{4})', value)
        return year_match.group(1) if year_match else None
    elif header == 'Flickr URL':
        return value if value.startswith('http') else None
    else:
        return value.strip()

def create_dataframe(headers: List[str], data: List[Dict]) -> pd.DataFrame:
    """Convierte los datos procesados a un DataFrame pandas"""
    df = pd.DataFrame(data, columns=headers)
    
    # Conversión de tipos
    df['Identifier'] = pd.to_numeric(df['Identifier'], errors='coerce')
    
    # Convertir fechas (asumiendo que tenemos solo años)
    df['Date of Publication'] = pd.to_numeric(
        df['Date of Publication'], 
        errors='coerce'
    ).astype('Int64')  # Usar Int64 para manejar NaN
    
    return df

def save_results(df: pd.DataFrame, output_path: str):
    """Guarda los resultados procesados"""
    df.to_csv(output_path, index=False)