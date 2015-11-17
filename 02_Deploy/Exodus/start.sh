home="/home/dev"

#logging
echo "Daily Job Started at `date`" >> $home/Exodus/Logs/log.txt

#copy html  files from macros
cnt_sites=`ls -lt $home/iMacros/Downloads | wc -l`
rm -f $home/Exodus/input/*
cp $home/iMacros/Downloads/* $home/Exodus/input

#run the python job to upload ads and create raw file
ext=`date +"%d%m%y%H%M%S"`
filename="url_$ext.csv"
python $home/Exodus/simple5.py > $home/Exodus/$filename 
cnt_images=`ls -lt $home/Exodus/input | grep 'img' | wc -l`
cnt_final=`cat $home/Exodus/$filename | wc -l`

#cleanup
rm -f $home/iMacros/Downloads/*	

#logging
echo "Total input sites processed is $cnt_sites; Total ad images found is $cnt_images; Total ad images uploaded and in DB is  $cnt_final" >> $home/Exodus/Logs/log.txt
echo "Daily Job Ended at `date`" >> $home/Exodus/Logs/log.txt
