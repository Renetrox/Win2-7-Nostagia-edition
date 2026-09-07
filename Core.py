#!/usr/bin/env python
# -*- coding: utf-8 -*-

# By: Shane & Jesus
# Homepage: http://gnome-look.org/content/show.php/Win2-7+Pack?content=113264

# Load Critical Functions & Variables: ====================================================================

VERSION="6.8.3"

import os
import sys
import commands
import unicodedata

reload(sys)
sys.setdefaultencoding( "latin-1" )

sys.path.append('Files/lang')
sys.path.append('Files/modules')

import PyZenity

try:
   import curses
except:
   PyZenity.InfoMessage(text="The Python Curses Libary is not currently installed and is requred for installaion.\n\n If your useing OpenSuse you can run the command: \"zypper install -y python-curses\" as root to install it.\n\n Setup will now abort.", title="Info")
   exit()

curses.setupterm()

COLUMNS=commands.getoutput('tput cols')

HIDE=curses.tigetstr('civis')
SHOW=curses.tigetstr('cnorm')
SAVE=curses.tigetstr('sc')
LOAD=curses.tigetstr('rc')
RESET=curses.tigetstr('sgr0')
CBOLD=curses.tparm(curses.tigetstr('bold'), curses.A_BOLD)
UNDERLINE=curses.tparm(curses.tigetstr('smul'), curses.A_UNDERLINE)

RED=curses.tparm(curses.tigetstr('setaf'), curses.COLOR_RED)
GREEN=curses.tparm(curses.tigetstr('setaf'), curses.COLOR_GREEN)
YELLOW=curses.tparm(curses.tigetstr('setaf'), curses.COLOR_YELLOW)
BLUE=curses.tparm(curses.tigetstr('setaf'), curses.COLOR_BLUE)
WHITE=curses.tparm(curses.tigetstr('setaf'), curses.COLOR_WHITE)

try:
   RUN = sys.argv[1]
except:
   os.chdir(os.path.dirname(sys.argv[0]))

try:
   RUN = sys.argv[1]
except:
   PyZenity.InfoMessage(text="Please run GUIInstall.sh and not Core.py.", title=WORD17)
   exit()

def TERMINAL_STATUS(STATUS_STRING,STATUS):

   global ERROR_CATCH
#   global PAD_SPACES
#   global CHARACTER_CURRENT_COUNT
#   global CHARACTER_COUNT

#   PAD_SPACES = ""
#   CHARACTER_CURRENT_COUNT = 0
#   CHARACTER_COUNT = 0
#   CHARACTER_COUNT = len(STATUS_STRING)
#   CHARACTER_COUNT = (60 - CHARACTER_COUNT)

#   while CHARACTER_COUNT != CHARACTER_CURRENT_COUNT:
#      CHARACTER_CURRENT_COUNT = (CHARACTER_CURRENT_COUNT + 1)
#      PAD_SPACES = (PAD_SPACES + " ")

   sys.stdout.write(SAVE + STATUS_STRING + LOAD)
   sys.stdout.flush()

   ERRORLEVEL = os.system('tput cuf ' + COLUMNS)
   ERRORLEVEL = os.system('tput cub 15')

   sys.stdout.write(CBOLD + "[ " + SAVE + BLUE + STATUS + RESET + CBOLD + " ]" + LOAD)
   sys.stdout.flush()

def TERMINAL_STATUS_PASS():
   sys.stdout.write(GREEN + " OK ")
   sys.stdout.write(RESET + CBOLD + " ]" + "\n" + RESET)
   sys.stdout.flush()

def TERMINAL_STATUS_FAIL():
   ERROR_CATCH = "YES"
   sys.stdout.write(RED + "FAIL")
   sys.stdout.write(RESET + CBOLD + " ]" + "\n" + RESET)
   sys.stdout.flush()

def TERMINAL_STATUS_WARN():
   sys.stdout.write(YELLOW + "WARN")
   sys.stdout.write(RESET + CBOLD + " ]" + "\n" + RESET)
   sys.stdout.flush()

def STATUSCHECK():

   global FAIL

   if ERRORLEVEL != 0:
      FAIL = "Yes"

def RESOLVE_ERRORLEVEL():

   global FAIL

   if FAIL == "Yes":
      TERMINAL_STATUS_FAIL()
   else:
      TERMINAL_STATUS_PASS()
   FAIL = ""

# Load Pre-Text: ====================================================================

UNKNOWN_LANG = "No"

LANG = commands.getoutput('echo "$LANG"')

if "fr" in LANG:
   INTRO_TEXT = "Welcome To The Win2-7 Pack"
   INT_TEXT = "# Initializing Win2-7 Installer..."
   INT_LANG_TEXT = "# Initializing Language Support..."
elif "es" in LANG:
   INTRO_TEXT = "Welcome To The Win2-7 Pack"
   INT_TEXT = "# Initializing Win2-7 Installer..."
   INT_LANG_TEXT = "# Initializing Language Support..."
elif "pt_BR" in LANG:
   INTRO_TEXT = "Welcome To The Win2-7 Pack"
   INT_TEXT = "# Initializing Win2-7 Installer..."
   INT_LANG_TEXT = "# Initializing Language Support..."
elif "pt" in LANG:
   INTRO_TEXT = "Welcome To The Win2-7 Pack"
   INT_TEXT = "# Initializing Win2-7 Installer..."
   INT_LANG_TEXT = "# Initializing Language Support..."
elif "hr" in LANG:
   INTRO_TEXT = "Welcome To The Win2-7 Pack"
   INT_TEXT = "# Initializing Win2-7 Installer..."
   INT_LANG_TEXT = "# Initializing Language Support..."
elif "da" in LANG:
   INTRO_TEXT = "Welcome To The Win2-7 Pack"
   INT_TEXT = "# Initializing Win2-7 Installer..."
   INT_LANG_TEXT = "# Initializing Language Support..."
else:
   INTRO_TEXT = "Welcome To The Win2-7 Pack"
   INT_TEXT = "# Initializing Win2-7 Installer..."
   INT_LANG_TEXT = "# Initializing Language Support..."

sys.stdout.write(HIDE)

sys.stdout.write(CBOLD + GREEN + "**** " + RESET + CBOLD + INTRO_TEXT + GREEN + " ****" + RESET + "\n")

sys.stdout.write("\n")

TERMINAL_STATUS(INT_TEXT,"BUSY")
TERMINAL_STATUS_PASS()

# Load language module: ====================================================================

TERMINAL_STATUS(INT_LANG_TEXT,"BUSY")

if "en" in LANG:
   from English import *
elif "fr" in LANG:
   from French import *
#elif "es" in LANG:
#   from Spanish import *
#elif "pt_BR" in LANG:
#   from BPortuguese import *
#elif "pt" in LANG:
#   from EPortuguese import *
elif "ru" in LANG:
   from Russian import *
elif "hr" in LANG:
   from Croatian import *
elif "da" in LANG:
   from Danish import *
else:
   from English import *
   UNKNOWN_LANG = "YES"

if (RUN == "--language") or (UNKNOWN_LANG == "Yes"):

   LANG = commands.getoutput('zenity --list --title="" --text="" --radiolist  --column="" --column="" FALSE "Croatian" FALSE "Danish" TRUE "English" FALSE "French" FALSE "Russian"')
    
   if LANG == "English":
      from English import *
   elif LANG == "Croatian":
      from Croatian import *
   elif LANG == "French":
      from French import *
   elif LANG == "Russian":
      from Russian import *
   elif LANG == "Danish":
      from Danish import *
   elif LANG == "Spanish":
      from Spanish import *
   elif LANG == "Brazilian Portuguese":
      from BPortuguese import *
   elif LANG == "European Portuguese":
      from EPortuguese import *
   else:
      QUIT()

TERMINAL_STATUS_PASS()

# Load Modules: ====================================================================

TERMINAL_STATUS(WORD7,"BUSY")

import os
import time
import urllib2
import fcntl
import getpass

TERMINAL_STATUS_PASS()

# Define Global Variables: ====================================================================

TERMINAL_STATUS(WORD8,"BUSY")

# Generic Variables:
USER = os.path.expanduser("~") 
GNOME = "No"
UNITY = "No"
NOTCERTIFIED = "No"
SUDORERS_EXIST = "No"
ME = getpass.getuser()
PASS = ""
CURRENT_USER = os.path.expanduser("~")
BACKUP = USER + "/.Win2-7_GUI_Backup"
EDESKTOPCONFIG = ""
RESPONSE = ""
ERROR_CATCH = "No"
MURRINEHOLD = "No"
MURRINE_REINSTALLED = "No"
FAIL = ""
INSTALLWALLPAPERPATH = USER + "/.backgrounds"
OPENOFFICE_COMPLETE="No"
METACITY_COMPOSITING="No"
TKINTER="No"

# Programs Variables:
APTITUDEINSTALLED="No"
GVFSBININSTALLED="No"
PLYMOUTHTHEMEINSTALLED="No"
XDGUSERDIRSINSTALLED="No"
TSCLIENTINSTALLED="No"
SUDOINSTALLED="No"

# Win2-7 Variables:
MURRINEINSTALLED="No"
GNOMENUINSTALLED="No"
CCSMINSTALLED="No"
DOCKBARXINSTALLED="No"
EMERALDINSTALLED="No"
EMESENEINSTALLED="No"
FUSIONICONINSTALLED="No"
SCREENLETSINSTALLED="No"
WINEINSTALLED="No"
STANDARDMURRINEINSTALLED="No"
ELEMENTRYNINSTALLED="No"
RESTRICTEDEXTRAS="No"

TERMINAL_STATUS_PASS()

# Define Functions: ====================================================================

TERMINAL_STATUS(WORD9,"BUSY")

def INSTALLED_PROGRAMS():

# Define Variables (INSTALLED_PROGRAMS Function: ====================================================================

   global STATUS_STRING

   TERMINAL_STATUS(WORD10,"BUSY")

   global MURRINEINSTALLED
   global GNOMENUINSTALLED
   global CCSMINSTALLED
   global DOCKBARXINSTALLED
   global EMERALDINSTALLED
   global EMESENEINSTALLED
   global FUSIONICONINSTALLED
   global SCREENLETSINSTALLED
   global WINEINSTALLED
   global STANDARDMURRINEINSTALLED
   global ELEMENTRYNINSTALLED
   global RESTRICTEDEXTRAS

   global APTITUDEINSTALLED
   global GVFSBININSTALLED
   global PLYMOUTHTHEMEINSTALLED
   global XDGUSERDIRSINSTALLED
   global TSCLIENTINSTALLED
   global SUDOINSTALLED

   # Murrine Check:
   if PMAN == "APT":
      ERRORLEVEL = os.system('apt-cache policy "gtk2-engines-murrine" > "/tmp/MURRINE.tmp" 2> /dev/null')
      if os.path.exists('/tmp/MURRINE.tmp') == True:
         readfile = open('/tmp/MURRINE.tmp','r')
         line = readfile.readline()
         while line:
            if "Installed: 0.90.3+git20100323-1" in line:
               MURRINEINSTALLED="Yes"
               break
            elif "Installed: 0.98.1.1-1" in line:
               MURRINEINSTALLED="Yes"
               break
            line = readfile.readline()
         readfile.close()
         os.remove('/tmp/MURRINE.tmp')

   # Murrine (Mandriva):
   if UVERSION == "Mandriva":
      ERRORLEVEL = os.system('rpm -qa > /tmp/packages.tmp')
      if os.path.exists('/tmp/packages.tmp') == True:
         readfile = open('/tmp/packages.tmp','r')
         line = readfile.readline()
         while line:
            if "murrine" in line:
               STANDARDMURRINEINSTALLED="Yes"
               break
            line = readfile.readline()
         readfile.close()
         os.remove('/tmp/packages.tmp')

   # Aptitude Check:
   if (UVERSION == "Ubuntu1010") or (UVERSION == "Ubuntu114") or (UVERSION == "Mint11"):
      if os.system('aptitude -h > /dev/null 2>&1') == 0:
         APTITUDEINSTALLED="Yes"
   else:
      APTITUDEINSTALLED="Yes"

   # gvfs-bin Check:
   if (os.system('gvfs-set-attribute -help > /dev/null 2>&1') == 0) or (os.path.exists('/usr/share/doc/gvfs-bin') == True):
      GVFSBININSTALLED="Yes"

   # Plymouth Check:
   if os.path.exists('/etc/alternatives/default.plymouth') == True:
      PLYMOUTHTHEMEINSTALLED="Yes"

   # Xdg User Dirs Check:
   if os.system('xdg-user-dirs-update > /dev/null 2>&1') == 0:
      XDGUSERDIRSINSTALLED="Yes"

   # Tsclient Check:
   if (os.path.exists('/usr/bin/tsclient') == True) or (os.path.exists('/usr/lib/tsclient') == True):
      TSCLIENTINSTALLED="Yes"

   # Gnomenu Check:
   if (os.path.exists('/usr/bin/GnoMenu.py') == True) or (os.path.exists('/usr/lib/gnomenu') == True):
      GNOMENUINSTALLED="Yes"

   # CCSM Check:
   if UVERSION == "openSUSE":
      if os.system('compizconfig-settings-manager -v > /dev/null 2>&1') == 0:
         CCSMINSTALLED="Yes" 
   else:
      if (os.path.exists('/usr/bin/ccsm') == True) or (os.path.exists('/usr/share/ccsm') == True):
         CCSMINSTALLED="Yes"

   # DockBarX Check:
   if (os.path.exists('/usr/bin/dockbarx_factory.py') == True) or (os.path.exists('/usr/bin/dockbarx_factory') == True) or (os.path.exists('/usr/share/doc/dockbarx') == True):
      DOCKBARXINSTALLED="Yes" 
   
   # Emerald Check:
   if (os.path.exists('/usr/bin/emerald') == True) or (os.path.exists('/usr/share/doc/emerald') == True):
      EMERALDINSTALLED="Yes" 
   
   # Emesene Check:
   if (os.path.exists('/usr/bin/emesene') == True) or (os.path.exists('/usr/share/doc/emesene') == True):
      EMESENEINSTALLED="Yes" 
   
   # Fusion Icon Check:
   if (os.path.exists('/usr/bin/fusion-icon') == True) or (os.path.exists('/usr/share/doc/fusion-icon') == True):
      FUSIONICONINSTALLED="Yes"
   
   # Screenlets Check:
   if (os.path.exists('/usr/bin/screenlets') == True) or (os.path.exists('/usr/share/doc/screenlets') == True):
      SCREENLETSINSTALLED="Yes"
   
   # Wine Check:
   if (os.path.exists('/usr/bin/wine') == True) or (os.path.exists('/usr/share/doc/wine') == True) or (os.path.exists('/usr/share/wine') == True):
      WINEINSTALLED="Yes"

   # Elementary Desktop (Ubuntu Based):
   if PMAN == "APT":
      readfile = open('/etc/apt/sources.list','r')
      line = readfile.readline()
      while line:
         if "elementarydesktop" in line:
            ELEMENTRYNINSTALLED="Yes"
            break
         line = readfile.readline()
      readfile.close()

   # Elementary Desktop (Mandriva):
   if UVERSION == "Mandriva":
      ERRORLEVEL = os.system('rpm -qa > /tmp/packages.tmp')
      if os.path.exists('/tmp/packages.tmp') == True:
         readfile = open('/tmp/packages.tmp','r')
         line = readfile.readline()
         while line:
            if "nautilus-elementary" in line:
               ELEMENTRYNINSTALLED="Yes"
               break
            line = readfile.readline()
         readfile.close()
         os.remove('/tmp/packages.tmp')

   # Sudo Check:
   if os.system('sudo -h > /dev/null 2>&1') == 0:
      SUDOINSTALLED="Yes"

   # Win2-7 Restricted Extras:
   RESPONSE = commands.getoutput('gconftool-2 --get /apps/win2-7pack/Win2-7_Restricted_Extras 2> /dev/null')
   if RESPONSE == "Installed":
      RESTRICTEDEXTRAS="Yes"

   TERMINAL_STATUS_PASS()

   CHECK_PACKAGE_HOLDS() # Check page holds - (Another Function)

def QUIT():
   sys.stdout.write(RESET + "# \n")
   if ERROR_CATCH == "YES":
      sys.stdout.write(RESET + "# " + CBOLD + RED + WORD11)
   else:
      sys.stdout.write(RESET + "# " + CBOLD + GREEN + WORD12 + "\n")
   ENTER_TO_CLOSE()

def CHECK_FOR_CANCEL():
   if RESPONSE == False:
      CANCEL_SCRIPT()

def ABORT():
   sys.stdout.write(RESET + "# " + CBOLD + RED + WORD13 + "\n")
   ENTER_TO_CLOSE()

def CANCEL_SCRIPT():
   sys.stdout.write(RESET + "# " + CBOLD + RED + WORD13 + "\n")
   PyZenity.InfoMessage(text=WORD16, title=WORD17)
   sys.stdout.write(RESET)
   sys.stdout.write(SHOW)
   exit()

def ENTER_TO_CLOSE():
   sys.stdout.write(RESET + "# \n")
   sys.stdout.write(WORD20 + " " + CBOLD + WORD22 + RESET + " " + WORD23)
   sys.stdout.write(RESET)
   sys.stdout.write(SHOW)
   raw_input()
   exit()

def INTERNET_CHECK():

   global INTERNETSTATUS
   global TERMINAL_STATUS

   TERMINAL_STATUS(WORD25,"BUSY")
   try:
      os.system('ping -c 1 www.google.com > /dev/null 2>&1')
      INTERNETSTATUS = "Connected"
      TERMINAL_STATUS_PASS()
   except:
      try:
         INTERNETSTATUS = urllib2.urlopen('http://google.com')
         INTERNETSTATUS = "Connected"
         TERMINAL_STATUS_PASS()
      except:
         INTERNETSTATUS = "Not Connected"
         TERMINAL_STATUS_WARN()

def CHECK_PACKAGE_HOLDS():

   global TERMINAL_STATUS
   global MURRINEHOLD

   if (PMAN == "APT") and (MURRINEINSTALLED == "Yes"):
      TERMINAL_STATUS(WORD26,"BUSY")
      os.system('dpkg --get-selections | grep gtk2-engines-murrine > /tmp/holds.tmp')
      if os.path.exists('/tmp/holds.tmp') == True:
         readfile = open('/tmp/holds.tmp','r')
         line = readfile.readline()
         while line:
            if "hold" in line:
               MURRINEHOLD = "Yes"
               break
            line = readfile.readline()
         readfile.close()
         os.remove('/tmp/holds.tmp')
      TERMINAL_STATUS_PASS()

def CHECK_PROGRAM_LOCKS():

   global TERMINAL_STATUS
   global LOCK

   TERMINAL_STATUS(WORD29,"BUSY")
   for LOCK in "synaptic","update-manager","software-center","apt-get","dpkg","urpmi","zypper","yum","aptitude":
      if commands.getoutput('ps -U root | grep ' + LOCK):
         TERMINAL_STATUS_FAIL()
         PyZenity.ErrorMessage(WORD33 + " \"" + LOCK + "\" " + WORD34, title=WORD35)
         ABORT()
   TERMINAL_STATUS_PASS()

TERMINAL_STATUS_PASS()

# Check for double instance: ====================================================================

TERMINAL_STATUS(WORD40,"BUSY")

pid_file = '/tmp/program.pid'

checklock = open(pid_file, 'w')

try:
   fcntl.lockf(checklock, fcntl.LOCK_EX | fcntl.LOCK_NB)
except IOError:
   TERMINAL_STATUS_FAIL()
   PyZenity.ErrorMessage(WORD36, title=WORD34)
   ABORT()

TERMINAL_STATUS_PASS()

# Check for Root: ====================================================================

TERMINAL_STATUS(WORD37,"BUSY")

if os.getuid() == 0:
   TERMINAL_STATUS_FAIL()
   PyZenity.ErrorMessage(WORD38, title=WORD34)
   ABORT()

TERMINAL_STATUS_PASS()

# Indexing and importing GPG keys: ====================================================================

TERMINAL_STATUS(WORD39,"BUSY")

KEYS = os.system('gpg --quiet --list-keys >> \"/dev/null\" 2>&1')

TERMINAL_STATUS_PASS()

if KEYS == 0:
   KEYS = commands.getoutput('gpg --list-keys | grep Win2-7')
   if not "Win" in KEYS: 
      TERMINAL_STATUS(WORD41,"BUSY")
      os.system('gpg --quiet --import Files/keys/Win-7Team.gpg')
      TERMINAL_STATUS_PASS()

   if not "SDK" in os.getcwd():
      TERMINAL_STATUS(WORD42,"BUSY")
      if (os.system('gpg --quiet --verify GUIInstall.sh.sig >> /dev/null 2>&1') != 0) or (os.system('gpg --quiet --verify Core.py.sig >> /dev/null 2>&1') != 0):
         TERMINAL_STATUS_WARN()
         RESPONSE = PyZenity.Warning(WORD43, title=WORD44)
	 CHECK_FOR_CANCEL()
      else:
         TERMINAL_STATUS_PASS()

# Check Program Locks: ====================================================================

CHECK_PROGRAM_LOCKS()

# Check Linux Distribution: ====================================================================

TERMINAL_STATUS(WORD45,"BUSY")

readfile = open("/etc/issue","r")
ISSUE = readfile.readline()
readfile.close()

if "Ubuntu" in ISSUE:
   if "9.04" in ISSUE:
      UVERSION="Ubuntu94"
   elif "9.10" in ISSUE:
      UVERSION="Ubuntu910"
   elif "10.04" in ISSUE:
      UVERSION="Ubuntu104"
   elif "10.10" in ISSUE:
      UVERSION="Ubuntu1010"
   elif "11.04" in ISSUE:
      UVERSION="Ubuntu114"
   else:
      OSTAG="Ubuntu"
      UVERSION="Ubuntu1010"
      NOTCERTIFIED = "Yes"

elif "Fedora" in ISSUE:
   if "13" in ISSUE:
      UVERSION="Fedora"
   elif "14" in ISSUE:
      UVERSION="Fedora"
   else:
      OSTAG="Fedora"
      UVERSION="Fedora"
      NOTCERTIFIED = "Yes"

elif "Debian" in ISSUE:
   if "5.0" in ISSUE:
      UVERSION="Debian"
   elif "6.0" in ISSUE:
      UVERSION="Debian"
   else:
      OSTAG="Debian"
      UVERSION="Debian"
      NOTCERTIFIED = "Yes"

elif "Mint" in ISSUE:
   if "9" in ISSUE:
      UVERSION="Mint9"
   elif "10" in ISSUE:
      UVERSION="Mint10"
   elif "11" in ISSUE:
      UVERSION="Mint11"
   else:
      OSTAG="Linux Mint"
      UVERSION="Mint11"
      NOTCERTIFIED = "Yes"

elif "Mandriva" in ISSUE:
   if "2010" in ISSUE:
      UVERSION="Mandriva"
   else:
      OSTAG="Mandriva"
      UVERSION="Mandriva"
      NOTCERTIFIED = "Yes"

elif "PCLinuxOS" in ISSUE:
   if "2010" in ISSUE:
      UVERSION="PCLinuxOS"
   else:
      OSTAG="PCLinuxOS"
      UVERSION="PCLinuxOS"
      NOTCERTIFIED = "Yes"

elif "CentOS" in ISSUE:
   from sys import exit
   if "5.5" in ISSUE:
      UVERSION="CentOS"
   elif "5.6" in ISSUE:
      UVERSION="CentOS"
   else:
      OSTAG="CentOS"
      UVERSION="CentOS"
      NOTCERTIFIED = "Yes"

elif "openSUSE" in ISSUE:
   if "11.3" in ISSUE:
      UVERSION="openSUSE"
   else:
      OSTAG="openSUSE"
      UVERSION="openSUSE"
      NOTCERTIFIED = "Yes"

else:

   TERMINAL_STATUS_FAIL()

   ERRORLEVEL = PyZenity.Warning(WORD47, title=WORD46)
   ABORT()

if NOTCERTIFIED == "Yes":
   TERMINAL_STATUS_WARN()
   ERRORLEVEL = PyZenity.Warning(OSTAG + WORD48 + OSTAG + WORD49 + OSTAG + WORD50, title=WORD46)

if NOTCERTIFIED == "No":
   TERMINAL_STATUS_PASS()

# Check Package Manager.: ====================================================================

TERMINAL_STATUS(WORD18,"BUSY")

if os.system('apt-get -v > /dev/null 2>&1') == 0:
   PMAN="APT"
elif os.system('yum -h > /dev/null 2>&1') == 0:
   PMAN="YUM"
elif os.system('urpmf --version > /dev/null 2>&1') == 0:
   PMAN="URPMI"
elif os.system('zypper --version  > /dev/null 2>&1') == 0:
   PMAN="ZYPPER"
elif os.system('dpkg --version > /dev/null 2>&1') == 0:
   PMAN="DPKG"
elif os.system('rpm --version > /dev/null 2>&1') == 0:
   PMAN="RPM"
else:
   TERMINAL_STATUS_FAIL()

   PyZenity.ErrorMessage(WORD52, title=WORD51)
   ABORT()

TERMINAL_STATUS_PASS()

# Detecting Internet Connection: ====================================================================

INTERNET_CHECK()

# Checking Installed Programs: ====================================================================

INSTALLED_PROGRAMS()

# Checking Package holds:: ====================================================================

# (Included In INSTALLED_PROGRAMS()

# Checking GDM Version: ====================================================================

TERMINAL_STATUS(WORD53,"BUSY")

if os.path.exists('/etc/gdm3') == True:
   GDM="3"
else:
   GDM="2"

TERMINAL_STATUS_PASS()

# Checking Desktop Manager: ====================================================================

TERMINAL_STATUS(WORD54,"BUSY")

ERRORLEVEL = os.system('ps -e | awk \'{print $4}\' > /tmp/processes.tmp')
if os.path.exists('/tmp/processes.tmp') == True:
   readfile = open('/tmp/processes.tmp','r')
   line = readfile.readline()
   while line:
      if "gnome-panel" in line:
         GNOME = "Yes"
      if "unity-panel" in line:
         UNITY = "Yes"
      if "unity-2d-panel" in line:
         UNITY = "Yes"
      line = readfile.readline()
   readfile.close()
   os.remove('/tmp/processes.tmp')
else:
   TERMINAL_STATUS_FAIL()
   PyZenity.ErrorMessage(WORD55, title=WORD35)
   ABORT()

if UNITY == "Yes":
   TERMINAL_STATUS_FAIL()
   PyZenity.ErrorMessage(WORD58, title=WORD35)
   ABORT()

if GNOME == "No":
   TERMINAL_STATUS_FAIL()
   PyZenity.ErrorMessage(WORD56, title=WORD35)
   ABORT()

TERMINAL_STATUS_PASS()

# Checking CPU: ====================================================================

TERMINAL_STATUS(WORD57,"BUSY")

ARCH = commands.getoutput('uname -m')

if ARCH == "x86_64":
   MANDRIVAARCHARCH = "x86_64"
   MURRINE_ARCH = "amd64"
elif ARCH == "i686":
   MANDRIVAARCHARCH = "i586"
   MURRINE_ARCH = "i386"
else:
   TERMINAL_STATUS_FAIL()
   PyZenity.ErrorMessage(WORD61, title=WORD35)
   ABORT()

TERMINAL_STATUS_PASS()

# install sudo: ====================================================================

if (PMAN == "URPMI") and (SUDOINSTALLED == "No"):

   RESPONSE = PyZenity.Warning(WORD62, title=WORD44)
   CHECK_FOR_CANCEL()

   if INTERNETSTATUS == "Connected":
      sys.stdout.write(SHOW)
      while True:
         if os.system('su -l -c \"urpmi --quiet sudo\" root >> \"/dev/null\"') == 0:
            break
      sys.stdout.write(HIDE)
      INSTALLED_PROGRAMS()
   else:
      PyZenity.ErrorMessage(WORD63, title=WORD35)
      ABORT()

# Check for sudoer Status: ====================================================================================

if (UVERSION == "Fedora") or (UVERSION == "Debian") or (UVERSION == "PCLinuxOS") or (UVERSION == "CentOS") or (UVERSION == "Mandriva"):
   sys.stdout.write(WORD64 + "\n")
   sys.stdout.flush()
   sys.stdout.write(SHOW)
   while True:
      if os.system('su -c \"cp /etc/sudoers /tmp/sudoers.tmp && chmod -t /tmp && chmod 777 /tmp/sudoers.tmp\"') == 0:
         break
   sys.stdout.write(HIDE)
   readfile = open('/tmp/sudoers.tmp','r')
   line = readfile.readline()
   while line:
      if ME in line:
         SUDORERS_EXIST = "Yes"
      line = readfile.readline()
   readfile.close()
   os.remove('/tmp/sudoers.tmp')
   if SUDORERS_EXIST != "Yes":
      sys.stdout.write(WORD65 + " " + ME + " " + WORD66 + "\n")
      while True:
         if os.system('su root -c \"echo \'%s	ALL=(ALL)	ALL\' >> /etc/sudoers\"' % (ME)) == 0:
            break

# Password Management: ====================================================================================

os.system('sudo -K')

while True: 
   TERMINAL_STATUS(WORD67,"WAIT")
   PASS = PyZenity.GetText(text=WORD68, entry_text='', password=True, title=WORD69)
   if PASS == "":
      TERMINAL_STATUS_FAIL()
      PyZenity.Warning(WORD70, title=WORD44)
   elif PASS == None:
      TERMINAL_STATUS_FAIL()
      CANCEL_SCRIPT()
   else:
      if os.system('echo \"%s\" | sudo -S -p \"\" /bin/true 2> \"/dev/null\"' % (PASS)) == 0:
         os.system('sudo chmod 440 /etc/sudoers')
         TERMINAL_STATUS_PASS()
         break
      else:
         TERMINAL_STATUS_FAIL()
         PyZenity.ErrorMessage(WORD71, title=WORD35)

