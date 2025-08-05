# Máquina de Estado Finito - Issuance Type

## Expresión Regular: `^(monographic|serial|integrating resource)(?=,|$)`

### Descripción
Esta expresión regular reconoce tipos específicos de publicación: monographic, serial, o integrating resource.

### Diagrama de Estado

```
Estado Inicial (q0) 
    |
    |--[m]--> q1 --[o]--> q2 --[n]--> q3 --[o]--> q4 --[g]--> q5 --[r]--> q6 --[a]--> q7 --[p]--> q8 --[h]--> q9 --[i]--> q10 --[c]--> Estado Final (qf1)
    |
    |--[s]--> q11 --[e]--> q12 --[r]--> q13 --[i]--> q14 --[a]--> q15 --[l]--> Estado Final (qf2)
    |
    |--[i]--> q16 --[n]--> q17 --[t]--> q18 --[e]--> q19 --[g]--> q20 --[r]--> q21 --[a]--> q22 --[t]--> q23 --[i]--> q24 --[n]--> q25 --[g]--> q26 --> [ ]--> q27 --[r]--> q28 --[e]--> q29 --[s]--> q30 --[o]--> q31 --[u]--> q32 --[r]--> q33 --[c]--> q34 --[e]--> Estado Final (qf3)
```

### Estados:
- **q0**: Estado inicial
- **qf1**: Aceptación para "monographic"
- **qf2**: Aceptación para "serial"
- **qf3**: Aceptación para "integrating resource"

### Ejemplos:
- Válidos: "monographic", "serial", "integrating resource"
- Inválidos: "book", "magazine", "unknown", "mono"
