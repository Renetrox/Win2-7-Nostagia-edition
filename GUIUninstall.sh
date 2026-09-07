#!/bin/bash
# BY: Dart00
# By: Jesus

# =============================================================================================================
# Declare Critical Varables:
if [[ `cat /etc/issue` =~ "PCLinuxOS" ]]; then
   TPUT_BOLD=""
   TPUT_CLEAR=""
   TPUT_RED=""
   TPUT_GREEN=""
   TPUT_YELLOW=""
   TPUT_CLYN=""
else
   TPUT_BOLD="tput bold"
   TPUT_CLEAR="tput sgr0"
   TPUT_RED="tput setf 4"
   TPUT_GREEN="tput setf 2"
   TPUT_YELLOW="tput setf 6"
   TPUT_CLYN="tput setf 3"
fi

# =============================================================================================================
# Execute Critical Commands:
tput civis

echo -n "# "
$TPUT_GREEN
$TPUT_BOLD
echo "*******************************************"
$TPUT_CLEAR
echo -n "# "
$TPUT_GREEN
$TPUT_BOLD
echo -n "* "
$TPUT_CLEAR
$TPUT_BOLD
echo -n "Welcome To The Win2-7 Pack Uninstaller!"
$TPUT_GREEN
echo " *"
$TPUT_CLEAR
echo -n "# "
$TPUT_GREEN
$TPUT_BOLD
echo "*******************************************"
echo ""

$TPUT_CLEAR

# =============================================================================================================
# Declare Critical Functions:

function STATUSCHECK {

if ! [ "$?" = "0" ]; then
   STATUS="FAIL"
fi

		}

function DISPLAYSTATUS {
echo -n "[ "
#if ! [[ `cat /etc/issue` =~ "PCLinuxOS" ]]; then
if [ "$WARN" = "YES" ]; then
   $TPUT_YELLOW
   echo -n "WARN"
   else
   if [ "$STATUS" = "FAIL" ] || [ "$FAIL" = "YES" ]; then
      $TPUT_RED
      echo -n "FAIL"
      ERRORS="YES"
   else
      $TPUT_GREEN
      echo -n " OK "
   fi
fi
$TPUT_CLEAR
$TPUT_BOLD
echo " ]"
$TPUT_CLEAR

STATUS=""
SPACE=""
WARN=""
FAIL=""
		}

function BUSY {
(( SPACE = (60 - `cat /tmp/status.tmp | wc -m`) ))
tput cuf $SPACE
$TPUT_BOLD
tput sc
echo -n "[ "
$TPUT_CLYN
echo -n "BUSY"
$TPUT_CLEAR
$TPUT_BOLD
echo -n " ]"
tput rc
		}

# =============================================================================================================
# Switch to correct Working Directory:
cd "`dirname \"$0\"`"

# =============================================================================================================
# Declare Variables:

echo -n "# Initializing Variables..." | tee /tmp/status.tmp ; BUSY

RMF="/tmp/win2-7.tmp" ; STATUSCHECK
DF="/tmp/Dwin2-7.tmp" ; STATUSCHECK
BU="/tmp/bwin2-7.tmp" ; STATUSCHECK
UP="/tmp/uwin2-7.tmp" ; STATUSCHECK
MLANG="ENGLISH" ; STATUSCHECK
DOCKBARXINSTALLED="No" ; STATUSCHECK
GNOMENUINSTALLED="No" ; STATUSCHECK
EMERALDINSTALLED="No" ; STATUSCHECK
SCREENLETSINSTALLED="No" ; STATUSCHECK
FUSIONICONINSTALLED="No" ; STATUSCHECK
CCSMINSTALLED="No" ; STATUSCHECK
WINEINSTALLED="No" ; STATUSCHECK
EMESENEINSTALLED="No" ; STATUSCHECK
WALLPAPERS_INSTALLED="No" ; STATUSCHECK
DOCKBARX_THEME_INSTALLED="No" ; STATUSCHECK
EMERALD_THEMES_INSTALLED="No" ; STATUSCHECK
EMESENE_THEMES_INSTALLED="No" ; STATUSCHECK
FONTS_INSTALLED="No" ; STATUSCHECK
GNOMENU_THEMES_INSTALLED="No" ; STATUSCHECK
GTK_THEMES_INSTALLED="No" ; STATUSCHECK
ICON_THEME_INSTALLED="No" ; STATUSCHECK
LOGIN_SPLASH_SCREEN_INSTALLED="No" ; STATUSCHECK
MOUSE_THEME_INSTALLED="No" ; STATUSCHECK
OPENOFFICE_SPLASHTHEME_INSTALLED="No" ; STATUSCHECK
SOUND_THEME_INSTALLED="No" ; STATUSCHECK
TSCLIENT_INSTALLED="No" ; STATUSCHECK
BREADCRUMBS_INSTALLED="No" ; STATUSCHECK
GNOMEPANEL_PIXMAPS_INSTALLED="No" ; STATUSCHECK
RGBA_INSTALLED="No" ; STATUSCHECK
GNOME_CONTROLCENTER_INSTALLED="No" ; STATUSCHECK
LOCK_THEME="No" ; STATUSCHECK
CUSTOM_UNINSTALL_DATA="No" ; STATUSCHECK
LOCK_THEME_INSTALLED="No" ; STATUSCHECK
DESKTOP_ICONS_INSTALLED="No" ; STATUSCHECK
PLYMOUTHTHEME_INSTALLED="No" ; STATUSCHECK
RESTRICTEDEXTRASINSTALLED="No"
MURRINEINSTALLED="No"
WINE_THEME_INSTALLED="No" ; STATUSCHECK
TSCLIENTINSTALLED="No"
COMPIZ_REFLECT_INSTALLED="No" ; STATUSCHECK
HEIGHT="550" ; STATUSCHECK
WIDTH="750" ; STATUSCHECK
ME=`whoami` ; STATUSCHECK
ISSUE=`head -n 1 /etc/issue | tail -n 1` ; STATUSCHECK
WDIR=$(pwd) ; STATUSCHECK
DEBUGLOG="Uninstalldebug.log"

DISPLAYSTATUS

# =============================================================================================================
# Declare Functions:

echo -n "# Initializing Functions..." | tee /tmp/status.tmp ; BUSY