# =============================================================================================================
# Set GDM password (openSUSE):
if (UVERSION == "openSUSE") and (GDM == "2"):
   RESPONSE = PyZenity.InfoMessage(WORD72, title=WORD17)
   CHECK_FOR_CANCEL()

   TERMINAL_STATUS(WORD73,"WAIT")
   os.system('echo \"#!/bin/bash\" > /tmp/GDM.sh')
   os.system('echo \"echo \\"%s\\" | sudo -S -p \\\"\\\" bash -c \'echo \\"%s\\" | passwd -q --stdin \\\"gdm\\\"\'\" >> /tmp/GDM.sh' % (PASS,PASS))
   os.system('chmod 777 /tmp/GDM.sh')
   os.system('bash /tmp/GDM.sh')
   os.remove('/tmp/GDM.sh')
   TERMINAL_STATUS_PASS()

# Graphic Card Detections: ====================================================================

if (PLYMOUTHTHEMEINSTALLED == "Yes") and ((UVERSION == "Ubuntu104") or (UVERSION == "Ubuntu1010") or (UVERSION == "Ubuntu114")):

   TERMINAL_STATUS(WORD74,"BUSY")

   GRAPHICS = commands.getoutput('echo \"%s\" | sudo -S -p \"\" lshw -quiet -c display' % (PASS))

   if "nVidia Corporation" in GRAPHICS:
      TERMINAL_STATUS_WARN()
      GRAPHICS="No"
      RESPONSE = PyZenity.Warning(WORD75, title=WORD44)
      CHECK_FOR_CANCEL()
   else:
      TERMINAL_STATUS_PASS()
      GRAPHICS="Yes"
else:
   GRAPHICS="No"

# Install gvfs-bin.: ====================================================================

if (GVFSBININSTALLED == "No") and (UVERSION != "CentOS"):
   RESPONSE = PyZenity.Warning(WORD76, title=WORD44)
   CHECK_FOR_CANCEL()
   
   TERMINAL_STATUS(WORD77,"BUSY")

   if INTERNETSTATUS == "Connected":
      if PMAN == "APT":
         if os.system('echo \"%s\" | sudo -S -p \"\" apt-get -y install gvfs-bin >> \"/dev/null\" 2>&1' % (PASS)) == 0:
            INSTALL_STATUS = "PASS"
         else:
            INSTALL_STATUS = "FAIL"
      elif PMAN == "YUM":
         if os.system('echo \"%s\" | sudo -S -p \"\" yum -y install gvfs-bin >> \"/dev/null\" 2>&1' % (PASS)) == 0:
            INSTALL_STATUS = "PASS"
         else:
            INSTALL_STATUS = "FAIL"
      else:
         TERMINAL_STATUS_FAIL()
         PyZenity.ErrorMessage(WORD78, title=WORD35)
	 ABORT()
   else:
      TERMINAL_STATUS_FAIL()
      PyZenity.ErrorMessage(WORD83, title=WORD35)
      ABORT()

   if INSTALL_STATUS == "PASS":
      TERMINAL_STATUS_PASS()
      INSTALLED_PROGRAMS()
   else:
      TERMINAL_STATUS_FAIL()
      PyZenity.ErrorMessage("gvfs-bin " + WORD80, title=WORD35)
      ABORT()

# Install Aptitude: ====================================================================

if ((UVERSION == "Ubuntu1010") or (UVERSION == "Ubuntu114")) and (APTITUDEINSTALLED == "No"):
   RESPONSE = PyZenity.Warning(WORD81, title=WORD44)
   CHECK_FOR_CANCEL()
   
   TERMINAL_STATUS(WORD82,"BUSY")

   if INTERNETSTATUS == "Connected":
      if os.system('echo \"%s\" | sudo -S -p \"\" apt-get -y install aptitude >> \"/dev/null\" 2>&1' % (PASS)) == 0:
         INSTALL_STATUS = "PASS"
      else:
         INSTALL_STATUS = "FAIL"
   else:
      TERMINAL_STATUS_FAIL()
      PyZenity.ErrorMessage(WORD83, title=WORD35)
      ABORT()

   if INSTALL_STATUS == "PASS":
      TERMINAL_STATUS_PASS()
      INSTALLED_PROGRAMS()
   else:
      TERMINAL_STATUS_FAIL()
      PyZenity.ErrorMessage("Aptitude " + WORD80, title=WORD35)
      ABORT()

# xdg-user-dirs: ====================================================================

if (XDGUSERDIRSINSTALLED == "No") and (UVERSION != "CentOS"):
   RESPONSE = PyZenity.Warning(WORD85, title=WORD44)
   CHECK_FOR_CANCEL()

   TERMINAL_STATUS(WORD86,"BUSY")
   
   if INTERNETSTATUS == "Connected":
      if PMAN == "APT":
         if os.system('echo \"%s\" | sudo -S -p \"\" apt-get -y install xdg-user-dirs >> \"/dev/null\" 2>&1' % (PASS)) == 0:
            INSTALL_STATUS = "PASS"
         else:
            INSTALL_STATUS = "FAIL"
      elif PMAN == "YUM":
         if os.system('echo \"%s\" | sudo -S -p \"\" yum -y install xdg-user-dirs >> \"/dev/null\" 2>&1' % (PASS)) == 0:
            INSTALL_STATUS = "PASS"
         else:
            INSTALL_STATUS = "FAIL"
      else:
         TERMINAL_STATUS_FAIL()
         PyZenity.ErrorMessage(WORD87, title=WORD35)
	 ABORT()
   else:
      TERMINAL_STATUS_FAIL()
      PyZenity.ErrorMessage(WORD83, title=WORD35)
      ABORT()

   if INSTALL_STATUS == "PASS":
      TERMINAL_STATUS_PASS()
      INSTALLED_PROGRAMS()
   else:
      TERMINAL_STATUS_FAIL()
      PyZenity.ErrorMessage("Xdg-user-dirs " + WORD80, title=WORD35)
      ABORT()

# Update Locals: ====================================================================

if XDGUSERDIRSINSTALLED == "Yes":
   TERMINAL_STATUS(WORD79,"BUSY")
   os.system('xdg-user-dirs-update')
   TERMINAL_STATUS_PASS()

# Update directory localization: ====================================================================

if XDGUSERDIRSINSTALLED == "Yes":
   TERMINAL_STATUS(WORD84,"BUSY")

   MASTER_LINE=""

   readfile = open(USER + '/.config/user-dirs.dirs','r')
   line = readfile.readline()
   while line:
      MASTER_LINE=MASTER_LINE + line 
      line = readfile.readline()
   readfile.close()

   writefile = file("Files/modules/dirs.py", 'w')
   writefile.write("#!/usr/bin/env python\n")
   writefile.write("# -*- coding: utf-8 -*-\n")
   writefile.write("\n")
   writefile.write(MASTER_LINE)
   writefile.close()

   from dirs import *

   os.remove('Files/modules/dirs.py')
   DOCUMENTS = XDG_DOCUMENTS_DIR
   DESKTOP = XDG_DESKTOP_DIR
   DOWNLOAD = XDG_DOWNLOAD_DIR
   TERMINAL_STATUS_PASS()

# Reinstall Murrine Switch: ===================================================================================

if RUN == "--reinstallmurrine":
   if PMAN == "APT":
      if MURRINEINSTALLED == "Yes":
	 RESPONSE = PyZenity.Question(title=WORD88, text=WORD89)

	 if RESPONSE == False:
            CANCEL_SCRIPT()

         if MURRINEHOLD == "Yes":
            TERMINAL_STATUS(WORD90,"BUSY")
            if os.system('echo \"%s\" | sudo -S -p "" echo gtk2-engines-murrine install | sudo dpkg --set-selections' % (PASS)) == 0:
               TERMINAL_STATUS_PASS()
            else:
               TERMINAL_STATUS_FAIL()
               PyZenity.ErrorMessage(WORD91, title=WORD35)
               ABORT()

         TERMINAL_STATUS(WORD92,"BUSY")

         if UVERSION == "Ubuntu104":
            if ARCH == "i686":
               if os.system('echo \"%s\" | sudo -S -p "" dpkg -i Files/debs/10.04/gtk2-engines-murrine_Win2-7Pack_0.90.3+git20100323-1_i386.deb >> /dev/null 2>&1' % (PASS)) == 0:
                  MURRINE_REINSTALLED = "Yes"
            else:
               if os.system('echo \"%s\" | sudo -S -p "" dpkg -i Files/debs/10.04/gtk2-engines-murrine_Win2-7Pack_0.90.3+git20100323-1_amd64.deb >> /dev/null 2>&1' % (PASS)) == 0:
                  MURRINE_REINSTALLED = "Yes"
         else:
            if ARCH == "i686":
               if os.system('echo \"%s\" | sudo -S -p "" dpkg -i Files/debs/10.10/gtk2-engines-murrine_0.98.1.1-1_i386.deb >> /dev/null 2>&1' % (PASS)) == 0:
                  MURRINE_REINSTALLED = "Yes"
	    else:
               if os.system('echo \"%s\" | sudo -S -p "" dpkg -i Files/debs/10.10/gtk2-engines-murrine_0.98.1.1-1_amd64.deb >> /dev/null 2>&1' % (PASS)) == 0:
                  MURRINE_REINSTALLED = "Yes"

         if MURRINE_REINSTALLED == "Yes":
            TERMINAL_STATUS_PASS()
	    os.system('gconftool-2 --set /apps/win2-7pack/advanced_murrine_installed --type string Yes')
            QUIT() 
         else:
            TERMINAL_STATUS_FAIL()
            PyZenity.ErrorMessage(WORD93, title=WORD35)
            ABORT() 
 
      else:
         PyZenity.ErrorMessage(WORD94, title=WORD35)
         ABORT()
   else:
      PyZenity.ErrorMessage(WORD95, title=WORD35)
      ABORT()

# =============================================================================================================
# Unhold Murrine:

if RUN == "--unholdmurrine":
   if PMAN == "APT":
      if MURRINEINSTALLED == "Yes":
         TERMINAL_STATUS(WORD96,"BUSY")
         if MURRINEHOLD == "Yes":
            if os.system('echo \"%s\" | sudo -S -p \"\" echo gtk2-engines-murrine install | sudo dpkg --set-selections' % (PASS)) == 0:
               TERMINAL_STATUS_PASS()
            else:
               TERMINAL_STATUS_FAIL()
               PyZenity.ErrorMessage(WORD97, title=WORD35)
               ABORT()
         else:
            TERMINAL_STATUS_FAIL()
            PyZenity.ErrorMessage(WORD98, title=WORD35)
            ABORT()
      else:
         PyZenity.ErrorMessage(WORD99, title=WORD35)
         ABORT()
   else:
      PyZenity.ErrorMessage(WORD100, title=WORD35)
      ABORT()

# Load GUI Lib.: ====================================================================

TERMINAL_STATUS(WORD101,"BUSY")



try:
   from Tkinter import *
   from tkFont import *
   from tkMessageBox import *
   TERMINAL_STATUS_PASS()
except:
   try:
      from tkinter import *
      from tkFont import *
      from tkMessageBox import *
      TERMINAL_STATUS_PASS()
   except:
      TERMINAL_STATUS_WARN()
      RESPONSE = PyZenity.Warning(WORD102, title=WORD44)
      CHECK_FOR_CANCEL()

      if INTERNETSTATUS == "Connected":

         TERMINAL_STATUS(WORD103,"BUSY")
   
         if PMAN == "APT":
            if os.system('echo \"%s\" | sudo -S -p "" apt-get install -y python-tk >> /dev/null 2>&1' % (PASS)) == 0:
               TKINTER = "Yes"
         elif PMAN == "YUM":
            if os.system('echo \"%s\" | sudo -S -p "" yum -y install tkinter >> /dev/null 2>&1' % (PASS)) == 0:
               TKINTER = "Yes"
         elif PMAN == "URPMI":
            if os.system('echo \"%s\" | sudo -S -p "" urpmi --auto --quiet --force tkinter >> /dev/null 2>&1' % (PASS)) == 0:
               TKINTER = "Yes"
         else:
            if os.system('echo \"%s\" | sudo -S -p "" zypper install -y python-tk >> /dev/null 2>&1' % (PASS)) == 0:
               TKINTER = "Yes"

         if TKINTER == "Yes":
            TERMINAL_STATUS_PASS()
	    TERMINAL_STATUS(WORD101,"BUSY")

            try:
               from Tkinter import *
               from tkFont import *
               from tkMessageBox import *
               TERMINAL_STATUS_PASS()
            except:
               try:
                  from tkinter import *
                  from tkFont import *
                  from tkMessageBox import *
                  TERMINAL_STATUS_PASS()
               except:
                  TERMINAL_STATUS_PASS()
                  PyZenity.InfoMessage(WORD106, title=WORD17)
		  QUIT()
         else:
            TERMINAL_STATUS_FAIL()
            PyZenity.ErrorMessage(WORD105, title=WORD35)
            ABORT()

      else:
         TERMINAL_STATUS_FAIL()
         PyZenity.ErrorMessage(WORD104, title=WORD35)
         ABORT()

# Classes: ====================================================================

class MyApp:
    def __init__(self, parent):

	self.PAGE = "1"

        self.myParent = parent

        root.option_add("*Dialog.msg.wrapLength", "5i")

	if (os.path.exists(USER + '/.fonts/Arial.ttf') != True):
           os.system('mkdir -p \"$HOME\"/.fonts')
           os.system('cp Files/pics/Arial.ttf \"$HOME\"/.fonts/Arial.ttf')

	root.option_add('*Font','Arial 12 normal')

	self.boldfont = Font(weight="bold")

	self.imageT = PhotoImage(file="Files/pics/transparent.gif")
	self.image1 = PhotoImage(file="Files/pics/background.gif")
	self.image2 = PhotoImage(file="Files/pics/bottomlevel.gif")
	self.image3 = PhotoImage(file="Files/pics/arrow.gif")
	self.image4 = PhotoImage(file="Files/pics/checkmark.gif")
	self.image5 = PhotoImage(file="Files/pics/x.gif")
	self.image6 = PhotoImage(file="Files/pics/question.gif")
	self.image7 = PhotoImage(file="Files/pics/Forward.gif")
	self.image8 = PhotoImage(file="Files/pics/Back.gif")

        self.centerWindow()

	self.accepted_EULA = StringVar()
	self.TIMEFORMAT = StringVar()
	self.RESTRICTEDEXTRAS = StringVar()
        self.EULA_ACCEPT = IntVar()
	self.PRESET = StringVar()
	self.MURRINE = IntVar()
	self.CCSM = IntVar()
	self.COMPIZFUSIONICON = IntVar()
	self.DOCKBARX = IntVar()
	self.ELEMENTRYN = IntVar()
	self.EMERALD = IntVar()
	self.EMESENE = IntVar()
	self.GNOMENU = IntVar()
	self.SCREENLETS = IntVar()
	self.SUPERBAR = StringVar()
	self.WINMAN = StringVar()
	self.PLYMOUTHTHEME = StringVar()
	self.ICONBRAND = StringVar()
	self.DESK = StringVar()
	self.ALLWORKSPACES = StringVar()
	self.WALLPAPERNAME = StringVar()
	self.GTKTHEME = StringVar()
	self.STARTUP = StringVar()
	self.ETHEME = StringVar()
	self.PANELSTYLECOLOR = StringVar()
	self.BCRUMBS = StringVar()
	self.INSTALLTYPE = StringVar()
	self.PUSERNAME = StringVar()
	self.PUSERNAME = commands.getoutput('whoami')
	self.PUSERNAME = self.PUSERNAME.capitalize()
	self.EDESKTOP_INSTALL = StringVar()
	self.EDESKTOP_INSTALL.set("No")
	self.METACITYTHEME = StringVar()
	self.BCRUMBTHEME = StringVar()
	self.DOCKBAR_REP = StringVar()
	self.DOCKBAR_REP.set("No")
	self.GNOMENU_REP = StringVar()
	self.GNOMENU_REP.set("No")
	self.USS = StringVar()
	self.USS.set("No")

	self.RGBA_COUNTER = IntVar()
	self.RGBA_COUNTER.set(0)
        self.RGBA_GEDIT = IntVar()
        self.RGBA_RHYTHMBOX = IntVar()

	self.DESKTOP_ICONS_COUNTER = IntVar()
	self.DESKTOP_ICONS_COUNTER.set(0)
        self.DESKTOPCOMPUTER = IntVar()
        self.DESKTOPHOMEFOLDER = IntVar()
        self.DESKTOPNETWORK = IntVar()
        self.DESKTOPRECYLEBIN = IntVar()
        self.DESKTOPREMOVABLEDEVICES = IntVar()

	self.EDESTKOP_COUNTER = IntVar()
	self.EDESTKOP_COUNTER.set(0)
        self.EDESKTOP_MENU_INT = IntVar()
        self.EDESKTOP_MENU = StringVar()
        self.EDESKTOP_MENU.set("")
        self.EDESKTOP_BACK_INT = IntVar()
        self.EDESKTOP_BACK = StringVar()
        self.EDESKTOP_BACK.set("")
        self.EDESKTOP_FORWARD_INT = IntVar()
        self.EDESKTOP_FORWARD = StringVar()
        self.EDESKTOP_FORWARD.set("")
        self.EDESKTOP_PARENT_INT = IntVar()
        self.EDESKTOP_PARENT = StringVar()
        self.EDESKTOP_PARENT.set("")
        self.EDESKTOP_RELOAD_INT = IntVar()
        self.EDESKTOP_RELOAD = StringVar()
        self.EDESKTOP_RELOAD.set("")
        self.EDESKTOP_HOME_INT = IntVar()
        self.EDESKTOP_HOME = StringVar()
        self.EDESKTOP_HOME.set("")
        self.EDESKTOP_COMPUTER_INT = IntVar()
        self.EDESKTOP_COMPUTER = StringVar()
        self.EDESKTOP_COMPUTER.set("")
        self.EDESKTOP_NEWTAB_INT = IntVar()
        self.EDESKTOP_NEWTAB = StringVar()
        self.EDESKTOP_NEWTAB.set("")
        self.EDESKTOP_NEWWINDOW_INT = IntVar()
        self.EDESKTOP_NEWWINDOW = StringVar()
        self.EDESKTOP_NEWWINDOW.set("")
        self.EDESKTOP_SEARCH_INT = IntVar()
        self.EDESKTOP_SEARCH = StringVar()
        self.EDESKTOP_SEARCH.set("")
        self.EDESKTOP_LOCATION_INT = IntVar()
        self.EDESKTOP_LOCATION = StringVar()
        self.EDESKTOP_LOCATION.set("")
        self.EDESKTOP_MODE_INT = IntVar()
        self.EDESKTOP_MODE = StringVar()
        self.EDESKTOP_MODE.set("")

	self.rootpanel = Label(root, image=self.image1)
	self.rootpanel.pack(side=TOP, fill=BOTH, expand=YES)

	self.middlepanel = Label(self.rootpanel, image=self.image1)
	self.middlepanel.pack(side=TOP, expand=YES, fill=BOTH)

	self.bottompanel = Label(self.rootpanel, image=self.image2)
	self.bottompanel.pack(side=TOP, fill=BOTH)

	self.button2 = Button(self.middlepanel, text=WORD107, relief=RAISED, borderwidth=4, font=self.boldfont, image=self.image3, compound=RIGHT, command=self.forward_to_page_2, height=30)
	self.button2.pack(side=TOP, expand=YES)

	self.button1 = Button(self.bottompanel, text=WORD108, width=8, command=self.exit)
	self.button1.pack(side=LEFT, padx=10, pady=10)

	root.option_add('*tearOff', FALSE)
	self.menubar = Menu(root)
	self.menu_Presets = Menu(self.menubar)
	self.menubar.add_cascade(menu=self.menu_Presets, label=WORD109, state=DISABLED)
	self.menubar.add_command(label=WORD110, command=self.about)

	root.config(menu=self.menubar)

