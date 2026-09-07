#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
FILES_DIR="$ROOT_DIR/Files"
THEME="Aerobird-Blue"
ICONS="Windows-7"
APPLY=false
PANEL=false
ONLINE_MODE="ask"
TEMP_DIR=""

usage() {
    cat <<'EOF'
Uso: ./install.sh [opciones]
  --apply                         Activa tema, iconos, cursor y fondo
  --full                          Instala, activa y completa menú/panel (requiere Internet)
  --offline                       No consulta ni descarga componentes
  --panel                         Aplica el panel Win2-7 si Kesú y Docklike están instalados
  --theme Aerobird|Aerobird-Blue
  --icons Windows-7|Win2-7Libre|Win2-7
EOF
}

ok() { printf '  [INSTALADO] %s\n' "$1"; }
info() { printf '  [INFO] %s\n' "$1"; }
warn() { printf '  [PENDIENTE] %s\n' "$1"; }

cleanup() {
    [ -z "$TEMP_DIR" ] || rm -rf "$TEMP_DIR"
}
trap cleanup EXIT

while [ "$#" -gt 0 ]; do
    case "$1" in
        --apply) APPLY=true ;;
        --full) APPLY=true; PANEL=true; ONLINE_MODE="yes" ;;
        --offline) ONLINE_MODE="no" ;;
        --panel) APPLY=true; PANEL=true ;;
        --theme)
            [ "$#" -ge 2 ] || { usage; exit 2; }
            THEME="$2"; shift ;;
        --icons)
            [ "$#" -ge 2 ] || { usage; exit 2; }
            ICONS="$2"; shift ;;
        -h|--help) usage; exit 0 ;;
        *) echo "Opción desconocida: $1" >&2; usage; exit 2 ;;
    esac
    shift
done

case "$THEME" in Aerobird|Aerobird-Blue) ;; *) echo "Tema no compatible: $THEME" >&2; exit 2 ;; esac
case "$ICONS" in Windows-7|Win2-7Libre|Win2-7) ;; *) echo "Iconos no compatibles: $ICONS" >&2; exit 2 ;; esac

THEME_SRC="$FILES_DIR/gtk3-theme/$THEME"
ICON_DIR="$FILES_DIR/icon-theme/$ICONS"
ICON_ARCHIVE="$FILES_DIR/icon-theme/$ICONS.tar.bz2"
CURSOR_SRC="$FILES_DIR/cursor/aero-drop"
SOUND_SRC="$FILES_DIR/sounds/Win2-7"
WALLPAPER_SRC="$FILES_DIR/backgrounds/Win2-7.jpg"
WALLPAPER_DEST="$HOME/.local/share/backgrounds/win2-7-nostalgia/Win2-7.jpg"
STATE_DIR="$HOME/.config/win2-7-nostalgia"

for path in "$THEME_SRC" "$CURSOR_SRC" "$SOUND_SRC" "$WALLPAPER_SRC"; do
    [ -e "$path" ] || { echo "Falta un recurso requerido: $path" >&2; exit 1; }
done

ask_yes() {
    local prompt="$1" answer
    [ -t 0 ] || return 1
    read -r -p "$prompt [S/n] " answer
    case "$answer" in n|N|no|NO) return 1 ;; *) return 0 ;; esac
}

have_internet() {
    if command -v git >/dev/null 2>&1; then
        timeout 10 git ls-remote https://github.com/Renetrox/Angujanu.git HEAD >/dev/null 2>&1
    elif command -v curl >/dev/null 2>&1; then
        curl -fsSI --max-time 10 https://github.com/ >/dev/null
    else
        return 1
    fi
}

run_root() {
    if [ "$(id -u)" -eq 0 ]; then "$@"
    elif command -v sudo >/dev/null 2>&1; then sudo "$@"
    else
        echo "Se necesita sudo para instalar dependencias del sistema." >&2
        return 1
    fi
}

apt_install() {
    command -v apt-get >/dev/null 2>&1 || return 1
    run_root apt-get install -y "$@"
}

plugin_present() {
    local plugin="$1"
    find /usr/share/xfce4/panel/plugins /usr/local/share/xfce4/panel/plugins \
        -maxdepth 1 -name "$plugin.desktop" -print -quit 2>/dev/null | grep -q .
}

copy_angujanu_themes() {
    local target="$HOME/.local/share/xfcemenu/themes" kind
    [ -d "$target" ] || return 1
    [ -d "$FILES_DIR/gnomenu/Themes" ] || return 1
    for kind in Menu Button Sound Icon; do
        if [ -d "$FILES_DIR/gnomenu/Themes/$kind" ]; then
            mkdir -p "$target/$kind"
            cp -a "$FILES_DIR/gnomenu/Themes/$kind/." "$target/$kind/"
        fi
    done
}

