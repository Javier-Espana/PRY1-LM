# Funciones de validación y pruebas de patrones
import re
import logging
from . import patterns

logger = logging.getLogger(__name__)

def test_patterns():
    """Ejecuta pruebas de validación para todos los patrones"""
    results = {}
    
    for field, config in patterns.PATTERNS.items():
        pattern = config['pattern']
        valid = config['example_valid']
        invalid = config['example_invalid']
        
        # Probar ejemplo válido
        valid_match = re.match(pattern, valid)
        valid_result = valid_match is not None
        
        # Probar ejemplo inválido
        invalid_match = re.match(pattern, invalid) if invalid else None
        invalid_result = invalid_match is None if invalid else True
        
        results[field] = {
            'valid_test': valid_result,
            'invalid_test': invalid_result,
            'pattern': pattern
        }
        
        if not valid_result:
            logger.warning(f"Patrón para '{field}' no coincide con ejemplo válido: {valid}")
        if not invalid_result:
            logger.warning(f"Patrón para '{field}' coincide con ejemplo inválido: {invalid}")
    
    return results

def generate_regex_tests():
    """Genera pruebas para documentación"""
    tests = []
    
    for field, config in patterns.PATTERNS.items():
        test = {
            'field': field,
            'pattern': config['pattern'],
            'description': config['description'],
            'examples': [
                {'input': config['example_valid'], 'should_match': True},
                {'input': config['example_invalid'], 'should_match': False} if config['example_invalid'] else None
            ]
        }
        tests.append(test)
    
    return tests