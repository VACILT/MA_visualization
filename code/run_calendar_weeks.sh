#!/bin/bash
# conda activate myenv
startdate='2021-01-04' # first Sunday this year
startdate='2015-06-07'
enddate='2021-08-01'
enddate='2021-10-31'


enddate=$( date -d "$enddate" +%Y%m%d )  # rewrite in YYYYMMDD format
thedate=$( date -d "$startdate" +%Y%m%d )
i=0
while [ $thedate -lt $enddate ]
do # [ "$thedate" <= "$enddate" ]
    thedate=$( date -d "$startdate + $i days" +%Y%m%d ) # get $i days forward
    #printf 'The date is "%s"\n' "$thedate"
    #echo $enddate
    i=$(( i + 6 ))
    anotherdate=$( date -d "$startdate + $i days" +%Y%m%d ) # get $i days forward
    echo $thedate $anotherdate
    /opt/matlab/r2020a/bin/matlab -nodisplay -r "MR_analysis_leipzig2_offline $thedate $anotherdate"
    time python summary_script.py $thedate $anotherdate
    #exit
    i=$(( i + 1 ))
done


#/opt/matlab/r2020a/bin/matlab -nodesktop -nodisplay -nosplash -r "MR_analysis_leipzig2_offline {} {}"

# time python summary_script.py
