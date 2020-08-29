
#
# The syntax of this 'find' is delicate. Don't prepend a './' or it messes up the slash calculation
#

find output -name "*.pdf" | xargs python buildManifest.py

cd output && zip ../../src/export.zip *.xml attachment/*/*/*/*.pdf && cd ..



