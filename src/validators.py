# Módulo de funciones de validación y pruebas de patrones regex
# Este módulo proporciona funcionalidades para:
# - Ejecutar pruebas automáticas de todos los patrones definidos
# - Validar que las expresiones regulares funcionen correctamente
# - Detectar patrones que no coinciden con sus ejemplos de prueba

import re
import patterns

def test_patterns(): # Ejecuta pruebas de validación automática para todos los patrones regex definidos
    """
    Ejecuta pruebas de validación automática para todos los patrones regex definidos.
    
    Esta función itera sobre todos los patrones en el diccionario PATTERNS y:
    - Prueba cada patrón con su ejemplo válido (debe coincidir)
    - Prueba cada patrón con su ejemplo inválido (debe rechazar)
    - Registra advertencias si algún patrón no funciona como esperado
    - Retorna un diccionario con los resultados de todas las pruebas
    
    Returns:
        dict: Diccionario con resultados de pruebas para cada campo
              - valid_test: bool indicando si el ejemplo válido pasó
              - invalid_test: bool indicando si el ejemplo inválido fue rechazado
              - pattern: la expresión regular probada
    """
    results = {}
    
    # Iterar sobre todos los patrones definidos en el módulo patterns
    for field, config in patterns.PATTERNS.items(): # Verifica cada patrón regex con el PATTERNS definido en patterns.py
        pattern = config['pattern']
        valid = config['example_valid']
        invalid = config['example_invalid']
        
        # Probar que el ejemplo válido sea aceptado por el patrón
        valid_match = re.match(pattern, valid)
        valid_result = valid_match is not None
        
        # Probar que el ejemplo inválido sea rechazado por el patrón
        invalid_match = re.match(pattern, invalid) if invalid else None
        invalid_result = invalid_match is None if invalid else True
        
        # Almacenar resultados de las pruebas
        results[field] = {
            'valid_test': valid_result,
            'invalid_test': invalid_result,
            'pattern': pattern
        }
        
        # Mostrar advertencias si las pruebas fallan
        if not valid_result:
            print(f"ADVERTENCIA: Patrón para '{field}' no coincide con ejemplo válido: {valid}")
        if not invalid_result:
            print(f"ADVERTENCIA: Patrón para '{field}' coincide con ejemplo inválido: {invalid}")
    
    return results