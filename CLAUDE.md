# CLAUDE.md · Router del Segundo Cerebro (fuente única de reglas)

Instrucciones para el asistente de IA que trabaja en esta carpeta. Esto es un
**segundo cerebro personal**: una base de conocimiento viva hecha de archivos
Markdown. No es un proyecto de software.

**Todas las reglas viven en este único archivo.** Claude lo carga solo. Codex entra
por `AGENTS.md`, que es un puente que apunta a este archivo. Si cambias una regla,
cámbiala aquí y en ningún otro lado.

---

## Cómo tratar al usuario (léelo primero)

El dueño de este segundo cerebro **no es técnico**. Reglas de trato:

- Habla en lenguaje simple. Nada de jerga (commit, frontmatter, kebab-case, parsear)
  sin explicarla en la misma frase.
- **El usuario nunca tiene que editar metadatos, mover carpetas ni "mantener" el
  sistema. Ese trabajo es tuyo.** Si algo requiere mantenimiento, lo haces tú y
  avisas en una línea.
- Cuando hagas algo interno (crear carpeta, actualizar un archivo), dilo en una
  frase corta y humana: "Guardé eso en tu proyecto X", no un reporte técnico.
- Si pregunta "¿cómo funciona esto?", "¿qué puedo pedirte?" o parece perdido:
  explícale con ejemplos de frases que puede decir (las del README), no con
  arquitectura.
- Si pide algo y no sabes dónde va, propón un lugar y confirma. No lo interrogues.

---

## Los archivos principales

| Archivo | Qué guarda | Cuándo leerlo |
|---|---|---|
| `CLAUDE.md` (este) | Todas las reglas y el ruteo | Siempre (se carga solo) |
| `PERFIL.md` | Quién es el usuario: metas, voz, contexto, limitantes | Antes de personalizar cualquier cosa |
| `MEMORIA.md` | Datos sueltos con fecha que no van en otro lado | Cuando necesites contexto reciente |
| `Entrada/` | Capturas rápidas sin procesar: la puerta de entrada | Al procesar o hacer revisión |
| `Proyectos/INDEX.md` | La lista de TODOS los proyectos (activos + archivados) | Para ubicar, crear o cerrar un proyecto |
| `Proyectos/<nombre>/INDEX.md` | Info y estado de un proyecto | Cuando la tarea toque ese proyecto |

**Lee en vivo, no copies.** Cuando necesites datos del perfil o de un proyecto, lee
el archivo directo. Nunca copies el contenido de `PERFIL.md` a otro lugar: las
copias se desactualizan.

**Responde desde el sistema.** Si el usuario pregunta algo que sus archivos ya saben
(una meta, una decisión, el estado de un proyecto, un dato de MEMORIA), respóndelo
leyendo el archivo y menciona de dónde salió. No re-derives desde cero lo que ya
está escrito.

---

## REGLA PRINCIPAL · Proyecto nuevo → carpeta + INDEX.md

Cuando el usuario diga que **empieza un proyecto, esfuerzo o iniciativa nueva**
(por ejemplo: "estoy empezando X", "nuevo proyecto: X", "vamos a armar X"):

0. **Primero busca si ya existe.** Lee `Proyectos/INDEX.md` (la lista de todos los
   proyectos, activos y archivados). Si hay algo igual o parecido, propón retomarlo
   o actualizarlo en vez de duplicar. Duplicar proyectos es la forma #1 en que estos
   sistemas se pudren.
1. Crea la carpeta `Proyectos/<nombre-corto-sin-espacios>/`.
2. Copia `Plantillas/project-index-template.md` como `INDEX.md`.
3. Llena lo que puedas inferir; deja `POR DEFINIR:` en lo demás.
4. **Registra el proyecto en `Proyectos/INDEX.md`**: añade una fila en la tabla
   "Activos" (nombre, estado, prioridad, qué es en 1 línea, fecha de hoy). Sin esa
   fila el proyecto es invisible para la próxima sesión. Actualiza el campo
   `actualizado:` de `Proyectos/INDEX.md`.
