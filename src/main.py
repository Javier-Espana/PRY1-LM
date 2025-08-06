# Programa principal para el procesamiento de dataset BL-Flickr-Images-Book.csv
# Este módulo coordina todo el flujo de trabajo del proyecto:
# 1. Carga del archivo CSV como texto plano
# 2. Validación de estructura de encabezados usando regex
# 3. Aplicación de patrones regex para extraer y validar datos
# 4. Transformación de datos a estructura pandas DataFrame
# 5. Exportación de resultados procesados

from config import DATA_PATH, OUTPUT_PATH
from processors import load_file, validate_headers, parse_content
from validators import test_patterns
from utils import create_dataframe, save_results

def main():
    """
    Función principal que ejecuta el pipeline completo de procesamiento.
    
    El flujo incluye:
    - Carga del archivo CSV sin usar librerías especializadas (solo como texto)
    - Validación de estructura mediante expresiones regulares
    - Procesamiento de contenido aplicando patrones regex específicos
    - Conversión final a DataFrame con tipos de datos apropiados
    - Guardado de resultados y generación de resumen estadístico
    
    Raises:
        ValueError: Si los encabezados del CSV no coinciden con el patrón esperado
        Exception: Para cualquier error durante el procesamiento
    """
    try:
        print("Iniciando procesamiento del archivo CSV")
        
        # Paso 1: Cargar archivo CSV como texto plano (sin usar pandas/csv inicialmente)
        content = load_file(DATA_PATH) # Usa la función de processors para cargar el archivo
        
        # Paso 2: Validar que los encabezados coincidan con el patrón regex esperado
        if not validate_headers(content): # Usa validate_headers del processors.py para validar encabezados
            raise ValueError("Encabezados no válidos") # Esto detiene el procesamiento si los encabezados no coinciden
        
        # Paso 3: Ejecutar pruebas de validación de todos los patrones regex definidos
        test_results = test_patterns() # Usa la función de validators para validar todos los patrones
        print("Pruebas de patrones regex completadas")
        
        # Paso 4: Procesar el contenido aplicando algoritmos de parsing y regex
        headers, data = parse_content(content) # Usa la función de processors para extraer datos
        
        # Paso 5: Crear DataFrame de pandas con tipos de datos correctos
        df = create_dataframe(headers, data) # Usa la función de utils para crear el DataFrame y lo guarda en df
        
        # Paso 6: Guardar resultados procesados en archivo CSV de salida
        save_results(df, OUTPUT_PATH) # Usa la función de utils para guardar el DataFrame
        print(f"Resultados guardados en {OUTPUT_PATH}")
        
        # Mostrar resumen estadístico del procesamiento realizado
        print("\nResumen del procesamiento:")
        print(f"- Registros procesados: {len(df)}")
        print(f"- Columnas: {list(df.columns)}")
        print("\nEjemplo de datos:")
        print(df.head(3))
        
    except Exception as e:
        print(f"Error en el procesamiento: {str(e)}")
        raise

if __name__ == "__main__":
    main()