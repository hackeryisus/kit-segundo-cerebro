---
name: mi-voz
version: 0.1.0
description: |
  Escribe contenido en la voz documentada del usuario: posts, emails,
  hilos, newsletters, cualquier texto firmable donde la voz del autor deba
  ser reconocible. Lee PERFIL.md. Activa cuando el usuario pida escribir
  "en mi voz", "como yo lo escribiría", "redacta esto por mí", o pida un
  post/email/hilo/newsletter a su nombre.
allowed-tools:
  - Read
  - Write
  - Edit
  - AskUserQuestion
---

# Mi Voz · proto

Nota de compatibilidad: el bloque `allowed-tools` del frontmatter es para Claude.
En Codex, lee esta skill como instrucciones operativas y usa las herramientas
equivalentes disponibles para leer el perfil, editar archivos si hace falta y hacer
preguntas al usuario cuando sea indispensable.

Escribe como el usuario. No simules su voz, **adóptala**. Simular produce texto que
suena bien pero es intercambiable. Adoptar produce texto que solo esa persona podría
haber escrito.

> **Estado proto:** esta habilidad se activa una vez que `PERFIL.md` está lleno
> (sección 3, "Tu voz al escribir"). Si `PERFIL.md` sigue siendo plantilla, detente
> y corre `grill-me` primero para construir el perfil.

## Paso 0 · Cargar el perfil (lee en vivo, no copies)

Lee `PERFIL.md`. Si `estado: plantilla` o la sección 3 está vacía → dile al usuario
que la voz no está definida todavía y ofrece correr `grill-me`. Si sí hay contenido,
extrae de la sección 3:

- **Tono**: las 3 palabras y qué implican.
- **Movimientos firma**: frases, ritmos, hábitos que usar activamente.
- **Anti-patrones**: lo que NUNCA escribiría. Son prohibiciones duras.
- **Muestra**: el texto real que pegó. Iguala su cadencia, largo de oraciones y
  densidad de puntuación. Esta es tu referencia de calibración.

Nunca copies contenido del perfil a esta skill. Léelo en vivo cada vez.

## Paso 1 · Encuadrar la pieza

Confirma en una línea (pregunta solo si no es claro): formato (post / email / hilo /
newsletter / otro), audiencia, objetivo y longitud. No sobre-entrevistes: infiere
del contexto y del perfil, luego avanza.

## Paso 2 · Redactar en voz

- Arranca con sustancia, no con calentamiento.
- Usa los movimientos firma del perfil; evita cada anti-patrón.
- Iguala el ritmo de la muestra: si el usuario escribe corto y directo, no escribas
  largo y adornado.
- Nada de tics genéricos de IA a menos que el perfil diga explícitamente que son
  parte de su voz. Los que reaparecen siempre, y por los que a un texto se le nota
  la IA a un kilómetro:
  - **Guion largo (—) cero.** Es el conector default de los modelos, no de las
    personas. Usa coma, dos puntos o punto y aparte. Es el tell más caro porque el
    lector lo reconoce sin saber nombrarlo.
  - **"No es X, es Y." Prohibido.** Y sus primos: "no se trata de X, sino de Y".
    Suena a frase de molde porque lo es.
  - Aforismos de cierre que suenan profundos y no dicen nada.
  - Intensificadores vacíos, "en el mundo de hoy", regla de tres forzada.

## Paso 3 · Auto-auditoría (obligatoria, antes de entregar)

Dos pasadas, en este orden:

1. **La mecánica:** cuenta los guiones largos del borrador. Si hay uno solo,
   reescribe esa frase. Busca "no es… es…" y reescríbelo. Esto se hace **antes** de
   entregar, nunca después: un texto que ya se publicó no se corrige, se re-publica,
   y para entonces el lector ya lo vio.
2. **La honesta:** pregúntate en voz alta, en un bloque corto, **"¿qué de esto NO
   suena al usuario?"** Nombra las líneas más débiles y los riesgos de cliché,
   corrígelos, y entrega. Si el perfil no tiene suficiente señal de voz para hacer
   esto honestamente, dilo y sugiere enriquecer la sección 3 de `PERFIL.md`.

## Entrega

Entrega el texto terminado. Luego una línea: en qué te apoyaste del perfil y qué
agregarías al perfil para afinar borradores futuros.
