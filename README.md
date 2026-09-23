# 🧠 Segundo Cerebro · Kit de Inicio

Una carpeta simple para organizar tu vida, tus proyectos y tus ideas con ayuda de
tu asistente de IA. **Tú hablas; el sistema guarda, ordena y recuerda por ti.**

No necesitas saber nada técnico. Si sabes usar WhatsApp, puedes usar esto.

> 📄 **¿Prefieres leerlo con calma fuera de la compu?** Abre **`GUIA-DE-INICIO.pdf`**
> (misma info, en bonito, para imprimir o ver en el teléfono).

---

## 🇬🇧 English summary

**A "second brain" starter kit for Claude Cowork and ChatGPT Work.** It is a plain
Markdown folder plus one rule file (`AGENTS.md`; `CLAUDE.md` imports it)
that turns Claude or ChatGPT into the person who files, links and remembers your
notes. You point the app at the folder, say one sentence, and the agent writes.

Everything else in this repo is written in Spanish on purpose. It targets
**non-developers in Latin America**: consultants, small business owners, students
who will never read agent documentation in English. They install the kit, open it in
Obsidian, and say one sentence in Spanish (*"Inicia mi segundo cerebro"*) to start.

- **Who it is for:** people who do not code. If you can use WhatsApp, you can use this.
- **What the agent does:** onboarding interview, capture, weekly review, business
  dossier, voice matching, session handoff, actionable summaries. Six skills under
  `Habilidades/`.
- **Shared rules:** one source (`AGENTS.md`); `CLAUDE.md` is a one-line `@AGENTS.md`
  import for Claude. In ChatGPT Work, ask it to read `AGENTS.md` if it does not confirm.
- **License:** MIT.

---

## 🚀 Instalación en 3 pasos

### Paso 1 · Descarga el kit

En GitHub: botón verde **`Code`** ▸ **`Download ZIP`**. Descomprime el ZIP y guarda
la carpeta en un lugar fijo que no vayas a mover.

> 💡 **Tip que te salvará algún día:** guárdala DENTRO de tu carpeta de iCloud Drive,
> Google Drive o OneDrive para sincronizarla. Conserva también una copia independiente
> con fecha: la sincronización puede propagar borrados.

### Paso 2 · Ábrelo en Obsidian (recomendado, gratis)

**Obsidian** es una app gratuita para notas. Descárgala aquí:
👉 **https://obsidian.md/download** — el kit ya trae la configuración lista, no
tienes que ajustar nada.

1. Instala Obsidian (Windows / Mac / Linux).
2. Ábrelo y elige **"Open folder as vault"** (Abrir carpeta como bóveda).
3. Selecciona la carpeta que descomprimiste (`kit-segundo-cerebro`).
4. Si Obsidian pregunta por los plugins, puedes habilitar las 4 ayudas incluidas:
   búsqueda de ajustes, archivos recientes, barra de edición e iconos. Son opcionales;
   también puedes empezar sin ellas.

Obsidian es para que TÚ leas y hojees tus notas. El trabajo pesado lo hace tu
asistente en el paso 3.

### Paso 3 · Conecta tu asistente de IA

El kit funciona con **Claude Cowork** y con **ChatGPT Work en la app de escritorio**.
Elige el que ya uses y conecta la carpeta local del kit.

**Con Claude:**
1. Descarga la app aquí: 👉 **https://claude.com/download** (Mac y Windows) y entra
   con tu cuenta.
2. Entra a **Cowork** y selecciona la carpeta del kit (la misma que abriste en
   Obsidian).
3. Escríbele la frase mágica de abajo.

**Con ChatGPT:**
1. Abre la app de ChatGPT y entra con tu cuenta.
2. Entra a **Work local** y abre un proyecto local con la carpeta del kit como
   carpeta principal. El modo en la nube y la versión web no tienen por sí solos
   acceso directo a esa carpeta de tu computadora.
3. En el primer chat, escribe: **«Lee `AGENTS.md` de esta carpeta y sigue sus
   instrucciones. Inicia mi segundo cerebro.»** En chats nuevos del mismo proyecto,
   vuelve a pedir la lectura de `AGENTS.md` si Work no confirma que ya la hizo.

> 💡 Si tu app no encuentra la carpeta a la primera, revisa que la hayas guardado en
> un lugar normal (Documentos, Escritorio, iCloud Drive) y no dentro del ZIP sin
> descomprimir. Es el tropiezo más común del paso 3.

> ### ✨ La primera frase con Claude:
> # « Inicia mi segundo cerebro »

El asistente comprueba el acceso a la carpeta. Después te pregunta por un trabajo
real y te ayuda a obtener un primer
resultado. No necesitas completar todo tu perfil ni decidir cómo organizarte hoy.
Si todavía no sabes cómo llamar a tus asuntos, conserva «Proyectos» y sigue.

Las ayudas del kit se usan cuando las necesitas. No hace falta instalarlas
todas para empezar. Si la aplicación no puede guardar o habilitar alguna, te dirá
qué falta; puedes continuar con las instrucciones de la carpeta.
Al cambiar entre Work y Cowork, solo se revisa la adaptación, no se reinicia tu perfil.

