#!/bin/bash
re='^[0-9]$'
for i in {4..25}
do
    if  [[ $i =~ $re ]] ;
    then
        DAY="0$i"

    else
        DAY="$i"
    fi
    echo "Requesting day $DAY"
    ./start.sh 2016 $DAY
done