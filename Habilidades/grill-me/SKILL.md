---
name: grill-me
version: 1.0.0
description: |
  Entrevista al usuario a fondo sobre un plan, tema o sobre sí mismo,
  guardando cada respuesta en un archivo para que nada se pierda. Úsalo
  cuando el usuario quiera hacer brainstorm, stress-test de una idea,
  sacar lo que tiene en la cabeza, construir su PERFIL.md la primera vez,
  o cuando diga "grill me" o "entrevístame".
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
---

# Grill Me — Entrevista a Fondo

Nota de compatibilidad: el bloque `allowed-tools` del frontmatter es para Claude.
En Codex, lee esta skill como instrucciones operativas y usa las herramientas
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

**A. Modo perfil (arranque inicial).** Cuando `PERFIL.md` todavía es plantilla sin
llenar, el archivo destino ES `PERFIL.md`. Entrevista al usuario por cada sección
(identidad, metas, voz, limitantes, personas/proyectos) y escribe cada respuesta
directo en la sección correspondiente, reemplazando los `POR DEFINIR:`. Al terminar
pon `estado: activo` y llena `actualizado:`.

> **El nombre no se pregunta, se confirma.** Antes de la primera pregunta busca su
> nombre en lo que ya tienes: el nombre configurado en la máquina
> (`git config user.name`, o el nombre completo de la cuenta del sistema), una firma
> en algún archivo suyo. Si lo encuentras, no gastes una pregunta en él: confírmalo
> de pasada (*"Voy a llamarte Ana, ¿te queda?"*) y arranca la entrevista en la
> pregunta que de verdad no puedes deducir. Solo pregúntalo directo si no hay
> ninguna señal. Vale para cualquier dato del perfil: **una pregunta que un archivo
> ya contesta es una pregunta que no se hace** (el método de abajo lo dice también,
> y en modo perfil es donde más se nota, porque es la primera impresión del sistema).

**B. Modo brainstorm (por defecto).** Para cualquier otro tema, el archivo destino es
nuevo: `Ideas/{YYYY-MM-DD}-{tema-slug}.md` (crea la carpeta `Ideas/` si
no existe). Saca la fecha con `date +%F`.

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
