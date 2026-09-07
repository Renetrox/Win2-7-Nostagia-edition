#!/bin/bash
# BY: Dart00

cd "`dirname \"$0\"`"

SWITCH="--reinstallmurrine"

export SWITCH

cd ..

bash GUIInstall.sh "$SWITCH"

exit

