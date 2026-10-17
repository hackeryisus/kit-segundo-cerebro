---
name: revision-semanal
metadata:
  version: "1.2.3"
description: 'Úsala con "revisión semanal", "cómo voy", "qué está atorado" o "revisa mi sistema": avances, Entrada, MEMORIA y lo olvidado. Solo en el kit Segundo Cerebro.'
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
---

# Revisión Semanal

Antes de actuar, identifica la raíz del kit seleccionada. Lee su `AGENTS.md`
solo si aún no se leyó en esta conversación; no lo recargues por esta habilidad.
Si no hay kit accesible, pide la carpeta; no apliques estas reglas a otros trabajos.
Resuelve todas las rutas de abajo en el Mapa de carpetas; no son nombres fijos.
Sigue la cascada y la comprobación de registro del router. Una copia instalada
no contiene el perfil ni sustituye las reglas actuales del kit.

Compatibilidad: `allowed-tools` no concede permisos ni garantiza disponibilidad.
En ChatGPT, lee esta skill como instrucciones operativas y usa las herramientas
equivalentes disponibles para leer, escribir, editar, listar archivos y consultar la
fecha.

El ritual que convierte carpetas en un *sistema*. Tres trabajos: **reportar** (qué
pasó, qué está atorado), **mantener** (rutar, podar, archivar, reparar) y
**rescatar** (traer de vuelta lo que se estaba olvidando). Se corre cuando el
usuario lo pida. Solo corre automáticamente si existe una programación autorizada
y comprobada en la aplicación; instalar esta skill no la programa.

Recuerda con quién hablas: usuario no técnico. El reporte se escribe en lenguaje
humano, corto, sin jerga. Todo el mantenimiento lo haces tú; el usuario solo decide
cuando haya una decisión real que tomar.

## Paso 0 · Cargar contexto (lee en vivo, no copies)

- `PERFIL.md`: metas y dirección, para juzgar qué va bien y qué no.
- Primero `Proyectos/INDEX.md`, después los `INDEX.md` enlazados de trabajo activo.
  Resuelve la ruta en el mapa. No leas todos los entregables ni los archivados;
  abre documentos adicionales solo para verificar un cambio concreto.
- `Habilidades/estado-local.md` si existe: fecha de revisión completada y avisos.
- `Dossier — *.md` (si existe): el espejo del negocio y sus preguntas abiertas.
- `MEMORIA.md`: el registro suelto.
- `Entrada/`: lista qué hay sin procesar y desde cuándo. Saca la fecha con `date +%F`.

## Paso 1 · Reporte

