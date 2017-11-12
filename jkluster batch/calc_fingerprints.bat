@echo off
title Generate clusters
echo GenerateMD is running...

:: Calculate fingerprints
java -cp "C:\Program Files\ChemAxon\JChemSuite\lib\jchem.jar;%CLASSPATH%" chemaxon.descriptors.GenerateMD c molecules.sdf -k CF -c config\cfp.xml -D -g -v -o fingerprints.txt

echo calculation completed.
pause