# Forward Progress: ====================================================================

    def forward_to_page_2(self):
	self.PAGE = "2"
	self.clear_screen()

        # Install Type:

	self.install_type_frame = Frame(self.middlepanel, relief=RAISED, borderwidth=4)
	self.install_type_frame.pack(pady=(75,10))

	self.install_type_header = Label(self.install_type_frame, text=WORD111, font=self.boldfont)
	self.install_type_header.grid(row=0, column=0, pady=3, padx=10, sticky=W)

	self.INSTALLTYPE.set(WORD551)

        if commands.getoutput('gconftool-2 --get /apps/win2-7pack/status') == "Installed":
	   self.install_type_menu = OptionMenu(self.install_type_frame, self.INSTALLTYPE, WORD551,WORD552,WORD553,WORD554)
	else:
	   self.install_type_menu = OptionMenu(self.install_type_frame, self.INSTALLTYPE, WORD551)
	self.install_type_menu["width"] = 45
	self.install_type_menu["anchor"] = W
	self.install_type_menu.grid(row=1, column=0, columnspan=2, padx=10, pady=3, sticky=N+S+E+W)

	self.install_type_help_button = Button(self.install_type_frame, image=self.image6, command=self.install_type_help)
	self.install_type_help_button.grid(row=0, column=1, ipadx=4, ipady=4, padx=10, pady=3, sticky=E)

        # Time And Date Format:

	self.local_format_frame = Frame(self.middlepanel, relief=RAISED, borderwidth=4)
	self.local_format_frame.pack(pady=10)

	self.local_format_header = Label(self.local_format_frame, text=WORD112, font=self.boldfont)
	self.local_format_header.grid(row=0, column=0, pady=3, padx=10, sticky=W)

	self.TIMEFORMAT.set(WORD556)

	self.local_format_menu = OptionMenu(self.local_format_frame, self.TIMEFORMAT, WORD556,WORD557,WORD558,WORD559)
	self.local_format_menu["width"] = 45
	self.local_format_menu["anchor"] = W
	self.local_format_menu.grid(row=1, column=0, columnspan=2, padx=10, pady=3, sticky=N+S+E+W)

	self.local_format_help_button = Button(self.local_format_frame, image=self.image6, command=self.time_and_date_help)
	self.local_format_help_button.grid(row=0, column=1, ipadx=4, ipady=4, padx=10, pady=3, sticky=E)

        # Restricted Extras:

	self.restricted_extras_frame = Frame(self.middlepanel, relief=RAISED, borderwidth=4)
	self.restricted_extras_frame.pack(pady=10)

	self.restricted_extras_header = Label(self.restricted_extras_frame, text=WORD113, font=self.boldfont)
	self.restricted_extras_header.grid(row=0, column=0, pady=3, padx=10, sticky=W)

        if RESTRICTEDEXTRAS == "Yes":
	   self.RESTRICTEDEXTRAS.set(WORD560)
	   self.restricted_extras_menu = OptionMenu(self.restricted_extras_frame, self.RESTRICTEDEXTRAS, WORD560)
        else:
	   self.RESTRICTEDEXTRAS.set(WORD555)
	   self.restricted_extras_menu = OptionMenu(self.restricted_extras_frame, self.RESTRICTEDEXTRAS, WORD555, WORD560)
	self.restricted_extras_menu["width"] = 45
	self.restricted_extras_menu["anchor"] = W
	self.restricted_extras_menu.grid(row=1, column=0, columnspan=2, padx=10, pady=3, sticky=N+S+E+W)

	self.restricted_extras_help_button = Button(self.restricted_extras_frame, image=self.image6, command=self.restricted_extras_help)
	self.restricted_extras_help_button.grid(row=0, column=1, ipadx=4, ipady=4, padx=10, pady=3, sticky=E)

	self.button4 = Button(self.bottompanel, text=WORD550, width=110, command=self.forward_to_page_3A, image=self.image7, compound=RIGHT)
	self.button4.pack(side=RIGHT, padx=10, pady=10)

	self.button2 = Button(self.bottompanel, text=WORD549, width=110, command=self.go_back, state=DISABLED, image=self.image8, compound=LEFT)
	self.button2.pack(side=RIGHT, padx=10, pady=10)

    def forward_to_page_3A(self):
	self.PAGE = "3A"
	self.clear_screen()

        if self.RESTRICTEDEXTRAS.get() == WORD560:
           self.button4.configure(command=self.forward_to_page_3B)
        else:
           if os.path.exists(BACKUP) == True:
              self.button4.configure(command=self.forward_to_page_5)
	   else:
              self.button4.configure(command=self.forward_to_page_4)

        self.CALL_EULA(WORD114 + "\n\n" + WORD115 + "\n\n" + WORD116 + "\n" + WORD117 + "\n" + WORD118 + "\n" + WORD119 + "\n" + WORD120 + "\n\n" + WORD121 + "\n" + "http://gnome-look.org/content/show.php/Win2-7+Pack?content=113264",WORD122)

    def forward_to_page_3B(self):
	self.PAGE = "3B"
	self.clear_screen()

	if os.path.exists(BACKUP) == True:
           self.button4.configure(command=self.forward_to_page_5)
        else:
           self.button4.configure(command=self.forward_to_page_4)

        self.CALL_EULA(WORD123 + "\n\n" + WORD124 + "\n\n" + WORD125,WORD126)

    def forward_to_page_4(self):
	self.PAGE = "4"
	self.clear_screen()

	self.main_frame = Frame(self.middlepanel, relief=RAISED, borderwidth=4)
	self.main_frame.place(in_=self.middlepanel, anchor="c", relx=.5, rely=.5)

	self.backup_header = Label(self.main_frame, text=WORD127, font=self.boldfont)
	self.backup_header.grid(row=0, column=0, padx=10, pady=3, sticky=W)

	self.backup_inner_frame = Frame(self.main_frame, relief=RAISED, borderwidth=1)
	self.backup_inner_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=(3,10))

	self.backup_header = Label(self.backup_inner_frame, text=WORD128 + " %s..." % (CURRENT_USER))
	self.backup_header.pack(side=TOP, padx=10, pady=10)

	self.button4.configure(state=DISABLED)
	self.button1.configure(state=DISABLED)

	root.update()

	sys.stdout.write("# \n")

        TERMINAL_STATUS(WORD129,"BUSY")
	os.mkdir(os.path.expanduser("~/.Win2-7_GUI_Backup"))
	os.mkdir(os.path.expanduser("~/.Win2-7_GUI_Backup/xmls"))
        RESOLVE_ERRORLEVEL()

	if PLYMOUTHTHEMEINSTALLED == "Yes":
           TERMINAL_STATUS(WORD130,"BUSY")
           os.system('ls -l /etc/alternatives/default.plymouth | tr -s " " | cut -d " " -f 10 > \"$HOME\"/.Win2-7_GUI_Backup/plymouth')
           RESOLVE_ERRORLEVEL()

        TERMINAL_STATUS(WORD131,"BUSY")
	os.system('gconftool-2 --dump /apps/gwd > \"$HOME\"/.Win2-7_GUI_Backup/xmls/Metacity_Gwd.xml')
	os.system('gconftool-2 --dump /apps/metacity/general > \"$HOME\"/.Win2-7_GUI_Backup/xmls/Metacity_General.xml')
        RESOLVE_ERRORLEVEL()

        TERMINAL_STATUS(WORD132,"BUSY")
	os.system('gconftool-2 --dump /apps/nautilus/desktop > \"$HOME\"/.Win2-7_GUI_Backup/xmls/Nautilus_Desktop.xml')
	os.system('gconftool-2 --dump /apps/nautilus/preferences > \"$HOME\"/.Win2-7_GUI_Backup/xmls/Nautilus_Preferences.xml')
	os.system('gconftool-2 --dump /apps/nautilus/sidebar_panels/tree > \"$HOME\"/.Win2-7_GUI_Backup/xmls/Nautilus_Tree.xml')
        RESOLVE_ERRORLEVEL()

        TERMINAL_STATUS(WORD133,"BUSY")
	if GDM == "2":
	   os.system('echo \"%s\" | sudo -S -p \"\" -u \"gdm\" gconftool-2 --dump /desktop/gnome/background > \"$HOME\"/.Win2-7_GUI_Backup/xmls/Gnome_GDM.xml' % (PASS))
	os.system('gconftool-2 --dump /apps/gnome-screensaver > \"$HOME\"/.Win2-7_GUI_Backup/xmls/Gnome_Screensaver.xml')
	os.system('gconftool-2 --dump /apps/gnome-session/options > \"$HOME\"/.Win2-7_GUI_Backup/xmls/Gnome_Options.xml')
	os.system('gconftool-2 --dump /apps/panel > \"$HOME\"/.Win2-7_GUI_Backup/xmls/Gnome_Panel.xml')
	os.system('gconftool-2 --dump /desktop/gnome/background > \"$HOME\"/.Win2-7_GUI_Backup/xmls/Gnome_Background.xml')
	os.system('gconftool-2 --dump /desktop/gnome/interface > \"$HOME\"/.Win2-7_GUI_Backup/xmls/Gnome_Interface.xml')
	os.system('gconftool-2 --dump /desktop/gnome/peripherals/mouse > \"$HOME\"/.Win2-7_GUI_Backup/xmls/Gnome_Mouse.xml')
	os.system('gconftool-2 --dump /desktop/gnome/sound > \"$HOME\"/.Win2-7_GUI_Backup/xmls/Gnome_Sound.xml')
	os.system('gconftool-2 --dump /desktop/gnome/url-handlers/mailto > \"$HOME\"/.Win2-7_GUI_Backup/xmls/Gnome_Mailto.xml')
        RESOLVE_ERRORLEVEL()

	if DOCKBARXINSTALLED == "Yes":
           TERMINAL_STATUS(WORD134,"BUSY")
	   os.system('gconftool-2 --dump /apps/dockbarx > \"$HOME\"/.Win2-7_GUI_Backup/xmls/DockBarX.xml')
           RESOLVE_ERRORLEVEL()

        TERMINAL_STATUS(WORD135,"BUSY")
	os.system('gconftool-2 --dump /apps/gnome-terminal/profiles/Default > \"$HOME\"/.Win2-7_GUI_Backup/xmls/Terminal.xml')
        RESOLVE_ERRORLEVEL()

	self.button4.configure(state=NORMAL)
	self.button1.configure(state=NORMAL)

        self.forward_to_page_5()

    def forward_to_page_5(self):
	self.PAGE = "5"
	self.clear_screen()

	self.button2.configure(state=DISABLED)

        self.button4.configure(command=self.install_essentials)

	self.main_frame = Frame(self.middlepanel, relief=RAISED, borderwidth=4)
	self.main_frame.place(in_=self.middlepanel, anchor="c", relx=.5, rely=.5)

	self.essentials_header = Label(self.main_frame, text=WORD136, font=self.boldfont)
	self.essentials_header.grid(row=0, column=0, columnspan=2, padx=10, pady=5, sticky=W)

	self.essentials_help_button = Button(self.main_frame, image=self.image6, command=self.essentials_help)
	self.essentials_help_button.grid(row=0, column=1, ipadx=4, ipady=4, padx=(10), pady=(3), sticky=E)

	self.essentials_recommended_box_frame = Frame(self.main_frame, relief=RAISED, borderwidth=1)
	self.essentials_recommended_box_frame.grid(row=2, column=0, columnspan=2,padx=10, pady=(0,10), sticky=N+S+E+W)

	self.essentials_aero_box_frame = Frame(self.main_frame, relief=RAISED, borderwidth=1)
	self.essentials_aero_box_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=(0,10), sticky=N+S+E+W)

	self.essentials_aero_header = Label(self.essentials_aero_box_frame, text=WORD137)
	self.essentials_aero_header.grid(row=0, column=0, columnspan=3, padx=10, pady=3, sticky=W)

        # Advanced True Aero:

	self.essentials_aero_engine_help_button = Button(self.essentials_aero_box_frame, image=self.image6, command=self.murrine_help)
	self.essentials_aero_engine_help_button.grid(row=1, column=0, ipadx=4, ipady=4, padx=(10,0), pady=3, sticky=W)

        self.MURRINE.set(0)
        if MURRINEINSTALLED == "Yes":
           self.essentials_cb5 = Checkbutton(self.essentials_aero_box_frame, text=WORD561 + " ", variable = self.MURRINE, image=self.image4, compound=RIGHT)
        else:
           self.essentials_cb5 = Checkbutton(self.essentials_aero_box_frame, text=WORD561 + " ", variable = self.MURRINE, image=self.image5, compound=RIGHT)
        self.essentials_cb5.grid(row=1, column=1, pady=3, padx=(0,10), sticky=W)

        # Fusion Icon:

	self.essentials_fusionicon_help_button = Button(self.essentials_aero_box_frame, image=self.image6, command=self.fusionicon_help)
	self.essentials_fusionicon_help_button.grid(row=2, column=0, ipadx=4, ipady=4, padx=(10,0), pady=3, sticky=W)

        self.COMPIZFUSIONICON.set(0)
        if FUSIONICONINSTALLED == "Yes":
           self.essentials_cb6 = Checkbutton(self.essentials_aero_box_frame, text=WORD562 + " ", variable = self.COMPIZFUSIONICON, image=self.image4, compound=RIGHT)
        else:
           self.essentials_cb6 = Checkbutton(self.essentials_aero_box_frame, text=WORD562 + " ", variable = self.COMPIZFUSIONICON, image=self.image5, compound=RIGHT)
        self.essentials_cb6.grid(row=2, column=1, pady=3, padx=(0,10), sticky=W)

        # CCSM:

	self.essentials_ccsm_help_button = Button(self.essentials_aero_box_frame, image=self.image6, command=self.ccsm_help)
	self.essentials_ccsm_help_button.grid(row=3, column=0, ipadx=4, ipady=4, padx=(10,0), pady=3, sticky=W)

        self.CCSM.set(0)
        if CCSMINSTALLED == "Yes":
           self.essentials_cb7 = Checkbutton(self.essentials_aero_box_frame, text=WORD563 + " ", variable = self.CCSM, image=self.image4, compound=RIGHT)
	else:
           self.essentials_cb7 = Checkbutton(self.essentials_aero_box_frame, text=WORD563 + " ", variable = self.CCSM, image=self.image5, compound=RIGHT)
        self.essentials_cb7.grid(row=3, column=1, pady=3, padx=(0,10), sticky=W)

        # Emerald:

	self.essentials_emerald_help_button = Button(self.essentials_aero_box_frame, image=self.image6, command=self.emerald_help)
	self.essentials_emerald_help_button.grid(row=4, column=0, ipadx=4, ipady=4, padx=(10,0), pady=3, sticky=W)

        self.EMERALD.set(0)
        if EMERALDINSTALLED == "Yes":
           self.essentials_cb8 = Checkbutton(self.essentials_aero_box_frame, text=WORD564 + " ", variable = self.EMERALD, image=self.image4, compound=RIGHT)
	else:
           self.essentials_cb8 = Checkbutton(self.essentials_aero_box_frame, text=WORD564 + " ", variable = self.EMERALD, image=self.image5, compound=RIGHT)
        self.essentials_cb8.grid(row=4, column=1, pady=3, padx=(0,10), sticky=W)

        # Elementry Nautilus:

	self.essentials_elementary_help_button = Button(self.essentials_aero_box_frame, image=self.image6, command=self.edesktop_help)
	self.essentials_elementary_help_button.grid(row=5, column=0, ipadx=4, ipady=4, padx=(10,0), pady=(3,6), sticky=W)

        self.ELEMENTRYN.set(0)
        if ELEMENTRYNINSTALLED == "Yes":
           self.essentials_cb9 = Checkbutton(self.essentials_aero_box_frame, text=WORD565 + " ", variable = self.ELEMENTRYN, image=self.image4, compound=RIGHT)
	else:
           self.essentials_cb9 = Checkbutton(self.essentials_aero_box_frame, text=WORD565 + " ", variable = self.ELEMENTRYN, image=self.image5, compound=RIGHT)
        self.essentials_cb9.grid(row=5, column=1, columnspan=3, pady=(3,6), padx=(0,10), sticky=W)

        # DockbarX:

	self.essentials_dockbarx_help_button = Button(self.essentials_recommended_box_frame, image=self.image6, command=self.dockbarx_help)
	self.essentials_dockbarx_help_button.grid(row=0, column=0, ipadx=4, ipady=4, padx=(10,0), pady=(6,3), sticky=W)

        self.DOCKBARX.set(0)
        if DOCKBARXINSTALLED == "Yes":
           self.essentials_cb1 = Checkbutton(self.essentials_recommended_box_frame, text=WORD566 + " ", variable = self.DOCKBARX, image=self.image4, compound=RIGHT)
        else:
           self.essentials_cb1 = Checkbutton(self.essentials_recommended_box_frame, text=WORD566 + " ", variable = self.DOCKBARX, image=self.image5, compound=RIGHT)
        self.essentials_cb1.grid(row=0, column=1, pady=(6,3), padx=(0,10), sticky=W)

        # Emesene:

	self.essentials_emesene_help_button = Button(self.essentials_recommended_box_frame, image=self.image6, command=self.emesene_help)
	self.essentials_emesene_help_button.grid(row=1, column=0, ipadx=4, ipady=4, padx=(10,5), pady=3, sticky=W)

        self.EMESENE.set(0)
        if EMESENEINSTALLED == "Yes":
           self.essentials_cb3 = Checkbutton(self.essentials_recommended_box_frame, text=WORD567 + " ", variable = self.EMESENE, image=self.image4, compound=RIGHT)
	else:
           self.essentials_cb3 = Checkbutton(self.essentials_recommended_box_frame, text=WORD567 + " ", variable = self.EMESENE, image=self.image5, compound=RIGHT)
        self.essentials_cb3.grid(row=1, column=1, pady=3, padx=(0,10), sticky=W)

        # Gnomenu:

	self.essentials_gnomenu_help_button = Button(self.essentials_recommended_box_frame, image=self.image6, command=self.gnomenu_help)
	self.essentials_gnomenu_help_button.grid(row=2, column=0, ipadx=4, ipady=4, padx=(10,5), pady=3, sticky=W)

        self.GNOMENU.set(0)
        if GNOMENUINSTALLED == "Yes":
           self.essentials_cb2 = Checkbutton(self.essentials_recommended_box_frame, text=WORD568 + " ", variable = self.GNOMENU, image=self.image4, compound=RIGHT)
	else:
           self.essentials_cb2 = Checkbutton(self.essentials_recommended_box_frame, text=WORD568 + " ", variable = self.GNOMENU, image=self.image5, compound=RIGHT)
        self.essentials_cb2.grid(row=2, column=1, pady=3, padx=(0,10), sticky=W)

        # Screenlets:

	self.essentials_screenlets_help_button = Button(self.essentials_recommended_box_frame, image=self.image6, command=self.screenlets_help)
	self.essentials_screenlets_help_button.grid(row=3, column=0, ipadx=4, ipady=4, padx=(10,5), pady=(3,6), sticky=W)

        self.SCREENLETS.set(0)
        if SCREENLETSINSTALLED == "Yes":
           self.essentials_cb4 = Checkbutton(self.essentials_recommended_box_frame, text=WORD569 + " ", variable = self.SCREENLETS, image=self.image4, compound=RIGHT)
	else:
           self.essentials_cb4 = Checkbutton(self.essentials_recommended_box_frame, text=WORD569 + " ", variable = self.SCREENLETS, image=self.image5, compound=RIGHT)
        self.essentials_cb4.grid(row=3, column=1, columnspan=3, pady=(3,6), padx=(0,10), sticky=W)

	if INTERNETSTATUS == "Not Connected":
	   self.essentials_cb1.configure(state=DISABLED)
	   self.essentials_dockbarx_help_button.configure(state=DISABLED)
	   self.essentials_cb2.configure(state=DISABLED)
	   self.essentials_gnomenu_help_button.configure(state=DISABLED)
	   self.essentials_cb3.configure(state=DISABLED)
	   self.essentials_emesene_help_button.configure(state=DISABLED)
	   self.essentials_cb4.configure(state=DISABLED)
	   self.essentials_screenlets_help_button.configure(state=DISABLED)
	   self.essentials_cb5.configure(state=DISABLED)
	   self.essentials_aero_engine_help_button.configure(state=DISABLED)
	   self.essentials_cb6.configure(state=DISABLED)
	   self.essentials_fusionicon_help_button.configure(state=DISABLED)
	   self.essentials_cb7.configure(state=DISABLED)
	   self.essentials_ccsm_help_button.configure(state=DISABLED)
	   self.essentials_cb8.configure(state=DISABLED)
	   self.essentials_emerald_help_button.configure(state=DISABLED)
	   self.essentials_cb9.configure(state=DISABLED)
	   self.essentials_elementary_help_button.configure(state=DISABLED)
	   showwarning(title=WORD44, message=WORD138)
   
        if UVERSION == "Mandriva":
	   self.essentials_cb5.configure(state=DISABLED)
	   self.essentials_aero_engine_help_button.configure(state=DISABLED)

	elif (UVERSION == "Ubuntu114") or (UVERSION == "Mint11"):
	   self.essentials_cb2.configure(state=DISABLED)
	   self.essentials_gnomenu_help_button.configure(state=DISABLED)
	   self.essentials_cb5.configure(state=DISABLED)
	   self.essentials_aero_engine_help_button.configure(state=DISABLED)

        elif (UVERSION == "Fedora") or (UVERSION == "Ubuntu94") or (UVERSION == "Ubuntu910"):
	   self.essentials_cb5.configure(state=DISABLED)
	   self.essentials_aero_engine_help_button.configure(state=DISABLED)
	   self.essentials_cb9.configure(state=DISABLED)
	   self.essentials_elementary_help_button.configure(state=DISABLED)

        elif UVERSION == "PCLinuxOS":
	   self.essentials_cb5.configure(state=DISABLED)
	   self.essentials_aero_engine_help_button.configure(state=DISABLED)
	   self.essentials_cb9.configure(state=DISABLED)
	   self.essentials_elementary_help_button.configure(state=DISABLED)
	   self.essentials_cb1.configure(state=DISABLED)
	   self.essentials_dockbarx_help_button.configure(state=DISABLED)
	   self.essentials_cb2.configure(state=DISABLED)
	   self.essentials_gnomenu_help_button.configure(state=DISABLED)

        elif UVERSION == "openSUSE":
	   self.essentials_cb1.configure(state=DISABLED)
	   self.essentials_dockbarx_help_button.configure(state=DISABLED)
	   self.essentials_cb2.configure(state=DISABLED)
	   self.essentials_gnomenu_help_button.configure(state=DISABLED)
	   self.essentials_cb3.configure(state=DISABLED)
	   self.essentials_emesene_help_button.configure(state=DISABLED)
	   self.essentials_cb4.configure(state=DISABLED)
	   self.essentials_screenlets_help_button.configure(state=DISABLED)
	   self.essentials_cb5.configure(state=DISABLED)
	   self.essentials_aero_engine_help_button.configure(state=DISABLED)
	   self.essentials_cb6.configure(state=DISABLED)
	   self.essentials_fusionicon_help_button.configure(state=DISABLED)
	   self.essentials_cb8.configure(state=DISABLED)
	   self.essentials_emerald_help_button.configure(state=DISABLED)
	   self.essentials_cb9.configure(state=DISABLED)
	   self.essentials_elementary_help_button.configure(state=DISABLED)

        elif UVERSION == "Debian":
	   self.essentials_cb1.configure(state=DISABLED)
	   self.essentials_dockbarx_help_button.configure(state=DISABLED)
	   self.essentials_cb2.configure(state=DISABLED)
	   self.essentials_gnomenu_help_button.configure(state=DISABLED)
	   self.essentials_cb5.configure(state=DISABLED)
	   self.essentials_aero_engine_help_button.configure(state=DISABLED)
	   self.essentials_cb8.configure(state=DISABLED)
	   self.essentials_emerald_help_button.configure(state=DISABLED)
	   self.essentials_cb9.configure(state=DISABLED)
	   self.essentials_elementary_help_button.configure(state=DISABLED)

        elif UVERSION == "CentOS":
	   self.essentials_cb1.configure(state=DISABLED)
	   self.essentials_dockbarx_help_button.configure(state=DISABLED)
	   self.essentials_cb2.configure(state=DISABLED)
	   self.essentials_gnomenu_help_button.configure(state=DISABLED)
	   self.essentials_cb3.configure(state=DISABLED)
	   self.essentials_emesene_help_button.configure(state=DISABLED)
	   self.essentials_cb4.configure(state=DISABLED)
	   self.essentials_screenlets_help_button.configure(state=DISABLED)
	   self.essentials_cb5.configure(state=DISABLED)
	   self.essentials_aero_engine_help_button.configure(state=DISABLED)
	   self.essentials_cb6.configure(state=DISABLED)
	   self.essentials_fusionicon_help_button.configure(state=DISABLED)
	   self.essentials_cb7.configure(state=DISABLED)
	   self.essentials_ccsm_help_button.configure(state=DISABLED)
	   self.essentials_cb8.configure(state=DISABLED)
	   self.essentials_emerald_help_button.configure(state=DISABLED)
	   self.essentials_cb9.configure(state=DISABLED)
	   self.essentials_elementary_help_button.configure(state=DISABLED)
	   showwarning(title=WORD44, message=WORD570)

        elif NOTCERTIFIED == "Yes":
	   self.essentials_cb1.configure(state=DISABLED)
	   self.essentials_dockbarx_help_button.configure(state=DISABLED)
	   self.essentials_cb2.configure(state=DISABLED)
	   self.essentials_gnomenu_help_button.configure(state=DISABLED)
	   self.essentials_cb3.configure(state=DISABLED)
	   self.essentials_emesene_help_button.configure(state=DISABLED)
	   self.essentials_cb4.configure(state=DISABLED)
	   self.essentials_screenlets_help_button.configure(state=DISABLED)
	   self.essentials_cb5.configure(state=DISABLED)
	   self.essentials_aero_engine_help_button.configure(state=DISABLED)
	   self.essentials_cb6.configure(state=DISABLED)
	   self.essentials_fusionicon_help_button.configure(state=DISABLED)
	   self.essentials_cb7.configure(state=DISABLED)
	   self.essentials_ccsm_help_button.configure(state=DISABLED)
	   self.essentials_cb8.configure(state=DISABLED)
   	   self.essentials_emerald_help_button.configure(state=DISABLED)
      	   self.essentials_cb9.configure(state=DISABLED)
   	   self.essentials_elementary_help_button.configure(state=DISABLED)
	   showwarning(title=WORD44, message=WORD139)

    def forward_to_page_5B(self):
	self.PAGE = "5B"
	self.clear_screen()

	self.button2.configure(state=DISABLED)
	self.button1.configure(state=DISABLED)
        self.button4.configure(state=DISABLED)

	self.main_frame = Frame(self.middlepanel, relief=RAISED, borderwidth=4)
	self.main_frame.place(in_=self.middlepanel, anchor="c", relx=.5, rely=.5)

	self.essentials_install_header = Label(self.main_frame, text=WORD140, font=self.boldfont)
	self.essentials_install_header.grid(row=0, column=0, padx=10, sticky=W)

	self.essentials_install_inner_frame = Frame(self.main_frame, relief=RAISED, borderwidth=1)
	self.essentials_install_inner_frame.grid(row=1, column=0, columnspan=2, sticky=N+S+E+W, padx=10, pady=(0,10))

	self.essentials_install_header2 = Label(self.essentials_install_inner_frame, text=WORD141)
	self.essentials_install_header2.pack(pady=10, padx=10)

	sys.stdout.write("# \n")

	root.update()

        CHECK_PROGRAM_LOCKS()

	self.SOFTWARE_SOURCES()

	# Prep System:
	
	if (UVERSION == "Mandriva") and (self.ELEMENTRYN.get() != 0) and (ELEMENTRYNINSTALLED != "Yes"):
           self.EDESKTOP_INSTALL.set("Yes")
	elif (self.ELEMENTRYN.get() != 0) and (ELEMENTRYNINSTALLED != "Yes"):
           TERMINAL_STATUS(WORD142,"BUSY")
           if os.system('echo \"%s\" | sudo -S -p \"\" apt-get upgrade -s > /tmp/upgrade.tmp' % (PASS)) == 0:
	      if sum(1 for line in open('/tmp/upgrade.tmp')) != 4:
                 TERMINAL_STATUS_WARN()
		 RESPONSE = PyZenity.Question(title=WORD88, text=WORD143, ok_label=WORD144, cancel_label=WORD145)
		 root.update()
		 if RESPONSE == True:
                    sys.stdout.write(WORD146 + "\n" + "\n")
                    sys.stdout.flush()
                    if (UVERSION == "Mint9") or (UVERSION == "Mint10") or (UVERSION == "Mint11"):
                       os.system('bash Files/modules/mintupdate.sh \"%s\"' % (PASS))
                       self.EDESKTOP_INSTALL.set("Yes")
                       sys.stdout.write("\n")
                       sys.stdout.flush()
                    else:
		       if os.system('echo \"%s\" | sudo -S -p \"\" apt-get -y upgrade' % (PASS)) == 0:
		          self.EDESKTOP_INSTALL.set("Yes")
                          sys.stdout.write("\n")
                          sys.stdout.flush()
#                         TERMINAL_STATUS_PASS()
		       else:
#                         TERMINAL_STATUS_FAIL()
                          RESPONSE = PyZenity.Warning(WORD147, title=WORD44)
			  CHECK_FOR_CANCEL()
	      else:
	         self.EDESKTOP_INSTALL.set("Yes")
                 TERMINAL_STATUS_PASS()
	   else:
              TERMINAL_STATUS_FAIL()
              RESPONSE = PyZenity.Warning(WORD148, title=WORD44)
	      CHECK_FOR_CANCEL()

	# Add Fedora Repository and key: 
	if (UVERSION == "Fedora") and (os.path.exists('/etc/yum.repos.d/win2-7.repo') == False) and ((self.DOCKBARX.get() != 0) or (self.GNOMENU.get() != 0) or (self.SCREENLETS.get() != 0)):
           TERMINAL_STATUS(WORD149,"BUSY")
	   ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" cp Files/keys/RPM-GPG-KEY-cert-forensics.asc /etc/pki/rpm-gpg/RPM-GPG-KEY-cert-forensics > /dev/null 2>&1' % (PASS)) ; STATUSCHECK
	   ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-cert-forensics > /dev/null 2>&1' % (PASS)) ; STATUSCHECK
	   RESOLVE_ERRORLEVEL()
           TERMINAL_STATUS(WORD150,"BUSY")
	   ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" bash -c \'echo \"[win2-7]\" > /etc/yum.repos.d/win2-7.repo\'' % (PASS)) ; STATUSCHECK
	   ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" bash -c \'echo \"name=CERT Forensics Win2-7 Repository\" >> /etc/yum.repos.d/win2-7.repo\'' % (PASS)) ; STATUSCHECK
	   ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" bash -c \'echo \"baseurl=http://www.cert.org/forensics/repository/fedora/win2-7/\\$releasever/\\$basearch\" >> /etc/yum.repos.d/win2-7.repo\'' % (PASS)) ; STATUSCHECK
	   ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" bash -c \'echo \"enabled=1\" >> /etc/yum.repos.d/win2-7.repo\'' % (PASS)) ; STATUSCHECK
	   ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" bash -c \'echo \"gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-cert-forensics\" >> /etc/yum.repos.d/win2-7.repo\'' % (PASS)) ; STATUSCHECK
	   ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" bash -c \'echo \"gpgcheck=1\" >> /etc/yum.repos.d/win2-7.repo\'' % (PASS)) ; STATUSCHECK
	   RESOLVE_ERRORLEVEL()

	# Scan Software Sources: 
	if (os.path.exists('/etc/apt/sources.list') == True) and (PMAN == "APT"):
           TERMINAL_STATUS(WORD151,"BUSY")
           readfile = open('/etc/apt/sources.list','r')
           line = readfile.readline()
           while line:
              if "dockbar-main" in line:
	         self.DOCKBAR_REP.set("Yes")
              if "gnomenu-team" in line:
	         self.GNOMENU_REP.set("Yes")
              line = readfile.readline()
           readfile.close()
	   RESOLVE_ERRORLEVEL()

	# Add DockbarX Repository and key:
	if (PMAN == "APT") and (self.DOCKBAR_REP.get() != "Yes") and (self.DOCKBARX.get() != 0):
           TERMINAL_STATUS(WORD152,"BUSY")
	   if UVERSION == "Mint11":
	      ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" bash -c \'echo \"deb http://ppa.launchpad.net/dockbar-main/ppa/ubuntu natty main\" >> /etc/apt/sources.list\'' % (PASS)) ; STATUSCHECK
	   elif UVERSION == "Mint10":
	      ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" bash -c \'echo \"deb http://ppa.launchpad.net/dockbar-main/ppa/ubuntu maverick main\" >> /etc/apt/sources.list\'' % (PASS)) ; STATUSCHECK
	   elif UVERSION == "Mint9":
	      ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" bash -c \'echo \"deb http://ppa.launchpad.net/dockbar-main/ppa/ubuntu lucid main\" >> /etc/apt/sources.list\'' % (PASS)) ; STATUSCHECK
	   elif UVERSION == "Ubuntu114":
	      ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" bash -c \'echo \"deb http://ppa.launchpad.net/dockbar-main/ppa/ubuntu natty main\" >> /etc/apt/sources.list\'' % (PASS)) ; STATUSCHECK
	   elif UVERSION == "Ubuntu1010":
	      ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" bash -c \'echo \"deb http://ppa.launchpad.net/dockbar-main/ppa/ubuntu maverick main\" >> /etc/apt/sources.list\'' % (PASS)) ; STATUSCHECK
	   elif UVERSION == "Ubuntu104":
	      ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" bash -c \'echo \"deb http://ppa.launchpad.net/dockbar-main/ppa/ubuntu lucid main\" >> /etc/apt/sources.list\'' % (PASS)) ; STATUSCHECK
	   elif UVERSION == "Ubuntu910":
	      ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" bash -c \'echo \"deb http://ppa.launchpad.net/dockbar-main/ppa/ubuntu karmic main\" >> /etc/apt/sources.list\'' % (PASS)) ; STATUSCHECK
	   elif UVERSION == "Ubuntu94":
	      ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" bash -c \'echo \"deb http://ppa.launchpad.net/dockbar-main/ppa/ubuntu jaunty main\" >> /etc/apt/sources.list\'' % (PASS)) ; STATUSCHECK
	   RESOLVE_ERRORLEVEL()
           TERMINAL_STATUS(WORD153,"BUSY")
	   ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" apt-key add Files/keys/dockbarx.asc > /dev/null 2>&1' % (PASS)) ; STATUSCHECK
	   self.USS.set("YES")
	   RESOLVE_ERRORLEVEL()

	# Add Gnomenu Repository and key:
	if (PMAN == "APT") and (self.GNOMENU_REP.get() != "Yes") and (self.GNOMENU.get() != 0):
           TERMINAL_STATUS(WORD154,"BUSY")
	   if UVERSION == "Mint10":
	      ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" bash -c \'echo \"deb http://ppa.launchpad.net/gnomenu-team/ppa/ubuntu maverick main\" >> /etc/apt/sources.list\'' % (PASS)) ; STATUSCHECK
	   elif UVERSION == "Mint9":
	      ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" bash -c \'echo \"deb http://ppa.launchpad.net/gnomenu-team/ppa/ubuntu lucid main\" >> /etc/apt/sources.list\'' % (PASS)) ; STATUSCHECK
	   elif UVERSION == "Ubuntu1010":
	      ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" bash -c \'echo \"deb http://ppa.launchpad.net/gnomenu-team/ppa/ubuntu maverick main\" >> /etc/apt/sources.list\'' % (PASS)) ; STATUSCHECK
	   elif UVERSION == "Ubuntu104":
	      ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" bash -c \'echo \"deb http://ppa.launchpad.net/gnomenu-team/ppa/ubuntu lucid main\" >> /etc/apt/sources.list\'' % (PASS)) ; STATUSCHECK
	   elif UVERSION == "Ubuntu910":
	      ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" bash -c \'echo \"deb http://ppa.launchpad.net/gnomenu-team/ppa/ubuntu karmic main\" >> /etc/apt/sources.list\'' % (PASS)) ; STATUSCHECK
	   elif UVERSION == "Ubuntu94":
	      ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" bash -c \'echo \"deb http://ppa.launchpad.net/gnomenu-team/ppa/ubuntu jaunty main\" >> /etc/apt/sources.list\'' % (PASS)) ; STATUSCHECK
	   RESOLVE_ERRORLEVEL()
           TERMINAL_STATUS(WORD155,"BUSY")
	   ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" apt-key add Files/keys/gnomenu.asc > /dev/null 2>&1' % (PASS)) ; STATUSCHECK
	   self.USS.set("YES")
	   RESOLVE_ERRORLEVEL()

	# Add Elementary Desktop and key:

	if (ELEMENTRYNINSTALLED == "No") and (self.EDESKTOP_INSTALL.get() == "Yes"):
           TERMINAL_STATUS(WORD156,"BUSY")
	   if UVERSION == "Mint11":
	      ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" bash -c \'echo \"deb http://ppa.launchpad.net/elementaryart/elementarydesktop/ubuntu natty main\" >> /etc/apt/sources.list\'' % (PASS)) ; STATUSCHECK
	   elif UVERSION == "Mint10":
	      ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" bash -c \'echo \"deb http://ppa.launchpad.net/elementaryart/elementarydesktop/ubuntu maverick main\" >> /etc/apt/sources.list\'' % (PASS)) ; STATUSCHECK
	   elif UVERSION == "Mint9":
	      ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" bash -c \'echo \"deb http://ppa.launchpad.net/elementaryart/elementarydesktop/ubuntu lucid main\" >> /etc/apt/sources.list\'' % (PASS)) ; STATUSCHECK
	   elif UVERSION == "Ubuntu114":
	      ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" bash -c \'echo \"deb http://ppa.launchpad.net/elementaryart/elementarydesktop/ubuntu natty main\" >> /etc/apt/sources.list\'' % (PASS)) ; STATUSCHECK
	   elif UVERSION == "Ubuntu1010":
	      ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" bash -c \'echo \"deb http://ppa.launchpad.net/elementaryart/elementarydesktop/ubuntu maverick main\" >> /etc/apt/sources.list\'' % (PASS)) ; STATUSCHECK
	   elif UVERSION == "Ubuntu104":
	      ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" bash -c \'echo \"deb http://ppa.launchpad.net/elementaryart/elementarydesktop/ubuntu lucid main\" >> /etc/apt/sources.list\'' % (PASS)) ; STATUSCHECK
	   elif UVERSION == "Mandriva":
	      ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" urpmi.addmedia mvt-free ftp://ftp.linux.org.tr/pub/mandriva-tr/2010.1/%s/free with media_info/synthesis.hdlist.cz > /dev/null 2>&1' % (PASS,MANDRIVAARCH)) ; STATUSCHECK
	      ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" urpmi.addmedia mvt-non-free ftp://ftp.linux.org.tr/pub/mandriva-tr/2010.1/%s/non-free with media_info/synthesis.hdlist.cz > /dev/null 2>&1' % (PASS,MANDRIVAARCH)) ; STATUSCHECK
	   self.USS.set("YES")
	   RESOLVE_ERRORLEVEL()
           if UVERSION != "Mandriva":
              TERMINAL_STATUS(WORD157,"BUSY")
	      ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" apt-key add Files/keys/ElementaryDesktop.asc > /dev/null 2>&1' % (PASS)) ; STATUSCHECK
	      RESOLVE_ERRORLEVEL()

	# Update Software Sources:

	if self.USS.get() == "YES":
	   self.SOFTWARE_SOURCES()

	# Install

	self.essentials_install_header2.configure(text=WORD158)

	root.update()

	if (self.CCSM.get() != 0) and (CCSMINSTALLED != "Yes"):
           if PMAN == "APT":
	      TERMINAL_STATUS(WORD159,"BUSY")
	      ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" apt-get -y --download-only install compizconfig-settings-manager >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
              RESOLVE_ERRORLEVEL()
	      TERMINAL_STATUS(WORD160,"BUSY")
	      ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" apt-get -y --no-download install compizconfig-settings-manager >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
	   elif PMAN == "YUM":
	      TERMINAL_STATUS(WORD161,"BUSY")
	      ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" yum -y install ccsm >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
	   elif PMAN == "URPMI":
	      TERMINAL_STATUS(WORD161,"BUSY")
	      ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" urpmi --auto --quiet --force ccsm >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
	   elif PMAN == "ZYPPER":
	      TERMINAL_STATUS(WORD161,"BUSY")
	      ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" zypper install -y compizconfig-settings-manager >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
           RESOLVE_ERRORLEVEL()

	if (self.DOCKBARX.get() != 0) and (DOCKBARXINSTALLED != "Yes"):
           if PMAN == "APT":
	      TERMINAL_STATUS(WORD162,"BUSY")
	      ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" apt-get -y --download-only install dockbarx >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
              RESOLVE_ERRORLEVEL()
	      TERMINAL_STATUS(WORD163,"BUSY")
	      ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" apt-get -y --no-download install dockbarx >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
	   elif PMAN == "YUM":
	      TERMINAL_STATUS(WORD164,"BUSY")
	      ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" yum -y install dockbarx >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
           RESOLVE_ERRORLEVEL()

	if (self.EMERALD.get() != 0) and (EMERALDINSTALLED != "Yes"):
           if PMAN == "APT":
	      TERMINAL_STATUS(WORD165,"BUSY")
	      ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" apt-get -y --download-only install emerald >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
              RESOLVE_ERRORLEVEL()
	      TERMINAL_STATUS(WORD166,"BUSY")
	      ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" apt-get -y --no-download install emerald >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
	   elif PMAN == "YUM":
	      TERMINAL_STATUS(WORD167,"BUSY")
	      ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" yum -y install emerald >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
	   elif PMAN == "URPMI":
	      TERMINAL_STATUS(WORD167,"BUSY")
	      ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" urpmi --auto --quiet --force emerald >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
           RESOLVE_ERRORLEVEL()

	if (self.EMESENE.get() != 0) and (EMESENEINSTALLED != "Yes"):
           if PMAN == "APT":
	      TERMINAL_STATUS(WORD168,"BUSY")
	      ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" apt-get -y --download-only install emesene >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
              RESOLVE_ERRORLEVEL()
	      TERMINAL_STATUS(WORD169,"BUSY")
	      ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" apt-get -y --no-download install emesene >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
	   elif PMAN == "YUM":
	      TERMINAL_STATUS(WORD170,"BUSY")
	      ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" yum -y install emesene >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
	   elif PMAN == "URPMI":
	      TERMINAL_STATUS(WORD170,"BUSY")
	      ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" urpmi --auto --quiet --force emesene >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
           RESOLVE_ERRORLEVEL()

	if (self.COMPIZFUSIONICON.get() != 0) and (FUSIONICONINSTALLED != "Yes"):
           if PMAN == "APT":
	      TERMINAL_STATUS(WORD171,"BUSY")
	      ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" apt-get -y --download-only install fusion-icon >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
              RESOLVE_ERRORLEVEL()
	      TERMINAL_STATUS(WORD172,"BUSY")
	      ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" apt-get -y --no-download install fusion-icon >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
	   elif PMAN == "YUM":
	      TERMINAL_STATUS(WORD173,"BUSY")
	      ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" yum -y install fusion-icon >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
	   elif PMAN == "URPMI":
	      TERMINAL_STATUS(WORD173,"BUSY")
	      ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" urpmi --auto --quiet --force fusion-icon >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
           RESOLVE_ERRORLEVEL()


	if (self.GNOMENU.get() != 0) and (GNOMENUINSTALLED != "Yes"):
           if PMAN == "APT":
	      TERMINAL_STATUS(WORD174,"BUSY")
	      ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" apt-get -y --download-only install gnomenu >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
              RESOLVE_ERRORLEVEL()
	      TERMINAL_STATUS(WORD175,"BUSY")
	      ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" apt-get -y --no-download install gnomenu >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
	   elif PMAN == "YUM":
	      TERMINAL_STATUS(WORD176,"BUSY")
	      ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" yum -y install gnomenu >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
           RESOLVE_ERRORLEVEL()

	if (self.SCREENLETS.get() != 0) and (SCREENLETSINSTALLED != "Yes"):
           if PMAN == "APT":
	      TERMINAL_STATUS(WORD177,"BUSY")
	      ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" apt-get -y --download-only install screenlets >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
              RESOLVE_ERRORLEVEL()
	      TERMINAL_STATUS(WORD178,"BUSY")
	      ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" apt-get -y --no-download install screenlets >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
	   elif PMAN == "URPMI":
	      TERMINAL_STATUS(WORD179,"BUSY")
	      ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" urpmi --auto --quiet --force screenlets >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
	   elif PMAN == "YUM":
	      TERMINAL_STATUS(WORD179,"BUSY")
	      ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" yum -y install screenlets >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
           RESOLVE_ERRORLEVEL()

	if (self.MURRINE.get() != 0) and (MURRINEINSTALLED != "Yes"):
           if MURRINEHOLD == "Yes":
              RESPONSE = PyZenity.Warning(WORD180, title=WORD44)
              ABORT()
	   TERMINAL_STATUS(WORD181,"BUSY")
           if UVERSION == "Mint9":
	      ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" dpkg -i Files/debs/10.04/gtk2-engines-murrine_Win2-7Pack_0.90.3+git20100323-1_%s.deb >> /dev/null 2>&1' % (PASS,MURRINE_ARCH)) ; STATUSCHECK
	   elif UVERSION == "Mint10":
	      ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" dpkg -i Files/debs/10.10/gtk2-engines-murrine_0.98.1.1-1_%s.deb >> /dev/null 2>&1' % (PASS,MURRINE_ARCH)) ; STATUSCHECK
	   elif UVERSION == "Ubuntu104":
	      ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" dpkg -i Files/debs/10.04/gtk2-engines-murrine_Win2-7Pack_0.90.3+git20100323-1_%s.deb >> /dev/null 2>&1' % (PASS,MURRINE_ARCH)) ; STATUSCHECK
	   elif UVERSION == "Ubuntu1010":
	      ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" dpkg -i Files/debs/10.10/gtk2-engines-murrine_0.98.1.1-1_%s.deb >> /dev/null 2>&1' % (PASS,MURRINE_ARCH)) ; STATUSCHECK
           os.system('gconftool-2 --set /apps/win2-7pack/advanced_murrine_installed --type string Yes')
           RESOLVE_ERRORLEVEL()

        if self.EDESKTOP_INSTALL.get() == "Yes":
	   if PMAN == "APT":
              sys.stdout.write(WORD182 + "\n" + "\n")
              sys.stdout.flush()
	      ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" apt-get -y upgrade' % (PASS)) ; STATUSCHECK
              sys.stdout.write("\n")
              sys.stdout.flush()
