#!/bin/bash

PPID=$(ps -p $$ | awk '{print $1}')


#copying the files from the doc-bd-a1 folder to the shared file
cp   /home/doc-bd-a1/* /service-result/
cd   /service-result/
rm   dpre.py eda.py vis.py model.py load.py train_titanic.csv final.sh



kill -KILL $PPID