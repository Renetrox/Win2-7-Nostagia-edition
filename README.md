# Win2-7 Nostalgia Edition
<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/c0e33c0e-d205-41dd-a9a6-7eb816ea69cb" />

Recuperación moderna para XFCE del clásico **Win2-7 Pack**, con una instalación legible y reversible.

> Estado: restauración en desarrollo. Pruébala primero en una cuenta secundaria.

## Incluye

- Temas **Aerobird** y **Aerobird-Blue** para GTK 2, GTK 3, GTK 4 y XFWM4; **Aerobird** es el perfil predeterminado por ser el más cercano al Win2-7 original.
- Tema de iconos moderno **Windows-7** y archivos históricos **Win2-7Libre** y **Win2-7**.
- Cursores **aero-drop**, sonidos FreeDesktop y fondo clásico.
- Temas Win2-7 para [Angujanú](https://github.com/Renetrox/Angujanu).
- Perfil opcional de panel con **Kesú + Docklike**, bandeja, volumen, reloj y mostrar escritorio.

El perfil no contiene datos personales, redes, clima ni lanzadores fijados.

## Instalación recomendada

```bash
chmod +x install.sh uninstall.sh
./install.sh --full
```

`--full` instala los recursos locales, activa la apariencia, intenta instalar Angujanú, Kesú y Docklike, aplica el panel y lo reinicia al final. Antes de modificar el panel crea una copia de seguridad.

Valores predeterminados:

- GTK/XFWM: `Aerobird`
- iconos: `Windows-7`
- cursor: `aero-drop`
- menú Angujanú: `Win2-7Blue`
- fondo: `Win2-7.jpg`

## Otros modos

```bash
./install.sh
```

Instala solamente los recursos. Si se ejecuta desde una terminal y hay Internet, pregunta si deseas añadir Angujanú, Kesú y Docklike.

```bash
./install.sh --apply
./install.sh --offline --apply
./install.sh --panel
./install.sh --apply --theme Aerobird --icons Win2-7Libre
```

- `--apply`: activa apariencia y fondo; si los complementos ya existen, ofrece aplicar el panel.
- `--offline`: no consulta ni descarga nada.
- `--panel`: aplica el perfil del panel únicamente si Kesú y Docklike están disponibles.
- `--theme` y `--icons`: seleccionan variantes.

En Debian, Docklike se instala desde `apt` cuando el paquete `xfce4-docklike-plugin` está disponible. En versiones que no lo incluyen, el instalador intenta compilarlo desde su [repositorio oficial](https://github.com/nsz32/docklike-plugin).

## Qué muestra el instalador

Cada etapa se informa por separado: temas GTK, XFWM, iconos, cursores, sonidos, fondo, Angujanú, Kesú, Docklike y panel. Los elementos que no pudieron completarse aparecen como `[PENDIENTE]`, sin ocultar una instalación parcial.

## Desinstalación

```bash
./uninstall.sh
```

Elimina los recursos propios de esta edición y restaura la apariencia, los fondos y el panel guardados antes de la primera activación. Angujanú, Kesú y Docklike se conservan porque son proyectos independientes y pueden estar siendo usados por otra configuración.

## Requisitos

- Linux con XFCE
- `xfconf-query` para activar la apariencia
- `tar` con bzip2
- Internet, `git`, compilador y `sudo` solamente para la experiencia completa

No se requieren Python 2, GConf, GNOME Panel, Compiz ni Emerald.

## Estructura

```text
Files/
├── gtk3-theme/     temas Aerobird GTK/XFWM
├── icon-theme/     iconos modernos e históricos
├── cursor/         cursores
├── sounds/         tema de sonidos
├── backgrounds/    fondos
├── gnomenu/        recursos para Angujanú
└── panel/          perfil XFCE portátil
```

## Nota histórica

El instalador original estaba dirigido a Ubuntu y GNOME 2 y modificaba numerosos componentes del sistema. Su código Python 2 y las operaciones globales inseguras fueron retirados del árbol activo; continúan disponibles en el historial del repositorio.

## Créditos

- **Juan de Jesús (juandejesuss)**: creador del Win2-7 Pack original,
  cuya idea, recursos y experiencia de transformación inspiran esta edición.
- **jmoney777**: creador de AeroBird y AeroBird-Blue para XFCE.
- **B00merang Artwork**: adaptación y mantenimiento moderno del tema
  de iconos Windows-7 basado en los iconos originales de Win2-7.
- **nsz32 y colaboradores**: desarrollo de Docklike Taskbar.
- **Renetrox**: restauración, adaptación para XFCE e integración con
  Angujanú y Kesú.
  
## Licencias y créditos

Esta edición combina material del Win2-7 Pack histórico y trabajos posteriores. Las licencias de cada recurso heredado deben documentarse individualmente antes de una publicación formal. Angujanú, Kesú y Docklike son proyectos separados y no se incluyen dentro de este repositorio.
