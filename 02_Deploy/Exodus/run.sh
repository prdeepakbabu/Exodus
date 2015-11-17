HOME="/home/dev/Exodus"
echo "Craw Job Started at `date`" >> $HOME/Logs/log.txt
echo "STAGE 1: crawling websites started at `date`" >> $HOME/Logs/log.txt
sh $HOME/macro.sh >> $HOME/macro.log 2>&1
echo "STAGE 2: Extraction of Ad Image URL and upload to S3 Started at `date`" >> $HOME/Logs/log.txt
sh $HOME/start.sh 
echo "STAGE 3: Uploading to mysql DB started at `date`" >> $HOME/Logs/log.txt
#python  $HOME/mysql/bulk_insert.py >/home/dev/null 2>&1 
echo "STAGE 4: Invoking email notification at `date`" >> $HOME/Logs/log.txt
#sh $HOME/mysql/cron_mail.sh
echo "Crawl job ended at `date`" >> $HOME/Logs/log.txt
