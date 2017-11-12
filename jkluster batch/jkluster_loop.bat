@echo off
title Generate clusters
echo jkluster is running...

:: Calculate fingerprints
java -cp "C:\Program Files\ChemAxon\JChemSuite\lib\jchem.jar;%CLASSPATH%" chemaxon.descriptors.GenerateMD c molecules.sdf -k CF -c config\cfp.xml -D -g -v -o fingerprints.txt

:: Cluster generation
java -cp "C:\Program Files\ChemAxon\JChemSuite\lib\jchem.jar;%CLASSPATH%" chemaxon.clustering.Ward -f 2048 -c 20 -g -z -v -i fingerprints.txt -o clusters\list_of_clusters.txt

:: Export SDFs through 20 (number of clusters) times
for /L %%A in (1,1,20) do (
    java -cp "C:\Program Files\ChemAxon\JChemSuite\lib\jchem.jar;%CLASSPATH%" chemaxon.clustering.CreateView -i id -c "clid=%%A" -s molecules.sdf -t clusters\list_of_clusters.txt -o clusters\cluster%%A.sdf
    echo %%A clusters generated.
)

echo calculation completed.
pause