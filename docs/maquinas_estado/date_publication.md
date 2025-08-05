# Máquina de Estado Finito - Date of Publication

## Expresión Regular: `^([^,]*\d{4}[^,]*)(?=,|$)`

### Descripción
Esta expresión regular reconoce fechas de publicación que contienen un año de 4 dígitos, permitiendo texto adicional antes y después del año.

### Diagrama de Estado

```
Estado Inicial (q0) --[cualquier char != ',']--> Estado Intermedio (q1)
     |                                               |
     |                                          [cualquier char != ',']
     |                                               |
     [dígito]                                        v
     |                                         Estado Intermedio (q1)
     v                                               |
Estado Año1 (q2) --[dígito]--> Estado Año2 (q3) --[dígito]--> Estado Año3 (q4) --[dígito]--> Estado Año4 (q5)
                                                                                                      |
                                                                                                [cualquier char != ',']
                                                                                                      |
                                                                                                      v
                                                                                              Estado Final (q6)
```

### Estados:
- **q0**: Estado inicial
- **q1**: Leyendo caracteres previos al año
- **q2-q5**: Leyendo los 4 dígitos del año
- **q6**: Estado de aceptación - año válido encontrado

### Ejemplos:
- Válidos: "1879 [1878]", "1851", "pp. 40. G. Bryan & Co: Oxford, 1898"
- Inválidos: "No date", "May 15", "abcd"
