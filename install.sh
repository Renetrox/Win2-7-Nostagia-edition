#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
FILES_DIR="$ROOT_DIR/Files"
THEME="Aerobird"
ICONS="Windows-7"
APPLY=false

usage() {
    echo "Usage: ./install.sh [--apply] [--theme Aerobird|Aerobird-Blue] [--icons Windows-7|Win2-7Libre|Win2-7]"
}

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
        *) echo "Unknown option: $1" >&2; usage; exit 2 ;;
    esac
    shift
done

case "$THEME" in Aerobird|Aerobird-Blue) ;; *) echo "Unsupported theme: $THEME" >&2; exit 2 ;; esac
case "$ICONS" in Windows-7|Win2-7Libre|Win2-7) ;; *) echo "Unsupported icon theme: $ICONS" >&2; exit 2 ;; esac

THEME_SRC="$FILES_DIR/gtk3-theme/$THEME"
ICON_DIR="$FILES_DIR/icon-theme/$ICONS"
ICON_ARCHIVE="$FILES_DIR/icon-theme/$ICONS.tar.bz2"
CURSOR_SRC="$FILES_DIR/cursor/aero-drop"
SOUND_SRC="$FILES_DIR/sounds/Win2-7"
WALLPAPER_SRC="$FILES_DIR/backgrounds/Win2-7.jpg"

for path in "$THEME_SRC" "$CURSOR_SRC" "$SOUND_SRC" "$WALLPAPER_SRC"; do
    [ -e "$path" ] || { echo "Missing required asset: $path" >&2; exit 1; }
done

mkdir -p "$HOME/.themes" "$HOME/.icons" "$HOME/.local/share/sounds"
mkdir -p "$HOME/.local/share/backgrounds/win2-7-nostalgia"
rm -rf "$HOME/.themes/Aerobird" "$HOME/.themes/Aerobird-Blue"
rm -rf "$HOME/.icons/aero-drop" "$HOME/.local/share/sounds/Win2-7"
cp -a "$FILES_DIR/gtk3-theme/Aerobird" "$HOME/.themes/Aerobird"
cp -a "$FILES_DIR/gtk3-theme/Aerobird-Blue" "$HOME/.themes/Aerobird-Blue"
cp -a "$CURSOR_SRC" "$HOME/.icons/aero-drop"
cp -a "$SOUND_SRC" "$HOME/.local/share/sounds/Win2-7"
cp -a "$WALLPAPER_SRC" "$HOME/.local/share/backgrounds/win2-7-nostalgia/Win2-7.jpg"
if [ -d "$ICON_DIR" ]; then
    rm -rf "$HOME/.icons/$ICONS"
    cp -a "$ICON_DIR" "$HOME/.icons/$ICONS"
elif [ -f "$ICON_ARCHIVE" ]; then
    tar -xjf "$ICON_ARCHIVE" -C "$HOME/.icons"
else
    echo "Missing icon theme: $ICONS" >&2
    exit 1
fi

ANGUJANU_DIR="$HOME/.local/share/xfcemenu/themes"
if [ -d "$ANGUJANU_DIR" ] && [ -d "$FILES_DIR/gnomenu/Themes" ]; then
    for kind in Menu Button Sound Icon; do
        if [ -d "$FILES_DIR/gnomenu/Themes/$kind" ]; then
            mkdir -p "$ANGUJANU_DIR/$kind"
            cp -a "$FILES_DIR/gnomenu/Themes/$kind/." "$ANGUJANU_DIR/$kind/"
        fi
    done
fi

if "$APPLY"; then
    command -v xfconf-query >/dev/null 2>&1 || {
        echo "xfconf-query is required by --apply" >&2
        exit 1
    }
    STATE_DIR="$HOME/.config/win2-7-nostalgia"
    STATE_FILE="$STATE_DIR/xfce-before-install"
    mkdir -p "$STATE_DIR"
    if [ ! -f "$STATE_FILE" ]; then
        {
            printf 'GTK_THEME=%q\n' "$(xfconf-query -c xsettings -p /Net/ThemeName 2>/dev/null || true)"
            printf 'ICON_THEME=%q\n' "$(xfconf-query -c xsettings -p /Net/IconThemeName 2>/dev/null || true)"
            printf 'CURSOR_THEME=%q\n' "$(xfconf-query -c xsettings -p /Gtk/CursorThemeName 2>/dev/null || true)"
            printf 'XFWM_THEME=%q\n' "$(xfconf-query -c xfwm4 -p /general/theme 2>/dev/null || true)"
            printf 'WALLPAPER=%q\n' "$(xfconf-query -c xfce4-desktop -p /backdrop/screen0/monitor0/workspace0/last-image 2>/dev/null || true)"
        } > "$STATE_FILE"
    fi
    xfconf-query -c xsettings -p /Net/ThemeName -s "$THEME"
    xfconf-query -c xsettings -p /Net/IconThemeName -s "$ICONS"
    xfconf-query -c xsettings -p /Gtk/CursorThemeName -s aero-drop
    xfconf-query -c xfwm4 -p /general/theme -s "$THEME"
    xfconf-query -c xfce4-desktop -p /backdrop/screen0/monitor0/workspace0/last-image         -s "$HOME/.local/share/backgrounds/win2-7-nostalgia/Win2-7.jpg" 2>/dev/null || true
fi

echo "Win2-7 Nostalgia Edition installed for $USER."
"$APPLY" && echo "The XFCE appearance was activated." || echo "Run ./install.sh --apply to activate it."
