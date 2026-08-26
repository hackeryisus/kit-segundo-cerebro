---
name: revision-semanal
version: 0.3.0
description: |
  Check-in periódico de todo el segundo cerebro: muestra qué avanzó, qué
  está atorado, corre los rituales de mantenimiento (procesar Entrada,
  podar MEMORIA, archivar proyectos cerrados), revisa la salud del
  sistema y rescata cosas olvidadas. Activa cuando el usuario diga
  "revisión semanal", "cómo voy", "qué está atorado", "revisa mi
  sistema", o quiera un check-in recurrente.
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
---

# Revisión Semanal

Nota de compatibilidad: el bloque `allowed-tools` del frontmatter es para Claude.
En ChatGPT, lee esta skill como instrucciones operativas y usa las herramientas
equivalentes disponibles para leer, escribir, editar, listar archivos y consultar la
fecha.

El ritual que convierte carpetas en un *sistema*. Tres trabajos: **reportar** (qué
pasó, qué está atorado), **mantener** (rutar, podar, archivar, reparar) y
**rescatar** (traer de vuelta lo que se estaba olvidando). Se corre cuando el
usuario lo pida o semanalmente.

Recuerda con quién hablas: usuario no técnico. El reporte se escribe en lenguaje
humano, corto, sin jerga. Todo el mantenimiento lo haces tú; el usuario solo decide
cuando haya una decisión real que tomar.

## Paso 0 · Cargar contexto (lee en vivo, no copies)

- `PERFIL.md`: metas y dirección, para juzgar qué va bien y qué no.
- Cada `Proyectos/*/INDEX.md`: estado actual de cada proyecto vivo. (Los nombres de
  carpeta se resuelven en el Mapa de carpetas de `CLAUDE.md`, no se asumen.)
- `Dossier — *.md` (si existe): el espejo del negocio y sus preguntas abiertas.
- `MEMORIA.md`: el registro suelto.
- `Entrada/`: lista qué hay sin procesar y desde cuándo. Saca la fecha con `date +%F`.

## Paso 1 · Reporte

Escribe un briefing corto (en el chat, o en
`Ideas/{YYYY-MM-DD}-revision-semanal.md` si el usuario quiere guardarlo):

- **Avanzó**: proyectos que se movieron; nombra el cambio concreto.
- **Atorado**: proyectos sin movimiento o con una pregunta abierta bloqueante. Di
  por qué. Si un proyecto lleva 3+ semanas igual, pregunta directo: ¿sigue vivo,
  se pausa o se cancela? Un proyecto zombi cuesta más que uno cancelado.
- **Deriva**: cualquier cosa que se esté alejando de las metas en `PERFIL.md`.
- **Enfriamiento**: si la revisión anterior (o el `actualizado:` del dossier) tiene
  14+ días, dilo sin rodeos: cuántos días estuvo frío el sistema y qué se enfrió
  (preguntas abiertas que nadie respondió, proyectos que nadie tocó). Un sistema
  que no se usa desactualiza su memoria, y una memoria vieja empieza a mentir.
- **Rescate de la semana**: 1 o 2 cosas valiosas que el sistema ya tiene y el
  usuario probablemente olvidó (una idea vieja de la Entrada, un dato de MEMORIA
  relevante a lo que trae entre manos, una decisión pasada que aplica hoy). Lo que
  se captura y nunca vuelve a aparecer está muerto; este paso lo revive.
- **Siguientes acciones**: máximo 3, la de mayor impacto primero. Marca cuáles
  **solo el usuario puede hacer** (grabar, llamar, decidir, pagar) y cuáles puedes
  adelantar tú. Las que solo él puede hacer son casi siempre las que se posponen:
  dilo sin rodeos.

Sé honesto, no animoso. Si algo se frenó, di que se frenó.

## Paso 2 · Mantenimiento (los rituales)

Corre estos en orden, reportando qué cambiaste en 1 línea cada uno:

1. **Procesar la Entrada.** Lleva cada cosa en `Entrada/` a su hogar real (`PERFIL.md`, un
   `INDEX.md` de proyecto, `MEMORIA.md`, o un proyecto nuevo), luego bórrala de ahí.
   Meta: vacío. Si algo lleva 14+ días ahí, decídelo hoy con el usuario: se procesa
   o se tira.
2. **Podar MEMORIA.** Para cada línea en `MEMORIA.md`: promueve datos duraderos a
   `PERFIL.md`, datos de proyecto a su `INDEX.md`, tira los que ya no apliquen.
   Borra las líneas promovidas.
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
   - Archivos duplicados o en la carpeta equivocada → júntalos o muévelos.
   - `PERFIL.md` sin tocar en 90+ días → ofrece un mini-repaso de 3 preguntas
     (¿metas iguales?, ¿algo grande cambió?, ¿la muestra de voz sigue sonando a ti?).
6. **Mantener el dossier (solo si existe `Dossier — *.md`).** Tres movimientos:
   - Agrega al final de "Qué ha aprendido el sistema" una entrada con la fecha de
     hoy: 1-3 líneas de lo nuevo que el sistema aprendió del negocio esta semana
     (datos confirmados, decisiones, correcciones del usuario). Si no aprendió
     nada, escribe eso mismo: es señal honesta de que hay que usarlo más.
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
opciones simples: (a) tener la carpeta dentro de iCloud Drive / Google Drive /
OneDrive, o (b) copiarla hoy a un USB o a un ZIP. Pregunta cuál usa; si no usa
ninguna, ayúdalo a elegir una ahora. Un segundo cerebro sin respaldo es un cerebro
que un café derramado puede borrar.

## Paso 4 · Cierre

Resumen en 3 líneas máximo: qué reportaste, qué limpiaste/reparaste, y la siguiente
acción #1. No sobre-expliques.
