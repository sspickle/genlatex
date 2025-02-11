#!/bin/bash

#
# assume we're in docker, everything is in src
#

echo "executing:" genlatex --src src $@

genlatex --src src $@

