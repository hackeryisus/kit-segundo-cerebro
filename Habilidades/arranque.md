# Arranque y adaptación del Segundo Cerebro

Procedimiento del router `AGENTS.md`, no una sexta habilidad que instalar.
Lee la fuente central de ESTA copia antes de actuar. No modifica el proveedor ni
las preferencias de modelo del cliente. Las rutas se resuelven en su mapa.

## Comprobación inicial (sin entrevista técnica)

1. Identifica la aplicación por el entorno verificable; si no está claro, pregunta
   cuál usa. Confirma la raíz seleccionada leyendo `AGENTS.md` y el índice general.
   Si no puedes leer, pide acceso a esa carpeta; no prometas persistencia.
2. Lee `estado-local.md` junto a este archivo si existe. Revisa capacidades reales:
   leer, escribir (sin crear un archivo de prueba), buscar/listar y registrar skills.
   Permiso declarado no es escritura verificada: confirma esta al guardar el primer
   resultado. Si es solo lectura, ofrece un borrador y explica que no quedó guardado.
3. Lista los nombres de las carpetas con `SKILL.md` en Habilidades (sin
   `_mantenimiento` ni `_archivo`); no abras su contenido por rutina. Conserva
   las originales del kit; no instales herramientas del consultor.
4. Instala todas esas habilidades en el arranque con el adaptador de la
   aplicación (abajo), y de nuevo cuando aparezca una habilidad nueva o la copia
   se abra con otra aplicación. Avisa en una línea qué instalaste; no lo preguntes
   habilidad por habilidad. Si el usuario pide no instalar, sigue por lectura
   directa y registra la preferencia; no repitas la oferta.
5. Usa el mecanismo comprobado de la aplicación. Si necesita un clic del usuario,
   explica ese paso concreto. Si no hay instalador accesible, no inventes comandos:
   deja «pendiente de habilitar», conserva lectura directa y ofrece la guía oficial.
   Para preparar ZIP, el consultor dispone de `_mantenimiento/preparar.py` (guía en
   `_mantenimiento/README.md`); el cliente no necesita instalar Python ni Git.

## Adaptadores (lee solo el correspondiente)

Regla común: si la aplicación ve el disco del usuario, **enlaza**, no copies, para
que la habilidad instalada sea siempre la de `Habilidades/`. Si corre en un
entorno aislado (sandbox o máquina virtual), usa el instalador propio de la
aplicación. Los enlaces van dentro de la raíz del kit, así las habilidades solo
se activan con esta carpeta abierta. Nunca toques la carpeta global de habilidades
del usuario sin que lo pida.

- **Claude Code:** por cada habilidad, crea el enlace simbólico relativo
  `.claude/skills/<nombre>` → `../../Habilidades/<nombre>` en la raíz del kit
  (en macOS y Linux: `ln -s`). Si el sistema no permite enlaces (Windows sin modo
  desarrollador), copia la carpeta y anota «copia» en el estado: al cambiar la
  fuente, se vuelve a copiar. Verifica que el catálogo de habilidades la liste;
  si no aparece, abre una conversación nueva y vuelve a comprobar.
- **Codex:** lo mismo en `.agents/skills/<nombre>` → `../../Habilidades/<nombre>`,
  dentro de la raíz del kit. Con la misma regla de copia y verificación.