#	      RESOLVE_ERRORLEVEL()
	      if (UVERSION == "Ubuntu1010") or (UVERSION == "Ubuntu114") or (UVERSION == "Mint11"):
                 sys.stdout.write(WORD183 + "\n" + "\n")
                 sys.stdout.flush()
	         ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" aptitude -y upgrade' % (PASS)) ; STATUSCHECK
                 sys.stdout.write("\n")
                 sys.stdout.flush()
#		 RESOLVE_ERRORLEVEL()
	   elif PMAN == "URPMI":
	      TERMINAL_STATUS(WORD184,"BUSY")
	      ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" urpmi --auto --quiet --force nautilus-elementary >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
              RESOLVE_ERRORLEVEL()
	      if STANDARDMURRINEINSTALLED == "No":
	         TERMINAL_STATUS(WORD183,"BUSY")
	         ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" urpmi --auto --quiet --force murrine >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
		 RESOLVE_ERRORLEVEL()

	   TERMINAL_STATUS(WORD185,"BUSY")
	   ERRORLEVEL = os.system('killall nautilus > /dev/null 2>&1') ; STATUSCHECK
	   time.sleep(10)
	   RESOLVE_ERRORLEVEL()

	self.essentials_install_header2.configure(text=WORD186)

	root.update()

	INSTALLED_PROGRAMS()

	self.SOFTWARE_SOURCES()

	# Offer to place hold on Advanced Murrine:
	if (MURRINEHOLD != "Yes") and (MURRINEINSTALLED == "Yes"):
           if askyesno(title = WORD187, message = WORD187):
	      TERMINAL_STATUS(WORD188,"BUSY")
	      ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" echo gtk2-engines-murrine hold | sudo dpkg --set-selections' % (PASS)) ; STATUSCHECK
	      RESOLVE_ERRORLEVEL()

        self.button4.configure(state=NORMAL)
	self.button1.configure(state=NORMAL)
	
	self.setup_presets_toolbar()

    def setup_presets_toolbar(self):

	self.menubar.delete(0, END)

	self.menubar.add_cascade(menu=self.menu_Presets, label=WORD109)
	if ELEMENTRYNINSTALLED == "Yes":
	   self.menu_Presets.add_command(label=WORD189, command=self.Preset_aero)
	else:
	   self.menu_Presets.add_command(label=WORD189, state=DISABLED)
	self.menu_Presets.add_command(label=WORD190, command=self.Preset_basic)
	self.menu_Presets.add_command(label=WORD191, command=self.Preset_classic)
	self.menu_Presets.add_command(label=WORD192, command=self.Preset_original)

	self.menubar.add_command(label=WORD193, command=self.about)

        # Set static Variables:

	self.SUPERBAR.set(WORD571)
	if GVFSBININSTALLED == "Yes":
	   self.DESK.set(WORD572)
        else:
	   self.DESK.set(WORD573)
	self.ALLWORKSPACES.set(WORD574)

	if DOCKBARXINSTALLED == "Yes":
	   self.WINMAN.set(WORD575)
	else:
	   self.WINMAN.set(WORD576)

	if self.RESTRICTEDEXTRAS.get() == WORD560:
	   self.PLYMOUTHTHEME.set(WORD577)
	else:
	   self.PLYMOUTHTHEME.set(WORD578)

	if self.RESTRICTEDEXTRAS.get() == WORD560:
	   self.ICONBRAND.set(WORD579)
	else:
	   self.ICONBRAND.set(WORD580)

	if self.RESTRICTEDEXTRAS.get() == WORD560:
	   self.WALLPAPERNAME.set(WORD579)
	else:
	   self.WALLPAPERNAME.set(WORD580)

	if self.RESTRICTEDEXTRAS.get() == WORD560:
	   self.STARTUP.set(WORD577)
	else:
	   self.STARTUP.set(WORD581)

	if ELEMENTRYNINSTALLED == "Yes":
	   self.Preset_aero()
	else:
	   self.Preset_original()

	self.forward_to_page_6()

    def forward_to_page_6(self):
	self.PAGE = "6"
	self.clear_screen()

        self.button4.configure(command=self.forward_to_page_7)

	self.button2.configure(state=DISABLED)

	self.main_frame = Frame(self.middlepanel, relief=RAISED, borderwidth=4)
	self.main_frame.place(in_=self.middlepanel, anchor="c", relx=.5, rely=.5)

	self.preferences_header = Label(self.main_frame, text=WORD194, font=self.boldfont)
	self.preferences_header.grid(row=0, column=0, padx=10, sticky=W)

	self.preferences_inner_frame = Frame(self.main_frame)
	self.preferences_inner_frame.grid(row=1, column=0, columnspan=2, sticky=N+S+E+W)

        # Plymouth Theme:

	self.plymouth_theme_frame = Frame(self.preferences_inner_frame, relief=RAISED, borderwidth=1)
	self.plymouth_theme_frame.grid(row=0, column=0, padx=10, pady=3, sticky=N+S+E+W)

	self.plymouth_theme_header = Label(self.plymouth_theme_frame, text=WORD197, font=self.boldfont)
	self.plymouth_theme_header.grid(row=0, column=0, pady=3, padx=10, sticky=W)

	self.plymouth_theme_help_button = Button(self.plymouth_theme_frame, image=self.image6, command=self.plymouth_help)
	self.plymouth_theme_help_button.grid(row=0, column=1, ipadx=4, ipady=4, padx=10, pady=3, sticky=E)

	if self.RESTRICTEDEXTRAS.get() == WORD560:
	   self.plymouth_theme_menu = OptionMenu(self.plymouth_theme_frame, self.PLYMOUTHTHEME, WORD578,WORD577,"Winbuntu")
	else:
	   self.plymouth_theme_menu = OptionMenu(self.plymouth_theme_frame, self.PLYMOUTHTHEME, WORD578)
	self.plymouth_theme_menu["width"] = 20
	self.plymouth_theme_menu["anchor"] = W
	self.plymouth_theme_menu.grid(row=1, column=0, columnspan=2, padx=10, pady=3, sticky=N+S+E+W)

        if (UVERSION != "Ubuntu104") and (UVERSION != "Ubuntu1010") and (UVERSION != "Ubuntu114"):
	   self.PLYMOUTHTHEME.set(WORD583)
	   self.plymouth_theme_header.configure(state=DISABLED)
	   self.plymouth_theme_help_button.configure(state=DISABLED)
	   self.plymouth_theme_menu.configure(state=DISABLED)

        # Panel Type:

	self.panel_type_frame = Frame(self.preferences_inner_frame, relief=RAISED, borderwidth=1)
	self.panel_type_frame.grid(row=0, column=1, padx=10, pady=3, sticky=N+S+E+W)

	self.panel_type_header = Label(self.panel_type_frame, text=WORD195, font=self.boldfont)
	self.panel_type_header.grid(row=0, column=0, pady=3, padx=10, sticky=W)

	self.panel_type_help_button = Button(self.panel_type_frame, image=self.image6, command=self.paneltype_help)
	self.panel_type_help_button.grid(row=0, column=1, ipadx=4, ipady=4, padx=10, pady=3, sticky=E)

	self.panel_type_menu = OptionMenu(self.panel_type_frame, self.SUPERBAR, WORD571,WORD578)
	self.panel_type_menu["width"] = 21
	self.panel_type_menu["anchor"] = W
	self.panel_type_menu.grid(row=1, column=0, columnspan=2, padx=10, pady=3, sticky=N+S+E+W)

        if (self.INSTALLTYPE.get() == WORD553):
	   self.SUPERBAR.set("N/A")
	   self.panel_type_header.configure(state=DISABLED)
	   self.panel_type_help_button.configure(state=DISABLED)
	   self.panel_type_menu.configure(state=DISABLED)
        
        # Window Selector:

	self.window_selector_frame = Frame(self.preferences_inner_frame, relief=RAISED, borderwidth=1)
	self.window_selector_frame.grid(row=1, column=0, padx=10, pady=3, sticky=N+S+E+W)

	self.window_selector_header = Label(self.window_selector_frame, text=WORD196, font=self.boldfont)
	self.window_selector_header.grid(row=0, column=0, pady=3, padx=10, sticky=W)

	self.window_selector_help_button = Button(self.window_selector_frame, image=self.image6, command=self.windowselector_help)
	self.window_selector_help_button.grid(row=0, column=1, ipadx=4, ipady=4, padx=10, pady=3, sticky=E)

	if DOCKBARXINSTALLED == "Yes":
	   self.window_selector_menu = OptionMenu(self.window_selector_frame, self.WINMAN, WORD575,WORD576)
	else:
	   self.window_selector_menu = OptionMenu(self.window_selector_frame, self.WINMAN, WORD576)
	self.window_selector_menu["width"] = 20
	self.window_selector_menu["anchor"] = W
	self.window_selector_menu.grid(row=1, column=0, columnspan=2, padx=10, pady=3, sticky=N+S+E+W)

        if (self.INSTALLTYPE.get() == WORD553):
	   self.WINMAN.set("N/A")
	   self.window_selector_header.configure(state=DISABLED)
	   self.window_selector_help_button.configure(state=DISABLED)
	   self.window_selector_menu.configure(state=DISABLED)

        # Start Menu Logo:

	self.start_logo_frame = Frame(self.preferences_inner_frame, relief=RAISED, borderwidth=1)
	self.start_logo_frame.grid(row=1, column=1, padx=10, pady=3, sticky=N+S+E+W)

	self.start_logo_header = Label(self.start_logo_frame, text=WORD199, font=self.boldfont)
	self.start_logo_header.grid(row=0, column=0, pady=3, padx=10, sticky=W)

	self.start_logo_help_button = Button(self.start_logo_frame, image=self.image6, command=self.startmenulogo_help)
	self.start_logo_help_button.grid(row=0, column=1, ipadx=4, ipady=4, padx=10, pady=3, sticky=E)

	if self.RESTRICTEDEXTRAS.get() == WORD560:
	   self.start_logo_menu = OptionMenu(self.start_logo_frame, self.STARTUP, "CentOS",WORD582,"Debian","Fedora",WORD581,"Gnome","Mint","Ubuntu","PCLinuxOS","Mandriva","Suse",WORD577)
	else:
	   self.start_logo_menu = OptionMenu(self.start_logo_frame, self.STARTUP, "CentOS",WORD582,"Debian","Fedora",WORD581,"Gnome","Mint","Ubuntu","PCLinuxOS","Mandriva","Suse")
	self.start_logo_menu["width"] = 21
	self.start_logo_menu["anchor"] = W
	self.start_logo_menu.grid(row=1, column=0, columnspan=2, padx=10, pady=3, sticky=N+S+E+W)

        # Icon Theme:

	self.icon_theme_frame = Frame(self.preferences_inner_frame, relief=RAISED, borderwidth=1)
	self.icon_theme_frame.grid(row=2, column=1, padx=10, pady=3, sticky=N+S+E+W)

	self.icon_theme_header = Label(self.icon_theme_frame, text=WORD198, font=self.boldfont)
	self.icon_theme_header.grid(row=0, column=0, pady=3, padx=10, sticky=W)

	self.icon_theme_help_button = Button(self.icon_theme_frame, image=self.image6, command=self.icontheme_help)
	self.icon_theme_help_button.grid(row=0, column=1, ipadx=4, ipady=4, padx=10, pady=3, sticky=E)

	if self.RESTRICTEDEXTRAS.get() == WORD560:
	   self.icon_theme_menu = OptionMenu(self.icon_theme_frame, self.ICONBRAND, WORD580,WORD579)
	else:
	   self.icon_theme_menu = OptionMenu(self.icon_theme_frame, self.ICONBRAND, WORD580)
	self.icon_theme_menu["width"] = 21
	self.icon_theme_menu["anchor"] = W
	self.icon_theme_menu.grid(row=1, column=0, columnspan=2, padx=10, pady=3, sticky=N+S+E+W)

        # Gnomenu Mail URL:

	self.gnomenu_mail_frame = Frame(self.preferences_inner_frame, relief=RAISED, borderwidth=1)
	self.gnomenu_mail_frame.grid(row=3, column=1, padx=10, pady=(3,6), sticky=N+S+E+W)

	self.gnomenu_mail_header = Label(self.gnomenu_mail_frame, text=WORD200, font=self.boldfont)
	self.gnomenu_mail_header.grid(row=0, column=0, pady=3, padx=10, sticky=W)

	self.gnomenu_mail_help_button = Button(self.gnomenu_mail_frame, image=self.image6, command=self.gnomenumailurl_help)
	self.gnomenu_mail_help_button.grid(row=0, column=1, ipadx=4, ipady=4, padx=10, pady=3, sticky=E)

	self.gnomenu_mail_entry = Entry(self.gnomenu_mail_frame, borderwidth=1, width=24)
	self.gnomenu_mail_entry.grid(row=1, column=0, columnspan=2, padx=10, pady=3, sticky=N+S+E+W)

	if GNOMENUINSTALLED != "Yes":
	   self.gnomenu_mail_entry.insert(0, WORD583)
	   self.gnomenu_mail_header.configure(state=DISABLED)
	   self.gnomenu_mail_help_button.configure(state=DISABLED)
	   self.gnomenu_mail_entry.configure(state=DISABLED)
	else:
	   self.gnomenu_mail_entry.insert(0, "www.hotmail.com")

        # GTK Theme:

	self.gtk_theme_frame = Frame(self.preferences_inner_frame, relief=RAISED, borderwidth=1)
	self.gtk_theme_frame.grid(row=2, column=0, padx=10, pady=3, sticky=N+S+E+W)

	self.gtk_theme_header = Label(self.gtk_theme_frame, text=WORD217, font=self.boldfont)
	self.gtk_theme_header.grid(row=0, column=0, pady=3, padx=10, sticky=W)

	self.gtk_theme_help_button = Button(self.gtk_theme_frame, image=self.image6, command=self.gtktheme_help)
	self.gtk_theme_help_button.grid(row=0, column=1, ipadx=4, ipady=4, padx=10, pady=3, sticky=E)

	if MURRINEINSTALLED == "Yes":
	   self.gtk_theme_menu = OptionMenu(self.gtk_theme_frame, self.GTKTHEME, WORD584,WORD582,"Darth-Vader",WORD585,"Pixmap",WORD596,WORD586,WORD587,WORD588,WORD589,WORD590,WORD591,WORD592,WORD593,WORD594,WORD595)
	else:
	   self.gtk_theme_menu = OptionMenu(self.gtk_theme_frame, self.GTKTHEME, WORD584,WORD582,"Darth-Vader",WORD585,"Pixmap",WORD596,WORD590,WORD591,WORD592,WORD593,WORD594,WORD595)

	self.gtk_theme_menu["width"] = 20
	self.gtk_theme_menu["anchor"] = W
	self.gtk_theme_menu.grid(row=1, column=0, columnspan=2, padx=10, pady=3, sticky=N+S+E+W)

        # Username:

	self.username_frame = Frame(self.preferences_inner_frame, relief=RAISED, borderwidth=1)
	self.username_frame.grid(row=3, column=0, padx=10, pady=(3,6), sticky=N+S+E+W)

	self.username_header = Label(self.username_frame, text=WORD231, font=self.boldfont)
	self.username_header.grid(row=0, column=0, pady=3, padx=10, sticky=W)

	self.username_help_button = Button(self.username_frame, image=self.image6, command=self.username_help)
	self.username_help_button.grid(row=0, column=1, ipadx=4, ipady=4, padx=10, pady=3, sticky=E)

	self.username_entry = Entry(self.username_frame, borderwidth=1, width=24)
	self.username_entry.grid(row=1, column=0, columnspan=2, padx=10, pady=3, sticky=N+S+E+W)
	self.username_entry.insert(0, self.PUSERNAME)

    def forward_to_page_7(self):
	self.PAGE = "7"
	self.clear_screen()

	self.button2.configure(state=NORMAL)

        self.button4.configure(command=self.forward_to_page_8)

	self.main_frame = Frame(self.middlepanel, relief=RAISED, borderwidth=4)
	self.main_frame.place(in_=self.middlepanel, anchor="c", relx=.5, rely=.5)

	self.preferences_header = Label(self.main_frame, text=WORD232, font=self.boldfont)
	self.preferences_header.grid(row=0, column=0, padx=10, sticky=W)

	self.preferences_inner_frame = Frame(self.main_frame)
	self.preferences_inner_frame.grid(row=1, column=0, columnspan=2, sticky=N+W+E+W)

        # Panel Color:

	self.panel_color_frame = Frame(self.preferences_inner_frame, relief=RAISED, borderwidth=1)
	self.panel_color_frame.grid(row=0, column=0, padx=10, pady=3, sticky=N+S+E+W)

	self.panel_color_header = Label(self.panel_color_frame, text=WORD233, font=self.boldfont)
	self.panel_color_header.grid(row=0, column=0, pady=3, padx=10, sticky=W)

	self.panel_color_help_button = Button(self.panel_color_frame, image=self.image6, command=self.panelcolor_help)
	self.panel_color_help_button.grid(row=0, column=1, ipadx=4, ipady=4, padx=10, pady=3, sticky=E)

	if MURRINEINSTALLED == "Yes":
	   self.panel_color_menu = OptionMenu(self.panel_color_frame, self.PANELSTYLECOLOR, WORD597,WORD598,WORD599,WORD600,WORD601,WORD602,WORD582,WORD603,WORD604,WORD605,WORD585,WORD607,WORD606,WORD608,WORD586,WORD587,WORD588,WORD589,WORD609)
	else:
	   self.panel_color_menu = OptionMenu(self.panel_color_frame, self.PANELSTYLECOLOR, WORD597,WORD598,WORD599,WORD600,WORD601,WORD602,WORD582,WORD603,WORD604,WORD605,WORD585,WORD607,WORD606,WORD608,WORD609)

	self.panel_color_menu["width"] = 23
	self.panel_color_menu["anchor"] = W
	self.panel_color_menu.grid(row=1, column=0, columnspan=2, padx=10, pady=3)

        # Breadcrumb Theme:

	self.bcrumb_theme_frame = Frame(self.preferences_inner_frame, relief=RAISED, borderwidth=1)
	self.bcrumb_theme_frame.grid(row=1, column=0, padx=10, pady=3, sticky=N+S+E+W)

	self.bcrumb_theme_header = Label(self.bcrumb_theme_frame, text=WORD234 + "\n" + WORD235, font=self.boldfont, justify=LEFT)
	self.bcrumb_theme_header.grid(row=0, column=0, pady=3, padx=10, sticky=W)

	self.bcrumb_theme_help_button = Button(self.bcrumb_theme_frame, image=self.image6, command=self.breadcrumb_help)
	self.bcrumb_theme_help_button.grid(row=0, column=1, ipadx=4, ipady=4, padx=10, pady=3, sticky=E)

	self.bcrumb_theme_menu = OptionMenu(self.bcrumb_theme_frame, self.BCRUMBS, "Aero",WORD584,WORD582,WORD610)
	self.bcrumb_theme_menu["width"] = 23
	self.bcrumb_theme_menu["anchor"] = W
	self.bcrumb_theme_menu.grid(row=1, column=0, columnspan=2, padx=10, pady=3)

	if ELEMENTRYNINSTALLED != "Yes":
	   self.BCRUMBS.set(WORD583)
	   self.bcrumb_theme_header.configure(state=DISABLED)
	   self.bcrumb_theme_help_button.configure(state=DISABLED)
	   self.bcrumb_theme_menu.configure(state=DISABLED)

        # Emerald Theme:

	self.emerald_theme_frame = Frame(self.preferences_inner_frame, relief=RAISED, borderwidth=1)
	self.emerald_theme_frame.grid(row=2, column=0, padx=10, pady=(3,6), sticky=N+S+E+W)

	self.emerald_theme_header = Label(self.emerald_theme_frame, text=WORD236, font=self.boldfont)
	self.emerald_theme_header.grid(row=0, column=0, pady=3, padx=10, sticky=W)

	self.emerald_theme_help_button = Button(self.emerald_theme_frame, image=self.image6, command=self.emeraldtheme_help)
	self.emerald_theme_help_button.grid(row=0, column=1, ipadx=4, ipady=4, padx=10, pady=3, sticky=E)

	if ELEMENTRYNINSTALLED != "Yes":
	   self.emerald_theme_menu = OptionMenu(self.emerald_theme_frame, self.ETHEME, WORD584,WORD602,WORD611,WORD582,WORD603,WORD604,WORD605,WORD585,WORD607,WORD606,WORD612,WORD596,WORD586,WORD587,WORD588,WORD589,WORD613,WORD609)
	else:
	   self.emerald_theme_menu = OptionMenu(self.emerald_theme_frame, self.ETHEME, WORD584,WORD602,WORD611,WORD582,WORD603,WORD604,WORD605,WORD585,WORD607,WORD606,WORD612,WORD596,WORD613,WORD609)
	self.emerald_theme_menu["width"] = 23
	self.emerald_theme_menu["anchor"] = W
	self.emerald_theme_menu.grid(row=1, column=0, columnspan=2, padx=10, pady=3, sticky=N+S+E+W)

	if EMERALDINSTALLED != "Yes":
	   self.ETHEME.set(WORD583)
	   self.emerald_theme_header.configure(state=DISABLED)
	   self.emerald_theme_help_button.configure(state=DISABLED)
	   self.emerald_theme_menu.configure(state=DISABLED)

        # Show Desktop Icon:

	self.show_desktop_frame = Frame(self.preferences_inner_frame, relief=RAISED, borderwidth=1)
	self.show_desktop_frame.grid(row=0, column=1, padx=10, pady=3, sticky=N+S+E+W)

	self.show_desktop_header = Label(self.show_desktop_frame, text=WORD237, font=self.boldfont)
	self.show_desktop_header.grid(row=0, column=0, pady=3, padx=10, sticky=W)

	self.show_desktop_help_button = Button(self.show_desktop_frame, image=self.image6, command=self.showdesktopicon_help)
	self.show_desktop_help_button.grid(row=0, column=1, ipadx=4, ipady=4, padx=10, pady=3, sticky=E)

	if GVFSBININSTALLED == "Yes":
	   self.show_desktop_menu = OptionMenu(self.show_desktop_frame, self.DESK, WORD573,WORD572)
	else:
	   self.show_desktop_menu = OptionMenu(self.show_desktop_frame, self.DESK, WORD573)
	self.show_desktop_menu["width"] = 21
	self.show_desktop_menu["anchor"] = W
	self.show_desktop_menu.grid(row=1, column=0, columnspan=2, padx=10, pady=3, sticky=N+S+E+W)

        # Show Workspaces:

	self.show_workspaces_frame = Frame(self.preferences_inner_frame, relief=RAISED, borderwidth=1)
	self.show_workspaces_frame.grid(row=1, column=1, padx=10, pady=3, sticky=N+S+E+W)

	self.show_workspaces_header = Label(self.show_workspaces_frame, text=WORD238, font=self.boldfont)
	self.show_workspaces_header.grid(row=0, column=0, pady=3, padx=10, sticky=W)

	self.show_workspaces_help_button = Button(self.show_workspaces_frame, image=self.image6, command=self.showworkspaces_help)
	self.show_workspaces_help_button.grid(row=0, column=1, ipadx=4, ipady=4, padx=10, pady=3, sticky=E)

	self.show_workspaces_menu = OptionMenu(self.show_workspaces_frame, self.ALLWORKSPACES, WORD574,WORD614)
	self.show_workspaces_menu["width"] = 21
	self.show_workspaces_menu["anchor"] = W
	self.show_workspaces_menu.grid(row=1, column=0, columnspan=2, padx=10, pady=3, sticky=N+S+E+W)

	if DOCKBARXINSTALLED != "Yes":
	   self.ALLWORKSPACES.set(WORD583)
	   self.show_workspaces_header.configure(state=DISABLED)
	   self.show_workspaces_help_button.configure(state=DISABLED)
	   self.show_workspaces_menu.configure(state=DISABLED)
	else:
	   if self.WINMAN.get() != WORD575:
	      self.ALLWORKSPACES.set("N/A")
	      self.show_workspaces_menu.configure(state=DISABLED)

        # Wallpaper:

	self.wallpaper_frame = Frame(self.preferences_inner_frame, relief=RAISED, borderwidth=1)
	self.wallpaper_frame.grid(row=2, column=1, padx=10, pady=(3,6), sticky=N+S+E+W)

	self.wallpaper_header = Label(self.wallpaper_frame, text=WORD239, font=self.boldfont)
	self.wallpaper_header.grid(row=0, column=0, pady=3, padx=10, sticky=W)

	self.wallpaper_help_button = Button(self.wallpaper_frame, image=self.image6, command=self.wallpaper_help)
	self.wallpaper_help_button.grid(row=0, column=1, ipadx=4, ipady=4, padx=10, pady=3, sticky=E)

	if self.RESTRICTEDEXTRAS.get() == WORD560:
	   self.wallpaper_menu = OptionMenu(self.wallpaper_frame, self.WALLPAPERNAME, WORD580,WORD579)
	else:
	   self.wallpaper_menu = OptionMenu(self.wallpaper_frame, self.WALLPAPERNAME, WORD580)
	self.wallpaper_menu["width"] = 21
	self.wallpaper_menu["anchor"] = W
	self.wallpaper_menu.grid(row=1, column=0, columnspan=2, padx=10, pady=3, sticky=N+S+E+W)

        if (self.INSTALLTYPE.get() == WORD553):
	   self.WALLPAPERNAME.set("N/A")
	   self.wallpaper_header.configure(state=DISABLED)
	   self.wallpaper_help_button.configure(state=DISABLED)
	   self.wallpaper_menu.configure(state=DISABLED)

    def forward_to_page_8(self):
	self.PAGE = "8"
	self.clear_screen()

	self.button4["image"] = ""
        self.button4.configure(width=12, command=self.confirm_start, text=WORD240)

	self.main_frame = Frame(self.middlepanel, relief=RAISED, borderwidth=4)
	self.main_frame.place(in_=self.middlepanel, anchor="c", relx=.5, rely=.5)

	self.preferences_header = Label(self.main_frame, text=WORD241, font=self.boldfont)
	self.preferences_header.grid(row=0, columnspan=2, column=0, padx=(10,0), sticky=W)

	self.preferences_left_inner_frame = Frame(self.main_frame)
	self.preferences_left_inner_frame.grid(row=1, column=0, pady=(0,6), sticky=N+W+E+W)

	self.preferences_right_inner_frame = Frame(self.main_frame)
	self.preferences_right_inner_frame.grid(row=1, column=1, pady=(0,6), sticky=N+W+E+W)

        # RGBA Apps:

	self.rgba_apps_frame = Frame(self.preferences_left_inner_frame, relief=RAISED, borderwidth=1)
	self.rgba_apps_frame.grid(row=0, column=0, padx=10, pady=3, sticky=N+S+E+W)

	self.rgba_apps_header = Label(self.rgba_apps_frame, text=WORD247, font=self.boldfont)
	self.rgba_apps_header.grid(row=0, column=0, pady=3, padx=10, sticky=W)

	self.rgba_apps_help_button = Button(self.rgba_apps_frame, image=self.image6, command=self.rgba_help)
	self.rgba_apps_help_button.grid(row=0, column=1, ipadx=4, ipady=4, padx=10, pady=3, sticky=E)

        self.rgba_apps_cb1 = Checkbutton(self.rgba_apps_frame, text="Gedit", variable = self.RGBA_GEDIT)
        self.rgba_apps_cb2 = Checkbutton(self.rgba_apps_frame, text="Rhythmbox", variable = self.RGBA_RHYTHMBOX)
        self.rgba_apps_cb1.grid(row=1, column=0, padx=10, pady=(0,12), sticky=W)
        self.rgba_apps_cb2.grid(row=2, column=0, padx=10, pady=(0,12), sticky=W)

	if ELEMENTRYNINSTALLED != "Yes":
	   self.rgba_apps_cb1.configure(state=DISABLED)
	   self.rgba_apps_cb2.configure(state=DISABLED)
	else:
	   if self.RGBA_COUNTER.get() == 0:
	      self.RGBA_COUNTER.set(self.RGBA_COUNTER.get() + 1)
              self.rgba_apps_cb1.select()
              self.rgba_apps_cb2.select()

        # Desktop Icons:

	self.desktop_icons_frame = Frame(self.preferences_left_inner_frame, relief=RAISED, borderwidth=1)
	self.desktop_icons_frame.grid(row=1, column=0, padx=10, pady=3, sticky=N+S+E+W)

	self.desktop_icons_header = Label(self.desktop_icons_frame, text=WORD248, font=self.boldfont)
	self.desktop_icons_header.grid(row=0, column=0, pady=3, padx=10, sticky=W)

	self.desktop_icons_help_button = Button(self.desktop_icons_frame, image=self.image6, command=self.desktopicons_help)
	self.desktop_icons_help_button.grid(row=0, column=1, ipadx=4, ipady=4, padx=10, pady=3, sticky=E)

        self.desktop_icons_cb1 = Checkbutton(self.desktop_icons_frame, text=WORD249, variable = self.DESKTOPCOMPUTER)
        self.desktop_icons_cb2 = Checkbutton(self.desktop_icons_frame, text=WORD250, variable = self.DESKTOPHOMEFOLDER)
        self.desktop_icons_cb3 = Checkbutton(self.desktop_icons_frame, text=WORD251, variable = self.DESKTOPNETWORK)
        self.desktop_icons_cb4 = Checkbutton(self.desktop_icons_frame, text=WORD252, variable = self.DESKTOPRECYLEBIN)
        self.desktop_icons_cb5 = Checkbutton(self.desktop_icons_frame, text=WORD253, variable = self.DESKTOPREMOVABLEDEVICES)
        self.desktop_icons_cb1.grid(row=1, column=0, padx=10, pady=(0,12), sticky=W)
        self.desktop_icons_cb2.grid(row=2, column=0, padx=10, pady=(0,12), sticky=W)
        self.desktop_icons_cb3.grid(row=3, column=0, padx=10, pady=(0,12), sticky=W)
        self.desktop_icons_cb4.grid(row=4, column=0, padx=10, pady=(0,12), sticky=W)
        self.desktop_icons_cb5.grid(row=5, column=0, padx=10, pady=(0,12), sticky=W)

	if self.DESKTOP_ICONS_COUNTER.get() == 0:
	   self.DESKTOP_ICONS_COUNTER.set(self.DESKTOP_ICONS_COUNTER.get() + 1)
           self.desktop_icons_cb1.select()
           self.desktop_icons_cb2.select()
           self.desktop_icons_cb4.select()

        # Elementry Nautilus Toolbar Icons:

	self.edesktop_frame = Frame(self.preferences_right_inner_frame, relief=RAISED, borderwidth=1)
	self.edesktop_frame.grid(row=0, column=0, padx=10, pady=3, sticky=N+S+E+W)

	self.edesktop_header = Label(self.edesktop_frame, text=WORD269 + "\n" + WORD270, font=self.boldfont, justify=LEFT)
	self.edesktop_header.grid(row=0, column=0, pady=3, padx=10, sticky=W)

	self.edesktop_help_button = Button(self.edesktop_frame, image=self.image6, command=self.toolbar_help)
	self.edesktop_help_button.grid(row=0, column=1, ipadx=4, ipady=4, padx=10, pady=3, sticky=E)

        self.edesktop_cb1 = Checkbutton(self.edesktop_frame, text=WORD254, variable = self.EDESKTOP_MENU_INT)
        self.edesktop_cb2 = Checkbutton(self.edesktop_frame, text=WORD255, variable = self.EDESKTOP_BACK_INT)
        self.edesktop_cb3 = Checkbutton(self.edesktop_frame, text=WORD256, variable = self.EDESKTOP_FORWARD_INT)
        self.edesktop_cb4 = Checkbutton(self.edesktop_frame, text=WORD257, variable = self.EDESKTOP_PARENT_INT)
        self.edesktop_cb5 = Checkbutton(self.edesktop_frame, text=WORD258, variable = self.EDESKTOP_RELOAD_INT)
        self.edesktop_cb6 = Checkbutton(self.edesktop_frame, text=WORD259, variable = self.EDESKTOP_HOME_INT)
        self.edesktop_cb7 = Checkbutton(self.edesktop_frame, text=WORD260, variable = self.EDESKTOP_COMPUTER_INT)
        self.edesktop_cb8 = Checkbutton(self.edesktop_frame, text=WORD263, variable = self.EDESKTOP_NEWTAB_INT)
        self.edesktop_cb9 = Checkbutton(self.edesktop_frame, text=WORD264, variable = self.EDESKTOP_NEWWINDOW_INT)
        self.edesktop_cb10 = Checkbutton(self.edesktop_frame, text=WORD265, variable = self.EDESKTOP_SEARCH_INT)
        self.edesktop_cb11 = Checkbutton(self.edesktop_frame, text=WORD267, variable = self.EDESKTOP_LOCATION_INT)
        self.edesktop_cb12 = Checkbutton(self.edesktop_frame, text=WORD268, variable = self.EDESKTOP_MODE_INT)
        self.edesktop_cb1.grid(row=1, column=0, padx=10, sticky=W)
        self.edesktop_cb2.grid(row=2, column=0, padx=10, sticky=W)
        self.edesktop_cb3.grid(row=3, column=0, padx=10, sticky=W)
        self.edesktop_cb4.grid(row=4, column=0, padx=10, sticky=W)
        self.edesktop_cb5.grid(row=5, column=0, padx=10, sticky=W)
        self.edesktop_cb6.grid(row=6, column=0, padx=10, sticky=W)
        self.edesktop_cb7.grid(row=7, column=0, padx=10, sticky=W)
        self.edesktop_cb8.grid(row=8, column=0, padx=10, sticky=W)
        self.edesktop_cb9.grid(row=9, column=0, padx=10, sticky=W)
        self.edesktop_cb10.grid(row=10, column=0, padx=10, sticky=W)
        self.edesktop_cb11.grid(row=11, column=0, padx=10, sticky=W)
        self.edesktop_cb12.grid(row=12, column=0, padx=10, pady=(0,3), sticky=W)

	if ELEMENTRYNINSTALLED != "Yes":
	   self.edesktop_cb1.configure(state=DISABLED)
	   self.edesktop_cb2.configure(state=DISABLED)
	   self.edesktop_cb3.configure(state=DISABLED)
	   self.edesktop_cb4.configure(state=DISABLED)
	   self.edesktop_cb5.configure(state=DISABLED)
	   self.edesktop_cb6.configure(state=DISABLED)
	   self.edesktop_cb7.configure(state=DISABLED)
	   self.edesktop_cb8.configure(state=DISABLED)
	   self.edesktop_cb9.configure(state=DISABLED)
	   self.edesktop_cb10.configure(state=DISABLED)
	   self.edesktop_cb11.configure(state=DISABLED)
	   self.edesktop_cb12.configure(state=DISABLED)
	else:
	   if self.EDESTKOP_COUNTER.get() == 0:
	      self.EDESTKOP_COUNTER.set(self.EDESTKOP_COUNTER.get() + 1)
              self.edesktop_cb2.select()
              self.edesktop_cb3.select()

