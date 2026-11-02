# Mantenimiento: Entrada, MEMORIA, archivos y procesos que se repiten

Procedimiento del router `AGENTS.md`, no una habilidad que instalar. Léelo al
procesar `Entrada/`, al limpiar MEMORIA, al cerrar una tarea que creó archivos o al
terminar un procedimiento que ninguna habilidad cubre.

**Idioma:** responde y escribe en español (o en el idioma de `PERFIL.md`).

## Procesar Entrada

- Ofrécelo si `Entrada/` tiene unas 20 capturas o alguna de 14+ días.
- Mueve cada captura a su hogar (colección, PERFIL, MEMORIA) solo tras verificar
  destino y registro. Si crea un elemento nuevo, sigue `Habilidades/colecciones.md`.
- No proceses README, configuración ni carpetas como capturas. Si hay duda o
  colisión, déjala pendiente y pregunta.
- Si un `POR DEFINIR:` puede llenarse con evidencia ya conocida, hazlo.
- No dupliques rutas para tapar una nota «perdida»: búscala primero.

## Archivos al cerrar una tarea

Trabajar un Excel o un PDF suele dejar copias, extractos y pruebas que nadie vuelve
a abrir. Guardarlo todo ensucia las carpetas y las búsquedas. Al cerrar, clasifica
cada archivo que creaste:

| Tipo | Ejemplo | Dónde va |
|---|---|---|
| Resultado | el reporte, la tabla limpia, el borrador | su hogar según el mapa, enlazado desde su ficha |
| Reutilizable | un script o plantilla que servirá otra vez | `Herramientas/<nombre>/` si es general; la carpeta de su habilidad si solo la usa una |
| De trabajo | copia del original, CSV intermedio, prueba | `.trabajo/YYYY-MM-DD-<tarea>/` |

- Crea los archivos de trabajo directo en `.trabajo/`, no sueltos. El original del
  dueño nunca se mueve ni se borra.
- `.trabajo/` debe quedar oculta para el dueño. Obsidian no la muestra, y en Mac
  Finder tampoco, por el punto. En Windows el punto no basta: al crearla, ejecuta
  `attrib +h .trabajo` desde la raíz. Si no puedes ejecutar comandos, pídele una
  sola vez: clic derecho en la carpeta › Propiedades › marcar «Oculto».
- En la duda entre resultado y de trabajo, pregunta una vez al cerrar, en una línea.
- Si un archivo de trabajo se vuelve a pedir, pásalo a su hogar: era un resultado.
- La revisión semanal vacía lo de `.trabajo/` con más de 14 días y dice cuántas
  carpetas quitó.

## Limpiar MEMORIA

En la revisión semanal o cuando el dueño lo pida: promueve datos duraderos a
`PERFIL.md` y datos de un elemento a su ficha; retira lo obsoleto. Conserva los
punteros a notas independientes hasta que tengan otro enlace o el dueño decida
retirarlos.

## Procesos que se repiten

No recuerdas otras conversaciones; la huella vive en MEMORIA. Al terminar una
tarea de procedimiento (recibir algo, seguir pasos, entregar algo) que ninguna
habilidad cubre, busca en `MEMORIA.md` una línea `repetido:` de ese proceso. Si
no existe, agrégala: `- YYYY-MM-DD — repetido: <proceso>`. Si existe, súmale la
fecha. Con tres fechas, ofrece en una línea convertirlo en habilidad. Si la
rechaza, anota `(no ofrecer)` y no repitas.

## Crear una habilidad

Por repetición o porque el dueño la pide. Usa la habilidad `skill-creator` que
trae la app; no la reescribas. Condiciones de esta carpeta:
1. Parte de su plantilla o ejemplo real, no de uno inventado.
2. Escríbela en español, con la línea de idioma al inicio.
3. Guárdala en `Habilidades/<nombre-corto>/SKILL.md` con `creado_por: asistente`
   y la fecha en el encabezado; sus plantillas y scripts viven en esa misma carpeta.
4. Pruébala con un caso real del dueño y muéstrale el resultado.
5. No la agregues a `AGENTS.md`: la fila «habilidad creada por el dueño» la cubre
   y el archivo tiene techo de 150 líneas. Instálala según `Habilidades/arranque.md`
   y retira la línea `repetido:`.
