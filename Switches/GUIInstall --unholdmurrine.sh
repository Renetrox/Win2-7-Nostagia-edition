#!/bin/bash
# BY: Dart00

cd "`dirname \"$0\"`"

SWITCH="--unholdmurrine"

export SWITCH

cd ..

bash GUIInstall.sh "$SWITCH"

exit