# Clear: ====================================================================

    def clear_screen(self):
	if self.PAGE == "2":
	   self.button2.pack_forget()
	elif self.PAGE == "3A":
	   self.install_type_frame.pack_forget()
	   self.local_format_frame.pack_forget()
	   self.restricted_extras_frame.pack_forget()
	else:
	   self.main_frame.place_forget()

# Backwards Navigation: ====================================================================

    def go_back(self):
	self.button4.configure(text=WORD271, image=self.image7, width=110)
	if self.PAGE == "6":
	   self.clear_screen()
	   self.forward_to_page_5()
	elif self.PAGE == "7":
	   self.clear_screen()
	   self.forward_to_page_6()
	elif self.PAGE == "8":
	   self.clear_screen()
	   self.forward_to_page_7()

# Install Win2-7 Essentials: ====================================================================

    def install_essentials(self):
	if (self.MURRINE.get() != 0) or (self.COMPIZFUSIONICON.get() != 0) or (self.CCSM.get() != 0) or (self.EMERALD.get() != 0) or (self.ELEMENTRYN.get() != 0) or (self.DOCKBARX.get() != 0) or (self.EMESENE.get() != 0) or (self.GNOMENU.get() != 0) or (self.SCREENLETS.get() != 0):
	   self.forward_to_page_5B()
	else:
	   self.setup_presets_toolbar()

# Confirm Finish: ====================================================================

    def confirm_start(self):
         if askyesno(title = WORD88, message = WORD274):
            self.finish()

# Presets: ====================================================================

    def Preset_original(self):
	self.GTKTHEME.set(WORD585)
	self.PANELSTYLECOLOR.set(WORD585)
	if self.RESTRICTEDEXTRAS.get() == WORD560:
	   self.STARTUP.set(WORD577)
	else:
	   self.STARTUP.set(WORD581)
	if ELEMENTRYNINSTALLED == "Yes":
	   self.BCRUMBS.set(WORD584)
	if EMERALDINSTALLED == "Yes":
	   self.ETHEME.set(WORD585)

    def Preset_aero(self):
	self.GTKTHEME.set(WORD589)
	self.PANELSTYLECOLOR.set(WORD589)
	if self.RESTRICTEDEXTRAS.get() == WORD560:
	   self.STARTUP.set(WORD577)
	else:
	   self.STARTUP.set(WORD581)
	if ELEMENTRYNINSTALLED == "Yes":
	   self.BCRUMBS.set("Aero")
	if EMERALDINSTALLED == "Yes":
	   self.ETHEME.set(WORD589)

    def Preset_basic(self):
	self.GTKTHEME.set(WORD584)
	self.PANELSTYLECOLOR.set(WORD598)
	if self.RESTRICTEDEXTRAS.get() == WORD560:
	   self.STARTUP.set(WORD577)
	else:
	   self.STARTUP.set(WORD581)
	if ELEMENTRYNINSTALLED == "Yes":
	   self.BCRUMBS.set(WORD584)
	if EMERALDINSTALLED == "Yes":
	   self.ETHEME.set(WORD584)

    def Preset_classic(self):
	self.GTKTHEME.set(WORD582)
	self.PANELSTYLECOLOR.set(WORD582)
	self.STARTUP.set(WORD582)
	if ELEMENTRYNINSTALLED == "Yes":
	   self.BCRUMBS.set(WORD582)
	if EMERALDINSTALLED == "Yes":
	   self.ETHEME.set(WORD582)

# Resolve Varables: ====================================================================

    def resolve_varables(self):

	# Resolve Restricted Extras:
	if self.RESTRICTEDEXTRAS.get() == WORD560:
	   self.RESTRICTEDEXTRAS.set("Yes")
	else:
	   self.RESTRICTEDEXTRAS.set("No")

	# Resolve Install Type:
	if self.INSTALLTYPE.get() == WORD551:
           self.INSTALLTYPE.set("NEW")
        elif self.INSTALLTYPE.get() == WORD552:
           self.INSTALLTYPE.set("REINSTALL")
        elif self.INSTALLTYPE.get() == WORD553:
           self.INSTALLTYPE.set("UPGRADE")
        elif self.INSTALLTYPE.get() == WORD554:
           self.INSTALLTYPE.set("UPDATE")

	# Resolve Icon Theme:
	if self.SUPERBAR.get() == WORD571:
	   self.SUPERBAR.set("YES")
	else:
 	   self.SUPERBAR.set("NO")

	# Resolve Window Manager:
	if self.WINMAN.get() == WORD575:
	   self.WINMAN.set(WORD575)
	else:
	   self.WINMAN.set("Lister")

	# Resolve Workspaces:
	if self.ALLWORKSPACES.get() == WORD574:
	   self.ALLWORKSPACES.set("YES")
	else:
	   self.ALLWORKSPACES.set("NO")

	# Resolve Start Icon:
	if self.STARTUP.get() == "CentOS":
	   self.STARTUP.set("centos")
	elif self.STARTUP.get() == "Debian":
	   self.STARTUP.set("Debian")
	elif self.STARTUP.get() == "Fedora":
	   self.STARTUP.set("Fedora")
	elif self.STARTUP.get() == WORD581:
	   self.STARTUP.set("generic")
	elif self.STARTUP.get() == "Gnome":
	  self. STARTUP.set("gnome")
	elif self.STARTUP.get() == "Mint":
	   self.STARTUP.set("mint")
	elif self.STARTUP.get() == "Ubuntu":
	   self.STARTUP.set("ubuntu")
	elif self.STARTUP.get() == "PCLinuxOS":
	   self.STARTUP.set("pclos")
	elif self.STARTUP.get() == "Mandriva":
	   self.STARTUP.set("mandriva")
	elif self.STARTUP.get() == "Suse":
	   self.STARTUP.set("suse")
	elif self.STARTUP.get() == WORD577:
	   self.STARTUP.set("win2-7")
	elif self.STARTUP.get() == WORD582:
	   self.STARTUP.set("win2-7classic")

	# Resolve GTK Theme:
	if self.GTKTHEME.get() == WORD584:
	   self.GTKTHEME.set("Win2-7Basic")
	   self.METACITYTHEME.set("Win2-7Basic")
	   self.BCRUMBTHEME.set("breadcrumbsWin2-7")
	elif self.GTKTHEME.get() == WORD582:
	   self.GTKTHEME.set("Win2-7Classic")
	   self.METACITYTHEME.set("Win2-7Classic")
	   self.BCRUMBTHEME.set("breadcrumbsWin2-7Classic")
	elif self.GTKTHEME.get() == "Darth-Vader":
	   self.GTKTHEME.set("Win2-7Darth-Vader")
	   self.METACITYTHEME.set("Win2-7Darth-Vader")
	   self.BCRUMBTHEME.set("breadcrumbsWin2-7")
	elif self.GTKTHEME.get() == WORD585:
	   self.GTKTHEME.set("Win2-7Original")
	   self.METACITYTHEME.set("Win2-7(Pixmap)")
	   self.BCRUMBTHEME.set("breadcrumbsWin2-7")
	elif self.GTKTHEME.get() == "Pixmap":
	   self.GTKTHEME.set("Win2-7(Pixmap)")
	   self.METACITYTHEME.set("Win2-7(Pixmap)")
	   self.BCRUMBTHEME.set("breadcrumbsWin2-7")
	elif self.GTKTHEME.get() == WORD596:
	   self.GTKTHEME.set(WORD577)
	   self.METACITYTHEME.set("Win2-7(Pixmap)")
	   self.BCRUMBTHEME.set("breadcrumbsWin2-7")
	elif self.GTKTHEME.get() == WORD590:
	   self.GTKTHEME.set("WLM9Black")
	   self.METACITYTHEME.set("Win2-7(Pixmap)")
	   self.BCRUMBTHEME.set("breadcrumbsWin2-7")
	elif self.GTKTHEME.get() == WORD591:
	   self.GTKTHEME.set("WLM9")
	   self.METACITYTHEME.set("Win2-7(Pixmap)")
	   self.BCRUMBTHEME.set("breadcrumbsWin2-7")
	elif self.GTKTHEME.get() == WORD592:
	   self.GTKTHEME.set("WLM9Green")
	   self.METACITYTHEME.set("Win2-7(Pixmap)")
	   self.BCRUMBTHEME.set("breadcrumbsWin2-7")
	elif self.GTKTHEME.get() == WORD593:
	   self.GTKTHEME.set("WLM9Human")
	   self.METACITYTHEME.set("Win2-7(Pixmap)")
	   self.BCRUMBTHEME.set("breadcrumbsWin2-7")
	elif self.GTKTHEME.get() == WORD594:
	   self.GTKTHEME.set("WLM9Pink")
	   self.METACITYTHEME.set("Win2-7(Pixmap)")
	   self.BCRUMBTHEME.set("breadcrumbsWin2-7")
	elif self.GTKTHEME.get() == WORD595:
	   self.GTKTHEME.set("WLM9Purple")
	   self.METACITYTHEME.set("Win2-7(Pixmap)")
	   self.BCRUMBTHEME.set("breadcrumbsWin2-7")
	elif self.GTKTHEME.get() == WORD586:
	   self.GTKTHEME.set("Win2-7Murrine-AeroBlack")
	   self.METACITYTHEME.set("Win2-7Murrine-AeroBlack")
	   self.BCRUMBTHEME.set("breadcrumbsWin2-7Black")
	elif self.GTKTHEME.get() == WORD587:
	   self.GTKTHEME.set("Win2-7Murrine-AeroBlue")
	   self.METACITYTHEME.set("Win2-7Murrine-AeroBlue")
	   self.BCRUMBTHEME.set("breadcrumbsWin2-7Blue")
	elif self.GTKTHEME.get() == WORD588:
	   self.GTKTHEME.set("Win2-7Murrine-AeroPink")
	   self.METACITYTHEME.set("Win2-7Murrine-AeroPink")
	   self.BCRUMBTHEME.set("breadcrumbsWin2-7Pink")
	elif self.GTKTHEME.get() == WORD589:
	   self.GTKTHEME.set("Win2-7Murrine-Aero")
	   self.METACITYTHEME.set("Win2-7Murrine-Aero")
	   self.BCRUMBTHEME.set("breadcrumbsWin2-7")

	# Resolve Emerald Theme:
	if self.ETHEME.get() == WORD584:
	   self.ETHEME.set("Win2-7Basic")
	elif self.ETHEME.get() == WORD602:
	   self.ETHEME.set("Win2-7Black")
	elif self.ETHEME.get() == WORD611:
	   self.ETHEME.set("Win2-7Brown")
	elif self.ETHEME.get() == WORD582:
	   self.ETHEME.set("Win2-7Classic")
	elif self.ETHEME.get() == WORD603:
	   self.ETHEME.set("Win2-7DarkBlue")
	elif self.ETHEME.get() == WORD604:
	   self.ETHEME.set("Win2-7Green")
	elif self.ETHEME.get() == WORD605:
	   self.ETHEME.set("Win2-7Human")
	elif self.ETHEME.get() == WORD585:
	   self.ETHEME.set("Win2-7Original")
	elif self.ETHEME.get() == WORD607:
	   self.ETHEME.set("Win2-7Pink")
	elif self.ETHEME.get() == WORD606:
	   self.ETHEME.set("Win2-7Purple")
	elif self.ETHEME.get() == WORD612:
	   self.ETHEME.set("Win2-7Red")
	elif self.ETHEME.get() == WORD596:
	   self.ETHEME.set(WORD577)
	elif self.ETHEME.get() == WORD586:
	   self.ETHEME.set("Win2-7Murrine-AeroBlack")
	elif self.ETHEME.get() == WORD587:
	   self.ETHEME.set("Win2-7Murrine-AeroBlue")
	elif self.ETHEME.get() == WORD588:
	   self.ETHEME.set("Win2-7Murrine-AeroPink")
	elif self.ETHEME.get() == WORD589:
	   self.ETHEME.set("Win2-7Murrine-Aero")
	elif self.ETHEME.get() == WORD613:
	   self.ETHEME.set("Win2-7Turquoise")
	elif self.ETHEME.get() == WORD609:
	   self.ETHEME.set("Win2-7White")

	# Resolve Plymouth Theme:
	if self.PLYMOUTHTHEME.get() == WORD577:
	   self.PLYMOUTHTHEME.set("7")
	elif self.PLYMOUTHTHEME.get() == "Winbuntu":
	   self.PLYMOUTHTHEME.set("winbuntu")

	# Resolve Breadcrumb Theme:
	if self.BCRUMBS.get() == "Aero":
	   self.BCRUMBS.set("Aero")
	elif self.BCRUMBS.get() == WORD584:
	   self.BCRUMBS.set(WORD584)
	elif self.BCRUMBS.get() == WORD582:
	   self.BCRUMBS.set(WORD582)
	elif self.BCRUMBS.get() == WORD610:
	   self.BCRUMBS.set(WORD610)

	# Resolve Time & Date:
	if self.TIMEFORMAT.get() == WORD556:
	   self.TIMEFORMAT.set("USNormal")
	elif self.TIMEFORMAT.get() == WORD557:
	   self.TIMEFORMAT.set("USMilitary")
	elif self.TIMEFORMAT.get() == WORD558:
	   self.TIMEFORMAT.set("EUNormal")
	elif self.TIMEFORMAT.get() == WORD559:
	   self.TIMEFORMAT.set("EUMilitary")

	# Resolve Wallpaper:
	if self.WALLPAPERNAME.get() == WORD579:
	   self.WALLPAPERNAME.set(WORD615)
	else:
	   self.WALLPAPERNAME.set(WORD616)

	# Resolve Panel Background:
	if self.PANELSTYLECOLOR.get() == WORD597:
	   self.PANELSTYLECOLOR.set("Panel_Win2-7Basic800.png")
	elif self.PANELSTYLECOLOR.get() == WORD598:
	   self.PANELSTYLECOLOR.set("Panel_Win2-7Basic1024.png")
	elif self.PANELSTYLECOLOR.get() == WORD599:
	   self.PANELSTYLECOLOR.set("Panel_Win2-7Basic1280.png")
	elif self.PANELSTYLECOLOR.get() == WORD600:
	   self.PANELSTYLECOLOR.set("Panel_Win2-7Basic-Dark.png")
	elif self.PANELSTYLECOLOR.get() == WORD601:
	   self.PANELSTYLECOLOR.set("Panel_Win2-7Basic-light.png")
	elif self.PANELSTYLECOLOR.get() == WORD602:
	   self.PANELSTYLECOLOR.set("Panel_Win2-7Black.png")
	elif self.PANELSTYLECOLOR.get() == WORD582:
	   self.PANELSTYLECOLOR.set("Panel_Win2-7Classic.png")
	elif self.PANELSTYLECOLOR.get() == WORD603:
	   self.PANELSTYLECOLOR.set("Panel_Win2-7DarkBlue.png")
	elif self.PANELSTYLECOLOR.get() == WORD604:
	   self.PANELSTYLECOLOR.set("Panel_Win2-7Green.png")
	elif self.PANELSTYLECOLOR.get() == WORD605:
	   self.PANELSTYLECOLOR.set("Panel_Win2-7Human.png")
	elif self.PANELSTYLECOLOR.get() == WORD585:
	   self.PANELSTYLECOLOR.set("Panel_Win2-7Original.png")
	elif self.PANELSTYLECOLOR.get() == WORD607:
	   self.PANELSTYLECOLOR.set("Panel_Win2-7Pink.png")
	elif self.PANELSTYLECOLOR.get() == WORD606:
	   self.PANELSTYLECOLOR.set("Panel_Win2-7Purple.png")
	elif self.PANELSTYLECOLOR.get() == WORD608:
	   self.PANELSTYLECOLOR.set("Panel_Win2-7Sea.png")
	elif self.PANELSTYLECOLOR.get() == WORD586:
	   self.PANELSTYLECOLOR.set("Panel_Win2-7Murrine-AeroBlack.png")
	elif self.PANELSTYLECOLOR.get() == WORD587:
	   self.PANELSTYLECOLOR.set("Panel_Win2-7Murrine-AeroBlue.png")
	elif self.PANELSTYLECOLOR.get() == WORD588:
	   self.PANELSTYLECOLOR.set("Panel_Win2-7Murrine-AeroPink.png")
	elif self.PANELSTYLECOLOR.get() == WORD589:
	   self.PANELSTYLECOLOR.set("Panel_Win2-7Murrine-Aero.png")
	elif self.PANELSTYLECOLOR.get() == WORD609:
	   self.PANELSTYLECOLOR.set("Panel_Win2-7White.png")

	# Resolve Show Desktop Icon:
	if self.DESK.get() == WORD573:
	   self.DESK.set("Desktop-Normal")
	else:
	   self.DESK.set("Desktop-Transparent")

	# Resolve Icon Theme:
        if self.ICONBRAND.get() == WORD579:
           self.ICONBRAND.set(WORD577)
	else:
           self.ICONBRAND.set("Win2-7Libre")

