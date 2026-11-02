# 🤖 Mi Asistente · Kit de Inicio

Una carpeta en tu computadora que convierte a Claude o ChatGPT en **tu asistente
de IA**: conoce tu trabajo, guarda lo que le dices y hace por ti las tareas que se
repiten. **Tú hablas; tu asistente guarda, ordena, recuerda y trabaja.**

No necesitas saber nada técnico. Si sabes usar WhatsApp, puedes usar esto.

> 📄 **¿Prefieres leerlo con calma fuera de la compu?** Abre **`GUIA-DE-INICIO.pdf`**
> (misma info, en bonito, para imprimir o ver en el teléfono).

---

## 🇬🇧 English summary

**A starter kit that turns Claude (desktop or Code), ChatGPT Work or Codex into a
personal AI assistant that knows your work.** It is a plain Markdown folder plus one
rule file (`AGENTS.md`; `CLAUDE.md` imports it). You point the app at the folder,
say one sentence, and the agent files, remembers and automates.

Everything else is written in Spanish on purpose. It targets **non-developers in
Latin America**: consultants, small business owners and employees who will never
read agent documentation in English. The assistant always answers in Spanish. To
start, say *"Inicia mi asistente"*.

- **What the agent does:** short onboarding, capture, collections that mirror how
  you organise your work (clients, cases, projects), weekly review, business dossier,
  voice matching, session handoff, actionable summaries and safe small tools.
- **Shared rules:** one source (`AGENTS.md`, 150 lines max). Skills install on demand:
  relative links in `.claude/skills/` or `.agents/skills/` for Claude Code and Codex;
  the app's own installer or local ZIPs for Claude desktop and ChatGPT Work.
- **License:** MIT.

---

## 🚀 Instalación en 3 pasos

### Paso 1 · Descarga la carpeta

Descomprime el ZIP y guarda la carpeta **`Mi Asistente`** en un lugar fijo que no
vayas a mover (Documentos, por ejemplo).

> 💡 Puedes guardarla dentro de iCloud Drive, Google Drive o OneDrive para
> sincronizarla. Conserva también una copia independiente con fecha: la
> sincronización puede propagar borrados.

### Paso 2 · Ábrela en Obsidian (gratis)

**Obsidian** es una app gratuita para leer tus notas. Descárgala aquí:
👉 **https://obsidian.md/download**. La carpeta ya trae la configuración lista.

1. Instala Obsidian (Windows / Mac / Linux).
2. Ábrelo y elige **"Open folder as vault"** (Abrir carpeta como bóveda).
3. Selecciona la carpeta `Mi Asistente`.
4. Si pregunta por los plugins, puedes habilitar las ayudas incluidas. Son opcionales.

Obsidian es para que TÚ leas y hojees. El trabajo lo hace tu asistente en el paso 3.

### Paso 3 · Conecta tu asistente de IA

Funciona en **Claude** (app de escritorio o Claude Code), **ChatGPT Work en la app
de escritorio** y **Codex**. Usa siempre la **app de escritorio**, no la versión
web: la web no ve las carpetas de tu computadora.

**Con Claude:**
1. Descarga la app: 👉 **https://claude.com/download** (Mac y Windows) y entra con
   tu cuenta.
2. Abre un chat nuevo y selecciona la carpeta `Mi Asistente`.
3. Escríbele la frase de abajo.

**Con ChatGPT:**
1. Abre la app de ChatGPT de escritorio y entra con tu cuenta.
2. Entra a **Work local** y abre un proyecto local con la carpeta `Mi Asistente`
   como carpeta principal.
3. En el primer chat, escribe: **«Lee `AGENTS.md` de esta carpeta y sigue sus
   instrucciones. Inicia mi asistente.»** En chats nuevos, vuelve a pedir la
   lectura de `AGENTS.md` si Work no confirma que ya la hizo.

**Con Claude Code o Codex** (si ya los usas):
1. Ábrelo dentro de la carpeta `Mi Asistente`.
2. Escríbele la frase de abajo. Las instrucciones se cargan solas.

> ### ✨ La primera frase (en Work, usa la de arriba):
> # « Inicia mi asistente »