install_angujanu() {
    [ -d "$HOME/.local/share/xfcemenu/themes" ] && return 0
    command -v git >/dev/null 2>&1 || apt_install git
    apt_install python3 python3-gi python3-cairo gir1.2-gtk-3.0 rsync dialog || return 1
    git clone --depth 1 https://github.com/Renetrox/Angujanu.git "$TEMP_DIR/Angujanu"
    (cd "$TEMP_DIR/Angujanu" && bash ./install_xfcemenu.sh)
}

install_kesu() {
    plugin_present kesu && return 0
    command -v git >/dev/null 2>&1 || apt_install git
    apt_install build-essential pkg-config libgtk-3-dev libxfce4panel-2.0-dev libxfce4ui-2-dev libxml2-dev || return 1
    git clone --depth 1 https://github.com/Renetrox/Kesu-button.git "$TEMP_DIR/Kesu-button"
    (cd "$TEMP_DIR/Kesu-button" && make clean && make && run_root make install)
}

install_docklike() {
    plugin_present docklike && return 0
    if command -v apt-cache >/dev/null 2>&1 && apt-cache show xfce4-docklike-plugin >/dev/null 2>&1; then
        apt_install xfce4-docklike-plugin
        return
    fi
    command -v git >/dev/null 2>&1 || apt_install git
    apt_install build-essential xfce4-dev-tools pkg-config libgtk-3-dev \
        libxfce4panel-2.0-dev libxfce4ui-2-dev libwnck-3-dev libcairo2-dev libx11-dev || return 1
    git clone --depth 1 https://github.com/nsz32/docklike-plugin.git "$TEMP_DIR/docklike-plugin"
    (cd "$TEMP_DIR/docklike-plugin" && ./autogen.sh --prefix=/usr/local && make && run_root make install)
}

install_online_components() {
    TEMP_DIR="$(mktemp -d)"
    echo
    echo "Componentes opcionales de la experiencia clásica"
    if install_angujanu; then ok "Angujanú (menú de aplicaciones)"; else warn "No se pudo instalar Angujanú"; fi
    if copy_angujanu_themes; then ok "Temas Win2-7 para Angujanú"; else warn "Temas de Angujanú no copiados"; fi
    if install_kesu; then ok "Kesú (botón del menú)"; else warn "No se pudo instalar Kesú"; fi
    if install_docklike; then ok "Docklike (barra de tareas)"; else warn "No se pudo instalar Docklike"; fi
}

apply_panel() {
    local panel_xml="$FILES_DIR/panel/xfce4-panel.xml"
    local docklike_rc="$FILES_DIR/panel/docklike-2.rc"
    local panel_dir="$HOME/.config/xfce4/panel"
    local xfconf_dir="$HOME/.config/xfce4/xfconf/xfce-perchannel-xml"
    local backup="$STATE_DIR/panel-before.tar.gz"
    local paths=()

    command -v xfce4-panel >/dev/null 2>&1 || { warn "XFCE Panel no está disponible"; return 1; }
    plugin_present kesu || { warn "El panel no se aplicó: falta Kesú"; return 1; }
    plugin_present docklike || { warn "El panel no se aplicó: falta Docklike"; return 1; }

    mkdir -p "$STATE_DIR" "$panel_dir" "$xfconf_dir"
    if [ ! -f "$backup" ]; then
        [ -d "$panel_dir" ] && paths+=(".config/xfce4/panel")
        [ -f "$xfconf_dir/xfce4-panel.xml" ] && paths+=(".config/xfce4/xfconf/xfce-perchannel-xml/xfce4-panel.xml")
        if [ "${#paths[@]}" -gt 0 ]; then
            tar -czf "$backup" -C "$HOME" "${paths[@]}"
        else
            tar -czf "$backup" --files-from /dev/null
        fi
    fi

    xfce4-panel --quit >/dev/null 2>&1 || true
    cp -a "$panel_xml" "$xfconf_dir/xfce4-panel.xml"
    cp -a "$docklike_rc" "$panel_dir/docklike-2.rc"
    : > "$STATE_DIR/panel-applied"
    if [ -n "${DISPLAY:-}" ]; then
        nohup xfce4-panel >/dev/null 2>&1 &
    fi
    ok "Panel Win2-7; la configuración anterior quedó respaldada"
}

echo
echo "Win2-7 Nostalgia Edition"
echo "========================================"

mkdir -p "$HOME/.themes" "$HOME/.icons" "$HOME/.local/share/sounds" "$(dirname "$WALLPAPER_DEST")"

rm -rf "$HOME/.themes/Aerobird" "$HOME/.themes/Aerobird-Blue"
cp -a "$FILES_DIR/gtk3-theme/Aerobird" "$HOME/.themes/Aerobird"
cp -a "$FILES_DIR/gtk3-theme/Aerobird-Blue" "$HOME/.themes/Aerobird-Blue"
ok "Temas GTK2/GTK3/GTK4: Aerobird y Aerobird-Blue"
ok "Decoraciones XFWM4"

if [ -d "$ICON_DIR" ]; then
    rm -rf "$HOME/.icons/$ICONS"
    cp -a "$ICON_DIR" "$HOME/.icons/$ICONS"
