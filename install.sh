#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
FILES_DIR="$ROOT_DIR/Files"
THEME="Aerobird-Blue"
ICONS="Windows-7"
APPLY=false

usage() {
    echo "Uso: ./install.sh [--apply] [--theme Aerobird|Aerobird-Blue] [--icons Windows-7|Win2-7Libre|Win2-7]"
}

ok() { printf '  [INSTALADO] %s\n' "$1"; }
info() { printf '  [INFO] %s\n' "$1"; }

while [ "$#" -gt 0 ]; do
    case "$1" in
        --apply) APPLY=true ;;
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

for path in "$THEME_SRC" "$CURSOR_SRC" "$SOUND_SRC" "$WALLPAPER_SRC"; do
    [ -e "$path" ] || { echo "Falta un recurso requerido: $path" >&2; exit 1; }
done

echo
echo "Win2-7 Nostalgia Edition"
echo "========================================"

mkdir -p "$HOME/.themes" "$HOME/.icons" "$HOME/.local/share/sounds"
mkdir -p "$(dirname "$WALLPAPER_DEST")"

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

ANGUJANU_DIR="$HOME/.local/share/xfcemenu/themes"
if [ -d "$ANGUJANU_DIR" ] && [ -d "$FILES_DIR/gnomenu/Themes" ]; then
    for kind in Menu Button Sound Icon; do
        if [ -d "$FILES_DIR/gnomenu/Themes/$kind" ]; then
            mkdir -p "$ANGUJANU_DIR/$kind"
            cp -a "$FILES_DIR/gnomenu/Themes/$kind/." "$ANGUJANU_DIR/$kind/"
        fi
    done
    ok "Temas clásicos para Angujanú"
else
    info "Angujanú no está instalado; sus temas no fueron copiados"
fi

if "$APPLY"; then
    command -v xfconf-query >/dev/null 2>&1 || {
        echo "xfconf-query es necesario para usar --apply" >&2
        exit 1
    }

    STATE_DIR="$HOME/.config/win2-7-nostalgia"
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
        xfconf-query -c xfce4-desktop -l 2>/dev/null |
        grep -E '/(last-image|image-path)$' || true
    )

    if [ ! -f "$WALLPAPER_STATE" ]; then
        : > "$WALLPAPER_STATE"
        for property in "${WALLPAPER_PROPERTIES[@]}"; do
            old_value="$(xfconf-query -c xfce4-desktop -p "$property" 2>/dev/null || true)"
            printf '%s\t%s\n' "$property" "$old_value" >> "$WALLPAPER_STATE"
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
        info "XFCE no publicó propiedades de fondo; selecciónalo manualmente desde Escritorio"
    fi

    if [ -f "$HOME/.config/xfcemenu/config.ini" ]; then
        CONFIG_FILE="$HOME/.config/xfcemenu/config.ini"
        if grep -q '^[[:space:]]*menu_theme[[:space:]]*=' "$CONFIG_FILE"; then
            sed -i 's/^[[:space:]]*menu_theme[[:space:]]*=.*/menu_theme = Win2-7Blue/' "$CONFIG_FILE"
            ok "Menú de Angujanú: Win2-7Blue"
        fi
    fi
fi

echo "========================================"
echo "Instalación finalizada para $USER."
if "$APPLY"; then
    echo "La apariencia de XFCE fue activada."
else
    echo
    echo "Para activar la apariencia, ejecuta solamente:"
    echo "  ./install.sh --apply"
fi
