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
        content = load_file(DATA_PATH)
        
        # Paso 2: Validar que los encabezados coincidan con el patrón regex esperado
        if not validate_headers(content):
            raise ValueError("Encabezados no válidos")
        
        # Paso 3: Ejecutar pruebas de validación de todos los patrones regex definidos
        test_results = test_patterns()
        print("Pruebas de patrones regex completadas")
        
        # Paso 4: Procesar el contenido aplicando algoritmos de parsing y regex
        headers, data = parse_content(content)
        
        # Paso 5: Crear DataFrame de pandas con tipos de datos correctos
        df = create_dataframe(headers, data)
        
        # Paso 6: Guardar resultados procesados en archivo CSV de salida
        save_results(df, OUTPUT_PATH)
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