**Para empezar basta con tres frases:** «guarda esto», «ayúdame con este asunto» y
«retomemos donde quedamos». Las demás capacidades aparecen cuando las necesitas.

---

## 🗣️ Las frases que mueven todo

| Tú dices… | Y el sistema… |
|---|---|
| **"Inicia mi segundo cerebro"** | Adapta el kit a tu aplicación y te ayuda con un primer trabajo; el perfil se completa poco a poco |
| **"Este es el cerebro de mi negocio"** | Te hace 4 preguntas, explora los archivos que le señales (solo los lee, no los toca) y arma el **Dossier** de tu negocio: qué entendió, qué encontró, qué está en riesgo y qué le falta saber. Si tu equipo ya usa IA sin reglas, te propone su política de uso en una página |
| **"Estoy empezando un proyecto nuevo: X"** | Crea su carpeta y ficha, y lo enlaza en tu lista para retomarlo |
| **"Guárdame esto para después"** | Lo deja en tu Entrada, sin interrumpirte |
| **"Acuérdate de que…"** | Anota el dato con fecha en tu memoria |
| **"Escribe esto en mi voz"** | Redacta el texto como tú lo escribirías |
| **"Resúmeme esto con pendientes"** | Convierte notas o una reunión en decisiones, próximos pasos y preguntas abiertas, sin inventar nada |
| **"Dame una segunda opinión de esto"** | Prepara tu documento para que otro chat (o la otra app) lo critique sin ver esta conversación; luego deciden juntos qué aplicar |
| **"Revisión semanal"** | Te dice qué avanzó, qué está atorado, rescata cosas olvidadas y limpia el sistema |

> No hay que memorizarlas: pregúntale a tu asistente **"¿qué puedo pedirte?"** cuando
> sea y te las recuerda.

---

## 🔁 Los 3 hábitos que hacen que funcione

**1. Captura el pensamiento, vuelve después a completarlo.**
En cuanto llega una idea, link o pendiente: díselo al asistente ("guárdame esto") o
suéltalo como una nota. En Obsidian, **toda nota nueva nace ya en `Entrada/`** — no
eliges carpeta, solo capturas. No tienes que dejarla perfecta: la sueltas, sigues con
lo tuyo, y cuando la necesites (o en la revisión) regresas a completarla. Ordenar no
es tu trabajo; es del sistema.

**2. Revisión semanal, una vez por semana.**
Es el corazón del sistema: 10-15 minutos donde el asistente te reporta, limpia todo
y te rescata lo que se estaba olvidando. Ponla en tu calendario (por ejemplo, viernes
o domingo).

**3. Respaldo sin esfuerzo.**
Además de sincronizar, conserva una copia independiente con fecha en USB o ZIP.
El asistente lo recordará durante la primera revisión de cada mes. La revisión
se inicia cuando la pides; no queda programada automáticamente al instalar el kit.

---

## ❓ Preguntas y sustos comunes

**"¿Tengo que abrir el mismo chat de siempre?"**
No. Ya no dependes de un chat ni de un historial: **todo vive en los archivos de esta
carpeta.** Abre una conversación nueva cuando quieras; lo único importante es tener
**seleccionada la carpeta del kit** al empezar. Con Work, pídele que lea
`AGENTS.md` al comenzar cada chat si no consta esa lectura. Luego se pone al día
abriendo solo los archivos pertinentes.

**"¿Por qué se me acaba el límite de uso tan rápido?"**
Lo que más consume es una conversación larga: cada mensaje nuevo arrastra todo lo
anterior. Usa una conversación por asunto y, cuando una se alargue, di «déjalo
listo para continuar» y sigue en un chat nuevo; nada se pierde porque todo vive en
la carpeta. Pide lo concreto («revisa la cotización de Juan») en lugar de «lee
todo».

**"El asistente escribió algo mal o donde no era."**
Díselo: "eso está mal, corrígelo" o "eso va en otro lado". Él lo arregla. No
necesitas editar archivos a mano (aunque puedes: son texto normal).

**"Work creó el archivo en otra carpeta. ¿Ya quedó guardado?"**
Todavía no. Pídele: "guárdalo dentro de mi segundo cerebro y verifica el enlace".
El asistente debe llevarlo a esta carpeta, comprobarlo allí y decirte dónde quedó.

**"¿Puedo mover carpetas o renombrar archivos yo mismo?"**
Mejor pídeselo al asistente. Debe actualizar y verificar los enlaces al moverlos,
sin crear una segunda carpeta con el mismo propósito. Si hay dos carpetas posibles,
primero te ayudará a decidir qué conservar.

**"¿Qué archivos NO debo tocar?"**
`AGENTS.md`, `CLAUDE.md` y la carpeta `.obsidian/` son la maquinaria. No hace falta
tocarlos ni entenderlos. Todo lo demás es tuyo.