- **ChatGPT Work en escritorio:** inicia en un proyecto local con la carpeta del
  kit como carpeta principal. Si no consta que leíste `AGENTS.md` en este chat,
  léelo completo antes de actuar; su lectura automática en Work no está comprobada.
  Comprueba el catálogo de Habilidades y el flujo de instalación disponible.
  Invocación explícita: `@` y selección de la habilidad. No presupongas que Work
  descubre `Habilidades/` ni apliques rutas de Codex como configuración de Work.
  Si hace falta empaquetar, usa el mecanismo documentado vigente.
  [Guía oficial](https://learn.chatgpt.com/docs/build-skills).
- **Claude Cowork:** corre aislado; no crees enlaces. Las reglas llegan por
  `CLAUDE.md`, que importa `AGENTS.md`; si no las ves cargadas, lee `AGENTS.md`
  completo. Si tienes una herramienta para instalar habilidades en la cuenta, úsala
  con cada habilidad del kit. Si no, genera un ZIP por habilidad en
  `Habilidades/paquetes-locales/` (una carpeta con su `SKILL.md` y sus recursos,
  no archivos sueltos; sin PERFIL, MEMORIA, demos ni archivos del cliente), di la
  carpeta donde quedaron y guía el clic de subida en la interfaz de Skills.
  [Guía oficial](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills).
- **Otro entorno:** utiliza su descubrimiento documentado o lectura directa.
  No conviertas al cliente a otra aplicación para que el kit funcione.

Fecha de consulta de estas guías: 2026-09-22. Enlaces probados el 2026-10-17
con Claude Code 2.1.289 y Codex 0.160.0 en macOS. Las interfaces pueden cambiar.
Una instalación es verificada solo si el catálogo la reconoce; una activación es
verificada solo si una petición pertinente carga la skill y sigue su procedimiento.
Pruébala durante trabajo real, no ejecutando acciones de escritura ficticias.
Registra ambos estados por separado. Las copias instaladas llevan la versión de
su fuente; si difiere, ofrece actualización sin sobrescribir personalizaciones.
Una skill instalada fuera del kit debe pedir la raíz si no está seleccionada y
leer allí las reglas: nunca aplicar este sistema a cualquier carpeta por defecto.

## Reunión 0 (una pregunta a la vez)

Reutiliza respuestas ya dadas; no vuelvas a preguntar porque cambió el modo.

1. Confirma quién lo usará y para qué: contexto personal, negocio o mixto. Usa
   nombre confirmado en el chat/perfil; no lo deduzcas de Git ni de la computadora
   del consultor. Si falta, pregunta con naturalidad.
2. «Cuéntame un trabajo reciente: ¿qué recibiste, qué tuviste que hacer y qué
   entregaste?». Propón vocabulario a partir de ese ejemplo. Si no sabe, conserva
   Proyectos provisionalmente y continúa. Si acepta un nombre, aplica el renombrado
   completo del mapa de `AGENTS.md`; áreas permanentes y datos no son sinónimos de
   proyectos. No muestres toda la estructura como un menú que deba diseñar.
3. Elige con él UNA necesidad y, si hace falta, UNA muestra de archivos autorizada.
   Si pide entender el negocio, usa `dossier-inicial` sin repetir las dos primeras
   preguntas. Si pide un entregable concreto, hazlo sin obligar a crear un dossier.
4. Guarda el primer resultado dentro de la raíz del kit, no solo en la carpeta de
   trabajo de la aplicación. Reabre allí el archivo y verifica su registro según
   la regla dura del router.
   Solo crea un proyecto si existe una iniciativa real; no uno para cada pregunta.
   Completa únicamente los datos del perfil relevantes, con su fuente. Salud,
   metas completas y muestras de voz no son requisitos del arranque.
5. Muestra dónde quedó y cómo retomarlo. Enseña las tres frases del router. Marca
   arranque completado cuando haya resultado persistido y una forma de continuar;
   un perfil parcial es válido. Si se interrumpe, guarda el siguiente paso.

## Estado mínimo de esta copia (lo mantiene el asistente)

Crea `estado-local.md` aquí solo al guardar progreso autorizado. Es estado, no
otra fuente de reglas. No se distribuye con el kit ni se incluye en paquetes.
Plantilla orientativa; completa hechos, no ejemplos inventados:

```markdown
# Estado local
- Arranque: pendiente | en curso | completado
- Siguiente paso: acción o ninguno
- Primer resultado: enlace relativo desde este archivo o pendiente
- Nomenclatura: provisional | confirmada (el nombre real vive solo en AGENTS.md)
- Última revisión completada: YYYY-MM-DD o desconocida
- Último recordatorio de respaldo: YYYY-MM o ninguno
- Capacidades enseñadas / pospuestas: lista breve

## Adaptación por aplicación
### Aplicación identificada
- Acceso: lectura comprobada; escritura pendiente o comprobada con enlace
- Oferta de instalación: pendiente | aceptada | pospuesta
- Habilidad / versión fuente / habilitación / activación / evidencia o pendiente
```

En una copia antigua sin estado, usa el perfil y fichas para conservar decisiones,
pero no deduzcas onboarding completo del número de carpetas. Distingue demos de
trabajo real. Si hay ambigüedad, una confirmación breve; no borrar ni reiniciar.
Cambiar de app agrega otra adaptación y mantiene todo el avance compartido.
