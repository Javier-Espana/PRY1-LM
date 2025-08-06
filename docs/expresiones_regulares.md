# Expresiones Regulares Utilizadas - Proyecto BL-Flickr-Images-Book

Este documento describe todas las expresiones regulares implementadas para el análisis del dataset BL-Flickr-Images-Book.csv según los requerimientos de la materia Lógica Matemática.

## 1. Validación de Encabezados
- **Patrón**: `^Identifier,Edition Statement,Place of Publication,Date of Publication,Publisher,Title,Author,Contributors,Corporate Author,Corporate Contributors,Former owner,Engraver,Issuance type,Flickr URL,Shelfmarks$`
- **Descripción**: Valida el orden exacto de las columnas separadas por comas
- **Propósito**: Asegurar que el archivo CSV tiene la estructura esperada

## 2. Campos de Datos

### 2.1 Identifier
- **Patrón**: `^\d+`
- **Descripción**: Secuencia de dígitos que identifican de manera única cada registro en el dataset
- **Ejemplo válido**: `000000206`, `123456`
- **Ejemplo inválido**: `ABC123`, texto vacío
- **Máquina de estado**: Ver `docs/maquinas_estado/identifier.md`

### 2.2 Edition Statement
- **Patrón**: `^([^,]*?)(?=,|$)`
- **Descripción**: Declaración de edición del libro, captura texto libre hasta encontrar una coma o final de línea
- **Ejemplo válido**: `"A new edition, revised, etc."`, `"Fourth edition, revised, etc."`
- **Ejemplo inválido**: Campos que rompen la estructura CSV

### 2.3 Place of Publication
- **Patrón**: `^([^,]*?)(?=,|$)`
- **Descripción**: Lugar geográfico de publicación, extrae texto hasta la primera coma
- **Ejemplo válido**: `"London"`, `"London; Virtue & Yorston"`, `"pp. 40. G. Bryan & Co: Oxford, 1898"`
- **Ejemplo inválido**: Campos mal formateados en estructura CSV

### 2.4 Date of Publication (Patrón Importante)
- **Patrón**: `^([^,]*\d{4}[^,]*)(?=,|$)`
- **Descripción**: Fecha de publicación que debe contener un año de exactamente 4 dígitos, permite texto adicional
- **Ejemplo válido**: `"1879 [1878]"`, `"1851"`, `"1839, 38-54"`, `"[1847, 48 [1846-48]"`
- **Ejemplo inválido**: `"No date"`, fechas sin año de 4 dígitos
- **Máquina de estado**: Ver `docs/maquinas_estado/date_publication.md`

### 2.5 Publisher
- **Patrón**: `^([^,]*?)(?=,|$)`
- **Descripción**: Nombre del editor/publisher
- **Ejemplo válido**: `"S. Tinsley & Co."`, `"Virtue & Co."`, `"Bradbury, Evans & Co."`
- **Ejemplo inválido**: Formatos que rompen CSV

### 2.6 Title
- **Patrón**: `^([^,]*?)(?=,|$)`
- **Descripción**: Título del libro, texto hasta la primera coma
- **Ejemplo válido**: `"Walter Forbes. [A novel.] By A. A"`, `"All for Greed. [A novel...]"`
- **Ejemplo inválido**: Títulos mal formateados

### 2.7 Author
- **Patrón**: `^([^,]*?)(?=,|$)`
- **Descripción**: Nombre del autor, puede contener iniciales y apellidos
- **Ejemplo válido**: `"A. A."`, `"A., A. A."`, `"AALL, Jacob."`
- **Ejemplo inválido**: Formatos de nombre incorrectos

### 2.8 Contributors
- **Patrón**: `^([^,]*?)(?=,|$)`
- **Descripción**: Contribuidores del libro
- **Ejemplo válido**: `"FORBES, Walter."`, `"BLAZE DE BURY, Marie Pauline Rose - Baroness"`
- **Ejemplo inválido**: Formatos incorrectos

### 2.9 Corporate Author
- **Patrón**: `^([^,]*?)(?=,|$)`
- **Descripción**: Autor corporativo si aplica
- **Ejemplo válido**: `"British Library"`, campos vacíos (la mayoría)
- **Ejemplo inválido**: Formatos incorrectos

### 2.10 Corporate Contributors
- **Patrón**: `^([^,]*?)(?=,|$)`
- **Descripción**: Contribuidores corporativos
- **Ejemplo válido**: `"Oxford University Press"`, campos vacíos (la mayoría)
- **Ejemplo inválido**: Formatos incorrectos

### 2.11 Former owner
- **Patrón**: `^([^,]*?)(?=,|$)`
- **Descripción**: Propietario anterior del libro
- **Ejemplo válido**: `"Panizzi, Anthony - Sir"`, campos vacíos (la mayoría)
- **Ejemplo inválido**: Formatos que rompen la estructura CSV

### 2.12 Engraver
- **Patrón**: `^([^,]*?)(?=,|$)`
- **Descripción**: Grabador si aplica
- **Ejemplo válido**: `"William Hogarth"`, campos vacíos (la mayoría)
- **Ejemplo inválido**: Formatos incorrectos

### 2.13 Issuance type (Patrón Importante)
- **Patrón**: `^(monographic|serial|integrating resource|continuing)(?=,|$)`
- **Descripción**: Tipo de publicación: monográfica, serie, recurso integrado o continuo
- **Ejemplo válido**: `"monographic"`, `"serial"`, `"integrating resource"`, `"continuing"`
- **Ejemplo inválido**: `"book"`, `"magazine"`, `"unknown"`
- **Máquina de estado**: Ver `docs/maquinas_estado/issuance_type.md`

### 2.14 Flickr URL (Patrón Importante)
- **Patrón**: `^(https?://[^\s,]*flickr\.com[^\s,]*)(?=,|$)`
- **Descripción**: URL válida de Flickr que debe comenzar con protocolo HTTP/HTTPS y contener el dominio flickr.com
- **Ejemplo válido**: `"http://www.flickr.com/photos/britishlibrary/tags/sysnum000000206"`
- **Ejemplo inválido**: `"http://google.com"`, URLs que no son de Flickr
- **Máquina de estado**: Ver `docs/maquinas_estado/flickr_url.md`

### 2.15 Shelfmarks
- **Patrón**: `^([^,]*?)(?=,|$)`
- **Descripción**: Códigos de ubicación física del libro en la biblioteca, sistema de clasificación interno
- **Ejemplo válido**: `"British Library HMNTS 12641.b.30."`, `"British Library HMNTS|British Library HMNTS 796.i.18-21."`
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
- **Identifier**: Reconocimiento de secuencias de dígitos
- **Date of Publication**: Extracción de años de fechas complejas  
- **Flickr URL**: Validación de URLs específicas de Flickr
- **Issuance type**: Reconocimiento de tipos de publicación específicos

Cada máquina de estado se encuentra documentada en `docs/maquinas_estado/` con diagramas detallados y ejemplos de funcionamiento.