**"Quiero cambiar cómo se comporta el asistente."**
Díselo en el chat: "a partir de ahora, siempre haz X". Él guarda la regla en su
archivo de instrucciones y la aplica en cada conversación futura.

**"¿Y si cambio de app o dejo de pagar?"**
Tu información no se va con la app: son archivos de texto normales en tu
computadora. El kit funciona igual en Cowork y en Work, y al cambiar solo se
revisa la adaptación. Si dejas de pagar, la carpeta sigue siendo tuya completa.
Compruébalo cuando quieras: abre cualquier nota con el Bloc de notas o TextEdit,
sin exportar nada.

**"¿Sirve en el teléfono?"**
Para leer tus notas: sí, con la app de Obsidian y la carpeta en iCloud/Drive. El
asistente trabaja mejor desde la computadora.

---

## 📂 Qué hay adentro (por si te da curiosidad)

| Archivo / carpeta | Para qué sirve |
|---|---|
| `GUIA-DE-INICIO.pdf` | Esta guía, lista para imprimir o mandar al teléfono |
| `AGENTS.md` | Las instrucciones del asistente (fuente única de reglas) |
| `CLAUDE.md` | Puente de una línea para que Claude lea `AGENTS.md` |
| `PERFIL.md` | Todo sobre ti: quién eres, qué quieres lograr, cómo escribes |
| `MEMORIA.md` | Datos sueltos con fecha que vas descubriendo |
| `Entrada/` | Tu puerta de captura: aquí cae todo lo que sueltas (y toda nota nueva de Obsidian) |
| `Diario/` | Tus notas diarias. **No existe todavía**: se crea sola la primera vez que hagas una entrada de diario en Obsidian |
| `Ideas/` | Notas de brainstorm y traspasos de sesión. Se crea sola cuando la usas |
| `Proyectos/` | Una carpeta por proyecto, cada una con su ficha (`INDEX.md`) |
| `Dossier — … .md` | El dossier de tu negocio, si usas el kit como cerebro de tu empresa. Crece cada semana con lo que el sistema aprende |
| `Plantillas/` | Las plantillas con las que nacen los proyectos nuevos, el dossier y la política de uso de IA |
| `Habilidades/` | Lo que el asistente sabe hacer (dossier de tu negocio, entrevistarte, tu voz, resumen con pendientes, revisión semanal, traspaso de sesión) |
| `.obsidian/` | Configuración de Obsidian ya lista. No se toca |

---

## 🔄 Cómo se ve tu semana con el sistema

Todo el sistema es este ciclo de 3 movimientos. Nada más:

```
   ┌──────────────────────────────────────────────────────┐
   │  1. CAPTURAS · todos los días                        │
   │     Hablas con tu asistente o sueltas una nota.      │
   │     Todo cae en  Entrada/  sin que ordenes nada.     │
   └───────────────────────────┬──────────────────────────┘
                               │
   ┌───────────────────────────▼──────────────────────────┐
   │  2. TRABAJAS · cuando lo necesites                   │
   │     "empieza proyecto X"  ·  "escribe en mi voz"     │
   │     El asistente responde leyendo TUS archivos.      │
   └───────────────────────────┬──────────────────────────┘
                               │
   ┌───────────────────────────▼──────────────────────────┐
   │  3. REVISAS · 1 vez por semana                       │
   │     Vacía la Entrada, ordena todo, te reporta        │
   │     avances y rescata lo que estabas olvidando.      │
   └───────────────────────────┬──────────────────────────┘
                               │
                   ↺  vuelve al paso 1
```

Tú solo capturas, pides y revisas. **El orden y el mantenimiento son trabajo del
asistente, no tuyo.**

## Para quien instala el kit en consultoría

Conserva la demo como copia independiente. Nunca entregues a un cliente una copia
de la carpeta de demostración con proyectos, perfil o historial mezclados.
La entrega limpia y los paquetes de habilidades se preparan siguiendo
[la guía de mantenimiento](Habilidades/_mantenimiento/README.md). Es material del
consultor; el cliente no necesita abrirlo. El nombre Segundo Cerebro se conserva.

### Lista del consultor para la reunión 0

Antes de la primera sesión, en la cuenta del cliente y con su permiso:

1. **Limpia lo que no usa.** Revisa plugins, habilidades y conectores activos en
   su app y apaga los que no va a usar: cada uno ocupa lugar en lo que el
   asistente lee y compite con las habilidades del kit.
2. **Revisa su plan y sus límites.** Confirma qué plan tiene y si alcanza para el
   uso que espera. Explícale que las conversaciones largas son lo que más consume.
3. **Revisión semanal programada, si la quiere.** Si su app permite programar
   tareas y él lo autoriza, programa la revisión semanal; una rutina corta consume
   poco. Si no hay mecanismo comprobado, queda como hábito que él pide.
4. **Si su equipo ya usa IA sin reglas**, llenen juntos la política de uso de IA
   (`Plantillas/politica-uso-ia-template.md`) antes de meter datos del negocio.
