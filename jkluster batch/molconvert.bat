@echo off
title molconvert
@echo molconvert is running...

"molconvert.exe" inchikey temp.smiles -v -o temp.txt

echo calculation completed.
pause