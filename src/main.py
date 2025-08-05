# Programa principal
import logging
import logging.config
from .config import LOGGING_CONFIG, DATA_PATH, OUTPUT_PATH
from .processors import load_file, validate_headers, parse_content
from .validators import test_patterns
from .utils import create_dataframe, save_results

def main():
    # Configurar logging
    logging.config.dictConfig(LOGGING_CONFIG)
    logger = logging.getLogger(__name__)
    
    try:
        logger.info("Iniciando procesamiento del archivo CSV")
        
        # 1. Cargar archivo
        content = load_file(DATA_PATH)
        
        # 2. Validar encabezados
        if not validate_headers(content):
            raise ValueError("Encabezados no válidos")
        
        # 3. Validar patrones regex
        test_results = test_patterns()
        logger.info("Pruebas de patrones regex completadas")
        
        # 4. Procesar contenido
        headers, data = parse_content(content)
        
        # 5. Crear DataFrame
        df = create_dataframe(headers, data)
        
        # 6. Guardar resultados
        save_results(df, OUTPUT_PATH)
        logger.info(f"Resultados guardados en {OUTPUT_PATH}")
        
        # Mostrar resumen
        print("\nResumen del procesamiento:")
        print(f"- Registros procesados: {len(df)}")
        print(f"- Columnas: {list(df.columns)}")
        print("\nEjemplo de datos:")
        print(df.head(3))
        
    except Exception as e:
        logger.error(f"Error en el procesamiento: {str(e)}")
        raise

if __name__ == "__main__":
    main()