# Finish: ====================================================================

    def finish(self):

	self.resolve_varables()

	# Resolve Final Varables:

        if self.EDESKTOP_MENU_INT.get() == 1:	
	   self.EDESKTOP_MENU.set("Yes")

        if self.EDESKTOP_BACK_INT.get() == 1:	
	   self.EDESKTOP_BACK.set(" Back ")

        if self.EDESKTOP_FORWARD_INT.get() == 1:	
	   self.EDESKTOP_FORWARD.set(" Forward ")     

        if self.EDESKTOP_PARENT_INT.get() == 1:	
	   self.EDESKTOP_PARENT.set(" Up ")    

        if self.EDESKTOP_RELOAD_INT.get() == 1:	
	   self.EDESKTOP_RELOAD.set(" StopReload ") 

        if self.EDESKTOP_HOME_INT.get() == 1:	
	   self.EDESKTOP_HOME.set(" Home ")    

        if self.EDESKTOP_COMPUTER_INT.get() == 1:	
	   self.EDESKTOP_COMPUTER.set(" Go to Computer ")    

        if self.EDESKTOP_NEWTAB_INT.get() == 1:	
	   self.EDESKTOP_NEWTAB.set(" New Tab Button ")    

        if self.EDESKTOP_NEWWINDOW_INT.get() == 1:	
	   self.EDESKTOP_NEWWINDOW.set(" New Window ")    

        if self.EDESKTOP_SEARCH_INT.get() == 1:	
	   self.EDESKTOP_SEARCH.set(" Search ")    

        if self.EDESKTOP_LOCATION_INT.get() == 1:	
	   self.EDESKTOP_LOCATION.set(" EditLocation ")    

        if self.EDESKTOP_MODE_INT.get() == 1:	
	   self.EDESKTOP_MODE.set(" ViewModeButton ")       
	
	if ELEMENTRYNINSTALLED == "Yes":
	   EDESKTOPCONFIG = "[  " + str(self.EDESKTOP_BACK.get()) + str(self.EDESKTOP_FORWARD.get()) + str(self.EDESKTOP_PARENT.get()) + str(self.EDESKTOP_RELOAD.get()) + str(self.EDESKTOP_HOME.get()) + str(self.EDESKTOP_COMPUTER.get()) + str(self.EDESKTOP_NEWTAB.get()) + str(self.EDESKTOP_NEWWINDOW.get()) + str(self.EDESKTOP_SEARCH.get()) + str(self.EDESKTOP_LOCATION.get()) + " LocationPathBar " + str(self.EDESKTOP_MODE.get()) + "  ]"

	   EDESKTOPCONFIG = EDESKTOPCONFIG.replace( '   ', '' )
	   EDESKTOPCONFIG = EDESKTOPCONFIG.replace( '  ', ',' )

	self.config = file("/tmp/config.py", 'w')

	self.config.write(unicode("#!/usr/bin/env python").encode('utf8') + '\n')
	self.config.write(unicode("# -*- coding: utf-8 -*-").encode('utf8') + '\n' + '\n')

	self.config.write("INSTALLTYPE=\"" + unicode(self.INSTALLTYPE.get()).encode('utf8') + "\"" + '\n')
	self.config.write("TIMEFORMAT=\"" + unicode(self.TIMEFORMAT.get()).encode('utf8') + "\"" + '\n')
	self.config.write("PRESET=\"" + unicode(self.PRESET.get()).encode('utf8') + "\"" + '\n')
	self.config.write("RESTRICTEDEXTRAS=\"" + unicode(self.RESTRICTEDEXTRAS.get()).encode('utf8') + "\"" + '\n')

	self.config.write("MURRINE=\"" + unicode(self.MURRINE.get()).encode('utf8') + "\"" + '\n')
	self.config.write("COMPIZFUSIONICON=\"" + unicode(self.COMPIZFUSIONICON.get()).encode('utf8') + "\"" + '\n')
	self.config.write("EMERALD=\"" + unicode(self.EMERALD.get()).encode('utf8') + "\"" + '\n')
	self.config.write("ELEMENTRYN=\"" + unicode(self.ELEMENTRYN.get()).encode('utf8') + "\"" + '\n')
	self.config.write("DOCKBARX=\"" + unicode(self.DOCKBARX.get()).encode('utf8') + "\"" + '\n')
	self.config.write("EMESENE=\"" + unicode(self.EMESENE.get()).encode('utf8') + "\"" + '\n')
	self.config.write("GNOMENU=\"" + unicode(self.GNOMENU.get()).encode('utf8') + "\"" + '\n')
	self.config.write("SCREENLETS=\"" + unicode(self.SCREENLETS.get()).encode('utf8') + "\"" + '\n')
	self.config.write("CCSM=\"" + unicode(self.CCSM.get()).encode('utf8') + "\"" + '\n')

	self.config.write("SUPERBAR=\"" + unicode(self.SUPERBAR.get()).encode('utf8') + "\"" + '\n')
	self.config.write("WINMAN=\"" + unicode(self.WINMAN.get()).encode('utf8') + "\"" + '\n')
	self.config.write("PLYMOUTHTHEME=\"" + unicode(self.PLYMOUTHTHEME.get()).encode('utf8') + "\"" + '\n')
	self.config.write("ICONBRAND=\"" + unicode(self.ICONBRAND.get()).encode('utf8') + "\"" + '\n')
	self.config.write("STARTUP=\"" + unicode(self.STARTUP.get()).encode('utf8') + "\"" + '\n')
	self.config.write("URL=\"" + unicode(self.gnomenu_mail_entry.get()).encode('utf8') + "\"" + '\n')
	self.config.write("GTKTHEME=\"" + unicode(self.GTKTHEME.get()).encode('utf8') + "\"" + '\n')
	self.config.write("PUSERNAME=\"" + unicode(self.username_entry.get()).encode('utf8') + "\"" + '\n')
	self.config.write("PANELSTYLECOLOR=\"" + unicode(self.PANELSTYLECOLOR.get()).encode('utf8') + "\"" + '\n')
	self.config.write("BCRUMBS=\"" + unicode(self.BCRUMBS.get()).encode('utf8') + "\"" + '\n')
	self.config.write("ETHEME=\"" + unicode(self.ETHEME.get()).encode('utf8') + "\"" + '\n')
	self.config.write("DESK=\"" + unicode(self.DESK.get()).encode('utf8') + "\"" + '\n')
	self.config.write("ALLWORKSPACES=\"" + unicode(self.ALLWORKSPACES.get()).encode('utf8') + "\"" + '\n')
	self.config.write("WALLPAPERNAME=\"" + unicode(self.WALLPAPERNAME.get()).encode('utf8') + "\"" + '\n')
	self.config.write("METACITYTHEME=\"" + unicode(self.METACITYTHEME.get()).encode('utf8') + "\"" + '\n')
	self.config.write("BCRUMBTHEME=\"" + unicode(self.BCRUMBTHEME.get()).encode('utf8') + "\"" + '\n')

	self.config.write("DESKTOPCOMPUTER=\"" + unicode(self.DESKTOPCOMPUTER.get()).encode('utf8') + "\"" + '\n')
	self.config.write("DESKTOPHOMEFOLDER=\"" + unicode(self.DESKTOPHOMEFOLDER.get()).encode('utf8') + "\"" + '\n')
	self.config.write("DESKTOPNETWORK=\"" + unicode(self.DESKTOPNETWORK.get()).encode('utf8') + "\"" + '\n')
	self.config.write("DESKTOPRECYLEBIN=\"" + unicode(self.DESKTOPRECYLEBIN.get()).encode('utf8') + "\"" + '\n')
	self.config.write("DESKTOPREMOVABLEDEVICES=\"" + unicode(self.DESKTOPREMOVABLEDEVICES.get()).encode('utf8') + "\"" + '\n')

	self.config.write("RGBA_GEDIT=\"" + unicode(self.RGBA_GEDIT.get()).encode('utf8') + "\"" + '\n')
	self.config.write("RGBA_RHYTHMBOX=\"" + unicode(self.RGBA_RHYTHMBOX.get()).encode('utf8') + "\"" + '\n')

	if ELEMENTRYNINSTALLED == "Yes":
	   self.config.write("EDESKTOPMENU=\"" + unicode(self.EDESKTOP_MENU.get()).encode('utf8') + "\"" + '\n')
	   self.config.write("EDESKTOPCONFIG=\"" + unicode(EDESKTOPCONFIG).encode('utf8') + "\"" + '\n')
	self.config.close()

        self.exit()

    def SOFTWARE_SOURCES(self):
	if PMAN == "APT":
	   TERMINAL_STATUS(WORD277,"BUSY")
	   if os.system('echo \"%s\" | sudo -S -p \"\" apt-get update >> \"/dev/null\" 2>&1' % (PASS)) == 0:
	      TERMINAL_STATUS_PASS()
	   else:
	      TERMINAL_STATUS_FAIL()
	      showerror(title = WORD35, message = WORD278)
	      ABORT()
	elif PMAN == "ZYPPER":
	   TERMINAL_STATUS(WORD277,"BUSY")
	   if os.system('echo \"%s\" | sudo -S -p \"\" zypper refresh >> \"/dev/null\" 2>&1' % (PASS)) == 0:
	      TERMINAL_STATUS_PASS()
	   else:
	      TERMINAL_STATUS_FAIL()
	      showerror(title = WORD35, message = WORD278)
	      ABORT()

# Help Clicks: ====================================================================

    def help_window(self):
	showinfo(title = self.help_title, message = self.help_message)

    def install_type_help(self):
        self.help_title = Variable()
        self.help_title = WORD311
        self.help_message = Variable()
        self.help_message = WORD312 + "\n\n" + WORD313 + "\n\n" + WORD314 + "\n\n" + WORD315 + "\n\n" + WORD316
        self.help_window()

    def time_and_date_help(self):
        self.help_title = Variable()
        self.help_title = WORD311
        self.help_message = Variable()
        self.help_message = WORD317 + "\n\n" + WORD318 + "\n" + WORD319 + "\n\n" + WORD320 + "\n" + WORD321 + "\n\n" + WORD322 + "\n" + WORD323 + "\n\n" + WORD324 + "\n" + WORD325
        self.help_window()

    def restricted_extras_help(self):
        self.help_title = Variable()
        self.help_title = WORD311
        self.help_message = Variable()
        self.help_message = WORD326
        self.help_window()

    def eula_help(self):
        self.help_title = Variable()
        self.help_title = WORD311
        self.help_message = Variable()
        self.help_message = WORD327
        self.help_window()

    def essentials_help(self):
        self.help_title = Variable()
        self.help_title = WORD311
        self.help_message = Variable()
        self.help_message = WORD328
        self.help_window()

    def murrine_help(self):
        self.help_title = Variable()
        self.help_title = WORD311
        self.help_message = Variable()
        self.help_message = WORD329
        self.help_window()

    def fusionicon_help(self):
        self.help_title = Variable()
        self.help_title = WORD311
        self.help_message = Variable()
        self.help_message = WORD330
        self.help_window()

    def ccsm_help(self):
        self.help_title = Variable()
        self.help_title = WORD311
        self.help_message = Variable()
        self.help_message = WORD331
        self.help_window()

    def emerald_help(self):
        self.help_title = Variable()
        self.help_title = WORD311
        self.help_message = Variable()
        self.help_message = WORD332
        self.help_window()

    def edesktop_help(self):
        self.help_title = Variable()
        self.help_title = WORD311
        self.help_message = Variable()
        self.help_message = WORD333
        self.help_window()

    def dockbarx_help(self):
        self.help_title = Variable()
        self.help_title = WORD311
        self.help_message = Variable()
        self.help_message = WORD334
        self.help_window()

    def emesene_help(self):
        self.help_title = Variable()
        self.help_title = WORD311
        self.help_message = Variable()
        self.help_message = WORD335
        self.help_window()

    def gnomenu_help(self):
        self.help_title = Variable()
        self.help_title = WORD311
        self.help_message = Variable()
        self.help_message = WORD336
        self.help_window()

    def screenlets_help(self):
        self.help_title = Variable()
        self.help_title = WORD311
        self.help_message = Variable()
        self.help_message = WORD337
        self.help_window()

    def plymouth_help(self):
        self.help_title = Variable()
        self.help_title = WORD311
        self.help_message = Variable()
        self.help_message = WORD338
        self.help_window()

    def windowselector_help(self):
        self.help_title = Variable()
        self.help_title = WORD311
        self.help_message = Variable()
        self.help_message = WORD339
        self.help_window()

    def gtktheme_help(self):
        self.help_title = Variable()
        self.help_title = WORD311
        self.help_message = Variable()
        self.help_message = WORD340
        self.help_window()

    def username_help(self):
        self.help_title = Variable()
        self.help_title = WORD311
        self.help_message = Variable()
        self.help_message = WORD341
        self.help_window()

    def paneltype_help(self):
        self.help_title = Variable()
        self.help_title = WORD311
        self.help_message = Variable()
        self.help_message = WORD342
        self.help_window()

    def icontheme_help(self):
        self.help_title = Variable()
        self.help_title = WORD311
        self.help_message = Variable()
        self.help_message = WORD343
        self.help_window()

    def startmenulogo_help(self):
        self.help_title = Variable()
        self.help_title = WORD311
        self.help_message = Variable()
        self.help_message = WORD344
        self.help_window()

    def gnomenumailurl_help(self):
        self.help_title = Variable()
        self.help_title = WORD311
        self.help_message = Variable()
        self.help_message = WORD345
        self.help_window()

    def panelcolor_help(self):
        self.help_title = Variable()
        self.help_title = WORD311
        self.help_message = Variable()
        self.help_message = WORD346
        self.help_window()

    def breadcrumb_help(self):
        self.help_title = Variable()
        self.help_title = WORD311
        self.help_message = Variable()
        self.help_message = WORD347
        self.help_window()

    def emeraldtheme_help(self):
        self.help_title = Variable()
        self.help_title = WORD311
        self.help_message = Variable()
        self.help_message = WORD348
        self.help_window()

    def showdesktopicon_help(self):
        self.help_title = Variable()
        self.help_title = WORD311
        self.help_message = Variable()
        self.help_message = WORD349
        self.help_window()

    def showworkspaces_help(self):
        self.help_title = Variable()
        self.help_title = WORD311
        self.help_message = Variable()
        self.help_message = WORD350
        self.help_window()

    def wallpaper_help(self):
        self.help_title = Variable()
        self.help_title = WORD311
        self.help_message = Variable()
        self.help_message = WORD351
        self.help_window()

    def rgba_help(self):
        self.help_title = Variable()
        self.help_title = WORD311
        self.help_message = Variable()
        self.help_message = WORD352
        self.help_window()

    def desktopicons_help(self):
        self.help_title = Variable()
        self.help_title = WORD311
        self.help_message = Variable()
        self.help_message = WORD353
        self.help_window()

    def toolbar_help(self):
        self.help_title = Variable()
        self.help_title = WORD311
        self.help_message = Variable()
        self.help_message = WORD354
        self.help_window()

# About: ====================================================================

    def about(self):
        showinfo(title = WORD355, message = WORD356 + "\n    Dart00 " + WORD357 + "\n    Juandejesuss " + WORD358 + "\n\n" + WORD359 + "\n     http://tinyurl.com/33bhl5k\n\n" + WORD360 + "\n     Croatian: Cooleech\n     Danish: Noervang\n     English: Dart00\n     French: Magellan13\n     Portuguese: Gusreis1989\n     Russian: Stepan Suvorov\n     Spanish: Juandejesuss\n\n" + WORD361 + "\n     Dart00: globemaster22000@yahoo.com\n     Juandejesuss: juandejesuss@gmail.com\n\n" + WORD362)

# Accept Win2-7 EULA: ====================================================================

    def eula(self):

	if self.EULA_ACCEPT.get() == 1:
	   self.button4.configure(state=NORMAL)
           if self.accepted_EULA.get() == "":
              self.accepted_EULA.set("YES")
	else:
	   self.button4.configure(state=DISABLED)

# EULA: ====================================================================

    def CALL_EULA(self,TEXT,TITLE):

	self.button4.configure(state=DISABLED)

	self.main_frame = Frame(self.middlepanel, relief=RAISED, borderwidth=4)
	self.main_frame.place(in_=self.middlepanel, anchor="c", relx=.5, rely=.5)

	self.EULA_header = Label(self.main_frame, text=TITLE, font=self.boldfont)
	self.EULA_header.grid(row=0, column=0, columnspan=2, padx=10, pady=3, sticky=W)

	self.EULA_help_button = Button(self.main_frame, image=self.image6, command=self.eula_help)
	self.EULA_help_button.grid(row=0, column=1, ipadx=4, ipady=4, padx=10, pady=3, sticky=E)

	self.EULA_box_frame = Frame(self.main_frame, relief=RAISED, borderwidth=1)
	self.EULA_box_frame.grid(row=1, column=0, columnspan=2, padx=10, sticky=N+S+E+W)

	self.EULA_scrollbar = Scrollbar(self.EULA_box_frame)
	self.EULA_textbox = Text(self.EULA_box_frame, height=17, width=55, wrap=WORD)
	self.EULA_textbox.focus_set()
	self.EULA_scrollbar.grid(row=0, column=1, sticky=N+S+E+W)
	self.EULA_textbox.grid(row=0, column=0, sticky=N+S+E+W)
	self.EULA_scrollbar.config(command=self.EULA_textbox.yview)
	self.EULA_textbox.config(yscrollcommand=self.EULA_scrollbar.set)

   	self.EULA_textbox.insert(END, TEXT)

	self.EULA_textbox.configure(state=DISABLED)

        self.EULA_ACCEPT.set(0)
        self.EULA_cb1 = Checkbutton(self.main_frame, text=WORD363, variable = self.EULA_ACCEPT, command=self.eula)
        self.EULA_cb1.grid(row=3, column=1, padx=10, pady=5, sticky=E)

# Exit Clicks: ====================================================================

    def exit(self):

        self.myParent.destroy()

# Center Window: ====================================================================

    def centerWindow(self):
      
        w = self.image1.width()
        h = self.image1.height()

        sw = root.winfo_screenwidth()
        sh = root.winfo_screenheight()
        
        x = (sw - w)/2
        y = (sh - h)/2
        root.geometry('%dx%d+%d+%d' % (w, h, x, y))


root = Tk()
root.resizable(0,0)
root.title(WORD364)
myapp = MyApp(root)
root.mainloop()

if os.path.exists('/tmp/config.py') == True:
   os.system("mv /tmp/config.py Files/modules/config.py")
   from config import *
   os.remove('Files/modules/config.py')
   os.remove('Files/modules/config.pyc')
else:
   CANCEL_SCRIPT()

if DOCKBARXINSTALLED == "Yes":
   RESPONSE = PyZenity.InfoMessage(text=WORD365, title=WORD17)
   CHECK_FOR_CANCEL()

sys.stdout.write("# \n")

