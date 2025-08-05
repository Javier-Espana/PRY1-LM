# Expresiones Regulares Utilizadas

## Encabezados
- **Patrón**: `^Identifier\tEdition Statement\t...\tShelfmarks$`
- **Descripción**: Valida el orden exacto de las columnas separadas por tabs

## Campos

### Identifier
- **Patrón**: `^\d+`
- **Descripción**: Números enteros positivos
- **Ejemplo válido**: `12345`
- **Ejemplo inválido**: `ABC123`

### Date of Publication
- **Patrón**: `^(\d{4}(-\d{2}(-\d{2})?)?|\[\d{4}\])?`
- **Descripción**: Años en formato YYYY, YYYY-MM o YYYY-MM-DD, o [YYYY]
- **Ejemplo válido**: `1892`, `1892-05`, `[1892]`
- **Ejemplo inválido**: `May 15, 1892`

### Flickr URL
- **Patrón**: `^((https?://)?(www\.)?flickr\.com/[^\s\t]+)?`
- **Descripción**: URLs válidas de Flickr (opcional)
- **Ejemplo válido**: `https://www.flickr.com/photos/123`
- **Ejemplo inválido**: `http://example.com`