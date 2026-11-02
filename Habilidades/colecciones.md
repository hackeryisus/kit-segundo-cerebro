# Colecciones: crear, renombrar y archivar

Procedimiento del router `AGENTS.md`, no una habilidad que instalar. Léelo cuando
el dueño cuente cómo organiza su trabajo, empiece algo nuevo, pida renombrar o
archivar, o cuando aparezcan cosas del mismo tipo sin colección.

**Idioma:** responde y escribe en español (o en el idioma de `PERFIL.md`).

## Qué es una colección

Una carpeta de primer nivel que agrupa cosas del mismo tipo, cada una con su
ficha. `Proyectos/` es la colección de fábrica. El dueño puede tener otras con su
propio nombre: Clientes, Casos, Expedientes, Procesos, Proveedores, Obras.

Toda colección tiene las mismas cuatro piezas que Proyectos:
1. **Índice general** `<Colección>/INDEX.md`: tabla de activos y de archivados.
2. **Una carpeta por elemento** con su ficha `INDEX.md`.
3. **Plantilla de ficha** en `Plantillas/<singular>-template.md`.
4. **Una fila en el mapa** de `AGENTS.md`, con papel «Colección: <nombre>».

## Crear una colección (clonar Proyectos)

Cuando el dueño organiza por una unidad que no es «proyecto» (te dice «trabajo por
clientes», «cada caso es un expediente»), o hay tres elementos del mismo tipo
sueltos, propón la colección en una línea y créala con su sí:

1. Pregunta lo mínimo: cómo la llama, qué datos sigue de cada uno (estado,
   fechas, montos, responsable) y si los elementos terminan (casos, obras) o son
   permanentes (clientes, proveedores).
2. Crea `<Colección>/INDEX.md` clonando la estructura de `Proyectos/INDEX.md`, sin
   sus filas. Ajusta las columnas a lo que el dueño sigue, por ejemplo
   `Cliente | Estado | Qué le damos | Actualizado`.
3. Crea `Plantillas/<singular>-template.md` clonando
   `Plantillas/project-index-template.md`. Conserva Qué es, Estado actual,
   Pendientes, Decisiones, Qué leer según la tarea y Relaciones. Si los elementos
   son permanentes, cambia «Objetivo y cuándo está listo» por «Qué le damos» y usa
   estado `activo | inactivo`. Agrega solo los campos que el dueño nombró.
4. Agrega la fila al mapa de `AGENTS.md` y comprueba que la carpeta abre.
5. Si ya había elementos sueltos, propón moverlos a la colección; muévelos solo
   con su sí, registrando cada uno.

Una colección no reemplaza a otra: un proyecto para un cliente vive en
`Proyectos/` y su ficha enlaza la del cliente en «Relaciones», y viceversa.

## Elemento nuevo

1. Lee el índice de la colección y busca equivalentes activos o archivados. Si
   existe uno parecido, propón retomarlo.
2. Crea `<Colección>/<nombre-corto>/INDEX.md` desde su plantilla. Llena lo
   confirmado y deja `POR DEFINIR:` en lo demás.
3. Añade una fila enlazada en Activos del índice con estado, descripción breve y
   fecha real; actualiza `actualizado:`.
4. Abre la ficha desde ese enlace y comprueba que no haya duplicado. Un elemento
   es una carpeta, una ficha y una fila. Haz esto antes de su trabajo.

Un entregable se enlaza desde la ficha de su elemento. Si no pertenece a ninguno,
deja un puntero fechado en MEMORIA.

## Renombrar

Solo a petición del dueño. Mueve la carpeta con su contenido a un destino libre;
actualiza el mapa, enlaces, plantillas y ajustes de Obsidian que la citen, y
verifica que no quede la ruta antigua. Si ambas carpetas existen, inspecciona y
pide decisión antes de fusionar. Si falta una carpeta del mapa, busca evidencia de
renombrado antes de recrearla.

## Archivar

1. Solo por decisión o evidencia explícita: elemento `terminado`, `cancelado` o
   `inactivo`. Nunca por antigüedad.
2. Antes, busca quién lo cita: fichas, MEMORIA, habilidades. Si algo activo lo
   usa, sobre todo con fecha futura, avisa aunque el dueño ya lo haya pedido.
3. Mueve la carpeta a `<Colección>/_archivo/` (créala al primer uso, con destino
   libre), pasa su fila a Archivados y actualiza fechas y enlaces.