function CHECKFORCANCEL { 

if [ "$?" = "1" ]; then
   unset IFS
   echo -n "# "
   $TPUT_BOLD
   $TPUT_RED
   echo "$WORD3"
   zenity --info --title="$WORD261" --text="$WORD262"
   rm -f /tmp/*.tmp > "/dev/null" 2>&1
ENTERTOCLOSE
fi
                }

function ENTERTOCLOSE { 
   $TPUT_CLEAR
   echo "#"
   echo "# $WORD4"
   read key
   tput cnorm
   exit 0
                }

DISPLAYSTATUS

# =============================================================================================================
# Assign Language:

echo -n "# Auto Detecting Language..."  | tee /tmp/status.tmp ; BUSY

case "$LANG" in
  fr* )
      LANGUAGE="French"
. Files/lang/French.py ; STATUSCHECK
	     ;;
#  es* )
#      LANGUAGE="Spanish"
#. Files/lang/Spanish.py ; STATUSCHECK
#	     ;;
  en* ) 
      LANGUAGE="English"
. Files/lang/English.py ; STATUSCHECK
           ;;
#  pl* ) 
#      LANGUAGE="Polish"
#. Files/lang/Polish.py ; STATUSCHECK
#           ;;
#  pt_BR* ) 
#      LANGUAGE="BPortuguese"
#. Files/lang/BPortuguese.py ; STATUSCHECK
#           ;;
#  pt* ) 
#      LANGUAGE="EPortuguese"
#. Files/lang/EPortuguese.py ; STATUSCHECK
#           ;;
  ru* ) 
      LANGUAGE="Russian"
. Files/lang/Russian.py
           ;;
  da* ) 
      LANGUAGE="Danish"
. Files/lang/Danish.py ; STATUSCHECK
           ;;
#  hr* ) 
#      LANGUAGE="Croatian"
#. Files/lang/Croatian.py ; STATUSCHECK
#           ;;
  * ) 
      LANGUAGE="Unknown"
      WARN="YES"
           ;;
esac

DISPLAYSTATUS

# =============================================================================================================
# Override Language:
if ! [ "$INT" = "LOADED" ]; then

echo -n "# Activating Language Override..."  | tee /tmp/status.tmp ; BUSY

CASE=$(zenity --list --width="$WIDTH" --height="$HEIGHT" --title="" --text "" --radiolist  --column "Pick:" --column "Language:" FALSE "Croatian" FALSE "Danish" TRUE "English" FALSE "French" FALSE "Russian")

CHECKFORCANCEL

  case $CASE in
    "English" ) 
      LANGUAGE="English"
. Files/lang/English.py ; STATUSCHECK
           ;;
#    "French" )
#      LANGUAGE="French" 
#. Files/lang/French.py ; STATUSCHECK
#           ;;
#    "Spanish" )
#      LANGUAGE="Spanish" 
#. Files/lang/Spanish.py ; STATUSCHECK
#           ;;
#    "Polish" ) 
#      LANGUAGE="Polish"
#. Files/lang/Polish.py ; STATUSCHECK
#           ;;
#    "European Portuguese" ) 
#      LANGUAGE="EPortuguese"
#. Files/lang/EPortuguese.py ; STATUSCHECK
#           ;;
#    "Brazilian Portuguese" ) 
#      LANGUAGE="BPortuguese"
#. Files/lang/BPortuguese.py ; STATUSCHECK
#           ;;
    "Russian" ) 
      LANGUAGE="Russian"
. Files/lang/Russian.py ; STATUSCHECK
           ;;
    "Croatian" ) 
      LANGUAGE="Croatian"
. Files/lang/Croatian.py ; STATUSCHECK
           ;;
    "Danish" ) 
      LANGUAGE="Danish"
. Files/lang/Danish.py ; STATUSCHECK
           ;;
  esac
DISPLAYSTATUS
fi

# =============================================================================================================
# Checking Install:
echo -n "# $WORD546" | tee /tmp/status.tmp ; BUSY
if ! [ "`gconftool-2 --get /apps/win2-7pack/status 2> "/dev/null"`" = "Installed" ]; then
   FAIL="YES"
   DISPLAYSTATUS
   zenity --error --title="$WORD547" --text="$WORD548"
   ENTERTOCLOSE
fi
DISPLAYSTATUS

# =============================================================================================================
# Checking and Importing GPG Key:
echo -n "# $WORD242" | tee /tmp/status.tmp ; BUSY
gpg --quiet --list-keys >> "/dev/null" 2>&1
KEYS=`gpg --list-keys | grep Win2-7`
DISPLAYSTATUS
if [ "$KEYS" = "" ]; then 
   echo -n "# $WORD243" | tee /tmp/status.tmp ; BUSY
   gpg --quiet --import Files/keys/Win-7Team.asc ; STATUSCHECK
   DISPLAYSTATUS
fi

# =============================================================================================================
# Checking GPG Script Signatures:
if ! [[ "$WDIR" =~ "SDK" ]]; then
   echo -n "# $WORD244" | tee /tmp/status.tmp ; BUSY
   gpg --quiet --verify GUIInstall.sh.sig >> "/dev/null" 2>&1 ; STATUSCHECK
   gpg --quiet --verify GUIUninstall.sh.sig >> "/dev/null" 2>&1 ; STATUSCHECK
   if [ "$STATUS" = "FAIL" ]; then
      WARN="YES"
      DISPLAYSTATUS
      zenity --warning --title="$WORD245" --text="$WORD246"
   else
      DISPLAYSTATUS
   fi
fi

# =============================================================================================================
# Check Package Manager:

echo -n "$WORD18" | tee /tmp/status.tmp ; BUSY

if apt-get -v > "/dev/null" 2>&1 ; then
PMAN="APT"
fi

if urpmf --version > "/dev/null" 2>&1 ; then
PMAN="URPMI"
fi

if yum -h > "/dev/null" 2>&1 ; then
PMAN="YUM"
fi

if zypper --version  > "/dev/null" 2>&1 ; then
PMAN="ZYPPER"
fi

if dpkg --version > "/dev/null" 2>&1 ; then
MPMAN="DPKG"
fi

if rpm --version > "/dev/null" 2>&1 ; then
MPMAN="RPM"
fi

if [ "$PMAN" = "" ]; then
   FAIL="YES"
   DISPLAYSTATUS
   zenity --error --title="$WORD285" --text="$WORD19"
   echo "====== EID:22 Unsupported Package Manager! ======" >> "$ERRORFILE"
   CLEANANDQUIT
fi

DISPLAYSTATUS

# =============================================================================================================
# Check For only 1 script instance:
if ! [ "$SWITCHDIR" = "NO" ]; then
echo -n "# $WORD21" | tee /tmp/status.tmp ; BUSY
ps -e | awk '{print $4}' > /tmp/processes.tmp
TOTAL=`cat /tmp/processes.tmp | sort | uniq --all-repeated=separate -w 32`
rm -f /tmp/processes.tmp
if [[ "$TOTAL" =~ "GUIInstall.sh" ]]; then
   FAIL="YES"
   DISPLAYSTATUS
   zenity --error --title="$WORD272" --text="$WORD273"
   ENTERTOCLOSE
fi
DISPLAYSTATUS
fi

# =============================================================================================================
# Users Must Not Be Root:
echo -n "# $WORD24" | tee /tmp/status.tmp ; BUSY
if [ "$(id -u)" = "0" ]; then
   FAIL="YES"
   DISPLAYSTATUS
   echo "====== EID:90 Running As Root! ======" >> "$ERRORFILE"
   zenity --error --title="$WORD275" --text="$WORD276"
   rm -f /tmp/*.tmp > "/dev/null" 2>&1
   ENTERTOCLOSE
fi
   DISPLAYSTATUS

# =============================================================================================================
# Check Distribution And Version:

echo -n "# $WORD266" | tee /tmp/status.tmp ; BUSY

case $ISSUE in
      *Ubuntu* )
         if [[ "$ISSUE" =~ "9.04" ]]; then
            UVERSION="Ubuntu94" ; STATUSCHECK
         elif [[ "$ISSUE" =~ "9.10" ]]; then
            UVERSION="Ubuntu910" ; STATUSCHECK
         elif [[ "$ISSUE" =~ "10.04" ]]; then
            UVERSION="Ubuntu104" ; STATUSCHECK
         elif [[ "$ISSUE" =~ "10.10" ]]; then
            UVERSION="Ubuntu1010" ; STATUSCHECK
         elif [[ "$ISSUE" =~ "11.04" ]]; then
            UVERSION="Ubuntu114" ; STATUSCHECK
         elif [[ "$ISSUE" =~ "" ]]; then
            UVERSION="Unknown_Ubuntu" ; STATUSCHECK
            OSTAG="Ubuntu"
            WARN="YES"
         fi
             ;;
      *Fedora* )
         if [[ "$ISSUE" =~ "13" ]]; then
            UVERSION="Fedora" ; STATUSCHECK
         if [[ "$ISSUE" =~ "14" ]]; then
            UVERSION="Fedora" ; STATUSCHECK
         elif [[ "$ISSUE" =~ "" ]]; then
            UVERSION="Unknown_Fedora" ; STATUSCHECK
            OSTAG="Fedora"
            WARN="YES"
         fi
         fi
             ;;
      *Debian* )
         if [[ "$ISSUE" =~ "5.0" ]]; then
            UVERSION="Debian" ; STATUSCHECK
         elif [[ "$ISSUE" =~ "6.0" ]]; then
            UVERSION="Debian" ; STATUSCHECK
         elif [[ "$ISSUE" =~ "" ]]; then
            UVERSION="Unknown_Debian" ; STATUSCHECK
            OSTAG="Debian"
            WARN="YES"
         fi
             ;;
      *Mint* )
         if [[ "$ISSUE" =~ "9" ]]; then
            UVERSION="Mint9" ; STATUSCHECK
         elif [[ "$ISSUE" =~ "10" ]]; then
            UVERSION="Mint10" ; STATUSCHECK
         elif [[ "$ISSUE" =~ "11" ]]; then
            UVERSION="Mint11" ; STATUSCHECK
         elif [[ "$ISSUE" =~ "" ]]; then
            UVERSION="Unknown_Mint" ; STATUSCHECK
            OSTAG="Mint9"
            WARN="YES"
         fi
             ;;
      *Mandriva* )
         if [[ "$ISSUE" =~ "2010" ]]; then
            UVERSION="Mandriva" ; STATUSCHECK
         elif [[ "$ISSUE" =~ "" ]]; then
            UVERSION="Unknown_Mandriva" ; STATUSCHECK
            OSTAG="Mandriva"
            WARN="YES"
         fi
             ;;
      *PCLinuxOS* )
         if [[ "$ISSUE" =~ "2010" ]]; then
            UVERSION="PCLinuxOS" ; STATUSCHECK
         elif [[ "$ISSUE" =~ "" ]]; then
            UVERSION="Unknown_PCLinuxOS" ; STATUSCHECK
            OSTAG="PCLinuxOS"
            WARN="YES"
         fi
             ;;
      *CentOS* )
         if [[ "$ISSUE" =~ "5.5" ]]; then
            UVERSION="CentOS" ; STATUSCHECK
         elif [[ "$ISSUE" =~ "" ]]; then
            UVERSION="Unknown_CentOS" ; STATUSCHECK
            OSTAG="CentOS"
            WARN="YES"
         fi
             ;;
      *openSUSE* )
         if [[ "$ISSUE" =~ "11.3" ]]; then
            UVERSION="openSUSE" ; STATUSCHECK
         elif [[ "$ISSUE" =~ "" ]]; then
            UVERSION="Unknown_openSUSE" ; STATUSCHECK
            OSTAG="openSUSE"
            WARN="YES"
         fi
             ;;
      * )
        WARN="YES"
        UVERSION="Unknown_OS"
        NOSUPPORT="YES"
             ;;
esac

DISPLAYSTATUS

case $UVERSION in
      *Unknown_Ubuntu* )
         UVERSION="Ubuntu1010"
             ;;
      *Unknown_Fedora* )
         UVERSION="Fedora"
             ;;
      *Unknown_Debian* )
         UVERSION="Debian"
             ;;
      *Unknown_Mint* )
         UVERSION="Mint9"
             ;;
      *Unknown_Mandriva* )
         UVERSION="Mandriva"
             ;;
      *Unknown_PCLinuxOS* )
         UVERSION="PCLinuxOS"
             ;;
      *Unknown_CentOS* )
         UVERSION="CentOS"
             ;;
      *Unknown_openSUSE* )
         UVERSION="openSUSE"
             ;;
      *Unknown_OS* )
         zenity --warning --title="$WORD529" --text="$WORD533"
         ENTERTOCLOSE
             ;;
esac

# =============================================================================================================
# Check Desktop Environment:

echo -n "# $WORD279" | tee /tmp/status.tmp ; BUSY

ps -e | awk '{print $4}' > /tmp/processes.tmp ; STATUSCHECK
GNOMECHECK=`cat /tmp/processes.tmp | sort | uniq --all-repeated=separate -w 32` ; STATUSCHECK
rm -f /tmp/processes.tmp ; STATUSCHECK
if [[ "$GNOMECHECK" =~ "gnome-session" ]]; then
   FAIL="YES"
   DISPLAYSTATUS
   echo "====== EID:88 Non-Compatible Desktop Environment! ======" >> "$ERRORFILE"
   zenity --error --title="$WORD280" --text="$WORD281"
   CHECKFORCANCEL
fi

DISPLAYSTATUS

# =============================================================================================================
# Check GDM Version:

echo -n "# $WORD526" | tee /tmp/status.tmp ; BUSY

if [ -d "/etc/gdm3" ]; then
   GDM="3"
else
   GDM="2"
fi

DISPLAYSTATUS

# =============================================================================================================
# Check Installed Programs

echo -n "# $WORD5" | tee /tmp/status.tmp ; BUSY

echo "# Installed Win2-7 Essetials & Programs:" > "$DEBUGLOG"
echo "" > "$DEBUGLOG"

# Murrine:
if [ "$PMAN" = "APT" ]; then
   apt-cache policy "gtk2-engines-murrine" > "/tmp/MURRINE.tmp" 2> "/dev/null" ; STATUSCHECK
   if [ -s "/tmp/MURRINE.tmp" ]; then
      if grep -q "Installed: 0.90.3+git20100323-1" "/tmp/MURRINE.tmp"; then
         MURRINEINSTALLED="Yes" ; STATUSCHECK
         echo "MURRINEINSTALLED=Yes" >> "$DEBUGLOG"
      else
         echo "MURRINEINSTALLED=No" >> "$DEBUGLOG"
      fi 
      if grep -q "Installed: 0.98.1.1-1" "/tmp/MURRINE.tmp"; then
         MURRINEINSTALLED="Yes" ; STATUSCHECK
         echo "MURRINEINSTALLED=Yes" >> "$DEBUGLOG"
      else
         echo "MURRINEINSTALLED=No" >> "$DEBUGLOG"
      fi
      rm -f "/tmp/MURRINE.tmp" ; STATUSCHECK
   fi 
fi

# Aptitude Check:
if [ "$UVERSION" = "Ubuntu1010" ]; then
   if `aptitude -h > "/dev/null" 2>&1` ; then 
      APTITUDEINSTALLED="Yes"
      echo "APTITUDEINSTALLED=Yes" >> $DEBUGLOG
   else
      echo "APTITUDEINSTALLED=No" >> "$DEBUGLOG"
   fi
else
   APTITUDEINSTALLED="Yes"
   echo "APTITUDEINSTALLED=Yes" >> "$DEBUGLOG"
fi

# gvfs-bin Check:
if `gvfs-set-attribute -help > "/dev/null" 2>&1` ; then
   GVFSBININSTALLED="Yes"
   echo "GVFSBININSTALLED=Yes" >> "$DEBUGLOG"
else
   echo "GVFSBININSTALLED=No" >> "$DEBUGLOG"
fi

# Plymouth Check:
if `plymouth --help > "/dev/null" 2>&1` ; then
   PLYMOUTHTHEMEINSTALLED="Yes" 
   echo "PLYMOUTHTHEMEINSTALLED=Yes" >> "$DEBUGLOG"
else
   echo "PLYMOUTHTHEMEINSTALLED=No" >> "$DEBUGLOG"
fi

# Xdg User Dirs Check:
if `xdg-user-dirs-update > "/dev/null" 2>&1` ; then
   XDGUSERDIRSINSTALLED="Yes"
   echo "XDGUSERDIRSINSTALLED=Yes" >> "$DEBUGLOG"
else
   echo "XDGUSERDIRSINSTALLED=No" >> "$DEBUGLOG"
fi

# wget Check:
if `wget --help > "/dev/null" 2>&1` ; then
   WGETINSTALLED="Yes"
   echo "WGETINSTALLED=Yes" >> "$DEBUGLOG"
else
   echo "WGETINSTALLED=No" >> "$DEBUGLOG"
fi

# Tsclient Check:
if [ -e "/usr/bin/tsclient" ] || [ -d "/usr/lib/tsclient" ]; then
   TSCLIENTINSTALLED="Yes"
   echo "TSCLIENTINSTALLED=Yes" >> "$DEBUGLOG"
else
   echo "TSCLIENTINSTALLED=No" >> "$DEBUGLOG"
fi

# Gnomenu Check:
if [ -e "/usr/bin/GnoMenu.py" ] || [ -d "/usr/lib/gnomenu" ]; then
   GNOMENUINSTALLED="Yes"
   echo "GNOMENUINSTALLED=Yes" >> "$DEBUGLOG"
else
   echo "GNOMENUINSTALLED=No" >> "$DEBUGLOG"
fi

# CCSM Check:
if [ -e "/usr/bin/ccsm" ] || [ -d "/usr/share/ccsm" ]; then
   CCSMINSTALLED="Yes" 
   echo "CCSMINSTALLED=Yes" >> "$DEBUGLOG"
else
   echo "CCSMINSTALLED=No" >> "$DEBUGLOG"
fi
      
# DockBarX Check:
if [ -e "/usr/bin/dockbarx_factory.py" ] || [ -e "/usr/bin/dockbarx_factory" ] || [ -d "/usr/share/doc/dockbarx" ]; then
   DOCKBARXINSTALLED="Yes" 
   echo "DOCKBARXINSTALLED=Yes" >> "$DEBUGLOG"
else
   echo "DOCKBARXINSTALLED=No" >> "$DEBUGLOG"
fi
   
# Emerald Check:
if [ -e "/usr/bin/emerald" ] || [ -d "/usr/share/doc/emerald" ]; then
   EMERALDINSTALLED="Yes" 
   echo "EMERALDINSTALLED=Yes" >> "$DEBUGLOG"
else
   echo "EMERALDINSTALLED=No" >> "$DEBUGLOG"
fi

# Emesene Check:
if [ -e "/usr/bin/emesene" ] || [ -d "/usr/share/doc/emesene" ]; then
   EMESENEINSTALLED="Yes" 
   echo "EMESENEINSTALLED=Yes" >> "$DEBUGLOG"
else
   echo "EMESENEINSTALLED=No" >> "$DEBUGLOG"
fi

# Fusion Icon Check:
if [ -e "/usr/bin/fusion-icon" ] || [ -d "/usr/share/doc/fusion-icon" ]; then
   FUSIONICONINSTALLED="Yes"
   echo "FUSIONICONINSTALLED=Yes" >> "$DEBUGLOG"
else
   echo "FUSIONICONINSTALLED=No" >> "$DEBUGLOG"
fi
   
# Screenlets Check:
if [ -e "/usr/bin/screenlets" ] || [ -d "/usr/share/doc/screenlets" ]; then
   SCREENLETSINSTALLED="Yes"
   echo "SCREENLETSINSTALLED=Yes" >> "$DEBUGLOG"
else
   echo "SCREENLETSINSTALLED=No" >> "$DEBUGLOG"
fi
   
# Wine Check:
if [ -e "/usr/bin/wine" ] || [ -d "/usr/share/doc/wine" ]; then
   WINEINSTALLED="Yes"
   echo "WINEINSTALLED=Yes" >> "$DEBUGLOG"
else
   echo "WINEINSTALLED=No" >> "$DEBUGLOG"
fi

# Elementry Desktop (Ubuntu Based):
if [ "$UVERSION" = "Ubuntu104" ] || [ "$UVERSION" = "Ubuntu1010" ] || [ "$UVERSION" = "Mint9" ] || [ "$UVERSION" = "Mint10" ] || [ "$UVERSION" = "Mint11" ]; then
   if grep -q "elementarydesktop" "/etc/apt/sources.list"; then
      ELEMENTRYNINSTALLED="Yes"
      echo "ELEMENTRYNINSTALLED=Yes" >> "$DEBUGLOG"
   else
      echo "ELEMENTRYNINSTALLED=No" >> "$DEBUGLOG"
   fi
fi

# Elementry Desktop (Mandriva):
if [ "$UVERSION" = "Mandriva" ]; then
   rpm -qa > /tmp/packages.tmp 
   if grep -q "nautilus-elementary" "/tmp/packages.tmp" ; then
      ELEMENTRYNINSTALLED="Yes"
      echo "ELEMENTRYNINSTALLED=Yes" >> "$DEBUGLOG"
   else
      echo "ELEMENTRYNINSTALLED=No" >> "$DEBUGLOG"
   fi
   rm -f /tmp/packages.tmp
fi

# EMurrine (Mandriva):
if [ "$UVERSION" = "Mandriva" ]; then
   rpm -qa > /tmp/packages.tmp 
   if grep -q "murrine" "/tmp/packages.tmp" ; then
      STANDARDMURRINEINSTALLED="Yes"
      echo "STANDARDMURRINEINSTALLED=Yes" >> "$DEBUGLOG"
   else
      echo "STANDARDMURRINEINSTALLED=No" >> "$DEBUGLOG"
   fi
   rm -f /tmp/packages.tmp
fi

# Sudo:
if `sudo -h > "/dev/null" 2>&1` ; then
   SUDOINSTALLED="Yes"
   echo "SUDOINSTALLED=Yes" >> "$DEBUGLOG"
else
   echo "SUDOINSTALLED=No" >> "$DEBUGLOG"
fi

DISPLAYSTATUS

# =============================================================================================================
# Check if Murrine is held (included in program check):
echo -n "# $WORD6" | tee /tmp/status.tmp ; BUSY
if [ "$PMAN" = "APT" ] && [ "$MURRINEINSTALLED" = "Yes" ]; then
   dpkg --get-selections | grep gtk2-engines-murrine > /tmp/holds.tmp
   if grep -q "hold" "/tmp/holds.tmp" 2>> "/dev/null" ; then
      MURRINEHOLD="YES"
   fi
   rm -f /tmp/holds.tmp
fi
DISPLAYSTATUS

# =============================================================================================================
# Check Installed Components:

echo -n "# $WORD286" | tee /tmp/status.tmp ; BUSY

echo "" > "$DEBUGLOG"
echo "# Installed Win2-7 Components:" > "$DEBUGLOG"
echo "" > "$DEBUGLOG"

# Compiz Graphic:
if [ "`gconftool-2 --get /apps/win2-7pack/compiz_files 2> "/dev/null"`" = "Installed" ]; then
   COMPIZ_REFLECT_INSTALLED="Yes"
   echo "COMPIZ_REFLECT_INSTALLED=Yes" >> "$DEBUGLOG"
else
   echo "COMPIZ_REFLECT_INSTALLED=No" >> "$DEBUGLOG"
fi

# Wallpapers:
if [ "`gconftool-2 --get /apps/win2-7pack/wallpapers 2> "/dev/null"`" = "Installed" ]; then
   WALLPAPERS_INSTALLED="Yes"
   echo "WALLPAPERS_INSTALLED=Yes" >> "$DEBUGLOG"
else
   echo "WALLPAPERS_INSTALLED=No" >> "$DEBUGLOG"
fi

# Plymouth Theme:
if [ "`gconftool-2 --get /apps/win2-7pack/plymouth_theme 2> "/dev/null"`" = "Installed" ]; then
   PLYMOUTHTHEME_INSTALLED="Yes" ; STATUSCHECK
   echo "PLYMOUTHTHEME_INSTALLED=Yes" >> "$DEBUGLOG"
else
   echo "PLYMOUTHTHEME_INSTALLED=No" >> "$DEBUGLOG"
fi

# Wine Theme:
if [ "`gconftool-2 --get /apps/win2-7pack/wine_theme 2> "/dev/null"`" = "Installed" ]; then
   WINE_THEME_INSTALLED="Yes"
   echo "WINE_THEME_INSTALLED=Yes" >> "$DEBUGLOG"
else
   echo "WINE_THEME_INSTALLED=No" >> "$DEBUGLOG"
fi

# DockBarX Themes:
if [ "`gconftool-2 --get /apps/win2-7pack/dockbarx_themes 2> "/dev/null"`" = "Installed" ]; then
   DOCKBARX_THEME_INSTALLED="Yes"
   echo "DOCKBARX_THEME_INSTALLED=Yes" >> "$DEBUGLOG"
else
   echo "DOCKBARX_THEME_INSTALLED=No" >> "$DEBUGLOG"
fi

# Emerald Themes:
if [ "`gconftool-2 --get /apps/win2-7pack/emerald_themes 2> "/dev/null"`" = "Installed" ]; then
   EMERALD_THEMES_INSTALLED="Yes"
   echo "EMERALD_THEMES_INSTALLED=Yes" >> "$DEBUGLOG"
else
   echo "EMERALD_THEMES_INSTALLED=No" >> "$DEBUGLOG"
fi

# Emesene Theme:
if [ "`gconftool-2 --get /apps/win2-7pack/emesene_theme 2> "/dev/null"`" = "Installed" ]; then
   EMESENE_THEMES_INSTALLED="Yes"
   echo "EMESENE_THEMES_INSTALLED=Yes" >> "$DEBUGLOG"
else
   echo "EMESENE_THEMES_INSTALLED=No" >> "$DEBUGLOG"
fi

# Gnomenu Theme:
if [ "`gconftool-2 --get /apps/win2-7pack/gnomenu_themes 2> "/dev/null"`" = "Installed" ]; then
   GNOMENU_THEMES_INSTALLED="Yes"
   echo "GNOMENU_THEMES_INSTALLED=Yes" >> "$DEBUGLOG"
else
   echo "GNOMENU_THEMES_INSTALLED=No" >> "$DEBUGLOG"
fi

# GTK-Themes:
if [ "`gconftool-2 --get /apps/win2-7pack/gtk_theme 2> "/dev/null"`" = "Installed" ]; then
   GTK_THEMES_INSTALLED="Yes"
   echo "GTK_THEMES_INSTALLED=Yes" >> "$DEBUGLOG"
else
   echo "GTK_THEMES_INSTALLED=No" >> "$DEBUGLOG"
fi

# Fonts:
if [ "`gconftool-2 --get /apps/win2-7pack/fonts 2> "/dev/null"`" = "Installed" ]; then
   FONTS_INSTALLED="Yes"
   echo "FONTS_INSTALLED=Yes" >> "$DEBUGLOG"
else
   echo "FONTS_INSTALLED=No" >> "$DEBUGLOG"
fi

# Icon Theme:
if [ "`gconftool-2 --get /apps/win2-7pack/icon_theme 2> "/dev/null"`" = "Installed" ]; then
   ICON_THEME_INSTALLED="Yes"
   echo "ICON_THEME_INSTALLED=Yes" >> "$DEBUGLOG"
else
   echo "ICON_THEME_INSTALLED=No" >> "$DEBUGLOG"
fi

# Xsplash Theme:
if [ "`gconftool-2 --get /apps/win2-7pack/xsplash_theme 2> "/dev/null"`" = "Installed" ]; then
   LOGIN_SPLASH_SCREEN_INSTALLED="Yes"
   echo "LOGIN_SPLASH_SCREEN_INSTALLED=Yes" >> "$DEBUGLOG"
else
   echo "LOGIN_SPLASH_SCREEN_INSTALLED=No" >> "$DEBUGLOG"
fi

# GDM Theme:
if [ "`gconftool-2 --get /apps/win2-7pack/gdm_theme 2> "/dev/null"`" = "Installed" ] ; then
   LOGIN_SPLASH_SCREEN_INSTALLED="Yes"
   echo "LOGIN_SPLASH_SCREEN_INSTALLED=Yes" >> "$DEBUGLOG"
else
   echo "LOGIN_SPLASH_SCREEN_INSTALLED=No" >> "$DEBUGLOG"
fi

# Mouse Theme:
if [ "`gconftool-2 --get /apps/win2-7pack/curser_theme 2> "/dev/null"`" = "Installed" ]; then
   MOUSE_THEME_INSTALLED="Yes"
   echo "MOUSE_THEME_INSTALLED=Yes" >> "$DEBUGLOG"
else
   echo "MOUSE_THEME_INSTALLED=No" >> "$DEBUGLOG"
fi

# Openoffice theme:
if [ "`gconftool-2 --get /apps/win2-7pack/openoffice_splash 2> "/dev/null"`" = "Installed" ]; then
   OPENOFFICE_SPLASHTHEME_INSTALLED="Yes"
   echo "OPENOFFICE_SPLASHTHEME_INSTALLED=Yes" >> "$DEBUGLOG"
else
   echo "OPENOFFICE_SPLASHTHEME_INSTALLED=No" >> "$DEBUGLOG"
fi

# Sound Theme:
if [ "`gconftool-2 --get /apps/win2-7pack/sound_themes 2> "/dev/null"`" = "Installed" ]; then
   SOUND_THEME_INSTALLED="Yes"
   echo "SOUND_THEME_INSTALLED=Yes" >> "$DEBUGLOG"
else
   echo "SOUND_THEME_INSTALLED=No" >> "$DEBUGLOG"
fi

# Tsclient Theme:
if [ "`gconftool-2 --get /apps/win2-7pack/terminal_server_theme 2> "/dev/null"`" = "Installed" ]; then
   TSCLIENT_INSTALLED="Yes"
   echo "TSCLIENT_INSTALLED=Yes" >> "$DEBUGLOG"
else
   echo "TSCLIENT_INSTALLED=No" >> "$DEBUGLOG"
fi

# Gnome Panel Pixmaps:
if [ "`gconftool-2 --get /apps/win2-7pack/panel_pixmaps 2> "/dev/null"`" = "Installed" ]; then
   GNOMEPANEL_PIXMAPS_INSTALLED="Yes"
   echo "GNOMEPANEL_PIXMAPS_INSTALLED=Yes" >> "$DEBUGLOG"
else
   echo "GNOMEPANEL_PIXMAPS_INSTALLED=No" >> "$DEBUGLOG"
fi

# Gnome Control Center Theme:
if [ "`gconftool-2 --get /apps/win2-7pack/control_center_theme 2> "/dev/null"`" = "Installed" ]; then
   GNOME_CONTROLCENTER_INSTALLED="Yes"
   echo "GNOME_CONTROLCENTER_INSTALLED=Yes" >> "$DEBUGLOG"
else
   echo "GNOME_CONTROLCENTER_INSTALLED=No" >> "$DEBUGLOG"
fi

# Breadcrumb Theme:
if [ "`gconftool-2 --get /apps/win2-7pack/breadcrumb_theme 2> "/dev/null"`" = "Installed" ]; then
   BREADCRUMBS_INSTALLED="Yes"
   echo "BREADCRUMBS_INSTALLED=Yes" >> "$DEBUGLOG"
else
   echo "BREADCRUMBS_INSTALLED=No" >> "$DEBUGLOG"
fi

# RGBA Themes:
if [ "`gconftool-2 --get /apps/win2-7pack/rgba_apps 2> "/dev/null"`" = "Installed" ]; then
   RGBA_INSTALLED="Yes"
   echo "RGBA_INSTALLED=Yes" >> "$DEBUGLOG"
else
   echo "RGBA_INSTALLED=No" >> "$DEBUGLOG"
fi

# Lock Theme:
if [ "`gconftool-2 --get /apps/win2-7pack/lock_theme 2> "/dev/null"`" = "Installed" ]; then
   LOCK_THEME_INSTALLED="Yes"
   echo "LOCK_THEME_INSTALLED=Yes" >> "$DEBUGLOG"
else
   echo "LOCK_THEME_INSTALLED=No" >> "$DEBUGLOG"
fi

# Desktop Icons:
if [ "`gconftool-2 --get /apps/nautilus/desktop/computer_icon_visible 2> "/dev/null"`" = "true" ] || [ "`gconftool-2 --get /apps/nautilus/desktop/home_icon_visible 2> "/dev/null"`" = "true" ] || [ "`gconftool-2 --get /apps/nautilus/desktop/network_icon_visible 2> "/dev/null"`" = "true" ] || [ "`gconftool-2 --get /apps/nautilus/desktop/trash_icon_visible 2> "/dev/null"`" = "true" ]; then
   DESKTOP_ICONS_INSTALLED="Yes"
   echo "DESKTOP_ICONS_INSTALLED=Yes" >> "$DEBUGLOG"
else
   echo "DESKTOP_ICONS_INSTALLED=No" >> "$DEBUGLOG"
fi

# Win2-7 Restricted Extras:
if [ "`gconftool-2 --get /apps/win2-7pack/Win2-7_Restricted_Extras 2> "/dev/null"`" = "Installed" ]; then
   RESTRICTEDEXTRASINSTALLED="Yes"
   echo "RESTRICTEDEXTRASINSTALLED=Yes" >> "$DEBUGLOG"
else
   echo "RESTRICTEDEXTRASINSTALLED=No" >> "$DEBUGLOG"
fi

DISPLAYSTATUS

# =============================================================================================================
# Update xdg-user-dirs locals:
echo -n "# $WORD59" | tee /tmp/status.tmp ; BUSY
xdg-user-dirs-update ; STATUSCHECK
DISPLAYSTATUS

# =============================================================================================================
# Import Any Sources and Declare their sourced variables:
echo -n "# $WORD60" | tee /tmp/status.tmp ; BUSY
. ~/.config/user-dirs.dirs ; STATUSCHECK
DOCUMENTS="$XDG_DOCUMENTS_DIR" ; STATUSCHECK
DESKTOP="$XDG_DESKTOP_DIR" ; STATUSCHECK
DOWNLOAD="$XDG_DOWNLOAD_DIR" ; STATUSCHECK
DISPLAYSTATUS

# =============================================================================================================
# Check for sudoer Status:

if [ "$UVERSION" = "Fedora" ] || [ "$UVERSION" = "Debian" ] || [ "$UVERSION" = "PCLinuxOS" ] || [ "$UVERSION" = "CentOS" ] || [ "$UVERSION" = "Mandriva" ]; then
   if ! [ "$ME" = "root" ]; then
      echo "# $WORD27 $ME..."
   fi
   while true; do
   SUDOERS=`su root -c "cat /etc/sudoers"`

   if [ "$?" = "0" ]; then
   case "$SUDOERS" in
         *$ME* )
	   SUDORERS_EXIST="YES"
                ;;
   esac
      break
   fi
   done
   if ! [ "$SUDORERS_EXIST" = "YES" ]; then
      echo "# $WORD28 $ME $WORD29 /etc/sudoers..."
      while true; do
      su root -c "echo '$ME ALL=(ALL) ALL' >> /etc/sudoers"
      if [ "$?" = "0" ]; then
         break
      fi
      done
   fi
fi

# =============================================================================================================
# Password Management:

sudo -K

while true; do

   echo -n "# $WORD30" | tee /tmp/status.tmp ; BUSY

   while [ -z "$PASS" ]; do 
   if ! PASS=$(zenity --entry --title="$WORD31" --hide-text --text="$WORD32") ; then 
      FAIL="YES"
      DISPLAYSTATUS
      ENTERTOCLOSE
   fi
   done

   echo "$PASS" | sudo -S -p "" /bin/true 2> "/dev/null" 

   if [ "$?" = "1" ]; then 
      FAIL="YES"
      DISPLAYSTATUS
      PASS=""
   else
      DISPLAYSTATUS
      break
   fi

done

# =============================================================================================================
# Choose Uninstall Type:

if [ -d $HOME"/.Win2-7_GUI_Backup" ]; then
   UNINSTALLTYPE=$(zenity --list --width="$WIDTH" --height="$HEIGHT" --title="$WORD429" --text="$WORD430" --radiolist --column "$WORD15" --column "$WORD431" --column "$WORD432" TRUE "$OPTION_FullUninstall" "$WORD433" FALSE "$OPTION_PartialUninstall" "$WORD434" )
   CHECKFORCANCEL

  case $UNINSTALLTYPE in
    "$OPTION_FullUninstall" ) 
   REMOVEFILES="YES"
   RESTOREBACKUP="YES"
           ;;
    "$OPTION_PartialUninstall" ) 
   RESTOREBACKUP="YES"
   REMOVEFILES="NO"
           ;;
  esac
else
   RESTOREBACKUP="NO"
   REMOVEFILES="YES"
fi

if [ "$REMOVEFILES" = "YES" ]; then

# =============================================================================================================
# Uninstall Win2-7 Essentials:

RESPONSE=$(zenity --width="$WIDTH" --height="$HEIGHT" --list --checklist --title="$WORD439" --text="$WORD440" --column="$WORD15" --column="$WORD441" --column="$WORD438" FALSE "$WORD287" "$MURRINEINSTALLED" FALSE "$OPTION_UninstallCCSM" "$CCSMINSTALLED" FALSE "$OPTION_UninstallCompizFusionIcon" "$FUSIONICONINSTALLED" FALSE "$OPTION_UninstallDockbarX" "$DOCKBARXINSTALLED" FALSE "$OPTION_UninstallEmerald" "$EMERALDINSTALLED"  FALSE "$OPTION_UninstallEmesene"  "$EMESENEINSTALLED" FALSE "$OPTION_UninstallGnomenu" "$GNOMENUINSTALLED" FALSE "$OPTION_UninstallScreenlets" "$SCREENLETSINSTALLED" --separator=':' )

CHECKFORCANCEL

IFS=":" ; for WORD in $RESPONSE ; do 
   case $WORD in
      "$WORD287" )
UNINSTALL_WIN27E="YES"
UNINSTALL_ADVANCED_MURRINE="YES"
	;;
      "$OPTION_UninstallCompizFusionIcon" )
UNINSTALL_WIN27E="YES"
UNINSTALL_FUSION_ICON="YES"
	;;
      "$OPTION_UninstallDockbarX" )  
UNINSTALL_WIN27E="YES"
UNINSATLL_DOCKBARX="YES"
	;;
      "$OPTION_UninstallEmerald" ) 
UNINSTALL_WIN27E="YES"
UNINSTALL_EMERALD="YES"
	;;
      "$OPTION_UninstallEmesene" ) 
UNINSTALL_WIN27E="YES"
UNINSTALL_EMESENCE="YES"
	;;
      "$OPTION_UninstallGnomenu" ) 
UNINSTALL_WIN27E="YES"
UNINSTALL_GNOMENU="YES"
	;;
      "$OPTION_UninstallScreenlets" )
UNINSTALL_WIN27E="YES"
UNINSTALL_SCREENLETS="YES"
	;;
      "$OPTION_UninstallCCSM" )
UNINSTALL_WIN27E="YES"
UNINSTALL_CCSM="YES"
	;;
   esac
done

unset IFS

echo "#"

# =============================================================================================================
# Revert to Standard Theme if in use:

   case $UVERSION in
     "Ubuntu1010" ) 
        REVERT_METACITY="Ambiance"
        REVERT_GTKTHEME="Ambiance"
        REVERT_ICONS="ubuntu-mono-dark"
        REVERT_MOUSE="DMZ-White"
        REVERT_SOUND="ubuntu"
                ;;
     "Ubuntu104" ) 
        REVERT_METACITY="Ambiance"
        REVERT_GTKTHEME="Ambiance"
        REVERT_ICONS="ubuntu-mono-dark"
        REVERT_MOUSE="DMZ-White"
        REVERT_SOUND="ubuntu"
                ;;
     "Ubuntu114" ) 
        REVERT_METACITY="Ambiance"
        REVERT_GTKTHEME="Ambiance"
        REVERT_ICONS="ubuntu-mono-dark"
        REVERT_MOUSE="DMZ-White"
        REVERT_SOUND="ubuntu"
                ;;
     *Ubuntu* )
        REVERT_METACITY="Human"
        REVERT_GTKTHEME="Human"
        REVERT_ICONS="Humanity"
        REVERT_MOUSE="Human"
        REVERT_SOUND="ubuntu"
                ;;
      "Debian" )
        REVERT_METACITY="Clearlooks"
        REVERT_GTKTHEME="Clearlooks"
        REVERT_ICONS="gnome"
        REVERT_MOUSE="default"
        REVERT_SOUND="default"
                ;;
      "Mint9" )
         REVERT_METACITY="Shiki-Colors-Metacity"
         REVERT_GTKTHEME="Shiki-Wise"
         REVERT_ICONS="gnome-wise"
         REVERT_MOUSE="default"
         REVERT_SOUND="LinuxMint"
                ;;
      "Mint10" )
         REVERT_METACITY="Mint-X"
         REVERT_GTKTHEME="Mint-X-Metal"
         REVERT_ICONS="Mint-X"
         REVERT_MOUSE="default"
         REVERT_SOUND="LinuxMint"
                ;;
      "Mint11" )
         REVERT_METACITY="Mint-X"
         REVERT_GTKTHEME="Mint-X-Metal"
         REVERT_ICONS="Mint-X"
         REVERT_MOUSE="" # No Value
         REVERT_SOUND="LinuxMint"
                ;;
      "Fedora" )
        REVERT_METACITY="Clearlooks"
        REVERT_GTKTHEME="Clearlooks"
        REVERT_ICONS="Fedora"
        REVERT_MOUSE="Bluecurve"
        REVERT_SOUND="freedesktop"
                ;;
      "PCLinuxOS" )
        REVERT_METACITY="SlicknesS"
        REVERT_GTKTHEME="SlicknesS"
        REVERT_ICONS="nuoveXT-aero"
        REVERT_MOUSE="default"
        REVERT_SOUND="ia_ora"
                ;;
      "CentOS" )
        REVERT_METACITY="Clearlooks"
        REVERT_GTKTHEME="Clearlooks"
        REVERT_ICONS="Clearlooks"
        REVERT_MOUSE="Bluecurve"

        REVERT_SOUND="" # None
                ;;
      "Mandriva" )
        REVERT_METACITY="Ia Ora Steel"
        REVERT_GTKTHEME="Ia Ora Steel"
        REVERT_ICONS="gnome"
        REVERT_MOUSE="" # No Value
        REVERT_SOUND="ia_ora"
                ;;
      "openSUSE" )
        REVERT_METACITY="Sonar"
        REVERT_GTKTHEME="Sonar"
        REVERT_ICONS="Gilouche"
        REVERT_MOUSE="default" 
        REVERT_SOUND="freedesktop"
                ;;
   esac

if [ "$RESTOREBACKUP" = "YES" ]; then
zenity --info --title="$WORD288" --text="$WORD289"
else
zenity --info --title="$WORD290" --text="$WORD291"
fi

     echo -n "# $WORD282" | tee /tmp/status.tmp ; BUSY
     gconftool-2 --set "/apps/metacity/general/theme"                  --type string "$REVERT_METACITY" ; STATUSCHECK
     gconftool-2 --set "/desktop/gnome/interface/gtk_theme"            --type string "$REVERT_GTKTHEME" ; STATUSCHECK
     gconftool-2 --set "/desktop/gnome/interface/icon_theme"           --type string "$REVERT_ICONS" ; STATUSCHECK
     gconftool-2 --set "/desktop/gnome/peripherals/mouse/cursor_theme" --type string "$REVERT_MOUSE" ; STATUSCHECK
     gconftool-2 --set "/desktop/gnome/sound/theme_name"               --type string "$REVERT_SOUND" ; STATUSCHECK
     gconftool-2 --set "/apps/panel/toplevels/bottom_panel_0/background/type" --type string "gtk" ; STATUSCHECK

     if [ "$GVFSBININSTALLED" = "Yes" ]; then
        gvfs-set-attribute $DESKTOP -t unset metadata::custom-icon > "/dev/null" 2>&1
     fi
     sleep 5
     DISPLAYSTATUS

# =============================================================================================================
# Remove Background Wallpaper:
if [ -d $HOME"/.backgrounds" ]; then
   echo -n "# $WORD292" | tee /tmp/status.tmp ; BUSY
   if [ -e "/usr/share/backgrounds/warty-final-ubuntu2.png" ]; then
      gconftool-2 --set "/desktop/gnome/background/picture_filename" --type string "/usr/share/backgrounds/warty-final-ubuntu2.png" ; STATUSCHECK
   else
      gconftool-2 --set "/desktop/gnome/background/picture_filename" --type string "/usr/share/backgrounds/warty-final-ubuntu.png" ; STATUSCHECK
   fi
   rm -f -r $HOME"/.backgrounds" ; STATUSCHECK
   gconftool-2 --unset "/apps/win2-7pack/wallpapers" > "/dev/null" 2>&1
   DISPLAYSTATUS
fi

# =============================================================================================================
# Remove Compiz Blur Graphic:
if [ -e "$HOME/.Win2-7Reflect.png" ]; then
   echo -n "# $WORD293" | tee /tmp/status.tmp ; BUSY
   rm -f $HOME/.Win2-7Reflect.png ; STATUSCHECK
   NOTIFY_REFLECT_CCSM="YES"
   gconftool-2 --unset "/apps/win2-7pack/compiz_files" > "/dev/null" 2>&1
   DISPLAYSTATUS
fi

# =============================================================================================================
# Remove Desktop Icons:
   echo -n "# $WORD294" | tee /tmp/status.tmp ; BUSY
   gconftool-2 --set "/apps/nautilus/desktop/computer_icon_visible" --type bool false ; STATUSCHECK
   gconftool-2 --set "/apps/nautilus/desktop/home_icon_visible"     --type bool false ; STATUSCHECK
   gconftool-2 --set "/apps/nautilus/desktop/network_icon_visible"  --type bool false ; STATUSCHECK
   gconftool-2 --set "/apps/nautilus/desktop/trash_icon_visible"    --type bool false ; STATUSCHECK
   gconftool-2 --set "/apps/nautilus/desktop/volumes_visible"       --type bool true ; STATUSCHECK
   DISPLAYSTATUS

# =============================================================================================================
# Remove DockbarX Themes:
if [ -e "/usr/share/dockbarx/themes/shinybar_13_horiz.tar.gz" ]; then
   echo -n "# $WORD295" | tee /tmp/status.tmp ; BUSY 
   gconftool-2 --set "/apps/dockbarx/theme"  --type string "default" ; STATUSCHECK
   echo "$PASS" | sudo -S -p "" rm -f /usr/share/dockbarx/themes/shinybar* ; STATUSCHECK
   gconftool-2 --unset "/apps/win2-7pack/dockbarx_themes" > "/dev/null" 2>&1
   DISPLAYSTATUS
fi

# =============================================================================================================
# Restore Elemetary Desktop Toolbar:
if [ "$ELEMENTRYNINSTALLED" = "Yes" ]; then
   echo -n "# $WORD296" | tee /tmp/status.tmp ; BUSY
   gconftool-2 --set "/apps/nautilus/preferences/toolbar_items" --type list --list-type=string "[Back,Forward,StopReload,Search,LocationPathBar,ViewModeButton]" ; STATUSCHECK
   DISPLAYSTATUS
fi

# =============================================================================================================
# Remove Emerald Themes:
if [ -d "$HOME/.emerald/themes/Win2-7" ]; then
   echo -n "# $WORD297" | tee /tmp/status.tmp ; BUSY
   rm -r -f $HOME/.emerald/themes/Win2-7* ; STATUSCHECK
   if [ -d "$HOME/.emerald/theme.old" ]; then
      rm -r -f $HOME/.emerald/theme ; STATUSCHECK
      mv $HOME/.emerald/theme.old $HOME/.emerald/theme ; STATUSCHECK
   else
      if [ -d "$HOME/.emerald/default" ]; then
         if grep -q "Win2-7" "$HOME/.emerald/theme/theme.ini" 2>> "/dev/null" ; then
            rm -f -r $HOME/.emerald/theme ; STATUSCHECK
            mv $HOME/.emerald/default $HOME/.emerald/theme ; STATUSCHECK
         fi
      fi
   fi
   rm -r -f "$HOME/.emerald/default" ; STATUSCHECK
   rm -r -f "$HOME/.emerald/theme.old" ; STATUSCHECK
   gconftool-2 --unset "/apps/win2-7pack/emerald_themes" > "/dev/null" 2>&1
   DISPLAYSTATUS
fi

# =============================================================================================================
# Remove Emesene Themes:
if [ -d "/usr/share/emesene/themes/emesene" ]; then
   echo -n "# $WORD298" | tee /tmp/status.tmp ; BUSY
   echo "$PASS" | sudo -S -p "" rm -r -f /usr/share/emesene/themes/default ; STATUSCHECK			
   echo "$PASS" | sudo -S -p "" mv /usr/share/emesene/themes/emesene /usr/share/emesene/themes/default ; STATUSCHECK
   echo "$PASS" | sudo -S -p "" rm -r -f /usr/share/emesene/smilies/default ; STATUSCHECK
   echo "$PASS" | sudo -S -p "" mv /usr/share/emesene/smilies/emesene /usr/share/emesene/smilies/default ; STATUSCHECK
   echo "$PASS" | sudo -S -p "" rm -r -f /usr/share/emesene/sound_themes/default ; STATUSCHECK
   echo "$PASS" | sudo -S -p "" mv /usr/share/emesene/sound_themes/emesene /usr/share/emesene/sound_themes/default ; STATUSCHECK
   echo "$PASS" | sudo -S -p "" rm -f /usr/share/emesene/plugins_base/CustomGtkStyle.py ; STATUSCHECK
   gconftool-2 --unset "/apps/win2-7pack/emesene_theme" > "/dev/null" 2>&1
   DISPLAYSTATUS
fi

# =============================================================================================================
# Remove Icon Theme:
if [ -d "$HOME/.icons/Win2-7" ]; then
   echo -n "# $WORD299" | tee /tmp/status.tmp ; BUSY
   rm -f -r "$HOME/.icons/Win2-7" >> "/dev/null" 2>&1
   rm -f -r "$HOME/.icons/Win2-7Libre"
   gconftool-2 --unset "/apps/win2-7pack/icon_theme" > "/dev/null" 2>&1
   DISPLAYSTATUS
fi

# =============================================================================================================
# Remove Gnomenu Themes:
if [ -d "/usr/share/gnomenu/Themes/Menu/Win2-7Standard" ]; then
   echo -n "# $WORD300" | tee /tmp/status.tmp ; BUSY
   gconftool-2 --set "/apps/gnomenu/Icon_Name"                       --type string "Newstyles" ; STATUSCHECK
   gconftool-2 --set "/apps/gnomenu/Button_Name"                     --type string "GnoBlue" ; STATUSCHECK
   gconftool-2 --set "/apps/gnomenu/Menu_Name"                       --type string "Menu" ; STATUSCHECK
   echo "$PASS" | sudo -S -p "" rm -f -r /usr/share/gnomenu/Themes/Button/WinOrb ; STATUSCHECK
   echo "$PASS" | sudo -S -p "" rm -f -r /usr/share/gnomenu/Themes/Button/ViGlance ; STATUSCHECK
   echo "$PASS" | sudo -S -p "" rm -f -r /usr/share/gnomenu/Themes/Icon/Win7_Icons_1.1 ; STATUSCHECK
   echo "$PASS" | sudo -S -p "" rm -f -r /usr/share/gnomenu/Themes/Menu/Win2-7* ; STATUSCHECK
   echo "$PASS" | sudo -S -p "" rm -f -r /usr/share/gnomenu/Themes/Sound/Win2-7 ; STATUSCHECK
   gconftool-2 --unset "/apps/win2-7pack/gnomenu_themes" > "/dev/null" 2>&1
   DISPLAYSTATUS
fi

# =============================================================================================================
# Remove Gnome Control Center Themes:
if [ -d "/usr/share/gnome-control-center/pixmaps.old" ]; then
   echo -n "# $WORD301" | tee /tmp/status.tmp ; BUSY
   echo "$PASS" | sudo -S -p "" cp -r /usr/share/gnome-control-center/pixmaps.old /usr/share/gnome-control-center/pixmaps ; STATUSCHECK
   echo "$PASS" | sudo -S -p "" rm -r -f /usr/share/gnome-control-center/pixmaps.old ; STATUSCHECK
   gconftool-2 --unset "/apps/win2-7pack/control_center_theme" > "/dev/null" 2>&1
   DISPLAYSTATUS
fi

# =============================================================================================================
# Remove Gnome Panel Pixmaps:
if [ -d "/usr/share/gnome-panel/pixmaps.old" ]; then
   echo -n "# $WORD302" | tee /tmp/status.tmp ; BUSY
   echo "$PASS" | sudo -S -p "" rm -r -f /usr/share/gnome-panel/pixmaps ; STATUSCHECK
   echo "$PASS" | sudo -S -p "" mv /usr/share/gnome-panel/pixmaps.old /usr/share/gnome-panel/pixmaps ; STATUSCHECK
   gconftool-2 --unset "/apps/win2-7pack/panel_pixmaps" > "/dev/null" 2>&1
   DISPLAYSTATUS
fi

# =============================================================================================================
# Remove GTK-Themes:
if [ -d $HOME"/.themes" ]; then
   echo -n "# $WORD303" | tee /tmp/status.tmp ; BUSY
   rm -f -r $HOME/.themes/Win2-7* ; STATUSCHECK
   rm -f -r $HOME/.themes/WLM* ; STATUSCHECK
   gconftool-2 --unset "/apps/win2-7pack/gtk_theme" > "/dev/null" 2>&1
   DISPLAYSTATUS
fi

# =============================================================================================================
# Remove Win2-7 Fonts:
if [ -e $HOME"/.fonts/seguibk.ttf" ]; then
   echo -n "# $WORD304" | tee /tmp/status.tmp ; BUSY
   gconftool-2 --set "/desktop/gnome/interface/document_font_name"   --type string "Sans 10" ; STATUSCHECK
   gconftool-2 --set "/apps/metacity/general/titlebar_font"          --type string "Sans 10" ; STATUSCHECK
   gconftool-2 --set "/apps/nautilus/preferences/desktop_font"       --type string "Sans 10" ; STATUSCHECK
   gconftool-2 --set "/desktop/gnome/interface/font_name"            --type string "Sans 10" ; STATUSCHECK
   rm -f -r $HOME/.fonts/seguibd.ttf ; STATUSCHECK
   rm -f -r $HOME/.fonts/seguibk.ttf ; STATUSCHECK
   gconftool-2 --unset "/apps/win2-7pack/fonts" > "/dev/null" 2>&1
   DISPLAYSTATUS
fi

# =============================================================================================================
# Remove Lock Theme:
if [ -e "/usr/share/gnome-screensaver/lock-dialog-win2-7.gtkrc" ]; then
   echo -n "# $WORD305" | tee /tmp/status.tmp ; BUSY
   echo "$PASS" | sudo -S -p "" rm -f -r /usr/share/gnome-screensaver ; STATUSCHECK				
   echo "$PASS" | sudo -S -p "" mv /usr/share/gnome-screensaver.old /usr/share/gnome-screensaver ; STATUSCHECK
   gconftool-2 --set "/apps/gnome-screensaver/lock_dialog_theme" --type string "default" ; STATUSCHECK
   gconftool-2 --unset "/apps/win2-7pack/lock_theme" > "/dev/null" 2>&1
   DISPLAYSTATUS
fi

# =============================================================================================================
# Remove 9.10 Xsplash:
if [ -d "/usr/share/images/xsplash.old" ]; then
   echo -n "# $WORD306" | tee /tmp/status.tmp ; BUSY
   echo "$PASS" | sudo -S -p "" rm -r -f /usr/share/images/xsplash ; STATUSCHECK					
   echo "$PASS" | sudo -S -p "" mv /usr/share/images/xsplash.old /usr/share/images/xsplash ; STATUSCHECK
   gconftool-2 --unset "/apps/win2-7pack/xsplash_theme" > "/dev/null" 2>&1
   DISPLAYSTATUS
fi

# =============================================================================================================
# Remove GDM2 Wallpaper:

if [ "$GDM" = "3" ]; then
   if [ -e "/etc/gdm3/greeter.gconf-defaults.old" ]; then
      echo -n "# $WORD307" | tee /tmp/status.tmp ; BUSY
      rm -f "/etc/gdm3/greeter.gconf-defaults"
      mv "/etc/gdm3/greeter.gconf-defaults.old" "/etc/gdm3/greeter.gconf-defaults"
      gconftool-2 --unset "/apps/win2-7pack/gdm2_wallpaper" > "/dev/null" 2>&1
      DISPLAYSTATUS
   fi
fi

# =============================================================================================================
# Remove GDM2 Wallpaper:

if [ "$GDM" = "2" ]; then
   echo -n "# $WORD307" | tee /tmp/status.tmp ; BUSY

   case $UVERSION in
     *Ubuntu* )
        echo "$PASS" | sudo -S -p "" -u gdm gconftool-2 --type string --set /desktop/gnome/background/picture_filename "/usr/share/backgrounds/warty-final-ubuntu.png" ; STATUSCHECK
                ;;
     "Mint" )
         echo "$PASS" | sudo -S -p "" -u gdm gconftool-2 --type string --set /desktop/gnome/background/picture_filename "/usr/share/backgrounds/linuxmint/Talento-1.jpg" ; STATUSCHECK
                ;;
     "Fedora" )
         echo "$PASS" | sudo -S -p "" -u gdm gconftool-2 --type string --set /desktop/gnome/background/picture_filename "/usr/share/backgrounds/goddard/default/goddard.xml" ; STATUSCHECK
                ;;
     "Mandriva" )
         echo "$PASS" | sudo -S -p "" -u gdm gconftool-2 --type string --set /desktop/gnome/background/picture_filename "/usr/share/mdk/backgrounds/Mandriva.xml" ; STATUSCHECK
                ;;
     "openSUSE" )
         echo "$PASS" | sudo -S -p "" -u gdm gconftool-2 --type string --set /desktop/gnome/background/picture_filename "/usr/share/wallpapers/openSUSE113-1600x1200.jpg" ; STATUSCHECK
                ;;
   esac

   gconftool-2 --unset "/apps/win2-7pack/gdm2_wallpaper" > "/dev/null" 2>&1
   DISPLAYSTATUS
fi

# =============================================================================================================
# Remove GDM Theme:
if [ -d "/usr/share/gdm/themes/win2-7" ]; then
   echo -n "# $WORD309" | tee /tmp/status.tmp ; BUSY
   echo "$PASS" | sudo -S -p "" rm -r -f /usr/share/gdm/themes/win2-7 ; STATUSCHECK
   gconftool-2 --unset "/apps/win2-7pack/gdm_theme" > "/dev/null" 2>&1
   DISPLAYSTATUS
fi

# =============================================================================================================
# Remove Mouse Cursor Theme:
if [ -d $HOME"/.icons/aero-drop" ]; then
   echo -n "# $WORD310" | tee /tmp/status.tmp ; BUSY
   rm -r -f $HOME/.icons/aero-drop ; STATUSCHECK
   gconftool-2 --unset "/apps/win2-7pack/curser_theme" > "/dev/null" 2>&1
   DISPLAYSTATUS
fi

# =============================================================================================================
# Remove Nautilus Breadcrumbs:
if [ -d "$HOME/.themes/nautilus" ]; then
   echo -n "# $WORD201" | tee /tmp/status.tmp ; BUSY
   gconftool-2 --set "/apps/nautilus/preferences/pathbar_like_breadcrumbs" --type bool false ; STATUSCHECK
   rm -r -f $HOME/.gtkrc-2.0 ; STATUSCHECK
   rm -r -f $HOME/.themes/nautilus ; STATUSCHECK
   rm -r -f $HOME/.themes/breadcrumbs* ; STATUSCHECK
   if [ -d $HOME/.themes/nautilus.old ]; then
      mv $HOME/.themes/nautilus.old $HOME/.themes/nautilus ; STATUSCHECK
   fi
   if [ -e $HOME/.gtkrc-2.0.old ]; then
      mv $HOME/.gtkrc-2.0.old $HOME/.gtkrc-2.0 ; STATUSCHECK
   fi
   gconftool-2 --unset "/apps/win2-7pack/breadcrumb_theme" > "/dev/null" 2>&1
   DISPLAYSTATUS
fi


# =============================================================================================================
# Remove OpenOffice Splash Screen:
   
echo -n "# $WORD308" | tee /tmp/status.tmp ; BUSY

# Intro Graphic:
if [[ -e "/usr/lib/openoffice/program/openintro_ubuntu_sun1.bmp" ]]; then
   echo "$PASS" | sudo -S -p "" rm -f /usr/lib/openoffice/program/openintro_ubuntu_sun.bmp > "/dev/null" 2>&1 ; STATUSCHECK      
   echo "$PASS" | sudo -S -p "" mv /usr/lib/openoffice/program/openintro_ubuntu_sun1.bmp /usr/lib/openoffice/program/openintro_ubuntu_sun.bmp > "/dev/null" 2>&1 ; STATUSCHECK

elif [[ -e "/usr/lib/openoffice/program/openintro_ubuntu_oracle1.bmp" ]]; then
   echo "$PASS" | sudo -S -p "" rm -f /usr/lib/openoffice/program/openintro_ubuntu_oracle.bmp > "/dev/null" 2>&1 ; STATUSCHECK      
   echo "$PASS" | sudo -S -p "" mv /usr/lib/openoffice/program/openintro_ubuntu_oracle1.bmp /usr/lib/openoffice/program/openintro_ubuntu_oracle.bmp > "/dev/null" 2>&1 ; STATUSCHECK

elif [[ -e "/opt/openoffice.org3/program/intro1.bmp" ]]; then
   echo "$PASS" | sudo -S -p "" rm -f /opt/openoffice.org3/program/intro.bmp > "/dev/null" 2>&1 ; STATUSCHECK     
   echo "$PASS" | sudo -S -p "" mv /opt/openoffice.org3/program/intro1.bmp /opt/openoffice.org3/program/intro.bmp > "/dev/null" 2>&1 ; STATUSCHECK

elif [[ -e "/usr/lib/openoffice/program/intro1.bmp" ]]; then
   echo "$PASS" | sudo -S -p "" rm -f /usr/lib/openoffice/program/intro.bmp > "/dev/null" 2>&1 ; STATUSCHECK     
   echo "$PASS" | sudo -S -p "" mv /usr/lib/openoffice/program/intro1.bmp /usr/lib/openoffice/program/intro.bmp> "/dev/null" 2>&1 ; STATUSCHECK

elif [[ -e "/usr/lib/openoffice.org3/program/intro1.bmp" ]]; then
   echo "$PASS" | sudo -S -p "" rm -f /usr/lib/openoffice.org3/program/intro.bmp > "/dev/null" 2>&1 ; STATUSCHECK    
   echo "$PASS" | sudo -S -p "" mv /usr/lib/openoffice.org3/program/intro1.bmp /usr/lib/openoffice.org3/program/intro.bmp > "/dev/null" 2>&1 ; STATUSCHECK

elif [[ -e "/usr/lib/ooo/program/openintro_mandriva1.bmp" ]]; then
   echo "$PASS" | sudo -S -p "" rm -f /usr/lib/ooo/program/openintro_mandriva.bmp > "/dev/null" 2>&1 ; STATUSCHECK       
   echo "$PASS" | sudo -S -p "" mv /usr/lib/ooo/program/openintro_mandriva1.bmp /usr/lib/ooo/program/openintro_mandriva.bmp > "/dev/null" 2>&1 ; STATUSCHECK

elif [[ -e "/usr/share/ooo3/program/intro1.png" ]]; then
   echo "$PASS" | sudo -S -p "" rm -f /usr/share/ooo3/program/intro.png > "/dev/null" 2>&1 ; STATUSCHECK
   echo "$PASS" | sudo -S -p "" mv /usr/share/ooo3/program/intro1.png /usr/share/ooo3/program/intro.png > "/dev/null" 2>&1 ; STATUSCHECK

elif [[ -e "/usr/share/ooo3/program/intro1.bmp" ]]; then
   echo "$PASS" | sudo -S -p "" rm -f /usr/share/ooo3/program/intro.bmp > "/dev/null" 2>&1 ; STATUSCHECK   
   echo "$PASS" | sudo -S -p "" mv /usr/share/ooo3/program/intro1.bmp /usr/share/ooo3/program/intro.bmp > "/dev/null" 2>&1 ; STATUSCHECK 

fi

# About graphic:
if [[ -e "/usr/lib/openoffice/program/openabout_ubuntu_sun1.bmp" ]]; then
   echo "$PASS" | sudo -S -p "" rm -f /usr/lib/openoffice/program/openabout_ubuntu_sun.bmp > "/dev/null" 2>&1 ; STATUSCHECK      
   echo "$PASS" | sudo -S -p "" mv /usr/lib/openoffice/program/openabout_ubuntu_sun1.bmp /usr/lib/openoffice/program/openabout_ubuntu_sun.bmp > "/dev/null" 2>&1 ; STATUSCHECK 

elif [[ -e "/usr/lib/openoffice/program/openabout_ubuntu_oracle1.bmp" ]]; then
   echo "$PASS" | sudo -S -p "" rm -f /usr/lib/openoffice/program/openabout_ubuntu_oracle.bmp > "/dev/null" 2>&1 ; STATUSCHECK
   echo "$PASS" | sudo -S -p "" mv /usr/lib/openoffice/program/openabout_ubuntu_oracle1.bmp /usr/lib/openoffice/program/openabout_ubuntu_oracle.bmp > "/dev/null" 2>&1 ; STATUSCHECK

elif [[ -e "/opt/openoffice.org3/program/about1.bmp" ]]; then
   echo "$PASS" | sudo -S -p "" rm -f /opt/openoffice.org3/program/about.bmp > "/dev/null" 2>&1 ; STATUSCHECK
   echo "$PASS" | sudo -S -p "" mv /opt/openoffice.org3/program/about1.bmp /opt/openoffice.org3/program/about.bmp > "/dev/null" 2>&1 ; STATUSCHECK

elif [[ -e "/usr/lib/openoffice/program/about1.bmp" ]]; then
   echo "$PASS" | sudo -S -p "" rm -f /usr/lib/openoffice/program/about.bmp > "/dev/null" 2>&1 ; STATUSCHECK
   echo "$PASS" | sudo -S -p "" mv /usr/lib/openoffice/program/about1.bmp /usr/lib/openoffice/program/about.bmp > "/dev/null" 2>&1 ; STATUSCHECK

elif [[ -e "/usr/lib/openoffice/program/about1.png" ]]; then
   echo "$PASS" | sudo -S -p "" rm -f /usr/lib/openoffice/program/about.png > "/dev/null" 2>&1 ; STATUSCHECK
   echo "$PASS" | sudo -S -p "" mv /usr/lib/openoffice/program/about1.png /usr/lib/openoffice/program/about.png > "/dev/null" 2>&1 ; STATUSCHECK

elif [[ -e "/usr/lib/openoffice.org3/program/about1.bmp" ]]; then
   echo "$PASS" | sudo -S -p "" rm -f /usr/lib/openoffice.org3/program/about.bmp > "/dev/null" 2>&1 ; STATUSCHECK
   echo "$PASS" | sudo -S -p "" mv /usr/lib/openoffice.org3/program/about1.bmp /usr/lib/openoffice.org3/program/about.bmp > "/dev/null" 2>&1 ; STATUSCHECK

elif [[ -e "/usr/lib/ooo/program/openabout_mandriva1.bmp" ]]; then
   echo "$PASS" | sudo -S -p "" rm -f /usr/lib/ooo/program/openabout_mandriva.bmp > "/dev/null" 2>&1 ; STATUSCHECK
   echo "$PASS" | sudo -S -p "" mv /usr/lib/ooo/program/openabout_mandriva1.bmp /usr/lib/ooo/program/openabout_mandriva.bmp > "/dev/null" 2>&1 ; STATUSCHECK

elif [[ -e "/usr/share/ooo3/program/about1.png" ]]; then
   echo "$PASS" | sudo -S -p "" rm -f /usr/share/ooo3/program/about.png > "/dev/null" 2>&1 ; STATUSCHECK
   echo "$PASS" | sudo -S -p "" mv /usr/share/ooo3/program/about1.png /usr/share/ooo3/program/about.png > "/dev/null" 2>&1 ; STATUSCHECK
fi

gconftool-2 --unset "/apps/win2-7pack/openoffice_splash" > "/dev/null" 2>&1
DISPLAYSTATUS

# =============================================================================================================
# Remove Plymouth Theme:
if [ "$UVERSION" = "Ubuntu104" ] && [ -d "/lib/plymouth/themes/7" ] && [ -d "/lib/plymouth/themes/winbuntu" ]; then
   echo -n "# $WORD202" | tee /tmp/status.tmp ; BUSY
   echo "$PASS" | sudo -S -p "" rm -Rf /lib/plymouth/themes/7 ; STATUSCHECK
   echo "$PASS" | sudo -S -p "" rm -Rf /lib/plymouth/themes/winbuntu ; STATUSCHECK
   DISPLAYSTATUS
   gconftool-2 --unset "/apps/win2-7pack/plymouth_theme" > "/dev/null" 2>&1
fi

# =============================================================================================================
# Remove RGBA Config:
if [ -e "$HOME/.gnome2/gedit/plugins/instructions" ]; then
   echo -n "# $WORD203" | tee /tmp/status.tmp ; BUSY
   gconftool-2 --unset "/apps/rhythmbox/plugins/rgba-visual/active" ; STATUSCHECK
   gconftool-2 --unset "/apps/gedit-2/plugins/active-plugins" ; STATUSCHECK
   rm -f -r $HOME/.gnome2/gedit ; STATUSCHECK
   rm -f -r $HOME/.gnome2/rhythmbox ; STATUSCHECK
   gconftool-2 --unset "/apps/win2-7pack/rgba_apps"
   DISPLAYSTATUS
fi

# =============================================================================================================
# Remove Sound Theme:
if [ -d $HOME"/.local/share/sounds/Win2-7" ]; then
   echo -n "# $WORD204" | tee /tmp/status.tmp ; BUSY
   rm -r -f $HOME/.local/share/sounds/Win2-7 ; STATUSCHECK
   gconftool-2 --unset "/apps/win2-7pack/sound_themes" > "/dev/null" 2>&1
   DISPLAYSTATUS
fi

# =============================================================================================================
# Remove Tsclient Theme:
if [ -d "/usr/share/pixmaps/tsclient.old" ]; then
   echo -n "# $WORD205" | tee /tmp/status.tmp ; BUSY
   echo "$PASS" | sudo -S -p "" rm -r -f /usr/share/pixmaps/tsclient ; STATUSCHECK
   echo "$PASS" | sudo -S -p "" mv /usr/share/pixmaps/tsclient.old /usr/share/pixmaps/tsclient ; STATUSCHECK
   gconftool-2 --unset "/apps/win2-7pack/terminal_server_theme" > "/dev/null" 2>&1

   DISPLAYSTATUS
fi

# =============================================================================================================
# Remove Wine Theme:
if [ -d "$HOME/.wine/drive_c/windows/Resources/themes/Seven" ]; then
   echo -n "# $WORD206" | tee /tmp/status.tmp ; BUSY
   rm -r -f $HOME/.wine/drive_c/windows/Resources/themes/Seven ; STATUSCHECK
   if [ -e $HOME/.wine/user.old ]; then
      rm -f $HOME/.wine/user.reg  ; STATUSCHECK
      mv $HOME/.wine/user.old $HOME/.wine/user.reg ; STATUSCHECK
   fi
   gconftool-2 --unset "/apps/win2-7pack/wine_theme" > "/dev/null" 2>&1
   DISPLAYSTATUS
fi

# =============================================================================================================
# Remove final gconf values:
echo -n "# $WORD228" | tee /tmp/status.tmp ; BUSY
gconftool-2 --unset "/apps/win2-7pack/current_version" > "/dev/null" 2>&1
gconftool-2 --unset "/apps/win2-7pack/status" > "/dev/null" 2>&1
gconftool-2 --unset "/apps/win2-7pack/install_mode" > "/dev/null" 2>&1
gconftool-2 --unset "/apps/win2-7pack/Win2-7_Restricted_Extras" > "/dev/null" 2>&1
DISPLAYSTATUS

fi

# =============================================================================================================
# Remove Win2-7 Essentials:
if [ "$UNINSTALL_WIN27E" = "YES" ]; then

echo "#"

# =============================================================================================================
# Uninstall Advaned Murrine:
if [ "$PMAN" = "APT" ]; then
if [ "$UNINSTALL_ADVANCED_MURRINE" = "YES" ] && [ "$ADVANCED_MURRINE_INSTALLED" = "Yes" ]; then

if [ "$ADVANCED_MURRINE_INSTALLED" = "Yes" ] && [ "$MURRINEHOLD" = "YES" ]; then

zenity --info --title="# $WORD207" --text="$WORD208"

echo -n "# $WORD209" | tee /tmp/status.tmp ; BUSY
echo gtk2-engines-murrine install | sudo dpkg --set-selections ; STATUSCHECK
DISPLAYSTATUS
fi

   echo -n "# $WORD210" | tee /tmp/status.tmp ; BUSY

   case $UVERSION in
      "Ubuntu104" )
   case $ARCH in
    "i686" ) 
         echo "$PASS" | sudo -S -p "" dpkg -i Files/debs/10.04/gtk2-engines-murrine_0.90.3+git20100323-0ubuntu3_i386.deb >> "/dev/null" 2>&1 ; STATUSCHECK
         gconftool-2 --unset "/apps/win2-7pack/advanced_murrine_installed" ; STATUSCHECK
           ;;
    "x86_64" ) 
         echo "$PASS" | sudo -S -p "" dpkg -i Files/debs/10.04/gtk2-engines-murrine_0.90.3+git20100323-0ubuntu3_amd64.deb >> "/dev/null" 2>&1 ; STATUSCHECK
         gconftool-2 --unset "/apps/win2-7pack/advanced_murrine_installed" ; STATUSCHECK
           ;;
   esac
             ;;
      "Ubuntu1010" )
   case $ARCH in
    "i686" ) 
         echo "$PASS" | sudo -S -p "" dpkg -i Files/debs/10.10/gtk2-engines-murrine_0.98.1.1-0ubuntu1_i386.deb >> "/dev/null" 2>&1 ; STATUSCHECK
         gconftool-2 --unset "/apps/win2-7pack/advanced_murrine_installed" ; STATUSCHECK
           ;;
    "x86_64" ) 
         echo "$PASS" | sudo -S -p "" dpkg -i Files/debs/10.10/gtk2-engines-murrine_0.98.1.1-0ubuntu1_amd64.deb >> "/dev/null" 2>&1 ; STATUSCHECK
         gconftool-2 --unset "/apps/win2-7pack/advanced_murrine_installed" ; STATUSCHECK
           ;;
   esac
             ;;
   esac

   DISPLAYSTATUS
fi
fi

# =============================================================================================================
# Uninstall Compiz Fusion Icon:
if [ "$UNINSTALL_FUSION_ICON" = "YES" ] && [ "$FUSIONICONINSTALLED" = "Yes" ]; then
   echo -n "# $WORD211" | tee /tmp/status.tmp ; BUSY

      case $PMAN in
       "APT" ) 
          echo "$PASS" | sudo -S -p "" apt-get -y remove fusion-icon >> "/dev/null" 2>&1 ; STATUSCHECK
              ;;
       "YUM" ) 
          echo "$PASS" | sudo -S -p "" yum -y remove fusion-icon >> "/dev/null" 2>&1 ; STATUSCHECK
              ;;
       "ZYPPER" ) 
          echo "$PASS" | sudo -S -p "" zypper remove -y fusion-icon >> "/dev/null" 2>&1 ; STATUSCHECK
              ;;
       "URPMI" ) 
          echo "$PASS" | sudo -S -p "" urpme -y fusion-icon >> "/dev/null" 2>&1 ; STATUSCHECK
              ;;
      esac

   DISPLAYSTATUS
fi

# =============================================================================================================
# Uninstall DockBarX:
if [ "$UNINSATLL_DOCKBARX" = "YES" ] && [ "$DOCKBARXINSTALLED" = "Yes" ]; then
   echo -n "# $WORD212" | tee /tmp/status.tmp ; BUSY

      case $PMAN in
       "APT" ) 
          echo "$PASS" | sudo -S -p "" apt-get -y remove dockbarx >> "/dev/null" 2>&1 ; STATUSCHECK
              ;;
       "YUM" ) 
          echo "$PASS" | sudo -S -p "" yum -y remove dockbarx >> "/dev/null" 2>&1 ; STATUSCHECK
              ;;
       "ZYPPER" ) 
          echo "$PASS" | sudo -S -p "" zypper remove -y dockbarx >> "/dev/null" 2>&1 ; STATUSCHECK
              ;;
       "URPMI" ) 
          echo "$PASS" | sudo -S -p "" urpme -y dockbarx >> "/dev/null" 2>&1 ; STATUSCHECK
              ;;
      esac

   DISPLAYSTATUS
fi

# =============================================================================================================
# Uninstall Emerald:
if [ "$UNINSTALL_EMERALD" = "YES" ] && [ "$EMERALDINSTALLED" = "Yes" ]; then
   echo -n "# $WORD213" | tee /tmp/status.tmp ; BUSY

      case $PMAN in
       "APT" ) 
          echo "$PASS" | sudo -S -p "" apt-get -y remove emerald >> "/dev/null" 2>&1 ; STATUSCHECK
              ;;
       "YUM" ) 
          echo "$PASS" | sudo -S -p "" yum -y remove emerald >> "/dev/null" 2>&1 ; STATUSCHECK
              ;;
       "ZYPPER" ) 
          echo "$PASS" | sudo -S -p "" zypper remove -y emerald >> "/dev/null" 2>&1 ; STATUSCHECK
              ;;
       "URPMI" ) 
          echo "$PASS" | sudo -S -p "" urpme -y emerald >> "/dev/null" 2>&1 ; STATUSCHECK
              ;;
      esac

   DISPLAYSTATUS
fi

# =============================================================================================================
# Uninstall Emesene:
if [ "$UNINSTALL_EMESENCE" = "YES" ] && [ "$EMESENEINSTALLED" = "Yes" ]; then
   echo -n "# $WORD214" | tee /tmp/status.tmp ; BUSY

      case $PMAN in
       "APT" ) 
          echo "$PASS" | sudo -S -p "" apt-get -y remove emesene >> "/dev/null" 2>&1 ; STATUSCHECK
              ;;
       "YUM" ) 
          echo "$PASS" | sudo -S -p "" yum -y remove emesene >> "/dev/null" 2>&1 ; STATUSCHECK
              ;;
       "ZYPPER" ) 
          echo "$PASS" | sudo -S -p "" zypper remove -y emesene >> "/dev/null" 2>&1 ; STATUSCHECK
              ;;
       "URPMI" ) 
          echo "$PASS" | sudo -S -p "" urpme -y emesene >> "/dev/null" 2>&1 ; STATUSCHECK
              ;;
      esac

   DISPLAYSTATUS
fi

# =============================================================================================================
# Uninstall Gnomenu:
if [ "$UNINSTALL_GNOMENU" = "YES" ] && [ "$GNOMENUINSTALLED" = "Yes" ]; then
   echo -n "# $WORD215" | tee /tmp/status.tmp ; BUSY

      case $PMAN in
       "APT" ) 
          echo "$PASS" | sudo -S -p "" apt-get -y remove gnomenu >> "/dev/null" 2>&1 ; STATUSCHECK
              ;;
       "YUM" ) 
          echo "$PASS" | sudo -S -p "" yum -y remove gnomenu >> "/dev/null" 2>&1 ; STATUSCHECK
              ;;
       "ZYPPER" ) 
          echo "$PASS" | sudo -S -p "" zypper remove -y gnomenu >> "/dev/null" 2>&1 ; STATUSCHECK
              ;;
       "URPMI" ) 
          echo "$PASS" | sudo -S -p "" urpme -y gnomenu >> "/dev/null" 2>&1 ; STATUSCHECK
              ;;
      esac

   DISPLAYSTATUS
fi

# =============================================================================================================
# Uninstall Screenlets:
if [ "$UNINSTALL_SCREENLETS" = "YES" ] && [ "$SCREENLETSINSTALLED" = "Yes" ]; then
   echo -n "# $WORD216" | tee /tmp/status.tmp ; BUSY

      case $PMAN in
       "APT" ) 
          echo "$PASS" | sudo -S -p "" apt-get -y remove screenlets >> "/dev/null" 2>&1 ; STATUSCHECK
              ;;
       "YUM" ) 
          echo "$PASS" | sudo -S -p "" yum -y remove screenlets >> "/dev/null" 2>&1 ; STATUSCHECK
              ;;
       "ZYPPER" ) 
          echo "$PASS" | sudo -S -p "" zypper remove -y screenlets >> "/dev/null" 2>&1 ; STATUSCHECK
              ;;
       "URPMI" ) 
          echo "$PASS" | sudo -S -p "" urpme -y screenlets >> "/dev/null" 2>&1 ; STATUSCHECK
              ;;
      esac

   DISPLAYSTATUS
fi

# =============================================================================================================
# Uninstall CCSM:
if [ "$UNINSTALL_CCSM" = "YES" ] && [ "$CCSMINSTALLED" = "Yes" ]; then
   echo -n "# $WORD218" | tee /tmp/status.tmp ; BUSY

      case $PMAN in
       "APT" ) 
          echo "$PASS" | sudo -S -p "" apt-get -y remove compizconfig-settings-manager >> "/dev/null" 2>&1 ; STATUSCHECK
              ;;
       "YUM" ) 
          echo "$PASS" | sudo -S -p "" yum -y remove compizconfig-settings-manager >> "/dev/null" 2>&1 ; STATUSCHECK
              ;;
       "ZYPPER" ) 
          echo "$PASS" | sudo -S -p "" zypper remove -y compizconfig-settings-manager >> "/dev/null" 2>&1 ; STATUSCHECK
              ;;
       "URPMI" ) 
          echo "$PASS" | sudo -S -p "" urpme -y compizconfig-settings-manager >> "/dev/null" 2>&1 ; STATUSCHECK
              ;;
      esac

   DISPLAYSTATUS
fi


# =============================================================================================================
# Update Softare Sources:
if [ "$PMAN" = "APT" ]; then
   echo -n "# $WORD219" | tee /tmp/status.tmp ; BUSY
   echo "$PASS" | sudo -S -p "" apt-get update > "/dev/null" 2>&1 ; STATUSCHECK
   DISPLAYSTATUS
fi

fi

# =============================================================================================================
# Restore Backup:

if [ "$RESTOREBACKUP" = "YES" ]; then

echo "#"

# =============================================================================================================
# Restoring Plymouth Theme:
if [ -e "$HOME/.Win2-7_GUI_Backup/plymouth" ]; then
echo -n "# $WORD220" | tee /tmp/status.tmp ; BUSY
PLYMOUTH_NAME=$(cat $HOME/.Win2-7_GUI_Backup/plymouth) ; STATUSCHECK
echo "$PASS" | sudo -S -p "" ln -sf $PLYMOUTH_NAME /etc/alternatives/default.plymouth
DISPLAYSTATUS
fi

# =============================================================================================================
# Restoring Metacity:
echo -n "# $WORD221" | tee /tmp/status.tmp ; BUSY
gconftool-2 --load $HOME/.Win2-7_GUI_Backup/xmls/Metacity_Gwd.xml ; STATUSCHECK
gconftool-2 --load $HOME/.Win2-7_GUI_Backup/xmls/Metacity_General.xml ; STATUSCHECK
DISPLAYSTATUS

# =============================================================================================================
# Restoring Nautilus:
echo -n "# $WORD222" | tee /tmp/status.tmp ; BUSY
gconftool-2 --load $HOME/.Win2-7_GUI_Backup/xmls/Nautilus_Desktop.xml ; STATUSCHECK
gconftool-2 --load $HOME/.Win2-7_GUI_Backup/xmls/Nautilus_Preferences.xml ; STATUSCHECK
gconftool-2 --load $HOME/.Win2-7_GUI_Backup/xmls/Nautilus_Tree.xml ; STATUSCHECK
DISPLAYSTATUS

# =============================================================================================================
# Restoring Gnome:
echo -n "# $WORD223" | tee /tmp/status.tmp ; BUSY
if ! [ "$GDM" = "3" ]; then
   echo "$PASS" | sudo -S -p "" -u "gdm" gconftool-2 --load $HOME/.Win2-7_GUI_Backup/xmls/Gnome_GDM.xml ; STATUSCHECK
fi
gconftool-2 --load $HOME/.Win2-7_GUI_Backup/xmls/Gnome_Screensaver.xml ; STATUSCHECK
gconftool-2 --load $HOME/.Win2-7_GUI_Backup/xmls/Gnome_Options.xml ; STATUSCHECK
gconftool-2 --load $HOME/.Win2-7_GUI_Backup/xmls/Gnome_Panel.xml ; STATUSCHECK
gconftool-2 --load $HOME/.Win2-7_GUI_Backup/xmls/Gnome_Background.xml ; STATUSCHECK
gconftool-2 --load $HOME/.Win2-7_GUI_Backup/xmls/Gnome_Interface.xml ; STATUSCHECK
gconftool-2 --load $HOME/.Win2-7_GUI_Backup/xmls/Gnome_Mouse.xml ; STATUSCHECK
gconftool-2 --load $HOME/.Win2-7_GUI_Backup/xmls/Gnome_Sound.xml ; STATUSCHECK
gconftool-2 --load $HOME/.Win2-7_GUI_Backup/xmls/Gnome_Mailto.xml ; STATUSCHECK
DISPLAYSTATUS

# =============================================================================================================
# Restoring MISC:
echo -n "# $WORD442" | tee /tmp/status.tmp ; BUSY
if [ "$DOCKBARXINSTALLED" = "Yes" ] && [ -e $HOME/.Win2-7_GUI_Backup/xmls/DockBarX.xml ]; then
gconftool-2 --load $HOME/.Win2-7_GUI_Backup/xmls/DockBarX.xml ; STATUSCHECK
fi
gconftool-2 --load $HOME/.Win2-7_GUI_Backup/xmls/Terminal.xml ; STATUSCHECK
DISPLAYSTATUS

# =============================================================================================================
# Removeing Backup:
if `zenity --question --title="$WORD224" --text="$WORD225 $HOME $WORD226"` ; then
echo -n "# $WORD227" | tee /tmp/status.tmp ; BUSY
rm -f -r $HOME/.Win2-7_GUI_Backup ; STATUSCHECK
DISPLAYSTATUS
fi

fi

echo "#"

# =============================================================================================================
# Restarting Panel:
echo -n "$WORD284" | tee /tmp/status.tmp ; BUSY
killall gnome-panel ; STATUSCHECK
sleep 8
DISPLAYSTATUS

# =============================================================================================================
# Restarting nautilus:
if [ "$UVERSION" = "Ubuntu104" ] || [ "$UVERSION" = "Ubuntu1010" ]; then
echo -n "# $WORD283" | tee /tmp/status.tmp ; BUSY
killall nautilus ; STATUSCHECK
sleep 8
DISPLAYSTATUS
fi

# =============================================================================================================
# Uninstall Complete:

echo -n "# "

$TPUT_BOLD

if [ "$ERRORS" = "YES" ]; then
$TPUT_RED
echo "$WORD229"
else
$TPUT_GREEN
echo "$WORD230"
fi

$TPUT_CLEAR

# =============================================================================================================
# Give notice for removal of CCSM blur graphic:
if [ "$NOTIFY_REFLECT_CCSM" = "YES" ] && [ "$CCSMINSTALLED" = "Yes" ]; then
   zenity --info --title="$WORD443" --text="$WORD444"
fi

# =============================================================================================================
# Ask for a reboot:

if [ "$GDM" = "3" ]; then

         CASE=$(zenity --list --title="$WORD425" --text="$WORD531" --radiolist  --column="$WORD15" --column="$WORD14" TRUE "$WORD532" FALSE "$OPTION_logoutno" )
         CHECKFORCANCEL
 	    case "$CASE" in
               "$WORD532" )
                      echo "$PASS" | sudo -S -p "" reboot
          	    ;;
               "$OPTION_logoutno" )
                   ENTERTOCLOSE
          	    ;;
 	    esac
fi

if [ "$GDM" = "2" ]; then

         CASE=$(zenity --list --title="$WORD430" --text="$WORD426" --radiolist  --column="$WORD15" --column="$WORD14" TRUE "$OPTION_logoutyes" FALSE "$OPTION_logoutno" )
         CHECKFORCANCEL
 	    case "$CASE" in
               "$OPTION_logoutyes" )
                   if [ "$UVERSION" = "Debian" ] || [ "$UVERSION" = "CentOS" ]; then
                      echo "$PASS" | sudo -S -p "" pkill -u $ME
                   else
                      gnome-session-save --force-logout
                   fi
          	    ;;
               "$OPTION_logoutno" )
                   ENTERTOCLOSE
          	    ;;
 	    esac
fi

zenity --warning --title="$WORD545" --text="$WORD544"
ENTERTOCLOSE

exit 0

