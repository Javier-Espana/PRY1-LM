# Expresiones Regulares Utilizadas - Proyecto BL-Flickr-Images-Book

Este documento### 2.13 Issuance type (Patrón Importante)
- **Patrón**: `^(monographic|serial|integrating resource)(?=,|$)`
- **Descripción**: Tipo de publicación: monográfica, serie o recurso integrado
- **Ejemplo válido**: `"monographic"`, `"serial"`, `"integrating resource"`
- **Ejemplo inválido**: `"book"`, `"magazine"`, `"unknown"`
- **Máquina de estado**: Ver `docs/maquinas_estado/issuance_type.md`

### 2.14 Flickr URL (Patrón Importante)
- **Patrón**: `^(https?://[^\s,]*flickr\.com[^\s,]*)(?=,|$)`
- **Descripción**: URL válida de Flickr
- **Ejemplo válido**: `"http://www.flickr.com/photos/britishlibrary/tags/sysnum000000206"`
- **Ejemplo inválido**: `"http://google.com"`, URLs que no son de Flickr
- **Máquina de estado**: Ver `docs/maquinas_estado/flickr_url.md`as las expresiones regulares implementadas para el análisis del dataset BL-Flickr-Images-Book.csv según los requerimientos de la materia Lógica Matemática.

## 1. Validación de Encabezados
- **Patrón**: `^Identifier,Edition Statement,Place of Publication,Date of Publication,Publisher,Title,Author,Contributors,Corporate Author,Corporate Contributors,Former owner,Engraver,Issuance type,Flickr URL,Shelfmarks$`
- **Descripción**: Valida el orden exacto de las columnas separadas por comas
- **Propósito**: Asegurar que el archivo CSV tiene la estructura esperada
- **Máquina de estado**: Ver `docs/maquinas_estado/header_pattern.md`

## 2. Campos de Datos

### 2.1 Identifier
- **Patrón**: `^\d+`
- **Descripción**: Números enteros positivos que identifican únicamente cada registro
- **Ejemplo válido**: `000000206`, `123456`
- **Ejemplo inválido**: `ABC123`, texto vacío
- **Máquina de estado**: Ver `docs/maquinas_estado/identifier.md`

### 2.2 Edition Statement
- **Patrón**: `^([^,]*?)(?=,|$)`
- **Descripción**: Declaración de edición, texto libre hasta la primera coma
- **Ejemplo válido**: `"A new edition, revised, etc."`
- **Ejemplo inválido**: Campos con formato incorrecto

### 2.3 Place of Publication
- **Patrón**: `^([^,]*?)(?=,|$)`
- **Descripción**: Lugar de publicación, puede contener texto hasta la primera coma
- **Ejemplo válido**: `"London"`, `"London; Virtue & Yorston"`
- **Ejemplo inválido**: Campos mal formateados

### 2.4 Date of Publication (Patrón Importante)
- **Patrón**: `^([^,]*\d{4}[^,]*)(?=,|$)`
- **Descripción**: Fecha de publicación que contiene un año de 4 dígitos
- **Ejemplo válido**: `"1879 [1878]"`, `"1851"`, `"pp. 40. G. Bryan & Co: Oxford, 1898"`
- **Ejemplo inválido**: `"No date"`, `"May 15"`
- **Máquina de estado**: Ver `docs/maquinas_estado/date_publication.md`

### 2.5 Publisher
- **Patrón**: `^([^,]*?)(?=,|$)`
- **Descripción**: Nombre del editor/publisher
- **Ejemplo válido**: `"S. Tinsley & Co."`, `"Virtue & Co."`
- **Ejemplo inválido**: Formatos incorrectos

### 2.6 Title
- **Patrón**: `^([^,]*?)(?=,|$)`
- **Descripción**: Título del libro, texto hasta la primera coma
- **Ejemplo válido**: `"Walter Forbes. [A novel.] By A. A"`
- **Ejemplo inválido**: Formatos de título incorrectos
- **Máquina de estado**: Ver `docs/maquinas_estado/title.md`

