---
name: mi-voz
metadata:
  version: "1.2.0"
description: |
  Úsala cuando el usuario pida escribir "en mi voz", "como yo lo escribiría",
  "redacta esto por mí", o un post, email, hilo o newsletter a su nombre.
  Escribe en la voz documentada del usuario (lee PERFIL.md) cualquier texto
  firmable donde su voz deba reconocerse.
  Solo con una carpeta del kit Segundo Cerebro seleccionada.
allowed-tools:
  - Read
  - Write
  - Edit
  - AskUserQuestion
---

# Mi Voz · proto

Antes de actuar, identifica la raíz del kit seleccionada. Lee su `CLAUDE.md`
solo si aún no se leyó en esta conversación; no lo recargues por esta habilidad.
Si no hay kit accesible, pide la carpeta; no apliques estas reglas a otros trabajos.
Resuelve todas las rutas de abajo en el Mapa de carpetas; no son nombres fijos.
Sigue la cascada y la comprobación de registro del router. Una copia instalada
no contiene el perfil ni sustituye las reglas actuales del kit.

Compatibilidad: `allowed-tools` no concede permisos ni garantiza disponibilidad.
En ChatGPT, lee esta skill como instrucciones operativas y usa las herramientas
equivalentes disponibles para leer el perfil, editar archivos si hace falta y hacer
preguntas al usuario cuando sea indispensable.

Escribe como el usuario. No simules su voz, **adóptala**. Simular produce texto que
suena bien pero es intercambiable. Adoptar produce texto que solo esa persona podría
haber escrito.

No exige perfil completo. Usa la sección 3 si aporta señal; si falta, pide una
muestra breve o el tono deseado. Ofrece un borrador provisional si prefiere avanzar,
sin afirmar que ya reproduce su voz. No fuerces una entrevista sobre otras secciones.

## Paso 0 · Cargar el perfil (lee en vivo, no copies)

Lee `PERFIL.md`. Si la sección 3 está vacía, aplica la alternativa anterior.
Si sí hay contenido,
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

1. **La mecánica:** salvo rasgos expresamente presentes en la voz del usuario,
   cuenta los guiones largos del borrador. Si hay uno solo,
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
