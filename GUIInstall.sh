#!/bin/bash

cd "`dirname \"$0\"`"

case "$LANG" in
  fr* )
      LANGUAGE="French"
. Files/lang/French.py
	     ;;
#  es* )
#      LANGUAGE="Spanish"
#. Files/lang/Spanish.py
#	     ;;
#  pl* ) 
#      LANGUAGE="Polish"
#. Files/lang/Polish.py
#           ;;
#  pt_BR* ) 
#      LANGUAGE="BPortuguese"
#. Files/lang/BPortuguese.py
#           ;;
#  pt* ) 
#      LANGUAGE="EPortuguese"
#. Files/lang/EPortuguese.py
#           ;;
  ru* ) 
      LANGUAGE="Russian"
. Files/lang/Russian.py
           ;;
  da* ) 
      LANGUAGE="Danish"
. Files/lang/Danish.py
           ;;
  hr* ) 
      LANGUAGE="Croatian"
. Files/lang/Croatian.py
           ;;
  * ) 
      LANGUAGE="English"
. Files/lang/English.py
           ;;
esac

if [ "$SWITCH" = "" ]; then
   SWITCH="RUN"
fi

python -V > "/tmp/version.tmp" 2>&1

PYTHON=`cat /tmp/version.tmp`

rm -f "/tmp/version.tmp"

if [[ "$PYTHON" =~ "2.7" ]] || [[ "$PYTHON" =~ "2.6" ]] || [[ "$PYTHON" =~ "2.5" ]] || [[ "$PYTHON" =~ "2.4" ]]; then
   python Core.py "$SWITCH"
else
   zenity --error --text="$WORD1 $PYTHON. $WORD2"
   python Core.py "$SWITCH"
fi

exit


