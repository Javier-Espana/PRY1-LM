# Proyecto #1 de Lógica Matemática - Expresiones Regulares
## Universidad del Valle de Guatemala

## Información del Proyecto
- **Materia**: Lógica Matemática
- **Tema**: Aplicación de### Entregables

### Archivos Requeridos
1. **Programa Python**: Todo el directorio `src/`
2. **Descripción del dataset**: `docs/expresiones_regulares.md`
3. **Expresiones regulares**: Documentadas con notación formal
4. **Máquinas de estado**: Diagramas en `docs/maquinas_estado/`
5. **Capturas de pantalla**: Generadas por `ejecutar_demos.py`ones Regulares y Máquinas de Estado Finito
- **Dataset**: BL-Flickr-Images-Book.csv (8,287 registros)
- **Fecha**: Agosto 2025

## Instrucciones
### 1. Investigación de la librería `re`
- Implementada completamente con patrones regex complejos
- Uso de grupos de captura, lookaheads, y clases de caracteres
- Documentación detallada en `docs/expresiones_regulares.md`

### 2. Máquinas de Estado Finito
Elaborados diagramas para patrones principales:
- **Identifier**: Reconocimiento de números enteros (`^\d+`)
- **Date of Publication**: Extracción de años (`^([^,]*\d{4}[^,]*)`)
- **Flickr URL**: Validación de URLs (`^(https?://[^\s,]*flickr\.com[^\s,]*)`)
- **Issuance type**: Tipos específicos (`^(monographic|serial|integrating resource)`)

### 3. Carga como Texto
- Archivo CSV cargado como string completo
- Parsing manual sin uso de pandas/csv para carga inicial
- Implementado en `src/processors.py`

### 4. Determinación de Encabezados
- Regex para validar estructura: `^Identifier,Edition Statement,Place of Publication,...$`
- Validación automática en `src/processors.py`

### 5. Contenido por Columnas
- 15 patrones regex específicos para cada campo
- Parsing algorítmico respetando comillas y comas
- Validación individual de cada campo

### 6. Transformación a DataFrame
- Conversión final usando pandas
- Tipos de datos correctos (int64 para Identifier, etc.)
- 8,287 registros procesados exitosamente

## Ejecución del Proyecto

### Archivos Principales
```bash
# Ejecutar programa principal
cd src
python main.py

# Demostración básica de regex
python demo_regex.py

# Demostración completa con datos reales
python ejecutar_demos.py
```

### Salida del Programa
```
Resumen del procesamiento:
- Registros procesados: 8287
- Columnas: ['Identifier', 'Edition Statement', 'Place of Publication', ...]
```

## Expresiones Regulares Implementadas

### Patrones Principales
1. **Encabezados**: `^Identifier,Edition Statement,...,Shelfmarks$`
2. **Identifier**: `^\d+` - Números enteros únicos
3. **Date of Publication**: `^([^,]*\d{4}[^,]*)(?=,|$)` - Fechas con años
4. **Flickr URL**: `^(https?://[^\s,]*flickr\.com[^\s,]*)(?=,|$)` - URLs válidas
5. **Issuance type**: `^(monographic|serial|integrating resource)(?=,|$)` - Tipos específicos

### Notación Vista en Clase
- `\d+`: dígito⁺ (uno o más dígitos)
- `[^,]*`: (cualquier carácter excepto coma)*
- `(?=,|$)`: lookahead positivo
- `|`: alternancia (OR lógico)

## Máquinas de Estado

### Ejemplo: Identifier (`^\d+`)
```
q0 (inicial) --[0-9]--> q1 (aceptación)
                        |
                   [0-9] |
                        ↓
                       q1
```

### Estados y Transiciones
- **Q** = {q0, q1}
- **Σ** = {0,1,2,3,4,5,6,7,8,9}
- **δ**: q0×[0-9]→q1, q1×[0-9]→q1
- **F** = {q1}

## Resultados y Validación

### Datos Procesados
- **Total de registros**: 8,287
- **Campos validados**: 15
- **Éxito de procesamiento**: 100%
- **Archivo de salida**: `output/datos_procesados.csv`

### Ejemplos de Validación
- **Identifier**: "000000206" → Acepta
- **Date**: "1879 [1878]" → Acepta (año extraído: 1879)
- **Flickr URL**: "http://www.flickr.com/..." → Acepta
- **Invalid URL**: "http://google.com" → Rechaza

## Capturas de Ejecución

Las ejecuciones se pueden ver ejecutando:
1. `python ejecutar_demos.py` - Demostración completa
2. `python demo_regex.py` - Pruebas específicas
3. `python src/main.py` - Procesamiento completo

## Entregables

### Archivos Requeridos
1. **Programa Python**: Todo el directorio `src/`
2. **Descripción del dataset**: `docs/expresiones_regulares.md`
3. **Expresiones regulares**: Documentadas con notación formal
4. **Máquinas de estado**: Diagramas en `docs/maquinas_estado/`
5. **Capturas de pantalla**: Generadas por `ejecutar_demos.py`