elif [ -f "$ICON_ARCHIVE" ]; then
    tar -xjf "$ICON_ARCHIVE" -C "$HOME/.icons"
else
    echo "Falta el tema de iconos: $ICONS" >&2
    exit 1
fi
ok "Iconos: $ICONS"

rm -rf "$HOME/.icons/aero-drop"
cp -a "$CURSOR_SRC" "$HOME/.icons/aero-drop"
ok "Cursores: aero-drop"

rm -rf "$HOME/.local/share/sounds/Win2-7"
cp -a "$SOUND_SRC" "$HOME/.local/share/sounds/Win2-7"
ok "Sonidos: Win2-7"

cp -a "$WALLPAPER_SRC" "$WALLPAPER_DEST"
ok "Fondo de escritorio: Win2-7.jpg"

if copy_angujanu_themes; then
    ok "Temas clásicos para Angujanú"
else
    info "Angujanú todavía no está instalado"
fi

if [ "$ONLINE_MODE" != "no" ]; then
    if have_internet; then
        if [ "$ONLINE_MODE" = "yes" ] || ask_yes "Hay Internet. ¿Instalar Angujanú, Kesú y Docklike?"; then
            install_online_components
            [ "$ONLINE_MODE" = "yes" ] && PANEL=true
        fi
    else
        info "Sin conexión disponible; se continúa con los recursos locales"
    fi
fi

if "$APPLY"; then
    command -v xfconf-query >/dev/null 2>&1 || { echo "xfconf-query es necesario para activar XFCE" >&2; exit 1; }
    STATE_FILE="$STATE_DIR/xfce-before-install"
    WALLPAPER_STATE="$STATE_DIR/wallpapers-before"
    mkdir -p "$STATE_DIR"

    if [ ! -f "$STATE_FILE" ]; then
        {
            printf 'GTK_THEME=%q\n' "$(xfconf-query -c xsettings -p /Net/ThemeName 2>/dev/null || true)"
            printf 'ICON_THEME=%q\n' "$(xfconf-query -c xsettings -p /Net/IconThemeName 2>/dev/null || true)"
            printf 'CURSOR_THEME=%q\n' "$(xfconf-query -c xsettings -p /Gtk/CursorThemeName 2>/dev/null || true)"
            printf 'XFWM_THEME=%q\n' "$(xfconf-query -c xfwm4 -p /general/theme 2>/dev/null || true)"
        } > "$STATE_FILE"
    fi

    mapfile -t WALLPAPER_PROPERTIES < <(
        xfconf-query -c xfce4-desktop -l 2>/dev/null | grep -E '/(last-image|image-path)$' || true
    )
    if [ ! -f "$WALLPAPER_STATE" ]; then
        : > "$WALLPAPER_STATE"
        for property in "${WALLPAPER_PROPERTIES[@]}"; do
            printf '%s\t%s\n' "$property" "$(xfconf-query -c xfce4-desktop -p "$property" 2>/dev/null || true)" >> "$WALLPAPER_STATE"
        done
    fi

    xfconf-query -c xsettings -p /Net/ThemeName -s "$THEME"
    xfconf-query -c xsettings -p /Net/IconThemeName -s "$ICONS"
    xfconf-query -c xsettings -p /Gtk/CursorThemeName -s aero-drop
    xfconf-query -c xfwm4 -p /general/theme -s "$THEME"
    ok "Perfil visual XFCE: $THEME"

    changed_wallpapers=0
    for property in "${WALLPAPER_PROPERTIES[@]}"; do
        if xfconf-query -c xfce4-desktop -p "$property" -s "$WALLPAPER_DEST" 2>/dev/null; then
            changed_wallpapers=$((changed_wallpapers + 1))
        fi
    done
    if [ "$changed_wallpapers" -gt 0 ]; then
        command -v xfdesktop >/dev/null 2>&1 && xfdesktop --reload >/dev/null 2>&1 || true
        ok "Fondo aplicado en $changed_wallpapers configuración(es) de XFCE"
    else
        warn "XFCE no publicó propiedades de fondo; selecciónalo manualmente desde Escritorio"
    fi

    if [ -f "$HOME/.config/xfcemenu/config.ini" ]; then
        sed -i 's/^[[:space:]]*menu_theme[[:space:]]*=.*/menu_theme = Win2-7Blue/' "$HOME/.config/xfcemenu/config.ini"
        ok "Menú de Angujanú: Win2-7Blue"
    fi
fi

if "$PANEL"; then
    apply_panel || true
elif "$APPLY" && plugin_present kesu && plugin_present docklike && ask_yes "¿Aplicar también el panel Win2-7?"; then
    apply_panel || true
fi

echo "========================================"
echo "Instalación finalizada para $USER."
if "$APPLY"; then
    echo "La apariencia de XFCE fue activada."
else
    echo "Para activarla, ejecuta: ./install.sh --apply"
    echo "Para la experiencia completa: ./install.sh --full"
fi
