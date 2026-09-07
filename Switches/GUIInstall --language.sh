#!/bin/bash

cd "`dirname \"$0\"`"

SWITCH="--language"

export SWITCH

cd ..

bash GUIInstall.sh "$SWITCH"

exit


