# Máquina de Estado Finito - Header Pattern

## Expresión Regular: `^Identifier,Edition Statement,Place of Publication,Date of Publication,Publisher,Title,Author,Contributors,Corporate Author,Corporate Contributors,Former owner,Engraver,Issuance type,Flickr URL,Shelfmarks$`

### Descripción
Esta expresión regular valida que los encabezados del archivo CSV coincidan exactamente con la estructura esperada, verificando el orden y los nombres exactos de las 15 columnas.

### Diagrama de Estado

```
Estado Inicial (q0) --[I]--> q1 --[d]--> q2 --[e]--> q3 --[n]--> q4 --[t]--> q5 --[i]--> q6 --[f]--> q7 --[i]--> q8 --[e]--> q9 --[r]--> q10 --[,]--> q11
                                                                                                                                                              |
q11 --[E]--> q12 --[d]--> q13 --[i]--> q14 --[t]--> q15 --[i]--> q16 --[o]--> q17 --[n]--> q18 --> [ ] --> q19 --[S]--> q20 --[t]--> q21 --[a]--> q22 --[t]--> q23 --[e]--> q24 --[m]--> q25 --[e]--> q26 --[n]--> q27 --[t]--> q28 --[,]--> q29
                                                                                                                                                                                                                                                            |
q29 --[P]--> q30 --[l]--> q31 --[a]--> q32 --[c]--> q33 --[e]--> q34 --> [ ] --> q35 --[o]--> q36 --[f]--> q37 --> [ ] --> q38 --[P]--> q39 --[u]--> q40 --[b]--> q41 --[l]--> q42 --[i]--> q43 --[c]--> q44 --[a]--> q45 --[t]--> q46 --[i]--> q47 --[o]--> q48 --[n]--> q49 --[,]--> q50
                                                                                                                                                                                                                                                                                                    |
q50 --[D]--> q51 --[a]--> q52 --[t]--> q53 --[e]--> q54 --> [ ] --> q55 --[o]--> q56 --[f]--> q57 --> [ ] --> q58 --[P]--> q59 --[u]--> q60 --[b]--> q61 --[l]--> q62 --[i]--> q63 --[c]--> q64 --[a]--> q65 --[t]--> q66 --[i]--> q67 --[o]--> q68 --[n]--> q69 --[,]--> q70
                                                                                                                                                                                                                                                              |
q70 --[P]--> q71 --[u]--> q72 --[b]--> q73 --[l]--> q74 --[i]--> q75 --[s]--> q76 --[h]--> q77 --[e]--> q78 --[r]--> q79 --[,]--> q80
                                                                                                          |
q80 --[T]--> q81 --[i]--> q82 --[t]--> q83 --[l]--> q84 --[e]--> q85 --[,]--> q86
                                                                   |
q86 --[A]--> q87 --[u]--> q88 --[t]--> q89 --[h]--> q90 --[o]--> q91 --[r]--> q92 --[,]--> q93
                                                                               |
q93 --[C]--> q94 --[o]--> q95 --[n]--> q96 --[t]--> q97 --[r]--> q98 --[i]--> q99 --[b]--> q100 --[u]--> q101 --[t]--> q102 --[o]--> q103 --[r]--> q104 --[s]--> q105 --[,]--> q106
                                                                                                                                                                                |
q106 --[C]--> q107 --[o]--> q108 --[r]--> q109 --[p]--> q110 --[o]--> q111 --[r]--> q112 --[a]--> q113 --[t]--> q114 --[e]--> q115 --> [ ] --> q116 --[A]--> q117 --[u]--> q118 --[t]--> q119 --[h]--> q120 --[o]--> q121 --[r]--> q122 --[,]--> q123
                                                                                                                                                                                                                                                      |
q123 --[C]--> q124 --[o]--> q125 --[r]--> q126 --[p]--> q127 --[o]--> q128 --[r]--> q129 --[a]--> q130 --[t]--> q131 --[e]--> q132 --> [ ] --> q133 --[C]--> q134 --[o]--> q135 --[n]--> q136 --[t]--> q137 --[r]--> q138 --[i]--> q139 --[b]--> q140 --[u]--> q141 --[t]--> q142 --[o]--> q143 --[r]--> q144 --[s]--> q145 --[,]--> q146
                                                                                                                                                                                                                                                                                                                                                              |
q146 --[F]--> q147 --[o]--> q148 --[r]--> q149 --[m]--> q150 --[e]--> q151 --[r]--> q152 --> [ ] --> q153 --[o]--> q154 --[w]--> q155 --[n]--> q156 --[e]--> q157 --[r]--> q158 --[,]--> q159
                                                                                                                                                                                    |
q159 --[E]--> q160 --[n]--> q161 --[g]--> q162 --[r]--> q163 --[a]--> q164 --[v]--> q165 --[e]--> q166 --[r]--> q167 --[,]--> q168
                                                                                                                   |
q168 --[I]--> q169 --[s]--> q170 --[s]--> q171 --[u]--> q172 --[a]--> q173 --[n]--> q174 --[c]--> q175 --[e]--> q176 --> [ ] --> q177 --[t]--> q178 --[y]--> q179 --[p]--> q180 --[e]--> q181 --[,]--> q182
                                                                                                                                                                                                |
q182 --[F]--> q183 --[l]--> q184 --[i]--> q185 --[c]--> q186 --[k]--> q187 --[r]--> q188 --> [ ] --> q189 --[U]--> q190 --[R]--> q191 --[L]--> q192 --[,]--> q193
                                                                                                                                                     |
q193 --[S]--> q194 --[h]--> q195 --[e]--> q196 --[l]--> q197 --[f]--> q198 --[m]--> q199 --[a]--> q200 --[r]--> q201 --[k]--> q202 --[s]--> Estado Final (q203)
```

