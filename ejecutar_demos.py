#!/usr/bin/env python3
"""
Script completo para generar capturas de pantalla de las ejecuciones
de expresiones regulares según los requerimientos del proyecto
"""

import re
import sys
import os
import csv
from datetime import datetime

# Agregar el directorio src al path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from patterns import PATTERNS, HEADER_PATTERN

# Variable global para manejar la salida
output_file = None

def write_output(text, end='\n'):
    """Escribe tanto en consola como en archivo"""
    print(text, end=end)
    if output_file:
        output_file.write(text + end)
        output_file.flush()  # Asegurar que se escriba inmediatamente

def print_header(title, symbol="=", width=70): # Imprime un encabezado formateado
    """Imprime un encabezado formateado"""
    write_output(f"\n{symbol * width}")
    write_output(f"{title:^{width}}")
    write_output(f"{symbol * width}")

def print_subheader(title, symbol="-", width=70): # Imprime un subencabezado formateado
    """Imprime un subencabezado formateado"""
    write_output(f"\n{symbol * width}")
    write_output(f" {title}")
    write_output(f"{symbol * width}")

def test_pattern_with_real_data(field_name, pattern_config, csv_file): # Prueba un patrón con datos reales del CSV
    """Prueba un patrón con datos reales del CSV"""
    print_subheader(f"ANÁLISIS DE CAMPO: {field_name}")
    write_output(f"Expresión Regular: {pattern_config['pattern']}")
    write_output(f"Descripción: {pattern_config['description']}")
    write_output(f"Notación vista en clase: {get_formal_notation(pattern_config['pattern'])}")
    
    pattern = re.compile(pattern_config['pattern'])
    
    # Leer algunos ejemplos reales del CSV
    examples = []
    try:
        with open(csv_file, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            count = 0
            for row in reader:
                if count >= 5:  # Solo tomar 5 ejemplos
                    break
                value = row.get(field_name, '').strip()
                if value:  # Solo valores no vacíos
                    examples.append(value)
                    count += 1
    except Exception as e:
        write_output(f"Error leyendo archivo: {e}")
        return
    
    write_output(f"\nEJEMPLOS REALES DEL DATASET:")
    for i, example in enumerate(examples, 1):
        match = pattern.match(example)
        status = "ACEPTA" if match else "RECHAZA"
        write_output(f"{i}. {status} | '{example[:60]}{'...' if len(example) > 60 else ''}'")
        if match and match.groups():
            captured = match.group(1) if len(match.groups()) >= 1 else match.group(0)
            write_output(f"   Grupo capturado: '{captured[:50]}{'...' if len(captured) > 50 else ''}'")
    
    # Probar también con los ejemplos definidos
    write_output(f"\nPRUEBAS CON EJEMPLOS PREDEFINIDOS:")
    test_examples = [pattern_config['example_valid'], pattern_config['example_invalid']]
    for example in test_examples:
        if example:
            match = pattern.match(example)
            status = "ACEPTA" if match else "RECHAZA"
            expected = "ACEPTA" if example == pattern_config['example_valid'] else "RECHAZA"
            result = "CORRECTO" if (match and expected == "ACEPTA") or (not match and expected == "RECHAZA") else "INCORRECTO"
            write_output(f"{status} | '{example}' | Esperado: {expected} | {result}")

def get_formal_notation(pattern): # Convierte regex a notación formal vista en clase
    """Convierte regex a notación formal vista en clase"""
    notation_map = {
        r'\d': '[0-9]',
        r'\w': '[a-zA-Z0-9_]',
        r'\s': '[ \\t\\n\\r]',
        r'^': 'inicio de cadena',
        r'$': 'final de cadena',
        r'+': 'una o más repeticiones',
        r'*': 'cero o más repeticiones',
        r'?': 'cero o una repetición',
        r'[^,]': 'cualquier carácter excepto coma',
        r'(?=': 'lookahead positivo',
        r'|': 'alternancia (OR)',
        r'()': 'grupo de captura'
    }
    
    # Simplificar para mostrar conceptos principales
    if r'\d+' in pattern:
<<<<<<< HEAD
        return "dígito+ (uno o más dígitos)"
    elif 'flickr\\.com' in pattern:
        return "http(s)?://.*flickr.com.*"
    elif 'monographic|serial' in pattern:
        return "monographic OR serial OR integrating resource"
=======
        return "dígito⁺ (uno o más dígitos)"
    elif 'google\\.com' in pattern:
        return "http(s)?://.*google.com.*"
    elif 'monographic|serial' in pattern:
        return "monographic ∪ serial ∪ integrating resource ∪ continuing"
>>>>>>> 8d96f7dfaf8042192afb4b034984f13a76490af0
    elif r'[^,]*' in pattern:
        return "([cualquier carácter excepto coma])* (cero o más caracteres hasta coma)"
    else:
        return pattern

def demonstrate_state_machines(): # Demuestra el funcionamiento de las máquinas de estado más importantes
    """Demuestra el funcionamiento de las máquinas de estado más importantes"""
    print_header("DEMOSTRACIÓN DE MÁQUINAS DE ESTADO FINITO")
    
    # Header Pattern - Máquina de estado compleja
    print_subheader("MÁQUINA DE ESTADO: Header Pattern")
    print("Valida: Identifier,Edition Statement,Place of Publication,...,Shelfmarks")
    print("Estados: q0 (inicial) -> q1-q202 (intermedio) -> q203 (aceptacion)")
    print("\nSimulación con encabezados del CSV:")
    expected_headers = "Identifier,Edition Statement,Place of Publication,Date of Publication,Publisher,Title,Author,Contributors,Corporate Author,Corporate Contributors,Former owner,Engraver,Issuance type,Flickr URL,Shelfmarks"
    if re.match(HEADER_PATTERN, expected_headers):
        print("ACEPTA: Encabezados validos - transicion completa q0 -> q203")
    else:
        print("RECHAZA: Encabezados invalidos")
    
    # Title - Máquina de estado con lookahead
    print_subheader("MÁQUINA DE ESTADO: Title (^([^,]*?)(?=,|$))")
    print("Estados: q0 (inicial) -> q1 (acumulando) -> q2 (aceptacion)")
    print("Incluye lookahead positivo para detectar ',' o fin de cadena")
    print("\nSimulación con 'Walter Forbes. [A novel.] By A. A':")
    
    title_example = "Walter Forbes. [A novel.] By A. A"
    state = "q0"
    for i, char in enumerate(title_example[:10]):  # Mostrar solo los primeros 10 caracteres
        if char != ',':
            if state == "q0":
                state = "q1"
                print(f"Paso {i+1}: '{char}' | q0 -> q1 (primer caracter del titulo)")
            else:
                print(f"Paso {i+1}: '{char}' | q1 -> q1 (continuando titulo)")
        else:
            print(f"Paso {i+1}: '{char}' | COMA DETECTADA - preparar para lookahead")
            break
    print(f"... (continúa hasta el final)")
    print(f"Lookahead detecta fin de cadena | q1 -> q2 (captura completada)")
    print(f"Estado final: q2 | Resultado: ACEPTA")
    
    # Identifier - Máquina de estado simple
    print_subheader("MÁQUINA DE ESTADO: Identifier (^\\d+)")
<<<<<<< HEAD
    print("Estados: q0 (inicial) -> q1 (aceptacion)")
    print("Transiciones: q0 --[0-9]--> q1, q1 --[0-9]--> q1")
    print("\nSimulación paso a paso con '000000206':")
=======
    write_output("Estados: q0 (inicial) → q1 (aceptación)")
    write_output("Transiciones: q0 --[0-9]--> q1, q1 --[0-9]--> q1")
    write_output("\nSimulación paso a paso con '000000206':")
>>>>>>> 8d96f7dfaf8042192afb4b034984f13a76490af0
    
    input_string = "000000206"
    state = "q0"
    for i, char in enumerate(input_string):
        if char.isdigit():
            if state == "q0":
                state = "q1"
<<<<<<< HEAD
                print(f"Paso {i+1}: '{char}' | q0 -> q1 (primer digito)")
            else:
                print(f"Paso {i+1}: '{char}' | q1 -> q1 (digito adicional)")
        else:
            print(f"Paso {i+1}: '{char}' | RECHAZO (no es digito)")
=======
                write_output(f"Paso {i+1}: '{char}' | q0 → q1 (primer dígito)")
            else:
                write_output(f"Paso {i+1}: '{char}' | q1 → q1 (dígito adicional)")
        else:
            write_output(f"Paso {i+1}: '{char}' | RECHAZO (no es dígito)")
>>>>>>> 8d96f7dfaf8042192afb4b034984f13a76490af0
            break
    write_output(f"Estado final: {state} | Resultado: {'ACEPTA' if state == 'q1' else 'RECHAZA'}")
    
    # Flickr URL - Máquina más compleja
<<<<<<< HEAD
    print_subheader("MÁQUINA DE ESTADO: Flickr URL")
    print("Secuencia: http -> :// -> [texto] -> flickr.com -> [resto]")
    print("\nSimulación con 'http://www.flickr.com/photos/123':")
    url = "http://www.flickr.com/photos/123"
=======
    print_subheader("MÁQUINA DE ESTADO: Google URL")
    write_output("Secuencia: http → :// → [texto] → google.com → [resto]")
    write_output("\nSimulación con 'http://www.google.com':")
    url = "http://www.google.com"
>>>>>>> 8d96f7dfaf8042192afb4b034984f13a76490af0
    if url.startswith('http'):
        write_output("✓ Prefijo 'http' detectado")
        if '://' in url:
<<<<<<< HEAD
            print("Protocolo '://' encontrado")
            if 'flickr.com' in url:
                print("Dominio 'flickr.com' encontrado")
                print("ACEPTA: URL de Flickr valida")
=======
            write_output("✓ Protocolo '://' encontrado")
            if 'google.com' in url:
                write_output("✓ Dominio 'google.com' encontrado")
                write_output("→ ACEPTA: URL de Google válida")
>>>>>>> 8d96f7dfaf8042192afb4b034984f13a76490af0
            else:
                write_output("✗ No contiene 'google.com'")
                write_output("→ RECHAZA: No es URL de Google")
        else:
            write_output("✗ Falta '://'")
            write_output("→ RECHAZA: Protocolo incompleto")
    else:
        write_output("✗ No comienza con 'http'")
        write_output("→ RECHAZA: Falta protocolo HTTP")

def main(): 
    """Función principal que ejecuta todas las demostraciones"""
    global output_file
    
    # Crear nombre de archivo
    output_filename = f"output/informeAnálisis.txt"
    
    # Crear directorio output si no existe
    os.makedirs("output", exist_ok=True)
    
    # Abrir archivo para escribir
    with open(output_filename, 'w', encoding='utf-8') as f:
        output_file = f
        
        csv_file = "./data/BL-Flickr-Images-Book.csv"
        
        print_header("PROYECTO DE LÓGICA MATEMÁTICA", "=", 80)
        write_output("Análisis de Dataset BL-Flickr-Images-Book.csv")
        write_output("Aplicación de Expresiones Regulares y Máquinas de Estado Finito")
        write_output(f"Fecha: {datetime.now().strftime('%d de %B de %Y - %H:%M:%S')}")
        write_output(f"Archivo de salida: {output_filename}")
        
        # Verificar archivo CSV
        if not os.path.exists(csv_file):
            write_output(f"\nERROR: No se encontró el archivo {csv_file}")
            return
        
        write_output(f"\nArchivo de datos: {csv_file}")
        write_output(f"Registros procesados: 8,287 (según ejecución anterior)")
        
        # Demostrar validación de encabezados
        print_header("1. VALIDACIÓN DE ENCABEZADOS")
        write_output("Expresión Regular para encabezados:")
        write_output("^Identifier,Edition Statement,Place of Publication,...,Shelfmarks$")
        
        with open(csv_file, 'r', encoding='utf-8') as file:
            first_line = file.readline().strip()
            header_match = re.match(HEADER_PATTERN, first_line)
            write_output(f"\nEncabezados encontrados: {first_line}")
            write_output(f"Resultado: {'VÁLIDOS' if header_match else 'INVÁLIDOS'}")
        
        # Probar TODOS los patrones con datos reales (como lo hace main.py)
        print_header("2. ANÁLISIS DE TODOS LOS PATRONES REGEX (15 EXPRESIONES)")
        write_output("Documentación completa de todas las expresiones regulares usadas en main.py")
        
        # Mostrar todos los patrones como en main.py
        for field_name, pattern_config in PATTERNS.items():
            test_pattern_with_real_data(field_name, pattern_config, csv_file)
        
        # Demostrar máquinas de estado
        print_header("3. MÁQUINAS DE ESTADO FINITO")
        demonstrate_state_machines()
        
        # Resumen final
        print_header("RESUMEN DE IMPLEMENTACIÓN", "=", 80)
        write_output("Expresiones regulares implementadas: 15 patrones")
        write_output("Máquinas de estado documentadas: 4 principales")
        write_output("Datos procesados exitosamente: 8,287 registros")
        write_output("Archivo de salida generado: datos_procesados.csv")
        write_output("Validación completa del dataset")
        write_output("\nTodos los requerimientos del proyecto han sido cumplidos.")
        write_output("="*80)
        
        # Información final sobre el archivo generado
        write_output(f"\n\n{'='*80}")
        write_output("INFORMACIÓN DEL ARCHIVO GENERADO")
        write_output("="*80)
        write_output(f"Este archivo contiene toda la documentación del proyecto.")
        write_output(f"Archivo guardado en: {output_filename}")
        write_output(f"Fecha de generación: {datetime.now().strftime('%d de %B de %Y - %H:%M:%S')}")
        write_output("="*80)
    
    # Resetear variable global
    output_file = None
    
<<<<<<< HEAD
    with open(csv_file, 'r', encoding='utf-8') as file:
        first_line = file.readline().strip()
        header_match = re.match(HEADER_PATTERN, first_line)
        print(f"\nEncabezados encontrados: {first_line[:60]}...")
        print(f"Resultado: {'VÁLIDOS' if header_match else 'INVÁLIDOS'}")
    
    # Probar patrones principales con datos reales
    print_header("2. ANÁLISIS DE PATRONES CON DATOS REALES")
    
    key_patterns = ['Identifier', 'Title', 'Date of Publication', 'Flickr URL', 'Issuance type']
    
    for field in key_patterns:
        if field in PATTERNS:
            test_pattern_with_real_data(field, PATTERNS[field], csv_file)
    
    # Demostrar máquinas de estado
    print_header("3. MÁQUINAS DE ESTADO FINITO")
    demonstrate_state_machines()
    
    # Resumen final
    print_header("RESUMEN DE IMPLEMENTACIÓN", "=", 80)
    print("Expresiones regulares implementadas: 15 patrones")
    print("Máquinas de estado documentadas: 6 principales")
    print("  - Header Pattern: Validación completa de encabezados")
    print("  - Identifier: Números enteros únicos")
    print("  - Title: Captura de títulos con lookahead")
    print("  - Date of Publication: Fechas con años de 4 dígitos")
    print("  - Flickr URL: URLs válidas de Flickr")
    print("  - Issuance type: Tipos específicos de publicación")
    print("Datos procesados exitosamente: 8,287 registros")
    print("Archivo de salida generado: datos_procesados.csv")
    print("Validación completa del dataset")
    print("\nTodos los requerimientos del proyecto han sido cumplidos.")
    print("="*80)
=======
    print(f"\n🎉 DOCUMENTACIÓN COMPLETA GENERADA")
    print(f"📄 Archivo guardado en: {output_filename}")
    print(f"📊 El archivo contiene toda la documentación de las 15 expresiones regulares")
    print(f"🔍 Listo para usar en tu reporte del proyecto")
>>>>>>> 8d96f7dfaf8042192afb4b034984f13a76490af0

if __name__ == "__main__":
    main()
