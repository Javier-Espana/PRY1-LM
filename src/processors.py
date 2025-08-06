# Módulo de procesamiento de archivo CSV usando expresiones regulares
# Este módulo implementa el core del procesamiento de datos del proyecto:
# - Carga del archivo CSV como texto plano (sin librerías especializadas)
# - Validación de estructura mediante patrones regex
# - Parsing manual de contenido respetando formato CSV con comillas
# - Aplicación de expresiones regulares específicas para cada campo
# - Limpieza y estructuración de datos extraídos

import re
from typing import List, Dict, Tuple
import patterns
from utils import clean_value

def load_file(file_path: str) -> str: # Carga el archivo CSV completo como texto
    """
    Carga el archivo CSV completo como una cadena de texto.
    
    Esta función lee el archivo CSV de forma completa en memoria como texto plano,
    sin usar librerías.
    
    Args:
        file_path (str): Ruta absoluta al archivo CSV a procesar
        
    Returns:
        str: Contenido completo del archivo como cadena de texto
        
    Raises:
        Exception: Si el archivo no puede ser leído (no existe, permisos, encoding, etc.)
    """
    try:
        # Abrir archivo con encoding UTF-8 para manejar caracteres especiales
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        print(f"Error al cargar el archivo: {str(e)}")
        raise

def validate_headers(content: str) -> bool: # Valida que los encabezados del CSV coincidan con el patrón esperado
    """
    Valida que los encabezados del CSV coincidan exactamente con el patrón esperado.
    
    Esta función aplica una expresión regular estricta para verificar que:
    - El archivo tenga exactamente las 15 columnas esperadas
    - Los nombres de las columnas estén en el orden correcto
    - No haya columnas adicionales o faltantes
    
    Args:
        content (str): Contenido completo del archivo CSV como texto
        
    Returns:
        bool: True si los encabezados son válidos, False en caso contrario
    """
    # Extraer la primera línea que debe contener los encabezados
    first_line = content.split('\n')[0]
    
    # Aplicar el patrón regex para validar estructura de encabezados
    if re.match(patterns.HEADER_PATTERN, first_line): # Verifica si la primera línea coincide con el patrón HEADER_PATTERN definido en patterns.py
        return True
    else:
        print("Los encabezados no coinciden con el patrón esperado")
        return False

def parse_line(line: str, headers: List[str]) -> Dict: # Procesa una línea individual del CSV aplicando algoritmo manual de parsing
    """
    Parsea una línea individual del CSV aplicando algoritmo manual de parsing.
    
    Esta función implementa un parser CSV personalizado que:
    - Maneja correctamente las comillas que pueden contener comas
    - Respeta el formato CSV estándar
    - Aplica limpieza de datos específica para cada campo
    - Mantiene la correspondencia entre valores y encabezados
    
    Args:
        line (str): Línea individual del CSV a procesar
        headers (List[str]): Lista de nombres de columnas/encabezados
        
    Returns:
        Dict: Diccionario con datos de la fila, usando nombres de columnas como claves
    """
    row = {}
    
    # Implementar parser CSV manual que maneja comillas correctamente
    # Este algoritmo divide la línea por comas, pero respeta las comillas
    values = []
    current_value = ""
    in_quotes = False
    
    # Procesar cada carácter de la línea para detectar separadores válidos
    for char in line:
        if char == '"':
            # Cambiar estado de dentro/fuera de comillas
            in_quotes = not in_quotes
        elif char == ',' and not in_quotes:
            # Solo dividir por coma si no estamos dentro de comillas
            values.append(current_value.strip())
            current_value = ""
        else:
            # Agregar carácter al valor actual
            current_value += char
    
    # No olvidar agregar el último valor (después de la última coma)
    values.append(current_value.strip())
    
    # Asegurar que tenemos exactamente el número correcto de valores
    # Rellenar con strings vacíos si faltan valores
    while len(values) < len(headers):
        values.append("")
    
    # Crear diccionario asociando cada valor con su encabezado correspondiente
    for i, header in enumerate(headers):
        if i < len(values):
            # Limpiar comillas y espacios extra, luego aplicar limpieza específica
            value = values[i].strip('"').strip()
            row[header] = clean_value(header, value)
        else:
            # Si no hay suficientes valores, asignar None
            row[header] = None
    
    return row

def parse_content(content: str) -> Tuple[List[str], List[Dict]]: # Esto procesa todo el contenido del CSV línea por línea
    """
    Procesa todo el contenido del CSV línea por línea.
    
    Esta función coordina el procesamiento completo del archivo:
    - Separa encabezados del contenido de datos
    - Procesa cada línea individual aplicando el parser CSV
    - Maneja errores de líneas individuales sin afectar el procesamiento total
    - Proporciona estadísticas del procesamiento realizado
    
    Args:
        content (str): Contenido completo del archivo CSV
        
    Returns:
        Tuple[List[str], List[Dict]]: Tupla con (encabezados, lista_de_registros)
        - encabezados: Lista con nombres de las columnas
        - lista_de_registros: Lista de diccionarios, uno por cada fila de datos
    """
    # Dividir contenido en líneas individuales
    lines = content.split('\n')
    
    # Extraer encabezados de la primera línea y limpiar espacios
    headers = lines[0].split(',')
    headers = [h.strip() for h in headers]
    
    # Lista para almacenar todos los registros procesados
    data = []
    
    # Procesar cada línea de datos (saltando la línea de encabezados)
    for i, line in enumerate(lines[1:], start=2):
        # Saltar líneas vacías que pueden aparecer al final del archivo
        if not line.strip():
            continue
            
        try:
            # Procesar línea individual y agregar a la colección de datos
            row = parse_line(line, headers)
            data.append(row)
        except Exception as e:
            # Registrar error pero continuar con el procesamiento
            print(f"Error procesando línea {i}: {str(e)}")
            continue
    
    # Proporcionar estadísticas del procesamiento completado
    print(f"Procesamiento completado. {len(data)} registros procesados.")
    return headers, data