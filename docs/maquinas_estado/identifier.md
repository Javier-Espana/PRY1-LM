# Máquina de Estado Finito - Identifier

## Expresión Regular: `^\d+`

### Descripción
Esta expresión regular reconoce números enteros positivos que identifican de manera única cada registro en el dataset.

### Diagrama de Estado

```
Estado Inicial (q0) --[dígito 0-9]--> Estado Aceptación (q1)
                                           |
                                      [dígito 0-9]
                                           |
                                           v
                                      Estado Aceptación (q1)
```

### Estados:
- **q0**: Estado inicial - esperando el primer dígito
- **q1**: Estado de aceptación - uno o más dígitos válidos

### Transiciones:
- q0 → q1: al leer cualquier dígito [0-9]
- q1 → q1: al leer cualquier dígito adicional [0-9]

### Alfabeto: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

### Ejemplos:
- Válidos: "123", "000000206", "1", "999999"
- Inválidos: "ABC123", "12.34", "", "a123"

### Representación Formal:
- **Q** = {q0, q1}
- **Σ** = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
- **δ**: función de transición definida arriba
- **q0**: estado inicial
- **F** = {q1}: conjunto de estados finales