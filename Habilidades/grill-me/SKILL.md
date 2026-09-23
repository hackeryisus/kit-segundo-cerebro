---
name: grill-me
metadata:
  version: "1.2.1"
description: |
  Úsala cuando el usuario diga "grill me" o "entrevístame", o quiera hacer
  brainstorm, poner a prueba una idea, sacar lo que tiene en la cabeza o ampliar
  su PERFIL.md cuando lo pida. Lo entrevista a fondo sobre un plan, un tema o
  sobre sí mismo y guarda cada respuesta en un archivo para que nada se pierda.
  Solo con una carpeta del kit Segundo Cerebro seleccionada.
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
---

# Grill Me — Entrevista a Fondo

Antes de actuar, identifica la raíz del kit seleccionada. Lee su `AGENTS.md`
solo si aún no se leyó en esta conversación; no lo recargues por esta habilidad.
Si no hay kit accesible, pide la carpeta; no apliques estas reglas a otros trabajos.
Resuelve todas las rutas de abajo en el Mapa de carpetas; no son nombres fijos.
Sigue la cascada y la comprobación de registro del router. Una copia instalada
no contiene el perfil ni sustituye las reglas actuales del kit.

Compatibilidad: `allowed-tools` no concede permisos ni garantiza disponibilidad.
En ChatGPT, lee esta skill como instrucciones operativas y usa las herramientas
equivalentes disponibles para leer, escribir, editar y consultar la fecha.

Entrevista al usuario sobre cada aspecto del tema hasta que ambos tengan
entendimiento compartido. Baja por cada rama del árbol de decisión, resolviendo
dependencias una por una. El objetivo real es **sacar lo que tiene en la cabeza y
dejarlo en un archivo Markdown organizado** para que nada se pierda cuando el
contexto se llene.

## El archivo de captura es el punto central

Las entrevistas largas llenan el contexto. Si guardas las respuestas solo en tu
memoria de conversación, eventualmente vas a olvidar, mezclar o perder algo. Por eso
**guardas a disco después de cada respuesta**. El archivo, no tu contexto, es la
fuente de verdad. Nunca esperes a que el usuario te pida guardar.

## Dos modos

**A. Modo perfil (cuando el usuario quiera conocerse o ampliar su perfil).**
El destino ES `PERFIL.md`. Pregunta por la sección pertinente al trabajo actual;
recorrer todo el perfil es opcional. Escribe cada respuesta donde corresponde.
Pon `estado: activo` al tener contexto útil, aunque falten secciones, y fecha real.
Para el primer uso sigue `Habilidades/arranque.md`; no secuestres una petición
concreta con una entrevista completa porque el perfil esté vacío.
Usa el nombre confirmado por el usuario o su perfil. No deduzcas identidad de Git
ni del equipo, que puede ser del consultor. No repitas respuestas ya documentadas.

**B. Modo brainstorm (por defecto).** Para cualquier otro tema, el archivo destino es
`Ideas/{YYYY-MM-DD}-{tema-slug}.md`, reutilizando la nota si ya existe. Resuelve
Ideas en el mapa antes de crearla al primer uso. Saca la fecha de una herramienta
disponible (por ejemplo `date +%F`). Enlaza la nota desde la ficha del proyecto o,
si es independiente, desde MEMORIA con fecha y tema.

> **Dúo con `session-handoff`.** `grill-me` saca lo que está en la cabeza y lo deja
> en `Ideas/`; cuando toque parar o pasar a ejecutar, `session-handoff` recoge esa
> misma nota y escribe `Ideas/{fecha}-{tema}-handoff.md` con el siguiente paso, para
> que otra sesión retome sin releerlo todo. Al cerrar un brainstorm, ofrece el
> traspaso.

## Antes de la primera pregunta

1. Decide el modo. Crea o identifica el archivo destino.
2. En modo brainstorm, crea el archivo de inmediato con: título, fecha, objetivo de
   la sesión, y una sección vacía de "Pendientes".
3. Dile al usuario dónde estás guardando, en una línea. Luego haz la pregunta 1.

## La regla del checkpoint (no negociable)

Después de CADA respuesta del usuario, ANTES de hacer la siguiente pregunta:
- Escribe los hechos y decisiones clave de su respuesta (en sus palabras cuando
  la redacción importa) más cualquier pendiente (cosas que no pudo contestar +
  quién debería).
- Si una respuesta posterior cambia algo anterior, actualízalo.
- Solo entonces haz la siguiente pregunta.

Nunca acumules varias respuestas en una sola escritura. Un checkpoint por respuesta.

## Método de entrevista

- Haz **una pregunta a la vez**. Para cada una, ofrece tu **respuesta recomendada**
  (tu mejor inferencia del contexto) para que el usuario solo confirme, corrija o
  redirija.
- Resuelve dependencias en orden: la decisión de arriba primero.
- Si una pregunta se puede responder **leyendo un archivo o documento**, hazlo tú en
  vez de preguntar.
- Cuando el usuario **no pueda responder**, captura el pendiente y sigue. No te
  atores.
- Sigue hasta que el usuario diga que ya, o hayas cubierto cada rama. Cerca del
  final ofrece: "¿hay algo que no hayamos tocado?"
- Sé estricto. Cuestiona supuestos. No aceptes respuestas vagas.

## Estructura del archivo (modo brainstorm)

```
# {Tema}: Notas de Brainstorm / Descubrimiento
Fecha: {fecha} · Objetivo: {una línea}

## Resumen / decisiones clave
(síntesis en curso, se actualiza conforme avanzas)

## Registro de preguntas
### P1 — {tema}
- Pregunta: {la pregunta}
- Capturado: {hechos, decisiones, en sus palabras cuando importa}
- Pendientes: {cosa abierta -> quién puede responder}

## Pendientes (falta input)
- {cosa} -> {quién puede responder}
```

## Al terminar
- Relee el archivo buscando contradicciones o huecos; reconcílialos.
- Dale un resumen corto: qué se capturó, qué sigue pendiente, siguiente paso sugerido.
- En modo perfil, confirma que `PERFIL.md` ya tiene `estado: activo` y recuérdale que
  `mi-voz` y cada proyecto ahora leen de ahí.
