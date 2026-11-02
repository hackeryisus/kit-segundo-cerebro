---
name: construir-herramienta
metadata:
  version: "1.0.0"
description: 'Úsala antes de escribir código: "hazme un script", "una app", "un tablero", "automatiza esto": plan corto, carpeta propia, secretos fuera, punto de guardado y prueba. Solo en la carpeta Mi Asistente.'
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
---

# Construir una herramienta

**Idioma:** responde y escribe en español (o en el idioma de `PERFIL.md`), aunque
los archivos, comandos o errores estén en inglés. Traduce cada error al explicarlo.

Antes de actuar, identifica la raíz del kit seleccionada. Lee su `AGENTS.md` solo
si aún no se leyó en esta conversación. Resuelve las rutas en su Mapa de carpetas.

El dueño no programa: tú construyes, él decide y prueba. Esta habilidad no
reemplaza lo que trae la app: si existe una revisión de seguridad (`/security-review`
en Claude Code) o una habilidad para crear habilidades, úsala. Aquí solo van las
cinco cosas que la app no hace por él.

## 1 · Plan de cinco líneas, antes del código

Crea `Herramientas/<nombre-corto>/LEEME.md` desde `LEEME-plantilla.md` (junto a
este archivo) y llénalo con el dueño: qué resuelve, qué entra, qué sale, qué datos
o cuentas toca y cómo sabremos que funciona. Muéstraselo en cinco líneas y espera
su sí. Si lo que pide se resuelve sin código (una habilidad, una plantilla, una
fórmula), dilo y ofrece eso primero. Lo que se repite igual cada vez va en un
script: un script no gasta tokens; la IA sí.

## 2 · Dónde vive

- Todo en `Herramientas/<nombre-corto>/`: código, `LEEME.md` y su registro.
- Si necesita instalar dependencias pesadas (`node_modules`, entornos de Python),
  el código va en una carpeta fuera del kit (por ejemplo `~/Herramientas/<nombre>`)
  y el `LEEME.md` se queda aquí con la ruta. Obsidian no debe indexar miles de
  archivos de librerías.
- Regístrala en la ficha del proyecto al que sirve.

## 3 · Secretos y datos

- Nunca escribas contraseñas, llaves o tokens en archivos, código ni MEMORIA. Usa
  el llavero del sistema o un archivo `.env` fuera de Git; copia
  `gitignore-plantilla` como `.gitignore` antes del primer archivo.
- Para correo, usa una contraseña de aplicación, nunca la principal.
- Si el dueño pega una contraseña en el chat, no la guardes y sugiérele cambiarla.
- Prueba con una copia de los datos, nunca con el original. Primero solo lectura.
- Enviar, publicar, pagar o borrar: solo borrador, según `AGENTS.md`.
- Nada queda abierto a internet (servidor, puerto, página pública, webhook) sin
  que el dueño lo consulte antes con su consultor.

## 4 · Punto de guardado

Antes del primer cambio, y antes de cada cambio grande, guarda una versión con Git
en la carpeta de la herramienta (`git init` la primera vez, luego `git add` de los
archivos tocados y `git commit -m "<qué cambió>"`). Explícalo así: «guardé un punto
al que podemos volver si algo se rompe». Si algo falla, vuelve al último punto en
vez de parchar encima. Nunca subas a GitHub ni a otra nube sin que lo pida.

## 5 · Probar, revisar y dejarla lista

1. Córrela con un caso real del dueño (en copia) y muéstrale el resultado.
2. Revisión: en Claude Code, `/security-review`; en otras apps, ofrece la
   segunda opinión (`Habilidades/segunda-opinion.md`) con la otra IA.
3. Tarea programada: una sola cosa por tarea, corta. Cada corrida anota fecha y
   resultado al final de `LEEME.md`. Que no avise no prueba que funcionó.
4. Actualiza `LEEME.md`: cómo se usa en una frase, de qué depende, última vez que
   funcionó. Haz el punto de guardado final y entrega según `AGENTS.md`.