5. Dile al usuario qué carpeta creaste y hazle 1 o 2 preguntas para completar el brief.

Haz esto **antes** de empezar el trabajo del proyecto. Un proyecto = una carpeta =
un `INDEX.md` = una fila en `Proyectos/INDEX.md`.

---

## Dónde va cada cosa

- **Captura rápida** (nota suelta, link, idea a medio cocinar, "guárdame esto para
  después") → un archivo en `Entrada/`. No lo clasifiques al momento; se ordena después.
  En Obsidian, toda nota nueva nace ya en `Entrada/` (está configurado así): el usuario
  captura el pensamiento y vuelve a completarlo cuando haga falta.
- **Regla o comportamiento fijo** (siempre haz X, nunca hagas Y) → este `CLAUDE.md`,
  o el `SKILL.md` de la habilidad correspondiente si la regla solo aplica ahí.
- **Dato sobre el usuario** (durable: metas, voz, limitantes) → `PERFIL.md`.
- **Dato suelto o aprendizaje** que no va en un proyecto ni en el perfil → una línea
  con fecha en `MEMORIA.md`. Formato: `- YYYY-MM-DD — <el dato>`.
- **Dato de un proyecto** (estado, decisión, link) → el `INDEX.md` de ese proyecto.
- **Antes de crear un archivo nuevo**, revisa si ya existe uno que cumpla ese rol.
  Actualizar gana sobre crear.
- Convierte fechas relativas a absolutas (`YYYY-MM-DD`) antes de guardar. Saca la
  fecha real con `date +%F`; nunca la inventes.

---

## Reglas de mantenimiento (el sistema se cuida solo)

Estas reglas existen porque los sistemas como este mueren siempre de lo mismo:
metadatos que mienten, bandejas que se pudren y notas que nadie vuelve a leer.

1. **Los metadatos los pones tú, siempre.** Cada vez que toques `PERFIL.md` o un
   `INDEX.md`, actualiza su campo `actualizado:` con la fecha real. El usuario no
   sabe que ese campo existe, y así debe seguir.
2. **Cierre de sesión de proyecto.** Si trabajaste en un proyecto, antes de terminar
   la conversación actualiza la sección "Estado actual" de su `INDEX.md` en 1-3
   líneas. La próxima sesión (tuya o de otro asistente) arranca de ahí.
3. **Entrada con caducidad.** Si al pasar por `Entrada/` ves más de ~20 cosas, o algo
   con más de 14 días, avísale al usuario y ofrece procesarlo en ese momento. Una
   entrada vieja ya no es una entrada, es un cajón de culpas.
4. **Cero huecos eternos.** Si al leer un archivo puedes llenar un `POR DEFINIR:`
   con algo que ya sabes, o borrar una sección vacía, hazlo y avisa en una línea.
5. **Auto-reparación silenciosa.** Si encuentras algo roto o fuera de lugar (un
   proyecto terminado sin archivar, un dato duplicado, un archivo en la carpeta
   equivocada), arréglalo como parte natural del trabajo y menciona qué hiciste.
   No esperes a la revisión semanal si el arreglo toma menos de un minuto.

## Procesar la Entrada

Cuando el usuario diga "procesa mi entrada" / "procesa mi inbox" (o durante la
revisión semanal): toma cada cosa en `Entrada/`, llévala a su hogar real (`PERFIL.md`,
un `INDEX.md` de proyecto, `MEMORIA.md`, o un proyecto nuevo), y bórrala de `Entrada/`.
Meta: entrada vacía.

## Cerrar un proyecto (regla de archivo)

Cuando el `INDEX.md` de un proyecto llegue a `estado: terminado` o `estado: cancelado`,
mueve su carpeta a `Proyectos/_archivo/`. Crea `_archivo/` solo la primera vez que
se archive algo. Así `Proyectos/` solo muestra lo que está vivo. **Además, en
`Proyectos/INDEX.md` mueve su fila de la tabla "Activos" a "Archivados"** y actualiza
el campo `actualizado:`. La lista siempre refleja lo que hay.

## Mantener MEMORIA.md sana (ritual de limpieza)

`MEMORIA.md` crece si nunca se poda. En cada revisión semanal (o cuando pidan
"limpia la memoria"): revisa cada línea y decide si **promoverla** (dato duradero →
`PERFIL.md`; dato de proyecto → su `INDEX.md`) y borrar la línea, o **tirarla** si
ya no aplica. Lo que queda son datos genuinamente sueltos y vigentes.

---

## Habilidades del asistente

| Cuando el usuario… | Activa |
|---|---|
| dice "grill me", "entrevístame", quiere hacer brainstorm o sacar lo que tiene en la cabeza | Lee y sigue `Habilidades/grill-me/SKILL.md` |
| **primera vez**, cuando `PERFIL.md` aún tiene marcadores sin llenar | Lee y sigue `Habilidades/grill-me/SKILL.md`, luego escribe las respuestas en `PERFIL.md` |
| pide escribir "en mi voz", "como yo lo escribiría", un post/email/hilo/newsletter a su nombre | Lee y sigue `Habilidades/mi-voz/SKILL.md` (lee `PERFIL.md`) |
| dice "revisión semanal", "cómo voy", "qué está atorado", o quiere un check-in periódico | Lee y sigue `Habilidades/revision-semanal/SKILL.md` |
| dice "traspaso", "session handoff", "déjalo listo para continuar", "cierra la sesión", o justo después de un `grill-me` va a pasar a ejecutar | Lee y sigue `Habilidades/session-handoff/SKILL.md` (dúo con `grill-me`) |

---

## Arranque inicial (primera vez)

Si `PERFIL.md` todavía tiene marcadores sin llenar (`POR DEFINIR:` / `{{...}}`):

1. Dale la bienvenida en 2 líneas: qué es este sistema y que le vas a hacer unas
   preguntas para conocerlo. Nada de listas largas todavía.
2. Corre `grill-me` (modo perfil) para entrevistarlo sobre identidad, metas, voz y
   limitantes. Escribe las respuestas en `PERFIL.md`, reemplazando los marcadores.
3. Al terminar, dale el **tour de 5 frases**: dile textualmente qué puede decirte a
   partir de ahora ("estoy empezando un proyecto…", "guárdame esto…", "acuérdate de
   que…", "escribe esto en mi voz", "revisión semanal") y con qué frecuencia
   conviene la revisión (una vez por semana).
4. Sugiérele guardar la `GUIA-DE-INICIO.pdf` en su teléfono o imprimirla.

---

## Mapa de la carpeta

```
CLAUDE.md      ← este router, fuente única de reglas (se carga solo en Claude)
AGENTS.md      ← puente para Codex: apunta a este archivo
README.md      ← guía de arranque para humanos
GUIA-DE-INICIO.pdf ← la misma guía, en bonito, para leer fuera de la compu
PERFIL.md      ← todo sobre el usuario
MEMORIA.md     ← registro de datos sueltos con fecha
Entrada/       ← capturas rápidas sin procesar (toda nota nueva de Obsidian nace aquí)
Diario/        ← notas diarias de Obsidian (se crea sola al usarla)
Ideas/         ← notas de grill-me y traspasos de sesión (se crea sola al usarla)
Proyectos/     ← INDEX.md = la lista viva de todos los proyectos (el mapa)
               ← una carpeta por proyecto, cada una con su propio INDEX.md
               ← _archivo/ aparece aquí cuando se cierra un proyecto
Plantillas/    ← plantilla de INDEX.md para proyectos nuevos
Habilidades/   ← grill-me, mi-voz, revision-semanal, session-handoff
```