Escribe un briefing corto (en el chat, o en
`Ideas/{YYYY-MM-DD}-revision-semanal.md` si el usuario quiere guardarlo; al
guardarlo, aplica `Plantillas/formato.md`: lo que solo el usuario puede decidir
va como `decision`, el enfriamiento como `riesgo` y la acción #1 como `siguiente`):

- **Avanzó**: proyectos que se movieron; nombra el cambio concreto.
- **Atorado**: proyectos sin movimiento o con una pregunta abierta bloqueante. Di
  por qué. Si un proyecto lleva 3+ semanas igual, pregunta directo: ¿sigue vivo,
  se pausa o se cancela? Un proyecto zombi cuesta más que uno cancelado.
- **Deriva**: cualquier cosa que se esté alejando de las metas en `PERFIL.md`.
- **Enfriamiento**: si la última revisión completada del estado local tiene
  14+ días, dilo sin rodeos: cuántos días estuvo frío el sistema y qué se enfrió
  (preguntas abiertas que nadie respondió, proyectos que nadie tocó). Un sistema
  que no se usa desactualiza su memoria, y una memoria vieja empieza a mentir.
  Si la fecha se desconoce, dilo sin declarar atraso. Actualizar metadatos no es
  progreso; exige una decisión, tarea completada o cambio de entregable como evidencia.
- **Rescate de la semana**: 1 o 2 cosas valiosas que el sistema ya tiene y el
  usuario probablemente olvidó (una idea vieja de la Entrada, un dato de MEMORIA
  relevante a lo que trae entre manos, una decisión pasada que aplica hoy). Lo que
  se captura y nunca vuelve a aparecer está muerto; este paso lo revive. Cada
  rescate termina en una decisión del usuario: **se aplica** (pasa a Siguientes
  acciones o a la ficha de su proyecto) o **se suelta** (si venía de MEMORIA o
  Entrada, retíralo según sus reglas para que no vuelva cada semana). Rescatar
  sin decidir es volver a archivar.
- **Huecos**: las líneas `hueco:` de MEMORIA son cosas que el usuario buscó y su
  segundo cerebro no tenía. Muéstralas: «esto me preguntaste y no lo tenía;
  ¿lo completamos?». Si da el dato, guárdalo en su hogar y retira el hueco; si ya
  no importa, retíralo.
- **Aprendizajes y repeticiones**: las líneas `aprendizaje:` de MEMORIA son
  correcciones o preferencias detectadas en tareas. Propón para cada una si se
  vuelve regla (en `AGENTS.md` o en la habilidad de esa tarea) o se queda como
  dato. Aplica solo las que el usuario apruebe y retíralas al decidir. Las líneas
  `repetido:` con dos fechas se mencionan; con tres o más sin oferta hecha, ofrece
  la habilidad. Una vez al mes, lista las habilidades con `creado_por: asistente`
  y pregunta cuáles ya no usa; esas se mueven a `Habilidades/_archivo/`, nunca se
  borran.
- **Siguientes acciones**: máximo 3, la de mayor impacto primero. Marca cuáles
  **solo el usuario puede hacer** (grabar, llamar, decidir, pagar) y cuáles puedes
  adelantar tú. Las que solo él puede hacer son casi siempre las que se posponen:
  dilo sin rodeos.

Sé honesto, no animoso. Si algo se frenó, di que se frenó.

## Paso 2 · Mantenimiento (los rituales)

Corre estos en orden, reportando qué cambiaste en 1 línea cada uno:

1. **Procesar la Entrada.** Aplica el procedimiento de `AGENTS.md`: excluye README
   y configuración, verifica destino antes de retirar originales y deja pendientes
   las decisiones ambiguas. Nunca descarta contenido solo por antigüedad.
2. **Podar MEMORIA.** Para cada línea en `MEMORIA.md`: promueve datos duraderos a
   `PERFIL.md`, datos de proyecto a su `INDEX.md`, tira los que ya no apliquen.
   Borra las líneas promovidas. Los `hueco:`, `aprendizaje:` y `repetido:` no se
   podan en silencio: se resuelven con el usuario en el reporte.
3. **Archivar proyectos cerrados.** Cualquier `INDEX.md` con `estado: terminado` o
   `cancelado` → mueve su carpeta a `Proyectos/_archivo/` (créala solo si no existe)
   y baja su fila de "Activos" a "Archivados" en `Proyectos/INDEX.md`.
4. **Reconciliar `Proyectos/INDEX.md`.** La lista de proyectos debe cuadrar con la
   realidad: cada carpeta viva tiene su fila, cada fila apunta a una carpeta real, y
   los estados/prioridades coinciden con cada `INDEX.md`. Si un proyecto se creó sin
   fila (olvido de una sesión pasada), agrégala aquí; si hay filas huérfanas o estados
   desfasados, corrígelos. Este paso atrapa el error más común: un proyecto que existe
   como carpeta pero nunca entró a la lista.
5. **Chequeo de salud del sistema.** Revisa y repara tú mismo:
   - `INDEX.md` con `actualizado:` de hace 30+ días → confirma su estado real con
     el usuario y corrígelo.
   - Secciones vacías o `POR DEFINIR:` que ya se pueden llenar o borrar → hazlo.
   - Duplicados o archivos fuera de lugar → confirma identidad y aplica las reglas
     del router; una fusión o descarte ambiguo se propone, no se ejecuta.
   - `PERFIL.md` sin tocar en 90+ días → ofrece un mini-repaso de 3 preguntas
     (¿metas iguales?, ¿algo grande cambió?, ¿la muestra de voz sigue sonando a ti?).
6. **Mantener el dossier (solo si existe `Dossier — *.md`).** Tres movimientos:
   - Agrega al final de "Qué ha aprendido el sistema" una entrada con la fecha de
     hoy: 1-3 líneas de lo nuevo que el sistema aprendió del negocio esta semana
     (datos confirmados, decisiones, correcciones del usuario). Si no aprendió
     nada, no agregues una entrada vacía ni cambies la fecha del dossier por rutina.
   - Revisa "Lo que el sistema todavía no sabe": pregunta que ya tenga respuesta →
     muévela a "Lo que el sistema ya sabe" con su ✓ y su fuente. Surgieron dudas
     nuevas → agrégalas.
   - Renueva "Primer paso de esta semana": si el anterior se hizo, pon el
     siguiente; si no se hizo, pregunta si sigue siendo el correcto o si hay que
     cambiarlo por uno más chico.
7. **Actualizar fechas.** Pon la fecha de hoy en `actualizado:` de todo archivo que
   hayas tocado. Esto es tuyo, nunca del usuario.

## Paso 3 · Respaldo (solo la primera revisión de cada mes)

Si es la primera revisión del mes, recuérdale al usuario en 2 líneas: su segundo
cerebro es una carpeta normal; con copiarla a otro lado ya tiene respaldo. Las dos
opciones simples: una copia independiente en USB o ZIP con fecha. iCloud, Drive y
OneDrive sincronizan, pero también pueden propagar borrados: no equivalen por sí
solos a una copia independiente. Pregunta cuál usa; si no usa
ninguna, ayúdalo a elegir una ahora. Un segundo cerebro sin respaldo es un cerebro
que un café derramado puede borrar.

## Paso 4 · Cierre

Registra la fecha real en «Última revisión completada» del estado local únicamente
si terminaste la revisión; si quedó interrumpida, guarda el siguiente paso sin
cambiar esa fecha. Registra el mes del recordatorio de respaldo cuando lo hagas.
Si guardaste un informe, enlázalo desde MEMORIA y verifica el destino.

Resumen en 3 líneas máximo: qué reportaste, qué limpiaste/reparaste, y la siguiente
acción #1. No sobre-expliques.