Tu asistente comprueba el acceso a la carpeta y te hace tres preguntas cortas:
quién eres, **cómo organizas tu trabajo** (por clientes, casos, proyectos o
procesos) y **qué tarea te quita más tiempo**. Con eso arma tus carpetas a tu modo
y te entrega un primer resultado con un archivo real tuyo. No necesitas llenar
todo tu perfil hoy.

> 💡 **Para que siempre te responda en español:** en tu app, ve a Ajustes y escribe
> en tus preferencias personales «Responde siempre en español». Tu asistente te lo
> recordará en el arranque.

**Para empezar basta con tres frases:** «guarda esto», «ayúdame con este asunto» y
«retomemos donde quedamos».

---

## 🗣️ Las frases que mueven todo

| Tú dices… | Y tu asistente… |
|---|---|
| **"Inicia mi asistente"** | Se adapta a tu app, arma tus carpetas a tu modo y te ayuda con un primer trabajo |
| **"Organiza mis clientes"** (o casos, obras, proveedores…) | Crea esa carpeta con su lista y una ficha por cada uno, igual que los proyectos |
| **"Este es el cerebro de mi negocio"** | Te hace 4 preguntas, explora los archivos que le señales (solo los lee) y arma el **Dossier** de tu negocio |
| **"Estoy empezando un proyecto nuevo: X"** | Crea su carpeta y ficha, y lo enlaza en tu lista |
| **"Guárdame esto para después"** | Lo deja en tu Entrada, sin interrumpirte |
| **"Acuérdate de que…"** | Anota el dato con fecha en tu memoria |
| **"Hazme un script / una app / un tablero que…"** | Te propone un plan de cinco líneas, y con tu sí lo construye seguro: en su carpeta, sin contraseñas en archivos y con un punto de guardado para deshacer |
| **"Escribe esto en mi voz"** | Redacta el texto como tú lo escribirías |
| **"Resúmeme esto con pendientes"** | Convierte notas o una reunión en decisiones y próximos pasos, sin inventar |
| **"Redacta el correo para…"** | Deja el borrador listo. **Nunca envía nada por ti**: tú lo revisas y lo mandas |
| **"Revisión semanal"** | Te dice qué avanzó, qué está atorado y qué estabas olvidando |

> No hay que memorizarlas: pregúntale **"¿qué puedo pedirte?"** cuando quieras.

---

## 🔁 Los 3 hábitos que hacen que funcione

**1. Captura y sigue.** En cuanto llega una idea, link o pendiente, díselo («guárdame
esto»). En Obsidian, toda nota nueva nace en `Entrada/`. Ordenar es trabajo de tu
asistente, no tuyo.

**2. Practica con tu trabajo real.** Cada vez que repitas una tarea, pídesela a tu
asistente con el archivo real. A la tercera vez que hagas lo mismo, te ofrecerá
convertirlo en una habilidad propia.

**3. Revisión semanal.** 10-15 minutos donde te reporta, limpia y rescata lo
olvidado. Ponla en tu calendario. La primera de cada mes te recuerda el respaldo.

---

## 🔒 Tus datos

- Todo vive en archivos de texto en **tu** computadora. No depende de un chat.
- Tu asistente solo lee fuera de esta carpeta lo que tú le señales, y no lo cambia
  sin tu permiso.
- Si encuentra contraseñas, datos bancarios, de salud o de tus clientes, no los
  copia: te pregunta cómo tratarlos.
- Nunca pegues contraseñas en el chat. Para conectar tu correo, usa una
  «contraseña de aplicación».
- Si tu equipo ya usa IA sin reglas, pídele: «hagamos nuestra política de uso de IA».

---

## ❓ Preguntas y sustos comunes

**"¿Tengo que abrir el mismo chat de siempre?"**
No. **Todo vive en los archivos de esta carpeta.** Abre una conversación nueva
cuando quieras; solo ten **seleccionada la carpeta `Mi Asistente`** al empezar.

**"¿Por qué se me acaba el límite de uso tan rápido?"**
Lo que más consume es una conversación larga: cada mensaje arrastra todo lo
anterior. Usa una conversación por asunto y, cuando se alargue, di «déjalo listo
para continuar» y sigue en un chat nuevo. Pide lo concreto («revisa la cotización
de Juan») en lugar de «lee todo». Y lo que se repite igual cada vez, pídelo como
script: un script no gasta tu límite.

