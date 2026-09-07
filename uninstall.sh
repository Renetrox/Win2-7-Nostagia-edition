#!/usr/bin/env bash
set -euo pipefail

STATE_DIR="$HOME/.config/win2-7-nostalgia"
STATE_FILE="$STATE_DIR/xfce-before-install"
WALLPAPER_STATE="$STATE_DIR/wallpapers-before"
PANEL_BACKUP="$STATE_DIR/panel-before.tar.gz"
PANEL_MARKER="$STATE_DIR/panel-applied"

rm -rf \
    "$HOME/.themes/Aerobird" \
    "$HOME/.themes/Aerobird-Blue" \
    "$HOME/.icons/Windows-7" \
    "$HOME/.icons/Win2-7" \
    "$HOME/.icons/Win2-7Libre" \
    "$HOME/.icons/aero-drop" \
    "$HOME/.local/share/sounds/Win2-7" \
    "$HOME/.local/share/backgrounds/win2-7-nostalgia"

if [ -f "$STATE_FILE" ] && command -v xfconf-query >/dev/null 2>&1; then
    # Generado por install.sh con valores escapados para el shell.
    source "$STATE_FILE"
    [ -z "${GTK_THEME:-}" ] || xfconf-query -c xsettings -p /Net/ThemeName -s "$GTK_THEME"
    [ -z "${ICON_THEME:-}" ] || xfconf-query -c xsettings -p /Net/IconThemeName -s "$ICON_THEME"
    [ -z "${CURSOR_THEME:-}" ] || xfconf-query -c xsettings -p /Gtk/CursorThemeName -s "$CURSOR_THEME"
    [ -z "${XFWM_THEME:-}" ] || xfconf-query -c xfwm4 -p /general/theme -s "$XFWM_THEME"
fi

if [ -f "$WALLPAPER_STATE" ] && command -v xfconf-query >/dev/null 2>&1; then
    while IFS=$'\t' read -r property value; do
        [ -z "$property" ] || xfconf-query -c xfce4-desktop -p "$property" -s "$value" 2>/dev/null || true
    done < "$WALLPAPER_STATE"
    command -v xfdesktop >/dev/null 2>&1 && xfdesktop --reload >/dev/null 2>&1 || true
fi

if [ -f "$PANEL_MARKER" ]; then
    command -v xfce4-panel >/dev/null 2>&1 && xfce4-panel --quit >/dev/null 2>&1 || true
    rm -f \
        "$HOME/.config/xfce4/xfconf/xfce-perchannel-xml/xfce4-panel.xml" \
        "$HOME/.config/xfce4/panel/docklike-2.rc"
    if [ -f "$PANEL_BACKUP" ]; then
        tar -xzf "$PANEL_BACKUP" -C "$HOME"
        echo "  [RESTAURADO] Panel XFCE anterior"
    fi
    if command -v xfce4-panel >/dev/null 2>&1 && [ -n "${DISPLAY:-}" ]; then
        nohup xfce4-panel >/dev/null 2>&1 &
    fi
fi

rm -rf "$STATE_DIR"
echo "Win2-7 Nostalgia Edition eliminada. Angujanú, Kesú y Docklike se conservaron."
