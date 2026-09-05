---
name: session-handoff
metadata:
  version: "1.1.0"
description: |
  Habilidad del kit Segundo Cerebro, solo con una carpeta de este kit seleccionada.
  Deja lista una nota de "traspaso" para que otra conversación (o tú
  mañana) retome el trabajo sin perder el hilo y sin releerlo todo.
  Activa cuando el usuario diga "session handoff", "traspaso", "déjalo
  listo para continuar", "cierra la sesión", "voy a seguir esto después",
  o justo después de un `grill-me` cuando toque pasar a ejecutar.
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
---

# Session Handoff — Traspaso de Sesión

Antes de actuar, identifica la raíz del kit seleccionada y lee su `CLAUDE.md`.
Si no hay kit accesible, pide la carpeta; no apliques estas reglas a otros trabajos.
Resuelve todas las rutas de abajo en el Mapa de carpetas; no son nombres fijos.
Sigue la cascada y la comprobación de registro del router. Una copia instalada
no contiene el perfil ni sustituye las reglas actuales del kit.

Compatibilidad: `allowed-tools` no concede permisos ni garantiza disponibilidad.
En ChatGPT, lee esta skill como instrucciones operativas y usa las herramientas
equivalentes para leer, escribir, editar y consultar la fecha.

El chat se llena, o el usuario para y vuelve horas después. Este traspaso hace que
el trabajo **sobreviva** a cerrar la conversación: la siguiente sesión abre una nota
corta y sabe exactamente dónde retomar. El público es una **futura versión de ti**,
no un reporte para el usuario.

## Symbiosis con grill-me

Estas dos habilidades son las dos mitades de un mismo movimiento:

- **`grill-me` saca lo que está en la cabeza** y lo deja en una nota de `Ideas/`.
- **`session-handoff` recoge esa nota** (más lo que se haya avanzado) y la convierte
  en un punto de arranque para la siguiente sesión.

Flujo natural: entrevistas con `grill-me` → se llena `Ideas/{fecha}-{tema}.md` →
al cerrar, `session-handoff` escribe `Ideas/{fecha}-{tema}-handoff.md` que **apunta**
a la nota de grill-me (no la copia) y añade lo único que la nota no tiene: qué ya se
hizo y cuál es el siguiente paso.

## Regla central: apunta, no copies

El chiste es no gastar tokens re-explicando lo que ya está escrito. El traspaso es
**corto y de ruteo**: cabe en una pantalla. **Enlaza** el material fuente (la nota de
`grill-me`, el `INDEX.md` del proyecto, el archivo que se está construyendo); **no**
pega su contenido. La siguiente sesión lee el traspaso primero, y solo abre los
archivos enlazados cuando llega al paso que los necesita.

## Dos modos

- **Modo chat (por defecto).** Escribe el traspaso solo en el chat. Para un "¿dónde
  voy?" rápido antes de cerrar, cuando nada necesita quedar guardado.
- **Modo archivo.** Escribe el traspaso en `Ideas/{fecha}-{tema}-handoff.md` para que
  una sesión nueva lo retome leyendo ese archivo. Úsalo cuando el usuario vaya a
  parar horas, abrir un chat nuevo, o repartir el trabajo en varias sesiones.

Resuelve Ideas en el mapa. Reutiliza el traspaso vigente del tema si corresponde.
Regístralo en la ficha del proyecto o, si es independiente, en MEMORIA con un
enlace y tema. Actualiza el estado del proyecto sin duplicar el contenido.

Si no está claro cuál, pregunta en una línea: "¿solo en el chat, o te dejo un archivo
para continuar después?"

## Cómo armar el traspaso

1. **Repasa toda la conversación**, no solo los últimos mensajes.
2. **Junta el estado** de: la nota de `grill-me` si hubo una (enlázala, no la
   repitas), el `INDEX.md` del proyecto tocado, los archivos creados o modificados
   esta sesión, y cualquier pregunta que quedó sin responder.
3. **No audites toda la carpeta.** Sintetiza lo que pasó en ESTA sesión.
4. Escribe en el mismo idioma en que se trabajó la sesión.
5. Convierte fechas relativas a absolutas (`YYYY-MM-DD`) con `date +%F`.

## Plantilla (modo archivo)

```
# Traspaso — {tema} · {fecha}
viene-de-grill-me: [[{fecha}-{tema}]]   ← léela para el PORQUÉ; no lo repitas aquí

## Objetivo
{1-2 líneas: el trabajo de varios pasos que se está llevando adelante}

## Entregable(s)
- {qué se está produciendo} — `{ruta o [[enlace]]}` — estado {borrador | en revisión | final}

## Bitácora de pasos   ← lo único que la nota fuente NO tiene
- [x] 1. {hecho} — {dónde quedó}
- [~] 2. {en curso} — {punto exacto donde se paró}
- [ ] 3. {pendiente}

## Para leer cuando toque (punteros, no copias)
- `{ruta o [[enlace]]}` — leer al hacer el paso N

## Estado vivo
- Apps o archivos abiertos a medias — o "ninguno"

## Cómo saber que va bien
- {criterio de aceptación por entregable}

## Pendiente + preguntas abiertas
- Pospuesto: {cosa} — {por qué}
- Abierto: {pregunta para el usuario} — {contexto}

## Retoma aquí
{la única acción más probable siguiente}
```

Las dos secciones que cargan el peso: **Bitácora de pasos** (el ancla para retomar,
lo único que la nota de grill-me no tiene) y **Retoma aquí** (una sola acción).

## Cómo lo consume la siguiente sesión

- **Retomar (una sesión):** dile al chat nuevo una línea — `continúa desde
  [[{fecha}-{tema}-handoff]]`. Lee el traspaso y abre lo enlazado según cada paso.
- Si dice «retomemos donde quedamos», consulta primero el índice/ficha del tema
  o los punteros de MEMORIA. Si hay varios temas posibles, pide elegir; no adivines.
- **Repartir (varias sesiones):** abre N chats; a cada uno — `lee
  [[{fecha}-{tema}-handoff]] y haz solo la parte X`.

## Reglas duras

1. **Disciplina de modo.** Modo chat: nunca escribas archivo. Modo archivo: escribe
   exactamente un archivo de traspaso en `Ideas/` y menciona su ruta en el chat.
2. **Apunta, no pegues.** Enlaza el material fuente; nunca pegues el contenido de la
   nota de grill-me o del proyecto. Solo escribe el avance que esos archivos no tienen.
3. **Nunca inventes estado.** Una sección sin nada dice "ninguno" — no la borres. La
   estructura estable es el punto.
4. **Enlaces relativos al archivo o wikilinks inequívocos.** Resuelve desde la raíz
   seleccionada del kit; no dependas de rutas personales de otra computadora.
5. **Sin emojis, sin relleno, sin retrospectiva.** Escueto y concreto: rutas, estados,
   la siguiente acción. Tono de fin de turno.
