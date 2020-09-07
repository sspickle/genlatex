#!/bin/bash

echo Runing buildTeXs, buildPDFs, buildZip.sh with args $@

/bin/bash buildTeXs.sh  $@

/bin/bash buildPDFs.sh

/bin/bash buildZip.sh

