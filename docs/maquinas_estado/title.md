# Máquina de Estado Finito - Title

## Expresión Regular: `^([^,]*?)(?=,|$)`

### Descripción
Esta expresión regular reconoce el título del libro, capturando cualquier texto hasta encontrar la primera coma o el final de la cadena. Utiliza un grupo de captura no codicioso para extraer el contenido del título.

### Diagrama de Estado

```
Estado Inicial (q0) --[cualquier char != ',']--> Estado Intermedio (q1)
     |                                               |
     |                                     [cualquier char != ',']
     |                                               |
     |                                               v
     |                                         Estado Intermedio (q1) --[lookahead: ',' o fin]--> Estado Final (q2)
     |                                               |
     [fin de cadena]                        [fin de cadena]
     |                                               |
     v                                               v
Estado Final (q2)                            Estado Final (q2)
```

### Diagrama Detallado

```
                    [a-z, A-Z, 0-9, espacio, ., [, ], (, ), ", ', -, ;, :, etc. EXCEPTO ',']
                              ┌─────────────────────────────────────────────────────────────┐
                              │                                                             │
                              │                                                             ▼
Estado Inicial (q0) ────────────────────────────────────────────────────────► Estado Intermedio (q1)
     │                [cualquier carácter válido para título != ',']                       │
     │                                                                                     │
     │ [fin de cadena '$']                                                                 │ [lookahead: ',' o '$']
     │                                                                                     │
     ▼                                                                                     ▼
Estado Final Vacío (q_empty) ◄─────────────────────────────────────────────► Estado Final (q2)
                                              [captura realizada]
```

### Estados:
- **q0**: Estado inicial - puede aceptar cadena vacía o primer carácter del título
- **q1**: Estado intermedio - acumulando caracteres del título
- **q2**: Estado de aceptación - título capturado exitosamente
- **q_empty**: Estado de aceptación para títulos vacíos

### Transiciones:
- **q0 → q1**: al leer cualquier carácter válido para título (no coma)
- **q1 → q1**: al continuar leyendo caracteres válidos (no coma)
- **q1 → q2**: cuando el lookahead detecta ',' o final de cadena
- **q0 → q_empty**: cuando la cadena está vacía (título vacío)

### Funcionamiento del Lookahead `(?=,|$)`:
El lookahead positivo verifica que después del contenido capturado venga:
- Una coma `,` (indicando que hay más campos)
- Final de cadena `$` (último campo del registro)

### Caracteres válidos para título:
- Letras mayúsculas y minúsculas: [A-Za-z]
- Dígitos: [0-9]
- Espacios y puntuación: ` ` `.` `[` `]` `(` `)` `"` `'` `-` `;` `:` `!` `?`
- Caracteres especiales excepto coma

### Alfabeto: 
{A-Z, a-z, 0-9, espacio, ., [, ], (, ), ", ', -, ;, :, !, ?, todos excepto ','}

### Ejemplos:
- Válidos: 
  - "Walter Forbes. [A novel.] By A. A"
  - "All for Greed. [A novel. The dedication signed: A. A. A., i.e. Marie Pauline Rose, Baroness Blaze de Bury.]"
  - "Love the Avenger. By the author of \"All for Greed.\""
  - "Welsh Sketches, chiefly ecclesiastical, to the close of the twelfth century"
  - "" (título vacío)
  
- Inválidos en contexto CSV: 
  - Títulos que no respeten el formato CSV
  - Campos con comillas mal balanceadas en el contexto completo

### Representación Formal:
- **Q** = {q0, q1, q2, q_empty}
- **Σ** = {todos los caracteres ASCII excepto ','}
- **δ**: función de transición definida arriba
- **q0**: estado inicial
- **F** = {q2, q_empty}: conjunto de estados finales

### Simulación paso a paso:

#### Ejemplo 1: "Walter Forbes. [A novel.] By A. A"
```
Paso 1: 'W' | q0 → q1 (primer carácter del título)
Paso 2: 'a' | q1 → q1 (continuando título)
Paso 3: 'l' | q1 → q1 (continuando título)
...
Paso 34: 'A' | q1 → q1 (último carácter)
Paso 35: lookahead detecta ',' o '$' | q1 → q2 (captura completada)
Estado final: q2 | Resultado: ACEPTA
Grupo capturado: "Walter Forbes. [A novel.] By A. A"
```

#### Ejemplo 2: "" (cadena vacía)
```
Paso 1: fin de cadena detectado | q0 → q_empty (título vacío válido)
Estado final: q_empty | Resultado: ACEPTA
Grupo capturado: ""
```