**"Me respondió en inglés."**
Dile «respóndeme en español». La regla ya está en sus instrucciones; si pasa
seguido, revisa que tus preferencias de la app digan «Responde siempre en español».

**"El asistente escribió algo mal o donde no era."**
Díselo: «eso está mal, corrígelo» o «eso va en otro lado». Él lo arregla.

**"Creó el archivo en otra carpeta. ¿Ya quedó guardado?"**
Todavía no. Pídele: «guárdalo dentro de Mi Asistente y verifica el enlace».

**"¿Puedo mover carpetas o renombrar archivos yo mismo?"**
Mejor pídeselo: actualiza los enlaces al moverlos y no duplica carpetas.

**"¿Qué archivos NO debo tocar?"**
`AGENTS.md`, `CLAUDE.md` y la carpeta `.obsidian/` son la maquinaria. Todo lo demás
es tuyo.

**"Quiero cambiar cómo se comporta el asistente."**
Díselo: «a partir de ahora, siempre haz X». Guarda la regla y la aplica siempre.

**"¿Y si cambio de app o dejo de pagar?"**
Tu información no se va: son archivos de texto en tu computadora. Funciona igual en
Claude, ChatGPT Work y Codex. Compruébalo cuando quieras: abre cualquier nota con el
Bloc de notas o TextEdit.

**"¿Sirve en el teléfono?"**
Para leer tus notas, sí, con Obsidian y la carpeta en iCloud o Drive. Tu asistente
trabaja mejor desde la computadora.

---

## 📂 Qué hay adentro (por si te da curiosidad)

| Archivo / carpeta | Para qué sirve |
|---|---|
| `GUIA-DE-INICIO.pdf` | Esta guía, lista para imprimir o mandar al teléfono |
| `AGENTS.md` | Las instrucciones de tu asistente (fuente única de reglas) |
| `CLAUDE.md` | Puente para que Claude lea `AGENTS.md` |
| `PERFIL.md` | Todo sobre ti: quién eres, qué quieres lograr, cómo escribes, en qué idioma te responde |
| `MEMORIA.md` | Datos sueltos con fecha que vas descubriendo |
| `Entrada/` | Tu puerta de captura |
| `Proyectos/` | Una carpeta por proyecto con su ficha. Si trabajas por clientes o casos, tu asistente crea esas carpetas igual |
| `Herramientas/` | Los scripts y apps que construyas, cada uno con su `LEEME.md`. Nace al usarse |
| `Diario/`, `Ideas/` | Notas diarias y de brainstorm. Nacen al usarse |
| `Dossier — … .md` | El dossier de tu negocio, si lo pides |
| `Plantillas/` | Con lo que nacen las fichas nuevas, el dossier y la política de uso de IA |
| `Habilidades/` | Lo que tu asistente sabe hacer, y las habilidades que crees tú |
| `.obsidian/` | Configuración de Obsidian ya lista. No se toca |

---

## Para quien instala Mi Asistente en consultoría

Nunca entregues a un cliente una copia con proyectos, perfil o historial de otra
persona. La entrega limpia y los paquetes se preparan con
[la guía de mantenimiento](Habilidades/_mantenimiento/README.md).

### Lista del consultor para la sesión 0 (instalación)

1. **Antes de la sesión, que el cliente tenga listo:** Zoom de escritorio, la app
   de escritorio de Claude o ChatGPT (no la web), su usuario y contraseña a mano, y
   un archivo real de la tarea que más tiempo le quita. Si usa antivirus, avísale
   que puede pedir permisos.
2. **Privacidad primero:** abre la sesión con la sección «Tus datos», no al final.
3. **Idioma:** fija juntos «Responde siempre en español» en las preferencias de la app.
4. **Limpia lo que no usa:** plugins, habilidades y conectores que no va a usar.
5. **Plan y límites:** confirma su plan y explica que las conversaciones largas son
   lo que más consume.
6. **Organización:** en la pregunta 2 del arranque, pregúntale cómo funciona su
   trabajo y deja que el asistente clone Proyectos en su nomenclatura.
