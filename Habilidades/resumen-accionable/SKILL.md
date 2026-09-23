---
name: resumen-accionable
metadata:
  version: "1.0.0"
description: |
  Úsala cuando el usuario diga "resúmeme esto con pendientes", "qué se decidió",
  "qué sigue", o pegue notas, una reunión o texto desordenado y quiera saber qué
  importa y qué hacer después. Devuelve decisiones, próximos pasos y preguntas
  abiertas sin inventar nada. No la uses para resúmenes narrativos o académicos.
  Solo con una carpeta del kit Segundo Cerebro seleccionada.
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
---

# Resumen Accionable

Antes de actuar, identifica la raíz del kit seleccionada. Lee su `CLAUDE.md`
solo si aún no se leyó en esta conversación; no lo recargues por esta habilidad.
Si no hay kit accesible, pide la carpeta; no apliques estas reglas a otros trabajos.
Resuelve todas las rutas de abajo en el Mapa de carpetas; no son nombres fijos.
Sigue la cascada y la comprobación de registro del router. Una copia instalada
no contiene el perfil ni sustituye las reglas actuales del kit.

Compatibilidad: `allowed-tools` no concede permisos ni garantiza disponibilidad.
En ChatGPT, lee esta skill como instrucciones operativas y usa las herramientas
equivalentes disponibles para leer, escribir, editar, listar archivos y consultar
la fecha.

Convierte lo que el usuario trae (sus notas, las notas o la transcripción de una
reunión, un correo largo, texto desordenado) en algo que se pueda actuar sin
releer la fuente.

## Resultado

Adapta la extensión al material y conserva solo las secciones que aporten valor:

- **En una frase:** la idea central.
- **Puntos clave:** hechos y contexto indispensables.
- **Decisiones:** acuerdos explícitos ya tomados.
- **Próximos pasos:** acciones concretas, con responsable y fecha solo cuando la
  fuente los indique.
- **Preguntas abiertas:** vacíos que impiden avanzar.

## Criterios

- No inventes decisiones, responsables, fechas ni prioridades.
- Distingue **✓ confirmado** (está en la fuente) de **? inferido** (deducción tuya
  pendiente de confirmar), como en el resto del kit.
- Si la fuente se contradice, señala la contradicción en vez de resolverla.
- Mantén nombres, cifras y fechas tal como aparecen; convierte fechas relativas a
  `YYYY-MM-DD` solo si conoces la fecha de referencia.
- Agrupa duplicados y quita la conversación incidental que no cambie el sentido.
- Redacta cada próximo paso con un verbo de acción. Si no hay acciones reales,
  dilo claramente.
- Si el usuario pide otro formato, conserva estas garantías y sigue su estructura.
- Datos sensibles (salud, contraseñas, bancos, datos personales de empleados o
  clientes): aplica la regla de confianza de `CLAUDE.md`; menciona la categoría,
  no el detalle.

## Guardar (solo si el usuario lo pide)

El resumen se entrega en el chat. Si el usuario quiere conservarlo:

- Si pertenece a un proyecto, guárdalo en su carpeta, enlázalo desde su ficha
  `INDEX.md` y actualiza ahí «Estado actual» y el próximo paso.
- Si no pertenece a ninguno, guárdalo en `Ideas/{YYYY-MM-DD}-resumen-<tema>.md`
  con un puntero fechado en `MEMORIA.md`.
- No crees un proyecto por cada resumen; propónlo solo si aparece una iniciativa
  real.
- Verifica el archivo y su enlace dentro del kit antes de decir «guardado», según
  la regla dura del router.
