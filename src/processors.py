# Procesamiento del archivo CSV usando regex
import re
import logging
from typing import List, Dict, Tuple
from . import patterns
from .utils import clean_value

logger = logging.getLogger(__name__)

def load_file(file_path: str) -> str:
    """Carga el archivo CSV como texto"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        logger.error(f"Error al cargar el archivo: {str(e)}")
        raise

def validate_headers(content: str) -> bool:
    """Valida que los encabezados coincidan con el patrón esperado"""
    first_line = content.split('\n')[0]
    if re.match(patterns.HEADER_PATTERN, first_line):
        logger.info("Encabezados validados correctamente")
        return True
    else:
        logger.error("Los encabezados no coinciden con el patrón esperado")
        return False

def parse_line(line: str, headers: List[str]) -> Dict:
    """Parsea una línea del CSV usando los patrones regex"""
    row = {}
    remaining_line = line
    
    for header in headers:
        pattern_config = patterns.PATTERNS.get(header, {'pattern': r'^(.*?)(?=\t|$)'})
        pattern = pattern_config['pattern']
        match = re.match(pattern, remaining_line)
        
        if match:
            value = match.group(1)
            row[header] = clean_value(header, value)
            remaining_line = remaining_line[match.end():].lstrip('\t')
        else:
            row[header] = None
            logger.warning(f"No se encontró coincidencia para {header} en: {remaining_line[:50]}...")
    
    return row

def parse_content(content: str) -> Tuple[List[str], List[Dict]]:
    """Procesa todo el contenido del CSV"""
    lines = content.split('\n')
    headers = lines[0].split('\t')
    data = []
    
    for i, line in enumerate(lines[1:], start=2):
        if not line.strip():
            continue
            
        try:
            row = parse_line(line, headers)
            data.append(row)
        except Exception as e:
            logger.error(f"Error procesando línea {i}: {str(e)}")
            continue
    
    logger.info(f"Procesamiento completado. {len(data)} registros procesados.")
    return headers, data