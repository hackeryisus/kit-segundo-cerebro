# Mantenimiento del kit (para el consultor)

El cliente no necesita Python ni Git para usar el kit. Estas utilidades son solo
para preparar entregas desde el repositorio de desarrollo. No instalan nada en
ChatGPT ni Claude. El nombre y las habilidades del kit se conservan.

## Una sola carpeta

Este repositorio es la única base: fuentes, pruebas y entregas. No hay copia de
demostración permanente. Para una demo o un ensayo, descomprime el ZIP de entrega
en otra carpeta y úsala como cliente; al terminar se borra. Nunca edites esa copia
como fuente ni sincronices perfil, estado, documentos o proyectos de vuelta aquí.
El ZIP incluye solo archivos permitidos; no copia el árbol de trabajo entero.
El perfil, memoria e índice inicial deben coincidir con las huellas de fábrica
en `preparar.py`. Si se actualizan esas plantillas, revisa que estén vacías y
actualiza sus huellas deliberadamente; nunca para hacer pasar una copia de cliente
por una plantilla. La configuración estética original se lee del commit `634e107`.

Desde la raíz del repositorio, con Python 3.9+ y Git disponibles:

```sh
python3 Habilidades/_mantenimiento/preparar.py kit
python3 Habilidades/_mantenimiento/preparar.py skills
python3 -m unittest discover -s Habilidades/_mantenimiento -p 'test_*.py'
```

Sin ruta, la salida va a `Entregas/<fecha>/kit` o `Entregas/<fecha>/habilidades`
(carpeta ignorada por Git). También acepta una ruta nueva fuera de la base.
La carpeta de salida debe ser nueva; no se sobrescribe. El primer comando
crea `Kit-Segundo-Cerebro.zip`; el segundo, un ZIP individual por habilidad, con carpeta raíz
y SKILL.md. Son útiles cuando la interfaz de instalación acepta ese formato, no
una garantía de compatibilidad de importación con cualquier aplicación. En Work,
verifica el mecanismo disponible según [arranque](../arranque.md).
No empaquetes perfiles dentro de habilidades. Las fuentes siguen en Habilidades;
las copias instaladas no se editan como una segunda versión independiente.

Si recibes solo el ZIP de cliente sin Git, úsalo normalmente: la preparación de
nuevas distribuciones se hace en el repositorio del consultor, no en esa copia.

## Prueba de aceptación en Work y Cowork

Haz cada recorrido en una copia de ensayo, con datos ficticios. Estas pruebas son
manuales: los tests de empaquetado NO acreditan el comportamiento de los modelos.

| Caso | Petición / preparación | Evidencia requerida |
|---|---|---|
| Inicio limpio en Work | Proyecto local con el kit; «Lee CLAUDE.md de esta carpeta y sigue sus instrucciones. Inicia mi segundo cerebro» | Confirma lectura, pregunta por un trabajo real y no fuerza perfil completo ni instalación masiva. |
| Chat nuevo en Work | Abrir otro chat del mismo proyecto y pedir lectura de CLAUDE.md | Recupera las reglas sin presumir lectura automática de AGENTS.md. |
| No sabe nombrar | «Todavía no sé cómo organizarme» | Conserva Proyectos y entrega algo útil. |
| Renombrar | «Llamémoslos Expedientes» con contenido previo | Mismo contenido, mapa y enlaces válidos, sin Proyectos duplicado. |
| Colisión | Proyectos y Expedientes ya existen | Inspecciona y pide decisión; no fusiona ni borra automáticamente. |
| Cascada | Crear un asunto con entregable | Índice general enlaza ficha; ficha enlaza entregable; siguiente chat lo encuentra. |
| Carpeta separada | Pedir un entregable que Work genere primero en su carpeta de trabajo | La versión maestra aparece dentro de la raíz del kit, enlazada desde su ficha o MEMORIA y reabierta allí. Una copia externa por sí sola no cuenta como guardado. |
| Cambiar de app | Abrir la misma copia con otra aplicación | Comprueba adaptación; mantiene perfil y decisiones, no repite entrevista. |
| Skill | Petición pertinente para cada una de las seis | Se reconoce y carga la habilidad; registrar habilitación y activación por separado. |
| Contexto | Petición simple y luego una que active una habilidad | Lee CLAUDE.md una vez por chat; abre solo la habilidad y los archivos necesarios. Compara uso real en la app antes y después. |
| Instalación pospuesta | «Después instalamos» | Continúa por lectura directa y no insiste cada conversación. |
| Solo lectura | Revocar escritura, pedir análisis | No crea estado ni anuncia guardado. |
| Revisión | README en Entrada, archivo pendiente y área permanente | Conserva README; no pierde capturas; no archiva el área por antigüedad. |
| Reanudar | «Déjalo listo para continuar»; chat nuevo | Traspaso enlazado y siguiente paso recuperable. |
| Voz incompleta | Perfil vacío, pedir un correo en mi voz | Pide muestra/tono o ofrece borrador provisional, sin entrevista completa. |
| Resumen | Pegar notas de una reunión: «Resúmeme esto con pendientes» | Decisiones y próximos pasos sin inventar responsables ni fechas; lo inferido va marcado. |
| Segunda opinión | «Dame una segunda opinión de esto» sobre una propuesta | Paquete con documento, objetivo y criterios, sin la conversación; no aplica cambios sin decisión. |
| Hueco | Pedir un dato que el kit no tiene | Lo dice, anota `hueco:` con fecha en MEMORIA y la revisión semanal lo muestra. |

Anota aplicación/versión, fecha, resultado y evidencia en el estado de la copia de
ensayo. El tamaño de los archivos no equivale al consumo real de créditos o tokens;
para atribuir la causa registra modelo, duración, herramientas, archivos leídos y
uso mostrado por la app en tareas comparables. No anuncies compatibilidad total
hasta ejecutar el recorrido en la versión de Work del cliente.

## Antes de distribuir

Revisa el diff, valida habilidades, regenera el PDF desde su HTML y revisa sus
páginas. Ejecuta los tests y abre el ZIP: debe estar vacío de datos personales y
demos. Commit solo de fuentes de la base limpia. Publicar en GitHub o sustituir
la descarga de una web es un paso separado, no una consecuencia de crear el ZIP.