### 2.7 Author
- **Patrón**: `^([^,]*?)(?=,|$)`
- **Descripción**: Nombre del autor, puede contener iniciales y apellidos
- **Ejemplo válido**: `"A. A."`, `"Shakespeare, William"`
- **Ejemplo inválido**: Formatos de nombre incorrectos

### 2.8 Contributors
- **Patrón**: `^([^,]*?)(?=,|$)`
- **Descripción**: Contribuidores del libro
- **Ejemplo válido**: `"FORBES, Walter."`
- **Ejemplo inválido**: Formatos incorrectos

### 2.9 Corporate Author
- **Patrón**: `^([^,]*?)(?=,|$)`
- **Descripción**: Autor corporativo si aplica
- **Ejemplo válido**: `"British Library"`
- **Ejemplo inválido**: Formatos incorrectos

### 2.10 Corporate Contributors
- **Patrón**: `^([^,]*?)(?=,|$)`
- **Descripción**: Contribuidores corporativos
- **Ejemplo válido**: `"Oxford University Press"`
- **Ejemplo inválido**: Formatos incorrectos

### 2.11 Former owner
- **Patrón**: `^([^,]*?)(?=,|$)`
- **Descripción**: Propietario anterior del libro
- **Ejemplo válido**: `"John Smith Collection"`
- **Ejemplo inválido**: Formatos incorrectos

### 2.12 Engraver
- **Patrón**: `^([^,]*?)(?=,|$)`
- **Descripción**: Grabador si aplica
- **Ejemplo válido**: `"William Hogarth"`
- **Ejemplo inválido**: Formatos incorrectos

### 2.13 Issuance type (Patrón Importante)
- **Patrón**: `^(monographic|serial|integrating resource)(?=,|$)`
- **Descripción**: Tipo de publicación: monográfica, serie o recurso integrado
- **Ejemplo válido**: `"monographic"`, `"serial"`, `"integrating resource"`
- **Ejemplo inválido**: `"book"`, `"magazine"`, `"unknown"`
- **Máquina de estado**: Ver `docs/maquinas_estado/issuance_type.md`

### 2.14 Flickr URL (Patrón Importante)
- **Patrón**: `^(https?://[^\s,]+flickr\.com[^\s,]*)(?=,|$)`
- **Descripción**: URL válida de Flickr
- **Ejemplo válido**: `"http://www.flickr.com/photos/britishlibrary/tags/sysnum000000206"`
- **Ejemplo inválido**: `"http://google.com"`, URLs que no son de Flickr
- **Máquina de estado**: Ver `docs/maquinas_estado/flickr_url.md`

### 2.15 Shelfmarks
- **Patrón**: `^([^,]*?)(?=,|$)`
- **Descripción**: Códigos de ubicación en biblioteca
- **Ejemplo válido**: `"British Library HMNTS 12641.b.30."`
- **Ejemplo inválido**: Formatos incorrectos

## 3. Notación Utilizada

### Símbolos de Expresiones Regulares:
- `^`: Inicio de línea
- `$`: Final de línea
- `\d`: Cualquier dígito (0-9)
- `+`: Una o más repeticiones
- `*`: Cero o más repeticiones
- `?`: Cero o una repetición (opcional)
- `[^,]`: Cualquier carácter excepto coma
- `(?=,|$)`: Lookahead positivo (busca coma o final de línea)
- `()`: Grupo de captura
- `|`: Alternancia (OR lógico)

### Estrategia de Parsing:
1. **Validación de estructura**: Verificar encabezados con regex
2. **Parsing por CSV**: Dividir por comas respetando comillas
3. **Validación de contenido**: Aplicar regex específicos a cada campo
4. **Limpieza y conversión**: Transformar a tipos de datos apropiados
5. **Creación de DataFrame**: Estructurar datos para análisis

## 4. Máquinas de Estado Finito

Se han desarrollado máquinas de estado finito para los patrones más importantes:
- **Identifier**: Reconocimiento de números enteros
- **Date of Publication**: Extracción de años de fechas complejas  
- **Flickr URL**: Validación de URLs específicas de Flickr
- **Issuance type**: Reconocimiento de tipos de publicación específicos

Cada máquina de estado se encuentra documentada en `docs/maquinas_estado/` con diagramas detallados y ejemplos de funcionamiento.