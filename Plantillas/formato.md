---
tipo: guia-formato
actualizado: 2026-10-05
---

# Formato de lo que escribe el asistente

> Guía para el asistente. Léela cuando vayas a guardar un resumen, una revisión, un dossier, un plan o la ficha de un proyecto. El dueño no necesita leerla: solo nota que todo se lee fácil.

Obsidian pinta ciertos bloques como notas de color (callouts). Cada tipo significa una sola cosa. Así el dueño sabe qué hacer con un bloque antes de leerlo.

## Los siete tipos de bloque

Se escriben así, siempre con el rol en palabras en el título:

```
> [!decision] Decisión: ¿cobramos por proyecto?
> Recomiendo por proyecto por lo que me contaste del cliente. Si no decidimos esta semana, la propuesta sale por hora.
```

| Tipo | Significa | Debe incluir | Máximo por documento |
|---|---|---|---|
| `decision` | Necesita al dueño | Una pregunta, tu recomendación y qué pasa si nadie decide | 3 |
| `hallazgo` | Algo que encontraste | El dato concreto, con número si lo hay | 3 |
| `evidencia` | De dónde sale un dato | El archivo, la fecha o la conversación de origen | 3 |
| `riesgo` | Algo puede salir mal | «Si pasa esto, entonces aquello» | 3 |
| `correccion` | Cambia algo dicho antes | La fecha en el título y si cambia la conclusión | 2 |
| `hecho` | Quedó terminado | Cómo comprobaste que quedó | 2 |
| `siguiente` | El próximo paso | Una acción con fecha o con el momento en que toca | 1 por sección |

Reglas:

- **Un bloque, una idea.** Si son dos ideas, son dos bloques o es texto normal.
- **Máximo 8 bloques en un documento.** Un documento lleno de cajas ya no guía la vista.
- **El título siempre lleva el rol en palabras** («Decisión: …», «Riesgo: …»). Así se entiende aunque se abra fuera de Obsidian.
- Las marcas **✓ confirmado** y **? inferido** del kit siguen igual dentro de cualquier bloque.
- No inventes otros tipos ni metas un bloque dentro de otro.

## El resto de la página

| Elemento | Úsalo para | Regla |
|---|---|---|
| Tabla | Tres o más cosas que se comparan | Siempre con encabezado. Números alineados a la derecha (`---:`) |
| Lista numerada | Pasos con orden | |
| Viñetas | Cosas sin orden | Si cada una tiene tema, empieza con el tema en **negrita**. Máximo dos niveles |
| **Negrita** | La cifra o frase que hay que recordar | Una por párrafo como máximo |
| ==Resaltado== | Solo lo que le toca hacer al dueño | Rara vez |
| `Código` | Nombres de archivo, carpetas y valores exactos | Nunca para dar énfasis |
| Casillas `- [ ]` | Tareas reales | Con fecha `YYYY-MM-DD` si la tienen |

Además: un solo título `#` por documento; fechas en `YYYY-MM-DD`; cifras con su unidad; nada de HTML.

## Dónde aplica

- **Ficha de proyecto** (`INDEX.md`): sin bloques, salvo un `decision` para la pregunta abierta que frena el proyecto.
- **Resumen accionable y revisión semanal guardados**: lo que solo el dueño puede decidir va en `decision`; el próximo paso cierra con `siguiente`.
- **Dossier**: los focos rojos pueden ir como `riesgo`; un dato que cambió, como `correccion`.
