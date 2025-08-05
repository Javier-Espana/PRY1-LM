# Máquina de Estado Finito - Flickr URL

## Expresión Regular: `^(https?://[^\s,]+flickr\.com[^\s,]*)(?=,|$)`

### Descripción
Esta expresión regular reconoce URLs válidas de Flickr que comiencen con http o https.

### Diagrama de Estado

```
Estado Inicial (q0) --[h]--> q1 --[t]--> q2 --[t]--> q3 --[p]--> q4
                                                                   |
                                                                   v
                                                                  q5 --[s]--> q6
                                                                   |           |
                                                                   [:]         [:]
                                                                   |           |
                                                                   v           v
                                                              q7 --[/]--> q8 --[/]--> q9
                                                                                       |
                                                                                [no whitespace, no comma]
                                                                                       |
                                                                                       v
                                                                               q10 (buscar "flickr.com")
                                                                                       |
                                                                                [resto de URL]
                                                                                       |
                                                                                       v
                                                                              Estado Final (q11)
```

### Estados:
- **q0-q9**: Validando prefijo "http://" o "https://"
- **q10**: Buscando "flickr.com" en la URL
- **q11**: Estado de aceptación - URL de Flickr válida

### Ejemplos:
- Válidos: "http://www.flickr.com/photos/britishlibrary/tags/sysnum000000206"
- Inválidos: "http://google.com", "flickr.com", "ftp://flickr.com"
