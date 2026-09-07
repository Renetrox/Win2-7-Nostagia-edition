# Win2-7 Nostalgia Edition

A modern XFCE-oriented revival of the classic **Win2-7 Pack**.

This repository preserves the recognizable Windows 7-era Linux desktop style while replacing the original Ubuntu/GNOME 2 installer with a small, auditable installer for current XFCE desktops.

> Status: early restoration. Test in a secondary user account before applying the theme to a daily desktop.

## Included

- **Aerobird** and **Aerobird-Blue** themes with GTK 2, GTK 3, GTK 4 and XFWM4 support.
- **Windows-7** modern icon theme, plus the historical **Win2-7Libre** and **Win2-7** archives.
- **aero-drop** cursor theme.
- Win2-7 FreeDesktop sound theme.
- Classic wallpapers.
- Original GnoMenu menu/button/icon/sound themes for use with [Angujanú](https://github.com/Renetrox/Angujanu).

## Install

```bash
chmod +x install.sh uninstall.sh
./install.sh
```

This installs the assets for the current user without changing the active XFCE appearance.

To install and activate the default profile:

```bash
./install.sh --apply
```

The default profile uses:

- GTK/XFWM theme: `Aerobird`
- icons: `Windows-7`
- cursor: `aero-drop`
- wallpaper: `Win2-7.jpg`

Select the blue variant or the other icon archive:

```bash
./install.sh --apply --theme Aerobird-Blue
./install.sh --apply --icons Win2-7Libre
```

The installer copies the classic GnoMenu themes into an existing Angujanú installation when `~/.local/share/xfcemenu/themes` is present. It does not install Angujanú automatically.

## Uninstall

```bash
./uninstall.sh
```

The uninstaller removes only the paths installed by this edition. If `--apply` was used, it restores the XFCE settings recorded immediately before the first activation.

## Requirements

- XFCE on Linux
- `xfconf-query` only when using `--apply`
- `tar` with bzip2 support

No root privileges, Python 2, GConf, GNOME Panel, Compiz or Emerald are required.

## Project layout

```text
Files/
├── gtk3-theme/     Aerobird GTK/XFWM themes
├── icon-theme/     modern theme and historical icon archives
├── cursor/         cursor theme
├── sounds/         FreeDesktop sound theme
├── backgrounds/    wallpapers
└── gnomenu/        legacy themes consumed by Angujanú
```

## Historical note

The original Win2-7 Pack targeted Ubuntu and GNOME 2 and modified many system components. Its Python 2 installer and uninstaller have intentionally been removed from the active tree because they are incompatible with current distributions and performed unsafe system-wide operations. They remain available in the repository history.

## Licensing and credits

Win2-7 Nostalgia Edition combines assets originating from the historical Win2-7 Pack and later theme work. Rights and licenses for every inherited asset still need to be documented individually before producing a formal release. Do not assume that every file shares one license.

Angujanú and Kesú are separate projects and are not bundled here.