if INSTALLTYPE != WORD554:

   # Reset default look if theme is in use (copying over a file in memory will crash the computer)

   if WORD577 in commands.getoutput('gconftool-2 --get /desktop/gnome/interface/gtk_theme'):

      RESPONSE = PyZenity.Warning(WORD366, title=WORD44)
      CHECK_FOR_CANCEL()

      TERMINAL_STATUS(WORD367,"BUSY")

      if (UVERSION == "Ubuntu1010") or (UVERSION == "Ubuntu114") or (UVERSION == "Ubuntu104"):
         REVERT_METACITY="Ambiance"
         REVERT_GTKTHEME="Ambiance"
         REVERT_ICONS="ubuntu-mono-dark"
         REVERT_MOUSE="DMZ-White"
         REVERT_SOUND="ubuntu"

      elif "Ubuntu" in UVERSION:
         REVERT_METACITY=WORD605
         REVERT_GTKTHEME=WORD605
         REVERT_ICONS="Humanity"
         REVERT_MOUSE=WORD605
         REVERT_SOUND="ubuntu"

      elif UVERSION == "Debian":
         REVERT_METACITY="Clearlooks"
         REVERT_GTKTHEME="Clearlooks"
         REVERT_ICONS="gnome"
         REVERT_MOUSE="default"
         REVERT_SOUND="default"

      elif UVERSION == "Mint9":
         REVERT_METACITY="Shiki-Colors-Metacity"
         REVERT_GTKTHEME="Shiki-Wise"
         REVERT_ICONS="gnome-wise"
         REVERT_MOUSE="default"
         REVERT_SOUND="LinuxMint"

      elif UVERSION == "Mint10":
         REVERT_METACITY="Mint-X"
         REVERT_GTKTHEME="Mint-X-Metal"
         REVERT_ICONS="Mint-X"
         REVERT_MOUSE="default"
         REVERT_SOUND="LinuxMint"

      elif UVERSION == "Mint11":
         REVERT_METACITY="Mint-X"
         REVERT_GTKTHEME="Mint-X-Metal"
         REVERT_ICONS="Mint-X"
         REVERT_MOUSE="" # No Value
         REVERT_SOUND="LinuxMint"

      elif UVERSION == "Fedora":
         REVERT_METACITY="Clearlooks"
         REVERT_GTKTHEME="Clearlooks"
         REVERT_ICONS="Fedora"
         REVERT_MOUSE="Bluecurve"
         REVERT_SOUND="freedesktop"

      elif UVERSION == "PCLinuxOS":
         REVERT_METACITY="SlicknesS"
         REVERT_GTKTHEME="SlicknesS"
         REVERT_ICONS="nuoveXT-aero"
         REVERT_MOUSE="default"
         REVERT_SOUND="ia_ora"

      elif UVERSION == "CentOS":
         REVERT_METACITY="Clearlooks"
         REVERT_GTKTHEME="Clearlooks"
         REVERT_ICONS="Clearlooks"
         REVERT_MOUSE="Bluecurve"
         REVERT_SOUND="" # None

      elif UVERSION == "Mandriva":
         REVERT_METACITY="Ia Ora Steel"
         REVERT_GTKTHEME="Ia Ora Steel"
         REVERT_ICONS="gnome"
         REVERT_MOUSE="" # No Value
         REVERT_SOUND="ia_ora"

      elif UVERSION == "openSUSE":
         REVERT_METACITY="Sonar"
         REVERT_GTKTHEME="Sonar"
         REVERT_ICONS="Gilouche"
         REVERT_MOUSE="default" 
         REVERT_SOUND="freedesktop"

      ERRORLEVEL = os.system('gconftool-2 --set \"/apps/metacity/general/theme\" --type string \"%s\"' % (REVERT_METACITY)) ; STATUSCHECK()
      ERRORLEVEL = os.system('gconftool-2 --set \"/desktop/gnome/interface/gtk_theme\" --type string \"%s\"' % (REVERT_GTKTHEME)) ; STATUSCHECK()
      ERRORLEVEL = os.system('gconftool-2 --set \"/desktop/gnome/interface/icon_theme\" --type string \"%s\"' % (REVERT_ICONS)) ; STATUSCHECK()
      ERRORLEVEL = os.system('gconftool-2 --set \"/desktop/gnome/peripherals/mouse/cursor_theme\" --type string \"%s\"' % (REVERT_MOUSE)) ; STATUSCHECK()
      ERRORLEVEL = os.system('gconftool-2 --set \"/desktop/gnome/sound/theme_name\" --type string \"%s\"' % (REVERT_SOUND)) ; STATUSCHECK()
      ERRORLEVEL = os.system('gconftool-2 --set \"/apps/panel/toplevels/bottom_panel_0/background/type\" --type string \"gtk\"') ; STATUSCHECK()

      if GVFSBININSTALLED == "Yes":
         ERRORLEVEL = os.system('gvfs-set-attribute \"%s\" -t unset metadata::custom-icon > /dev/null 2>&1' % (DESKTOP)) ; STATUSCHECK()

      time.sleep(5)

      RESOLVE_ERRORLEVEL()

   # Copy/Install Files:

   # Extract Win2-7 Icon Theme:
   TERMINAL_STATUS(WORD368,"BUSY")
   ERRORLEVEL = os.system('tar jvxf Files/icon-theme/Win2-7Libre.tar.bz2 > \"/dev/null\" 2>&1') ; STATUSCHECK()
   if RESTRICTEDEXTRAS == "Yes":
      ERRORLEVEL = os.system('tar jvxf Files/icon-theme/Win2-7.tar.bz2 > \"/dev/null\" 2>&1') ; STATUSCHECK()
   RESOLVE_ERRORLEVEL()

   # Copy Icon Theme:
   TERMINAL_STATUS(WORD369,"BUSY")
   ERRORLEVEL = os.system('rm -r -f \"$HOME\"/.icons/Win2-7*') ; STATUSCHECK()  
   ERRORLEVEL = os.system('mkdir -p \"$HOME\"/.icons') ; STATUSCHECK() 
   if RESTRICTEDEXTRAS == "Yes":
      ERRORLEVEL = os.system('mv Win2-7 \"$HOME\"/.icons/ > /dev/null 2>&1') ; STATUSCHECK()
   ERRORLEVEL = os.system('mv Win2-7Libre \"$HOME\"/.icons/ > /dev/null 2>&1') ; STATUSCHECK()
   ERRORLEVEL = os.system('gconftool-2 --set /apps/win2-7pack/icon_theme --type string Installed') ; STATUSCHECK()
   RESOLVE_ERRORLEVEL()

   # Copy Terminal Services Theme:
   if (RESTRICTEDEXTRAS == "Yes") and (TSCLIENTINSTALLED == "Yes"):
      TERMINAL_STATUS(WORD370,"BUSY")
      if (os.path.exists("/usr/share/pixmaps/tsclient.old") == False) and (os.path.exists("/usr/share/pixmaps/tsclient") == True):
         ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" mv /usr/share/pixmaps/tsclient /usr/share/pixmaps/tsclient.old >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK()
      ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" cp -r Files/tsclient /usr/share/pixmaps/ >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK()
      ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" chmod -R 777 /usr/share/pixmaps/tsclient >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK()
      ERRORLEVEL = os.system('gconftool-2 --set /apps/win2-7pack/terminal_server_theme --type string Installed') ; STATUSCHECK()		
      RESOLVE_ERRORLEVEL()

   # Copying Libia-Ora Engine:
   if os.path.exists("/usr/lib/gtk-2.0/2.10.0/engines/libia_ora.so") == False:
      TERMINAL_STATUS(WORD371,"BUSY")
      ERRORLEVEL = os.system('mkdir -p /usr/lib/gtk-2.0/2.10.0/engines') ; STATUSCHECK()
      ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" cp Files/gtk2-engines/%s/libia_ora.so /usr/lib/gtk-2.0/2.10.0/engines >> /dev/null 2>&1' % (PASS,ARCH)) ; STATUSCHECK()
      ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" chmod 777 /usr/lib/gtk-2.0/2.10.0/engines/libia_ora.so >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK()
      RESOLVE_ERRORLEVEL()

   # Copying Wallpapers:
   TERMINAL_STATUS(WORD372,"BUSY")
   ERRORLEVEL = os.system('mkdir -p \"$HOME\"/.backgrounds') ; STATUSCHECK()
   ERRORLEVEL = os.system('cp -r Files/backgrounds/* \"$HOME\"/.backgrounds > /dev/null 2>&1') ; STATUSCHECK()
   ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" chmod -R 777 \"$HOME\"/.backgrounds >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK()
   ERRORLEVEL = os.system('gconftool-2 --set /apps/win2-7pack/wallpapers --type string Installed') ; STATUSCHECK()
   RESOLVE_ERRORLEVEL()

   # Copying Curser Theme:
   if RESTRICTEDEXTRAS == "Yes":
      TERMINAL_STATUS(WORD373,"BUSY")
      ERRORLEVEL = os.system('cp -r Files/cursor/aero-drop \"$HOME\"/.icons > /dev/null 2>&1') ; STATUSCHECK()	
      ERRORLEVEL = os.system('gconftool-2 --set /apps/win2-7pack/curser_theme --type string Installed') ; STATUSCHECK()	
      RESOLVE_ERRORLEVEL()

   # Copying GTK-Themes:
   TERMINAL_STATUS(WORD374,"BUSY")
   ERRORLEVEL = os.system('mkdir -p \"$HOME\"/.themes') ; STATUSCHECK
   ERRORLEVEL = os.system('rm -f -r \"$HOME\"/.themes/Win2-7* > /dev/null 2>&1') ; STATUSCHECK
   ERRORLEVEL = os.system('rm -f -r \"$HOME\"/.themes/WLM9* > /dev/null 2>&1') ; STATUSCHECK
   ERRORLEVEL = os.system('cp -r Files/gtk-theme/* \"$HOME\"/.themes > /dev/null 2>&1') ; STATUSCHECK
   if ELEMENTRYNINSTALLED == "Yes":
      ERRORLEVEL = os.system('cp -r Files/murrine/gtk-theme/* \"$HOME\"/.themes > /dev/null 2>&1') ; STATUSCHECK
   ERRORLEVEL = os.system('gconftool-2 --set /apps/win2-7pack/gtk_theme --type string Installed') ; STATUSCHECK
   RESOLVE_ERRORLEVEL()

   # Copying RGBA apps:
   if ELEMENTRYNINSTALLED == "Yes":
      TERMINAL_STATUS(WORD375,"BUSY")
      ERRORLEVEL = os.system('cp -r -f Files/murrine/RGBA-apps/gedit \"$HOME\"/.gnome2 > /dev/null 2>&1') ; STATUSCHECK
      ERRORLEVEL = os.system('cp -r -f Files/murrine/RGBA-apps/rhythmbox \"$HOME\"/.gnome2 > /dev/null 2>&1') ; STATUSCHECK
      ERRORLEVEL = os.system('gconftool-2 --set /apps/win2-7pack/rgba_apps --type string Installed') ; STATUSCHECK
      RESOLVE_ERRORLEVEL()

   # Copying Breadcrumbs:
   if ELEMENTRYNINSTALLED == "Yes":
      TERMINAL_STATUS(WORD376,"BUSY")
      if (os.path.exists(USER + "/.themes/nautilus.old") == False) and (os.path.exists(USER + "/.themes/nautilus") == True):
         ERRORLEVEL = os.system('mv \"$HOME\"/.themes/nautilus \"$HOME\"/.themes/nautilus.old > /dev/null 2>&1') ; STATUSCHECK
         ERRORLEVEL = os.system('rm -r -f \"$HOME\"/.themes/nautilus')  ; STATUSCHECK
      ERRORLEVEL = os.system('mkdir -p \"$HOME\"/.themes/nautilus') ; STATUSCHECK
      ERRORLEVEL = os.system('rm -r -f \"$HOME\"/.themes/breadcrumbsWin2-7') ; STATUSCHECK
      ERRORLEVEL = os.system('cp -r Files/murrine/breadcrumbs* \"$HOME\"/.themes/ > /dev/null 2>&1') ; STATUSCHECK
      ERRORLEVEL = os.system('cp -r \"$HOME\"/.themes/breadcrumbsWin2-7/nautilus \"$HOME\"/.themes/ > /dev/null 2>&1') ; STATUSCHECK
      if (os.path.exists(USER + "/.gtkrc-2.0.old") == False) and (os.path.exists(USER + "/.gtkrc-2.0") == True):
         ERRORLEVEL = os.system('mv \"$HOME\"/.gtkrc-2.0 \"$HOME\"/.gtkrc-2.0.old > /dev/null 2>&1') ; STATUSCHECK
      ERRORLEVEL = os.system('cp Files/murrine/gtkrc-2.0 \"$HOME\"/.gtkrc-2.0 > /dev/null 2>&1') ; STATUSCHECK
      ERRORLEVEL = os.system('gconftool-2 --set /apps/win2-7pack/breadcrumb_theme --type string Installed') ; STATUSCHECK
      RESOLVE_ERRORLEVEL()

   # Copying Lock Theme:
   if (UVERSION != "Debian") and (UVERSION != "CentOS"):
      TERMINAL_STATUS(WORD377,"BUSY")
      if (os.path.exists("/usr/share/gnome-screensaver.old") == False) and (os.path.exists("/usr/share/gnome-screensaver") == True):
         ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" mv -f /usr/share/gnome-screensaver /usr/share/gnome-screensaver.old >> \"/dev/null\" 2>&1' % (PASS)) ; STATUSCHECK
         ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" mkdir /usr/share/gnome-screensaver >> \"/dev/null\" 2>&1' % (PASS)) ; STATUSCHECK
         ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" cp -r Files/lock-dialog/win2-7-images /usr/share/gnome-screensaver >> \"/dev/null\" 2>&1' % (PASS)) ; STATUSCHECK
         ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" cp Files/lock-dialog/lock-dialog-win2-7.gtkrc /usr/share/gnome-screensaver >> \"/dev/null\" 2>&1' % (PASS)) ; STATUSCHECK
         ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" cp Files/lock-dialog/lock-dialog-win2-7.ui /usr/share/gnome-screensaver >> \"/dev/null\" 2>&1' % (PASS)) ; STATUSCHECK
      if UVERSION == "Fedora":
         ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" cp Files/lock-dialog/logoF.png /usr/share/gnome-screensaver/logo.png >> \"/dev/null\" 2>&1' % (PASS)) ; STATUSCHECK
      elif "Mint" in UVERSION:
         ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" cp Files/lock-dialog/logoM.png /usr/share/gnome-screensaver/logo.png >> \"/dev/null\" 2>&1' % (PASS)) ; STATUSCHECK
      elif UVERSION == "PCLinuxOS":
         ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" cp Files/lock-dialog/logoP.png /usr/share/gnome-screensaver/logo.png >> \"/dev/null\" 2>&1' % (PASS)) ; STATUSCHECK
      elif UVERSION == "Mandriva":
         ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" cp Files/lock-dialog/logoMA.png /usr/share/gnome-screensaver/logo.png >> \"/dev/null\" 2>&1' % (PASS)) ; STATUSCHECK
      elif UVERSION == "openSUSE":
         ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" cp Files/lock-dialog/logoO.png /usr/share/gnome-screensaver/logo.png >> \"/dev/null\" 2>&1' % (PASS)) ; STATUSCHECK
      elif "Ubuntu" in UVERSION:
         ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" cp Files/lock-dialog/logo.png /usr/share/gnome-screensaver/logo.png >> \"/dev/null\" 2>&1' % (PASS)) ; STATUSCHECK
      ERRORLEVEL = os.system('gconftool-2 --set /apps/win2-7pack/lock_theme --type string Installed') ; STATUSCHECK
      RESOLVE_ERRORLEVEL()

   # Copying Fonts:
   if RESTRICTEDEXTRAS == "Yes":
      TERMINAL_STATUS(WORD378,"BUSY")
      ERRORLEVEL = os.system('mkdir -p \"$HOME\"/.fonts') ; STATUSCHECK
      ERRORLEVEL = os.system('cp -r Files/fonts/* \"$HOME\"/.fonts > /dev/null 2>&1') ; STATUSCHECK
      ERRORLEVEL = os.system('gconftool-2 --set /apps/win2-7pack/fonts --type string Installed > /dev/null 2>&1') ; STATUSCHECK
      RESOLVE_ERRORLEVEL()

   # Copying DockBarX Theme:
   TERMINAL_STATUS(WORD379,"BUSY")
   ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" mkdir -p /usr/share/dockbarx >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
   ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" cp -r Files/dockbarx/* /usr/share/dockbarx >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
   ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" chmod -R 777 /usr/share/dockbarx >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
   ERRORLEVEL = os.system('gconftool-2 --set /apps/win2-7pack/dockbarx_themes --type string Installed') ; STATUSCHECK
   RESOLVE_ERRORLEVEL()

   # Copying Gnomenu Themes:
   TERMINAL_STATUS(WORD380,"BUSY")
   ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" mkdir -p /usr/share/gnomenu/Themes >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
   ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" cp -r Files/gnomenu/Themes/Menu /usr/share/gnomenu/Themes >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
   if RESTRICTEDEXTRAS == "Yes":
      ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" cp -r Files/gnomenu/Themes/Button /usr/share/gnomenu/Themes >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
      ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" cp -r Files/gnomenu/Themes/Icon /usr/share/gnomenu/Themes >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
      ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" cp -r Files/gnomenu/Themes/Sound /usr/share/gnomenu/Themes >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
   ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" chmod -R 777 /usr/share/gnomenu >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
   ERRORLEVEL = os.system('gconftool-2 --set "/apps/win2-7pack/gnomenu_themes" --type string Installed') ; STATUSCHECK
   RESOLVE_ERRORLEVEL()

   # Copying Gnome-Panel Pixmaps:
   if RESTRICTEDEXTRAS == "Yes":
      TERMINAL_STATUS(WORD381,"BUSY")
      if (os.path.exists("/usr/share/gnome-panel/pixmaps.old") == False) and (os.path.exists("/usr/share/gnome-panel/pixmaps") == True):
        ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" cp -r /usr/share/gnome-panel/pixmaps /usr/share/gnome-panel/pixmaps.old >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
      ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" cp -r Files/gnome-panel /usr/share/ >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
      ERRORLEVEL = os.system('gconftool-2 --set "/apps/win2-7pack/panel_pixmaps" --type string Installed') ; STATUSCHECK
      RESOLVE_ERRORLEVEL()

   # Copying Gnome-Control-Center Theme:
   if RESTRICTEDEXTRAS == "Yes":
      TERMINAL_STATUS(WORD382,"BUSY")
      if (os.path.exists("/usr/share/gnome-control-center/pixmaps.old") == False) and (os.path.exists("/usr/share/gnome-control-center/pixmaps") == True):
         ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" cp -r /usr/share/gnome-control-center/pixmaps /usr/share/gnome-control-center/pixmaps.old >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
      ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" cp -r Files/gnome-control-center /usr/share >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
      ERRORLEVEL = os.system('gconftool-2 --set /apps/win2-7pack/control_center_theme --type string Installed') ; STATUSCHECK
      RESOLVE_ERRORLEVEL()

   # Copying Sound Theme:
   if (RESTRICTEDEXTRAS == "Yes") and (UVERSION != "Debian") and (UVERSION != "CentOS"):
      TERMINAL_STATUS(WORD383,"BUSY")
      ERRORLEVEL = os.system('mkdir -p \"$HOME\"/.local/share/sounds') ; STATUSCHECK
      ERRORLEVEL = os.system('cp -r Files/sounds/Win2-7 \"$HOME\"/.local/share/sounds > /dev/null 2>&1') ; STATUSCHECK		
      ERRORLEVEL = os.system('gconftool-2 --set /apps/win2-7pack/sound_themes --type string Installed') ; STATUSCHECK
      RESOLVE_ERRORLEVEL()

   # Copying Emesene Theme:
   if (EMESENEINSTALLED == "Yes") and (RESTRICTEDEXTRAS == "Yes"):
      TERMINAL_STATUS(WORD384,"BUSY")
      ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" mkdir -p /usr/share/emesene/themes/default >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
      ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" mkdir -p /usr/share/emesene/themes/emesene >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
      ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" mkdir -p /usr/share/emesene/smilies/default >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
      ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" mkdir -p /usr/share/emesene/smilies/emesene >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
      ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" mkdir -p /usr/share/emesene/sound_themes/default >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
      ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" mkdir -p /usr/share/emesene/sound_themes/emesene >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
      if (os.path.exists("/usr/share/emesene/themes/emesene") == False) and (os.path.exists("/usr/share/emesene/themes/default") == True):
         ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" mv /usr/share/emesene/themes/default /usr/share/emesene/themes/emesene >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
      if (os.path.exists("/usr/share/emesene/smilies/emesene") == False) and (os.path.exists("/usr/share/emesene/smilies/default") == True):
         ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" mv /usr/share/emesene/smilies/default /usr/share/emesene/smilies/emesene >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
      if (os.path.exists("/usr/share/emesene/sound_themes/emesene") == False) and (os.path.exists("/usr/share/emesene/sound_themes/default") == True):
         ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" mv /usr/share/emesene/sound_themes/default /usr/share/emesene/sound_themes/emesene >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
      ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" cp -r Files/emesene /usr/share >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
      ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" chmod -R 777 /usr/share/emesene >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
      ERRORLEVEL = os.system('gconftool-2 --set "/apps/win2-7pack/emesene_theme" --type string Installed') ; STATUSCHECK
      RESOLVE_ERRORLEVEL()

   # Copying Emerald Themes:
   TERMINAL_STATUS(WORD385,"BUSY")
   ERRORLEVEL = os.system('rm -f -r \"$HOME\"/.emerald/themes/Win2-7*') ; STATUSCHECK
   ERRORLEVEL = os.system('mkdir -p \"$HOME\"/.emerald/theme') ; STATUSCHECK
   ERRORLEVEL = os.system('mkdir -p \"$HOME\"/.emerald/themes') ; STATUSCHECK
   ERRORLEVEL = os.system('cp -r Files/emerald-decoration/themes/* \"$HOME\"/.emerald/themes > /dev/null 2>&1') ; STATUSCHECK
   ERRORLEVEL = os.system('cp -r Files/emerald-decoration/default \"$HOME\"/.emerald > /dev/null 2>&1') ; STATUSCHECK
   if ELEMENTRYNINSTALLED == "Yes":
      if MURRINEINSTALLED == "Yes":
         ERRORLEVEL = os.system('cp -r Files/murrine/emerald-decoration/Advanced/* \"$HOME\"/.emerald/themes > /dev/null 2>&1') ; STATUSCHECK
      else:
         ERRORLEVEL = os.system('cp -r Files/murrine/emerald-decoration/Standard/* \"$HOME\"/.emerald/themes > /dev/null 2>&1') ; STATUSCHECK
   ERRORLEVEL = os.system('gconftool-2 --set /apps/win2-7pack/emerald_themes --type string Installed') ; STATUSCHECK
   RESOLVE_ERRORLEVEL()

   # Copying CCSM graphic:
   if CCSMINSTALLED == "Yes":
      TERMINAL_STATUS(WORD387,"BUSY")
      ERRORLEVEL = os.system('cp Files/compiz/Win2-7Reflect.png \"$HOME\"/.Win2-7Reflect.png > /dev/null 2>&1') ; STATUSCHECK
      ERRORLEVEL = os.system('gconftool-2 --set /apps/win2-7pack/compiz_files --type string Installed') ; STATUSCHECK
      RESOLVE_ERRORLEVEL()

   # Copying wine Theme:
   if WINEINSTALLED == "Yes":
      TERMINAL_STATUS(WORD388,"BUSY")
      os.system('mkdir -p \"$HOME\"/.wine/drive_c/windows/Resources/Themes/Seven')
      ERRORLEVEL = os.system('cp -r Files/wine/Shell/* \"$HOME\"/.wine/drive_c/windows/Resources/Themes/Seven > /dev/null 2>&1') ; STATUSCHECK
      ERRORLEVEL = os.system('cp -r Files/wine/Seven.msstyles \"$HOME\"/.wine/drive_c/windows/Resources/Themes/Seven > /dev/null 2>&1') ; STATUSCHECK
      if (os.path.exists(USER + "/.wine/user.old") == False) and (os.path.exists(USER + "/.wine/user.reg") == True):
         ERRORLEVEL = os.system('mv \"$HOME\"/.wine/user.reg \"$HOME\"/.wine/user.old > /dev/null 2>&1') ; STATUSCHECK
      ERRORLEVEL = os.system('cp Files/wine/user.reg \"$HOME\"/.wine > /dev/null 2>&1') ; STATUSCHECK
      ERRORLEVEL = os.system('gconftool-2 --set /apps/win2-7pack/wine_theme --type string Installed') ; STATUSCHECK
      RESOLVE_ERRORLEVEL()
   
   # Copying X-Splash Theme:
   if UVERSION == "Ubuntu910":
      TERMINAL_STATUS(WORD389,"BUSY")
      if os.path.exists("/usr/share/images/xsplash.old") == False:
         ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" mv /usr/share/images/xsplash /usr/share/images/xsplash.old >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
      ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" cp -r Files/xsplash /usr/share/images >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
      ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" chmod -R 777 /usr/share/images/xsplash >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
      ERRORLEVEL = os.system('gconftool-2 --set /apps/win2-7pack/xsplash_theme --type string Installed') ; STATUSCHECK
      RESOLVE_ERRORLEVEL()

   # Copying GDM Login Theme:
   if (RESTRICTEDEXTRAS == "Yes") and (GDM != "3"):
      if (UVERSION == "Ubuntu94") or (UVERSION == "Debian") or (UVERSION == "PCLinuxOS") or (UVERSION == "CentOS"):
         TERMINAL_STATUS(WORD389,"BUSY")
         ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" cp -r Files/gdm/win2-7 /usr/share/gdm/themes >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
         ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" chmod -R 777 /usr/share/gdm/themes/win2-7 >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK

         if UVERSION == "Debian":
            ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" rm -f /usr/share/gdm/themes/win2-7/Logo.png >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
            ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" rm -f /usr/share/gdm/themes/win2-7/Logo3.png >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
            ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" rm -f /usr/share/gdm/themes/win2-7/Logo4.png >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
            ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" rm -f /usr/share/gdm/themes/win2-7/screenshot.png >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
            ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" rm -f /usr/share/gdm/themes/win2-7/screenshot3.png >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
            ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" rm -f /usr/share/gdm/themes/win2-7/screenshot4.png >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
            ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" mv /usr/share/gdm/themes/win2-7/Logo2.png /usr/share/gdm/themes/win2-7/Logo.png >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
            ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" mv /usr/share/gdm/themes/win2-7/screenshot2.png /usr/share/gdm/themes/win2-7/screenshot.png >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK

   	 elif UVERSION == "PCLinuxOS":
            ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" rm -f /usr/share/gdm/themes/win2-7/Logo.png >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
            ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" rm -f /usr/share/gdm/themes/win2-7/Logo2.png >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
            ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" rm -f /usr/share/gdm/themes/win2-7/Logo4.png >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
            ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" rm -f /usr/share/gdm/themes/win2-7/screenshot.png >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
            ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" rm -f /usr/share/gdm/themes/win2-7/screenshot2.png >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
            ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" rm -f /usr/share/gdm/themes/win2-7/screenshot4.png >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
            ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" mv /usr/share/gdm/themes/win2-7/Logo3.png /usr/share/gdm/themes/win2-7/Logo.png >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
            ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" mv /usr/share/gdm/themes/win2-7/screenshot3.png /usr/share/gdm/themes/win2-7/screenshot.png >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK

   	 elif UVERSION == "CentOS":
            ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" rm -f /usr/share/gdm/themes/win2-7/Logo.png >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
            ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" rm -f /usr/share/gdm/themes/win2-7/Logo2.png >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
            ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" rm -f /usr/share/gdm/themes/win2-7/Logo3.png >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
            ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" rm -f /usr/share/gdm/themes/win2-7/screenshot.png >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
            ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" rm -f /usr/share/gdm/themes/win2-7/screenshot2.png >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
            ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" rm -f /usr/share/gdm/themes/win2-7/screenshot3.png >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
            ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" mv /usr/share/gdm/themes/win2-7/Logo4.png /usr/share/gdm/themes/win2-7/Logo.png >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
            ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" mv /usr/share/gdm/themes/win2-7/screenshot4.png /usr/share/gdm/themes/win2-7/screenshot.png >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK

   	 elif UVERSION == "Ubuntu94":
            ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" rm -f /usr/share/gdm/themes/win2-7/Logo2.png >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
            ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" rm -f /usr/share/gdm/themes/win2-7/Logo3.png >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
            ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" rm -f /usr/share/gdm/themes/win2-7/Logo4.png >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
            ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" rm -f /usr/share/gdm/themes/win2-7/screenshot2.png >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
            ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" rm -f /usr/share/gdm/themes/win2-7/screenshot3.png >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
            ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" rm -f /usr/share/gdm/themes/win2-7/screenshot4.png >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK

         ERRORLEVEL = os.system('gconftool-2 --set /apps/win2-7pack/gdm_theme --type string Installed') ; STATUSCHECK
         RESOLVE_ERRORLEVEL()

   # Copying Plymouth Themes:
   if (PLYMOUTHTHEMEINSTALLED == "Yes") and (GRAPHICS == "Yes") and (RESTRICTEDEXTRAS == "Yes"):
      if (UVERSION == "Ubuntu104") or (UVERSION == "Ubuntu1010") or (UVERSION == "Ubuntu114"):
         TERMINAL_STATUS(WORD390,"BUSY")
         ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" tar xzvf Files/plymouth/7.tar.gz -C /lib/plymouth/themes/ >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
         ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" tar xzvf Files/plymouth/winbuntu.tar.gz -C /lib/plymouth/themes/ >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
         ERRORLEVEL = os.system('gconftool-2 --set /apps/win2-7pack/plymouth_theme --type string Installed') ; STATUSCHECK
         RESOLVE_ERRORLEVEL()
   
   # Copying OpenOffice Splash Theme:

   # Intro Graphic:
   if os.path.exists("/usr/lib/openoffice/program/openintro_ubuntu_sun.bmp") == True:
      TERMINAL_STATUS(WORD391,"BUSY")
      if os.path.exists("/usr/lib/openoffice/program/openintro_ubuntu_sun1.bmp") == False:
         ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" mv /usr/lib/openoffice/program/openintro_ubuntu_sun.bmp /usr/lib/openoffice/program/openintro_ubuntu_sun1.bmp >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
      ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" cp Files/Openoffice/program/intro.bmp /usr/lib/openoffice/program/openintro_ubuntu_sun.bmp >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
      OPENOFFICE_COMPLETE="YES"
   
   elif os.path.exists("/usr/lib/openoffice/program/openintro_ubuntu_oracle.bmp") == True:
      TERMINAL_STATUS(WORD391,"BUSY")
      if os.path.exists("/usr/lib/openoffice/program/openintro_ubuntu_oracle1.bmp") == False:
         ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" mv /usr/lib/openoffice/program/openintro_ubuntu_oracle.bmp /usr/lib/openoffice/program/openintro_ubuntu_oracle1.bmp >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
      ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" cp Files/Openoffice/program/intro.bmp /usr/lib/openoffice/program/openintro_ubuntu_oracle.bmp >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK    
      OPENOFFICE_COMPLETE="YES"
   
   elif os.path.exists("/opt/openoffice.org3/program/intro.bmp") == True:
      TERMINAL_STATUS(WORD391,"BUSY")
      if os.path.exists("/opt/openoffice.org3/program/intro1.bmp") == False:
         ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" mv /opt/openoffice.org3/program/intro.bmp /opt/openoffice.org3/program/intro1.bmp >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
      ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" cp Files/Openoffice/program/intro.bmp /opt/openoffice.org3/program/intro.bmp >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK   
      OPENOFFICE_COMPLETE="YES"
   
   elif os.path.exists("/usr/lib/openoffice/program/intro.bmp") == True:
      TERMINAL_STATUS(WORD391,"BUSY")
      if os.path.exists("/usr/lib/openoffice/program/intro1.bmp") == False:
         ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" mv /usr/lib/openoffice/program/intro.bmp /usr/lib/openoffice/program/intro1.bmp >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
      ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" cp Files/Openoffice/program/intro.bmp /usr/lib/openoffice/program/intro.bmp >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
      OPENOFFICE_COMPLETE="YES"
   
   elif os.path.exists("/usr/lib/openoffice.org3/program/intro.bmp") == True:
      TERMINAL_STATUS(WORD391,"BUSY")
      if os.path.exists("/usr/lib/openoffice.org3/program/intro1.bmp") == False:
         ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" mv /usr/lib/openoffice.org3/program/intro.bmp /usr/lib/openoffice.org3/program/intro1.bmp >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
      ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" cp Files/Openoffice/program/intro.bmp /usr/lib/openoffice.org3/program/intro.bmp >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
      OPENOFFICE_COMPLETE="YES"
   
   elif os.path.exists("/usr/lib/ooo/program/openintro_mandriva.bmp") == True:
      TERMINAL_STATUS(WORD391,"BUSY")
      if os.path.exists("/usr/lib/ooo/program/openintro_mandriva1.bmp") == False:
         ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" mv /usr/lib/ooo/program/openintro_mandriva.bmp /usr/lib/ooo/program/openintro_mandriva1.bmp >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
      ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" cp Files/Openoffice/program/intro.bmp /usr/lib/ooo/program/openintro_mandriva.bmp >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
      OPENOFFICE_COMPLETE="YES"
   
   elif os.path.exists("/usr/share/ooo3/program/intro.png") == True:
      TERMINAL_STATUS(WORD391,"BUSY")
      if os.path.exists("/usr/share/ooo3/program/intro.png") == False:
         ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" mv /usr/share/ooo3/program/intro.png /usr/share/ooo3/program/intro1.png >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
      ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" cp Files/Openoffice/program/intro.png /usr/share/ooo3/program/intro.png >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
      OPENOFFICE_COMPLETE="YES"
   
   elif os.path.exists("/usr/share/ooo3/program/intro.bmp") == True:
      TERMINAL_STATUS(WORD391,"BUSY")
      if os.path.exists("/usr/share/ooo3/program/intro1.bmp") == False:
         ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" mv /usr/share/ooo3/program/intro.bmp /usr/share/ooo3/program/intro1.bmp >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
      ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" cp Files/Openoffice/program/intro.bmp /usr/share/ooo3/program/intro.bmp >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
      OPENOFFICE_COMPLETE="YES"


   # About graphic:
   if os.path.exists("/usr/lib/openoffice/program/openabout_ubuntu_sun.bmp") == True:
      if os.path.exists("/usr/lib/openoffice/program/openabout_ubuntu_sun1.bmp") == False:
         ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" mv /usr/lib/openoffice/program/openabout_ubuntu_sun.bmp /usr/lib/openoffice/program/openabout_ubuntu_sun1.bmp >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
      ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" cp Files/Openoffice/program/about.bmp /usr/lib/openoffice/program/openabout_ubuntu_sun.bmp >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK

   elif os.path.exists("/usr/lib/openoffice/program/openabout_ubuntu_oracle.bmp") == True:
      if os.path.exists("/usr/lib/openoffice/program/openabout_ubuntu_oracle1.bmp") == False:
         ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" mv /usr/lib/openoffice/program/openabout_ubuntu_oracle.bmp /usr/lib/openoffice/program/openabout_ubuntu_oracle1.bmp >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
      ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" cp Files/Openoffice/program/about.bmp /usr/lib/openoffice/program/openabout_ubuntu_oracle.bmp >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK

   elif os.path.exists("/opt/openoffice.org3/program/about.bmp") == True:
      if os.path.exists("/opt/openoffice.org3/program/about1.bmp") == False:
         ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" mv /opt/openoffice.org3/program/about.bmp /opt/openoffice.org3/program/about1.bmp >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
      ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" cp Files/Openoffice/program/about.bmp /opt/openoffice.org3/program/about.bmp >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK

   elif os.path.exists("/usr/lib/openoffice/program/about.bmp") == True:
      if os.path.exists("/usr/lib/openoffice/program/about1.bmp") == False:
         ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" mv /usr/lib/openoffice/program/about.bmp /usr/lib/openoffice/program/about1.bmp >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
      ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" cp Files/Openoffice/program/about.bmp /usr/lib/openoffice/program/about.bmp >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK

   elif os.path.exists("/usr/lib/openoffice/program/about.png") == True:
      if os.path.exists("/usr/lib/openoffice/program/about1.png") == False:
         ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" mv /usr/lib/openoffice/program/about.png /usr/lib/openoffice/program/about1.png >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
      ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" cp Files/Openoffice/program/about.png /usr/lib/openoffice/program/about.png >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK

   elif os.path.exists("/usr/lib/openoffice.org3/program/about.bmp") == True:
      if os.path.exists("/usr/lib/openoffice.org3/program/about1.bmp") == False:
         ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" mv /usr/lib/openoffice.org3/program/about.bmp /usr/lib/openoffice.org3/program/about1.bmp >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
      ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" cp Files/Openoffice/program/about.bmp /usr/lib/openoffice.org3/program/about.bmp >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK

   elif os.path.exists("/usr/lib/ooo/program/openabout_mandriva.bmp") == True:
      if os.path.exists("/usr/lib/ooo/program/openabout_mandriva1.bmp") == False:
         ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" mv /usr/lib/ooo/program/openabout_mandriva.bmp /usr/lib/ooo/program/openabout_mandriva1.bmp >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
      ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" cp Files/Openoffice/program/about.bmp /usr/lib/ooo/program/openabout_mandriva.bmp >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK

   elif os.path.exists("/usr/share/ooo3/program/about.png") == True:
      if os.path.exists("/usr/share/ooo3/program/about1.png") == False:
         ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" mv /usr/share/ooo3/program/about.png /usr/share/ooo3/program/about1.png >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
      ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" cp Files/Openoffice/program/about.png /usr/share/ooo3/program/about.png >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
   
   # Complete Openoffice:
   if OPENOFFICE_COMPLETE == "YES":
      ERRORLEVEL = os.system('gconftool-2 --set /apps/win2-7pack/openoffice_splash --type string Installed') ; STATUSCHECK
      RESOLVE_ERRORLEVEL()

   # If Win2-7 Restricted Extras is set to be installed, mark it as installed:
   if RESTRICTEDEXTRAS == "Yes":
      ERRORLEVEL = os.system('gconftool-2 --set /apps/win2-7pack/Win2-7_Restricted_Extras --type string Installed') ; STATUSCHECK

   # Assign Version Number:
   TERMINAL_STATUS(WORD392,"BUSY")
   ERRORLEVEL = os.system('gconftool-2 --set /apps/win2-7pack/current_version --type string \"%s\"' % (VERSION)) ; STATUSCHECK
   ERRORLEVEL = os.system('gconftool-2 --set /apps/win2-7pack/status --type string Installed') ; STATUSCHECK
   RESOLVE_ERRORLEVEL()

   sys.stdout.write("# \n")


# Apply Theme: =================================================================================================

# Configure Meta Data:
if (GVFSBININSTALLED == "Yes") and (UVERSION != "Debian"):
   TERMINAL_STATUS(WORD393,"BUSY")
   ERRORLEVEL = os.system('gvfs-set-attribute -t string \"%s\" metadata::custom-icon file:$HOME/.icons/\"%s\"/filesystems/folder-desktop.png' % (DESKTOP,ICONBRAND)) ; STATUSCHECK
   RESOLVE_ERRORLEVEL()

# Configure Nautilus and Root:
TERMINAL_STATUS(WORD394,"BUSY")

if os.path.exists("/root/.icons") == False:
   os.system('echo \"%s\" | sudo -S -p \"\" ln -s $HOME/.icons/ /root/ >> /dev/null 2>&1' % (PASS))

if os.path.exists("/root/.themes") == False:
   os.system('echo \"%s\" | sudo -S -p \"\" ln -s $HOME/.themes/ /root/ >> /dev/null 2>&1' % (PASS))

if os.path.exists("/root/.fonts") == False:
   os.system('echo \"%s\" | sudo -S -p \"\" ln -s $HOME/.fonts/ /root/ >> /dev/null 2>&1' % (PASS))

ERRORLEVEL = os.system('gconftool-2 --set /apps/nautilus/preferences/background_set --type bool FALSE') ; STATUSCHECK

RESOLVE_ERRORLEVEL()

# Configure Nautilus and Root:
TERMINAL_STATUS(WORD395,"BUSY")

if ELEMENTRYNINSTALLED == "Yes":

   ERRORLEVEL = os.system('gconftool-2 --set /apps/nautilus/preferences/pathbar_in_toolbar          --type bool TRUE') ; STATUSCHECK
   ERRORLEVEL = os.system('gconftool-2 --set /apps/nautilus/preferences/rgba_colormap               --type bool TRUE') ; STATUSCHECK
   ERRORLEVEL = os.system('gconftool-2 --set /apps/nautilus/preferences/show_zoom_slider            --type bool TRUE') ; STATUSCHECK
   ERRORLEVEL = os.system('gconftool-2 --set /apps/nautilus/preferences/show_zoom_slider_icons      --type bool TRUE') ; STATUSCHECK
   ERRORLEVEL = os.system('gconftool-2 --set /apps/nautilus/preferences/toolbar_horizontal          --type INTEGER 1') ; STATUSCHECK
   ERRORLEVEL = os.system('gconftool-2 --set /apps/nautilus/preferences/sidebar_show_places_menu    --type bool FALSE') ; STATUSCHECK
   ERRORLEVEL = os.system('gconftool-2 --set /apps/nautilus/preferences/sidebar_width               --type INTEGER 155') ; STATUSCHECK
   ERRORLEVEL = os.system('gconftool-2 --set /apps/nautilus/preferences/side_pane_background_color  --type string \"#F0F4FA\"') ; STATUSCHECK
   ERRORLEVEL = os.system('gconftool-2 --set /apps/nautilus/preferences/side_pane_background_set    --type bool TRUE') ; STATUSCHECK
   ERRORLEVEL = os.system('gconftool-2 --set /apps/nautilus/preferences/side_pane_view              --type string NautilusPlacesSidebar') ; STATUSCHECK
   ERRORLEVEL = os.system('gconftool-2 --set /apps/nautilus/preferences/start_with_location_bar     --type bool TRUE') ; STATUSCHECK
   ERRORLEVEL = os.system('gconftool-2 --set /apps/nautilus/preferences/start_with_sidebar          --type bool TRUE') ; STATUSCHECK
   ERRORLEVEL = os.system('gconftool-2 --set /apps/nautilus/preferences/start_with_status_bar       --type bool TRUE') ; STATUSCHECK
   ERRORLEVEL = os.system('gconftool-2 --set /apps/nautilus/preferences/start_with_toolbar          --type bool TRUE') ; STATUSCHECK
   ERRORLEVEL = os.system('gconftool-2 --set /apps/nautilus/preferences/toolbar_horizontal          --type INTEGER 1') ; STATUSCHECK
   ERRORLEVEL = os.system('gconftool-2 --set /apps/nautilus/preferences/view_switcher_miniwidget    --type bool TRUE') ; STATUSCHECK
   ERRORLEVEL = os.system('gconftool-2 --set /apps/nautilus/preferences/view_switcher_widget        --type INTEGER 1') ; STATUSCHECK
   ERRORLEVEL = os.system('gconftool-2 --set /apps/nautilus/preferences/toolbar_items               --type list --list-type=string \"%s\"' % (EDESKTOPCONFIG))
   
   if EDESKTOPMENU == "YES":
      ERRORLEVEL = os.system('gconftool-2 --set /apps/nautilus/preferences/start_with_menubar       --type bool TRUE') ; STATUSCHECK
   else:
      ERRORLEVEL = os.system('gconftool-2 --set /apps/nautilus/preferences/start_with_menubar       --type bool FALSE') ; STATUSCHECK

ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" mkdir -p /root/.config/nautilus >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" chmod -R 777 /root/.config >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK

RESOLVE_ERRORLEVEL()

