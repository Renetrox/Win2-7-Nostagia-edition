#!/bin/bash
# BY: Dart00

echo "$1" | sudo -S -p "" apt-get -y upgrade <<EOF
y
y
y
y
y
y
y
y
y
y
EOF