### Estados:
- **q0**: Estado inicial
- **q1-q202**: Estados intermedios para reconocer cada carácter de los encabezados
- **q203**: Estado de aceptación - encabezados válidos

### Transiciones principales:
1. **q0 → q10**: Reconoce "Identifier"
2. **q11 → q28**: Reconoce "Edition Statement"
3. **q29 → q49**: Reconoce "Place of Publication"
4. **q50 → q69**: Reconoce "Date of Publication"
5. **q70 → q79**: Reconoce "Publisher"
6. **q80 → q85**: Reconoce "Title"
7. **q86 → q92**: Reconoce "Author"
8. **q93 → q105**: Reconoce "Contributors"
9. **q106 → q122**: Reconoce "Corporate Author"
10. **q123 → q145**: Reconoce "Corporate Contributors"
11. **q146 → q158**: Reconoce "Former owner"
12. **q159 → q167**: Reconoce "Engraver"
13. **q168 → q181**: Reconoce "Issuance type"
14. **q182 → q192**: Reconoce "Flickr URL"
15. **q193 → q203**: Reconoce "Shelfmarks" (estado final)

### Alfabeto: 
{A-Z, a-z, espacio, coma}

### Ejemplos:
- Válidos: "Identifier,Edition Statement,Place of Publication,Date of Publication,Publisher,Title,Author,Contributors,Corporate Author,Corporate Contributors,Former owner,Engraver,Issuance type,Flickr URL,Shelfmarks"
- Inválidos: "ID,Title,Author", "Identifier,Title", "Identifier,Edition,Place,Date,Publisher,Title,Author,Contributors,Corporate Author,Corporate Contributors,Former owner,Engraver,Type,URL,Shelf"

### Representación Formal:
- **Q** = {q0, q1, q2, ..., q203}
- **Σ** = {A-Z, a-z, espacio, coma}
- **δ**: función de transición que reconoce secuencialmente cada campo
- **q0**: estado inicial
- **F** = {q203}: conjunto de estados finales