# Configure Breadcrumbs:
if ELEMENTRYNINSTALLED == "Yes":
   TERMINAL_STATUS(WORD396,"BUSY")
   if BCRUMBS == WORD584: 
      ERRORLEVEL = os.system('gconftool-2 --set "/apps/nautilus/preferences/pathbar_like_breadcrumbs"   --type bool FALSE') ; STATUSCHECK
      ERRORLEVEL = os.system('gconftool-2 --set "/apps/nautilus/preferences/always_use_location_entry"  --type bool FALSE') ; STATUSCHECK

   elif (BCRUMBS == "Aero") or (BCRUMBS == WORD582): 
      ERRORLEVEL = os.system('gconftool-2 --set "/apps/nautilus/preferences/pathbar_like_breadcrumbs"   --type bool TRUE') ; STATUSCHECK
      ERRORLEVEL = os.system('gconftool-2 --set "/apps/nautilus/preferences/always_use_location_entry"  --type bool FALSE') ; STATUSCHECK
      ERRORLEVEL = os.system('cp -r \"$HOME\"/.themes/$BCRUMBTHEME/nautilus \"$HOME\"/.themes/ >> /dev/null 2>&1') ; STATUSCHECK
      if INSTALLTYPE == "UPDATE":
         ERRORLEVEL = os.system('cp Files/murrine/Breadcrumb_Changer.sh \"%s\"' % (DESKTOP)) ; STATUSCHECK

   elif BCRUMBS == WORD610: 
      ERRORLEVEL = os.system('gconftool-2 --set "/apps/nautilus/preferences/pathbar_like_breadcrumbs"   --type bool FALSE') ; STATUSCHECK
      ERRORLEVEL = os.system('gconftool-2 --set "/apps/nautilus/preferences/always_use_location_entry"  --type bool TRUE') ; STATUSCHECK

   RESOLVE_ERRORLEVEL()

# Configuring RGBA Applications:
if (ELEMENTRYNINSTALLED == "Yes") and ("Aero" in GTKTHEME):
   TERMINAL_STATUS(WORD397,"BUSY")
   if RGBA_RHYTHMBOX == "YES":
      ERRORLEVEL = os.system('gconftool-2 --set /apps/rhythmbox/plugins/rgba-visual/active --type bool TRUE') ; STATUSCHECK
   if RGBA_GEDIT == "YES": 
      ERRORLEVEL = os.system('gconftool-2 --set /apps/gedit-2/plugins/active-plugins --type list --list-type=string [\'rgba-visual\',\'spell\',\'time\',\'changecase\',\'sort\',\'filebrowser\',\'taglist\']') ; STATUSCHECK
   RESOLVE_ERRORLEVEL()
   
# Restarting nautilus:
if ELEMENTRYNINSTALLED == "Yes":
   TERMINAL_STATUS(WORD185,"BUSY")
   ERRORLEVEL = os.system('killall nautilus > /dev/null 2>&1') ; STATUSCHECK
   time.sleep(10)
   RESOLVE_ERRORLEVEL()

# Configure Desktop Icon:
TERMINAL_STATUS(WORD398,"BUSY")
if UVERSION == "Debian":
   ERRORLEVEL = os.system('cp \"$HOME\"/.icons/\"%s\"/extras/desktop/\"%s\".png \"$HOME\"/.icons/\"%s\"/apps/desktop.png' % (ICONBRAND,DESK,ICONBRAND)) ; STATUSCHECK
else:
   ERRORLEVEL = os.system('cp \"$HOME\"/.icons/\"%s\"/extras/desktop/\"%s\".png \"$HOME\"/.icons/\"%s\"/apps/user-desktop.png' % (ICONBRAND,DESK,ICONBRAND)) ; STATUSCHECK
ERRORLEVEL = os.system('gconftool-2 --set /desktop/gnome/interface/icon_theme --type string \"%s\"' % (ICONBRAND)) ; STATUSCHECK
RESOLVE_ERRORLEVEL()

# Configure Gnome-Panel:
if SUPERBAR == "YES":
   TERMINAL_STATUS(WORD399,"BUSY")
   if WINMAN == "Lister":
      if UVERSION == "Ubuntu94":
         ERRORLEVEL = os.system('gconftool-2 --load Files/config/Panel_Menu_Lister_94.xml') ; STATUSCHECK
      elif UVERSION == "Ubuntu114":
         ERRORLEVEL = os.system('gconftool-2 --load Files/config/Panel_Menu_Lister_Ubuntu114.xml') ; STATUSCHECK
      elif UVERSION == "Fedora":
         ERRORLEVEL = os.system('gconftool-2 --load Files/config/Panel_Menu_Lister_Fedora.xml') ; STATUSCHECK
      elif UVERSION == "Mint11":
         ERRORLEVEL = os.system('gconftool-2 --load Files/config/Panel_Menu_Lister_Mint11.xml') ; STATUSCHECK
      elif "Mint" in UVERSION: # All other Mints
         ERRORLEVEL = os.system('gconftool-2 --load Files/config/Panel_Menu_Lister.xml') ; STATUSCHECK
      elif UVERSION == "PCLinuxOS":
	 ERRORLEVEL = os.system('gconftool-2 --load Files/config/Panel_Menu_Lister_PCLinuxOS.xml') ; STATUSCHECK
      elif UVERSION == "Debian":      
         ERRORLEVEL = os.system('gconftool-2 --load Files/config/Panel_Menu_Lister_Debian.xml') ; STATUSCHECK
      elif UVERSION == "CentOS": 
         ERRORLEVEL = os.system('gconftool-2 --load Files/config/Panel_Menu_Lister_CentOS.xml') ; STATUSCHECK
      elif UVERSION == "Mandriva": 
         ERRORLEVEL = os.system('gconftool-2 --load Files/config/Panel_Lister_Mandriva.xml') ; STATUSCHECK
      elif UVERSION == "openSUSE": 
         ERRORLEVEL = os.system('gconftool-2 --load Files/config/Panel_Lister_openSUSE.xml') ; STATUSCHECK
      else: # (meant for *Ubuntu*)
         ERRORLEVEL = os.system('gconftool-2 --load Files/config/Panel_Menu_Lister.xml') ; STATUSCHECK
   else:
      if UVERSION == "Ubuntu94": 
          ERRORLEVEL = os.system('gconftool-2 --load Files/config/Panel_Menu_DockBarX_94.xml') ; STATUSCHECK
      elif UVERSION == "Fedora":
          ERRORLEVEL = os.system('gconftool-2 --load Files/config/Panel_Menu_DockBarX_Fedora.xml') ; STATUSCHECK
      else:
          ERRORLEVEL = os.system('gconftool-2 --load Files/config/Panel_Menu_DockBarX.xml') ; STATUSCHECK
   RESOLVE_ERRORLEVEL()

# Configure Time/Date Format:
TERMINAL_STATUS(WORD400,"BUSY")
if UVERSION == "CentOS":
   if TIMEFORMAT == "USNormal":
      ERRORLEVEL = os.system('gconftool-2 --set /apps/panel/applets/applet_4/prefs/custom_format --type string \"%l:%M %p%n%m/%d/%Y\"') ; STATUSCHECK

   elif TIMEFORMAT == "USMilitary":
      ERRORLEVEL = os.system('gconftool-2 --set /apps/panel/applets/applet_4/prefs/custom_format --type string \"%H:%M %n%m/%d/%Y\"') ; STATUSCHECK

   elif TIMEFORMAT == "EUNormal":
      ERRORLEVEL = os.system('gconftool-2 --set /apps/panel/applets/applet_4/prefs/custom_format --type string \"%l:%M %p%n%d/%m/%Y\"') ; STATUSCHECK

   elif TIMEFORMAT == "EUMilitary":
      ERRORLEVEL = os.system('gconftool-2 --set /apps/panel/applets/applet_4/prefs/custom_format --type string \"%H:%M %n%d/%m/%Y\"') ; STATUSCHECK
else:
   if TIMEFORMAT == "USNormal":
      ERRORLEVEL = os.system('gconftool-2 --set /apps/panel/applets/applet_4/prefs/custom_format --type string \"<span font_desc=\'Trebuchet\ MS\ 8.0\' weight=\'bold\'>%l:%M %p%n%m/%d/%Y</span>\"') ; STATUSCHECK

   elif TIMEFORMAT == "USMilitary":
      ERRORLEVEL = os.system('gconftool-2 --set /apps/panel/applets/applet_4/prefs/custom_format --type string \"<span font_desc=\'Trebuchet\ MS\ 8.0\' weight=\'bold\'>%H:%M %n%m/%d/%Y</span>\"') ; STATUSCHECK

   elif TIMEFORMAT == "EUNormal": 
      ERRORLEVEL = os.system('gconftool-2 --set /apps/panel/applets/applet_4/prefs/custom_format --type string \"<span font_desc=\'Trebuchet\ MS\ 8.0\' weight=\'bold\'>%l:%M %p%n%d/%m/%Y</span>\"') ; STATUSCHECK

   elif TIMEFORMAT == "EUMilitary": 
      ERRORLEVEL = os.system('gconftool-2 --set /apps/panel/applets/applet_4/prefs/custom_format --type string \"<span font_desc=\'Trebuchet\ MS\ 8.0\' weight=\'bold\'>%H:%M %n%d/%m/%Y</span>\"') ; STATUSCHECK
RESOLVE_ERRORLEVEL()

# Configure DockBarX:
if (DOCKBARXINSTALLED == "Yes") and (INSTALLTYPE != "UPGRADE"):
   TERMINAL_STATUS(WORD401,"BUSY")
   if UVERSION == "Fedora":
      ERRORLEVEL = os.system('gconftool-2 --set "/apps/dockbarx/launchers" --type list --list-type=string [firefox;/usr/share/applications/mozilla-firefox.desktop,rhythmbox;/usr/share/applications/rhythmbox.desktop]') ; STATUSCHECK
   elif (UVERSION == "Ubuntu114") or (UVERSION == "Mint11"):
      ERRORLEVEL = os.system('gconftool-2 --set "/apps/dockbarx/launchers" --type list --list-type=string [\'Firefox;gio:firefox\',\'Nautilus;gio:nautilus\',\'Banshee;gio:banshee\']'); STATUSCHECK
   else:
      ERRORLEVEL = os.system('gconftool-2 --set "/apps/dockbarx/launchers" --type list --list-type=string [\'Firefox;gio:firefox\',\'Nautilus;gio:nautilus\',\'Rhythmbox;gio:rhythmbox\']'); STATUSCHECK
   if ALLWORKSPACES == "YES":
      ERRORLEVEL = os.system('gconftool-2 --set "/apps/dockbarx/show_only_current_desktop" --type bool false') ; STATUSCHECK
   else:
      ERRORLEVEL = os.system('gconftool-2 --set "/apps/dockbarx/show_only_current_desktop" --type bool true') ; STATUSCHECK
   ERRORLEVEL = os.system(' gconftool-2 --set "/apps/dockbarx/theme" --type string "Shinybar1.3 Horizontal"') ; STATUSCHECK
   RESOLVE_ERRORLEVEL()
   
# Configure Panel Colour:
TERMINAL_STATUS(WORD402,"BUSY")
ERRORLEVEL = os.system('gconftool-2 --set /apps/panel/toplevels/bottom_panel_0/background/image --type string \"$HOME\"/.themes/Win2-7\(Pixmap\)/gtk-2.0/Panel/\"%s\"' % (PANELSTYLECOLOR)) ; STATUSCHECK
ERRORLEVEL = os.system('gconftool-2 --set /apps/panel/toplevels/bottom_panel_0/background/type --type string image') ; STATUSCHECK
RESOLVE_ERRORLEVEL()

# Configure Start Menu Logo:
TERMINAL_STATUS(WORD403,"BUSY")
ERRORLEVEL = os.system('gconftool-2 --set /apps/panel/objects/object_0/custom_icon --type string \"$HOME\"/.icons/\"%s\"/extras/start-here/\"%s\".png' % (ICONBRAND,STARTUP)) ; STATUSCHECK
ERRORLEVEL = os.system('gconftool-2 --set /apps/panel/objects/object_0/use_custom_icon --type bool true') ; STATUSCHECK
RESOLVE_ERRORLEVEL()

# Restarting Panel:
if UVERSION != "openSUSE":
   TERMINAL_STATUS(WORD284,"BUSY")
   ERRORLEVEL = os.system('killall gnome-panel') ; STATUSCHECK
   time.sleep(10)
   RESOLVE_ERRORLEVEL()

# Configure Desktop Icons:
TERMINAL_STATUS(WORD404,"BUSY")

if DESKTOPREMOVABLEDEVICES == "1":
   ERRORLEVEL = os.system('gconftool-2 --set /apps/nautilus/desktop/volumes_visible       --type bool true') ; STATUSCHECK
else:
   ERRORLEVEL = os.system('gconftool-2 --set /apps/nautilus/desktop/volumes_visible       --type bool false') ; STATUSCHECK

if DESKTOPCOMPUTER == "1":
   ERRORLEVEL = os.system('gconftool-2 --set /apps/nautilus/desktop/computer_icon_visible --type bool true') ; STATUSCHECK
   if UNKNOWN_LANG != "Yes":
      ERRORLEVEL = os.system('gconftool-2 --set /apps/nautilus/desktop/computer_icon_name    --type string \"%s\"' % (COMPUTER_ICON_NAME)) ; STATUSCHECK
else:
   ERRORLEVEL = os.system('gconftool-2 --set "/apps/nautilus/desktop/computer_icon_visible" --type bool false') ; STATUSCHECK

if DESKTOPHOMEFOLDER == "1":
   ERRORLEVEL = os.system('gconftool-2 --set /apps/nautilus/desktop/home_icon_visible     --type bool true') ; STATUSCHECK
   ERRORLEVEL = os.system('gconftool-2 --set /apps/nautilus/desktop/home_icon_name        --type string \"%s\"' % (PUSERNAME)) ; STATUSCHECK
else:
   ERRORLEVEL = os.system('gconftool-2 --set /apps/nautilus/desktop/home_icon_visible     --type bool false') ; STATUSCHECK

if DESKTOPRECYLEBIN == "1":
   ERRORLEVEL = os.system('gconftool-2 --set /apps/nautilus/desktop/trash_icon_visible    --type bool true') ; STATUSCHECK
   if UNKNOWN_LANG != "Yes":
      ERRORLEVEL = os.system('gconftool-2 --set /apps/nautilus/desktop/trash_icon_name       --type string \"%s\"' % (RECYCLEBIN_ICON_NAME)) ; STATUSCHECK
else:
   ERRORLEVEL = os.system('gconftool-2 --set /apps/nautilus/desktop/trash_icon_visible    --type bool false') ; STATUSCHECK

if DESKTOPNETWORK == "1":
   ERRORLEVEL = os.system('gconftool-2 --set /apps/nautilus/desktop/network_icon_visible  --type bool true') ; STATUSCHECK
   if UNKNOWN_LANG != "Yes":
      ERRORLEVEL = os.system('gconftool-2 --set /apps/nautilus/desktop/network_icon_name     --type string \"%s\"' % (NETWORK_ICON_NAME)) ; STATUSCHECK
else:
   ERRORLEVEL = os.system('gconftool-2 --set /apps/nautilus/desktop/network_icon_visible  --type bool false') ; STATUSCHECK

RESOLVE_ERRORLEVEL()

# Configure Terminal Theme:
TERMINAL_STATUS(WORD405,"BUSY")
ERRORLEVEL = os.system('gconftool-2 --set /apps/gnome-terminal/profiles/Default/background_color --type string black') ; STATUSCHECK
ERRORLEVEL = os.system('gconftool-2 --set /apps/gnome-terminal/profiles/Default/foreground_color --type string white') ; STATUSCHECK
ERRORLEVEL = os.system('gconftool-2 --set /apps/gnome-terminal/profiles/Default/use_theme_colors  --type bool false') ; STATUSCHECK
RESOLVE_ERRORLEVEL()

# Metacity Buttons
if (UVERSION == "Ubuntu104") or (UVERSION == "Ubuntu1010") or (UVERSION == "Ubuntu114"):
   TERMINAL_STATUS(WORD406,"BUSY")
   ERRORLEVEL = os.system('gconftool-2 --set /apps/metacity/general/button_layout --type string menu:minimize,maximize,close') ; STATUSCHECK
   RESOLVE_ERRORLEVEL()

# Configure Metacity Theme:
TERMINAL_STATUS(WORD407,"BUSY")
ERRORLEVEL = os.system('gconftool-2 --set /apps/metacity/general/theme --type string \"%s\"' % (METACITYTHEME)) ; STATUSCHECK
RESOLVE_ERRORLEVEL()

# Configure GTK Theme:
TERMINAL_STATUS(WORD408,"BUSY")
ERRORLEVEL = os.system('gconftool-2 --set /desktop/gnome/interface/gtk_theme --type string \"%s\"' % (GTKTHEME)) ; STATUSCHECK
RESOLVE_ERRORLEVEL()

# Configure Mouse:
if RESTRICTEDEXTRAS == "Yes":
   TERMINAL_STATUS(WORD409,"BUSY")
   ERRORLEVEL = os.system('gconftool-2 --set /desktop/gnome/peripherals/mouse/cursor_theme --type string aero-drop') ; STATUSCHECK
   RESOLVE_ERRORLEVEL()

# Configure Fonts:
if RESTRICTEDEXTRAS == "Yes":
   TERMINAL_STATUS(WORD410,"BUSY")
   ERRORLEVEL = os.system('gconftool-2 --set /desktop/gnome/interface/document_font_name --type string \"Segoe UI 10\"') ; STATUSCHECK
   ERRORLEVEL = os.system('gconftool-2 --set /desktop/gnome/interface/font_name          --type string \"Segoe UI 10\"') ; STATUSCHECK
   ERRORLEVEL = os.system('gconftool-2 --set /desktop/gnome/interface/document_font_name --type string \"Segoe UI 10\"') ; STATUSCHECK
   ERRORLEVEL = os.system('gconftool-2 --set /apps/metacity/general/titlebar_font        --type string \"Segoe UI 10\"') ; STATUSCHECK
   ERRORLEVEL = os.system('gconftool-2 --set /apps/nautilus/preferences/desktop_font     --type string \"Segoe UI 10\"') ; STATUSCHECK
   RESOLVE_ERRORLEVEL()

# Configure Emerald Theme:
if EMERALDINSTALLED == "Yes":
   TERMINAL_STATUS(WORD411,"BUSY")
   if (os.path.exists(USER + "/.emerald/theme.old") == False) and (os.path.exists("\"$HOME\"/.emerald/theme") == True):
      ERRORLEVEL = os.system('mv \"$HOME\"/.emerald/theme \"$HOME\"/.emerald/theme.old') ; STATUSCHECK
   ERRORLEVEL = os.system('rm -r -f \"$HOME\"/.emerald/theme/*') ; STATUSCHECK
   ERRORLEVEL = os.system('cp -r \"$HOME\"/.emerald/themes/\"%s\"/* \"$HOME\"/.emerald/theme' % (ETHEME)) ; STATUSCHECK
   RESOLVE_ERRORLEVEL()

# Configure Plymouth Theme:
if (PLYMOUTHTHEMEINSTALLED == "Yes") and (GRAPHICS == "Yes") and (RESTRICTEDEXTRAS == "Yes"):
   if (UVERSION == "Ubuntu104") or (UVERSION == "Ubuntu1010") or (UVERSION == "Ubuntu114"):
      if (os.path.exists("/lib/plymouth/themes/7") == True) and (os.path.exists("/lib/plymouth/themes/winbuntu") == True):
         TERMINAL_STATUS(WORD412,"BUSY")
         ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" sed -i \'s/\/usr\/share\//\/lib\//g\' /lib/plymouth/themes/\"%s\"/\"%s\".plymouth >> /dev/null 2>&1' % (PASS,PLYMOUTHTHEME,PLYMOUTHTHEME)) ; STATUSCHECK
         ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" rm -f /etc/alternatives/default.plymouth >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
         ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" ln -s /lib/plymouth/themes/\"%s\"/\"%s\".plymouth /etc/alternatives/default.plymouth >> /dev/null 2>&1' % (PASS,PLYMOUTHTHEME,PLYMOUTHTHEME)) ; STATUSCHECK
         RESOLVE_ERRORLEVEL()
         TERMINAL_STATUS(WORD413,"BUSY")
         ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" update-initramfs -u -k all >> /dev/null 2>&1' % (PASS)) ; STATUSCHECK
         RESOLVE_ERRORLEVEL()

# Configure CCSM:
if (CCSMINSTALLED == "Yes") and (UVERSION == "CentOS"):
   TERMINAL_STATUS(WORD413,"BUSY")
   ERRORLEVEL = os.system('cp Files/compiz/Win2-7_CCSM.profile \"%s\"' % (DESKTOP)) ; STATUSCHECK
   ERRORLEVEL = os.system('cp Files/compiz/CompizReadMe.txt \"%s\"' % (DESKTOP)) ; STATUSCHECK
   RESOLVE_ERRORLEVEL()

# Configure Lock Theme:
if (UVERSION != "Debian") and (UVERSION != "CentOS"):
   TERMINAL_STATUS(WORD414,"BUSY")
   ERRORLEVEL = os.system('gconftool-2 --set /apps/gnome-screensaver/lock_dialog_theme --type string win2-7') ; STATUSCHECK
   RESOLVE_ERRORLEVEL()

# Configure Gnome:
TERMINAL_STATUS(WORD415,"BUSY")
ERRORLEVEL = os.system('gconftool-2 --set /desktop/gnome/interface/toolbar_style --type string both-horiz') ; STATUSCHECK
ERRORLEVEL = os.system('gconftool-2 --set /desktop/gnome/interface/menus_have_icons --type Boolean TRUE') ; STATUSCHECK
RESOLVE_ERRORLEVEL()

# Configure Sounds:
if (UVERSION != "Debian") and (UVERSION != "CentOS") and (RESTRICTEDEXTRAS == "Yes"):
   TERMINAL_STATUS(WORD416,"BUSY")
   ERRORLEVEL = os.system('gconftool-2 --set /desktop/gnome/sound/enable_esd --type Boolean TRUE') ; STATUSCHECK
   ERRORLEVEL = os.system('gconftool-2 --set /desktop/gnome/sound/event_sounds --type Boolean TRUE') ; STATUSCHECK
   ERRORLEVEL = os.system('gconftool-2 --set /desktop/gnome/sound/input_feedback_sounds --type Boolean TRUE') ; STATUSCHECK
   ERRORLEVEL = os.system('gconftool-2 --set /desktop/gnome/sound/theme_name --type string Win2-7') ; STATUSCHECK
   RESOLVE_ERRORLEVEL()

# Configure Mail Reader:
if GNOMENUINSTALLED == "Yes":
   TERMINAL_STATUS(WORD417,"BUSY")
   ERRORLEVEL = os.system('gconftool-2 --set /desktop/gnome/url-handlers/mailto/command --type string \"firefox %s\"' % (URL)) ; STATUSCHECK
   RESOLVE_ERRORLEVEL()

# Configure GDM2 Elements:
if GDM == "2":
   if (UVERSION == "Ubuntu114") or (UVERSION == "Ubuntu104") or (UVERSION == "Ubuntu1010") or (UVERSION == "Mint9") or (UVERSION == "Mint10") or (UVERSION == "Mint11") or (UVERSION == "Mandriva") or (UVERSION == "Fedora") or (UVERSION == "openSUSE"):
      TERMINAL_STATUS(WORD419,"BUSY")
      ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" -u gdm gconftool-2 --type string --set /desktop/gnome/background/picture_filename \"%s\"/.backgrounds/Win2-7.jpg >> /dev/null 2>&1' % (PASS,USER)) ; STATUSCHECK
      ERRORLEVEL = os.system('gconftool-2 --set /apps/win2-7pack/gdm2_theme --type string Installed') ; STATUSCHECK
      RESOLVE_ERRORLEVEL()

# Configure GDM3 Elements:
if GDM == "3":
   TERMINAL_STATUS(WORD420,"BUSY")
   ERRORLEVEL = os.system('echo \"%s\" | sudo -S -p \"\" chmod -R 777 /etc/gdm3 >> /dev/null 2>&1' % (PASS))
   ERRORLEVEL = os.system('cp /etc/gdm3/greeter.gconf-defaults /etc/gdm3/greeter.gconf-defaults.old') ; STATUSCHECK
   ERRORLEVEL = os.system('sed \'/picture_filename/d\' /etc/gdm3/greeter.gconf-defaults > /etc/gdm3/temp.tmp') ; STATUSCHECK
   ERRORLEVEL = os.system('sed \'/picture_options/d\' /etc/gdm3/temp.tmp > /etc/gdm3/greeter.gconf-defaults') ; STATUSCHECK
   ERRORLEVEL = os.system('rm -f /etc/gdm3/temp.tmp') ; STATUSCHECK
   ERRORLEVEL = os.system('echo \"\" >> /etc/gdm3/greeter.gconf-defaults') ; STATUSCHECK
   ERRORLEVEL = os.system('echo \"/desktop/gnome/background/picture_filename     \"%s\"/.backgrounds/Win2-7.jpg\" >> /etc/gdm3/greeter.gconf-defaults' % (USER)) ; STATUSCHECK
   ERRORLEVEL = os.system('echo \"/desktop/gnome/background/picture_options     zoom\" >> /etc/gdm3/greeter.gconf-defaults') ; STATUSCHECK
   ERRORLEVEL = os.system('gconftool-2 --set /apps/win2-7pack/gdm3_theme --type string Installed') ; STATUSCHECK
   RESOLVE_ERRORLEVEL()

# Configure Wallpaper:
if (INSTALLTYPE != "UPGRADE"):
   TERMINAL_STATUS(WORD421,"BUSY")
   if WALLPAPERNAME == WORD615:
#     WALLPAPERNAME="Win2-7Pixmap" ; STATUSCHECK
#     WALLPAPERFILESNAME="Win2-7Pixmap.jpg" ; STATUSCHECK
#     NONWALLPAPERNAME=WORD577 ; STATUSCHECK
#     NONWALLPAPERPATH="Win2-7.jpg" ; STATUSCHECK
      ERRORLEVEL = os.system('gconftool-2 --set /desktop/gnome/background/picture_filename --type string \"\"%s\"/Win2-7Pixmap.jpg\"' % (INSTALLWALLPAPERPATH)) ; STATUSCHECK
   else:
#     WALLPAPERNAME=WORD577 ; STATUSCHECK
#     WALLPAPERFILESNAME="Win2-7.jpg" ; STATUSCHECK
#     NONWALLPAPERNAME="Win2-7Pixmap" ; STATUSCHECK
#     NONWALLPAPERPATH="Win2-7Pixmap.jpg" ; STATUSCHECK
      ERRORLEVEL = os.system('gconftool-2 --set /desktop/gnome/background/picture_filename --type string \"\"%s\"/Win2-7.jpg\"' % (INSTALLWALLPAPERPATH)) ; STATUSCHECK

#   if RESTRICTEDEXTRAS == "Yes":
#      if ! grep -q "#FFFFFC" "$HOME/.gnome2/backgrounds.xml" 2>> "/dev/null" ; then
#         os.system('sed \'$d\' ~/.gnome2/backgrounds.xml >> ~/.gnome2/backgroundsModified.xml 2>> /dev/null')
#         rm -f ~/.gnome2/backgrounds.xml
#         mv ~/.gnome2/backgroundsModified.xml ~/.gnome2/backgrounds.xml
#         echo '  <wallpaper deleted="false">' >> ~/.gnome2/backgrounds.xml
#         echo "    <name>$NONWALLPAPERNAME</name>" >> ~/.gnome2/backgrounds.xml
#         echo "    <filename>$INSTALLWALLPAPERPATH/$NONWALLPAPERPATH</filename>" >> ~/.gnome2/backgrounds.xml
#         echo "    <options>zoom</options>" >> ~/.gnome2/backgrounds.xml
#         echo "    <shade_type>solid</shade_type>" >> ~/.gnome2/backgrounds.xml
#         echo "    <pcolor>#FFFFFC</pcolor>" >> ~/.gnome2/backgrounds.xml
#         echo "    <scolor>#142C3D</scolor>" >> ~/.gnome2/backgrounds.xml
#         echo "  </wallpaper>" >> ~/.gnome2/backgrounds.xml
#         echo "</wallpapers>" >> ~/.gnome2/backgrounds.xml

   ERRORLEVEL = os.system('gconftool-2 --set /desktop/gnome/background/picture_options --type string stretched') ; STATUSCHECK
   RESOLVE_ERRORLEVEL()

# Configure Metacity Compositing:
if METACITY_COMPOSITING == "YES":
   TERMINAL_STATUS(WORD422,"BUSY")
   ERRORLEVEL = os.system('gconftool-2 --type boolean --set /apps/metacity/general/compositing_manager TRUE') ; STATUSCHECK
   RESOLVE_ERRORLEVEL()
else:
   os.system('gconftool-2 --type boolean --set /apps/metacity/general/compositing_manager FALSE')

# Configuration Complete: =====================================================================================

sys.stdout.write(RESET + "# \n")
if ERROR_CATCH == "YES":
   sys.stdout.write(RESET + "# " + CBOLD + RED + WORD423)
else:
   sys.stdout.write(RESET + "# " + CBOLD + GREEN + WORD424 + "\n")

# Show Ending Documentation: ===================================================================================
PyZenity.InfoMessage(text=WORD427 + "\n\n" + WORD428 + "\n\n" + WORD435 + "\n\n" + WORD436 + "\n\n" + WORD437 + "\n\n" + WORD121 + "\n" + "http://gnome-look.org/content/show.php/Win2-7+Pack?content=113264", title=WORD17)

# Ask for a reboot :===========================================================================================
if GDM == "3":
#   RESPONSE = commands.getoutput('zenity --list --title="$WORD445" --text="$WORD446" --radiolist  --column="$WORD15" --column="$WORD14" TRUE "$WORD532" FALSE "$WORD240"')
   RESPONSE = PyZenity.List((WORD15,WORD14), text=WORD446, title=WORD445,  boolstyle="radiolist", editable=False, select_col=2, sep='|', data=[(True,WORD532),(False,WORD240)])

   if WORD532 in RESPONSE:
      os.system('echo \"%s\" | sudo -S -p \"\" reboot' % (PASS))
   else:
      ENTER_TO_CLOSE()

else:
#   RESPONSE = commands.getoutput('zenity --list --title="$WORD447" --text="$WORD448" --radiolist  --column="$WORD15" --column="$WORD14" TRUE "$WORD449" FALSE "$WORD240"')
   RESPONSE = PyZenity.List((WORD15,WORD14), text=WORD448, title=WORD447, boolstyle="radiolist", editable=False, select_col=2, sep='|', data=[(True,WORD449),(False,WORD240)])

   if WORD449 in RESPONSE:
      if (UVERSION == "Debian") or (UVERSION == "CentOS"):
         os.system('echo \"%s\" | sudo -S -p \"\" pkill -u \"%s\"' % (PASS,ME))
         exit()
      else:
         os.system('gnome-session-save --force-logout')
         exit()
   else:
      ENTER_TO_CLOSE()
