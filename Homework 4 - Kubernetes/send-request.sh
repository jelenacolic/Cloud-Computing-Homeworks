#!/bin/bash

mb=0
i=1
memoryUsage=0
memoryUsed=0
replicas=0

echo "Time,Memory,Pods" > izlaz.csv

while true
do
    mb=`echo $mb + 10 | bc `
    echo $mb
    url=`echo "http://147.91.204.85:32609/metod1?kolicinaMemorije=$mb"`
    
    curl -X GET $url --output izlaz.txt
    #sleep 60
    sleep 30
    memoryUsage=`kubectl get hpa | grep Mi | awk -F' ' '{ print $3 }'`
    memoryUsed=`echo $memoryUsage | tr "/" "\n" | head -n 1`
    memoryUsed=`echo $memoryUsed / 1024 / 1024 | bc`
    replicas=`kubectl get hpa | grep Mi | awk -F' ' '{ print $6 }'`

    echo "t$i,$memoryUsed,$replicas" >> izlaz.csv

    i=`echo $i + 1 | bc`
    if [[ $replicas -eq 8 ]]
    then
        break
    fi
done

echo "Stopped requests, calculating time ... "

# zauzeta memorija po pod-u ne opada dovoljno kako bi se smanjio broj pod-ova, bar nije opala u periodu tokom kog je bila pokrenuta skripta (1h)
# trebalo bi da je do jave, s obzirom da se desava da ni u lokalu memorija ne opada, nego samo raste, iako su sve reference sa zauzete memorije sklonjene i pozvan Garbage Collector
while true
do
    sleep 60

    replicasNew=`kubectl get hpa | grep Mi | awk -F' ' '{ print $6 }'`

    if [[ $replicasNew -lt $replicas ]]
    then
        memoryUsage=`kubectl get hpa | grep Mi | awk -F' ' '{ print $3 }'`
        memoryUsed=`echo $memoryUsage | tr "/" "\n" | head -n 1`
        memoryUsed=`echo $memoryUsed / 1024 / 1024 | bc`
        echo "t$i,$memoryUsed,$replicas" >> izlaz.csv
        i=`echo $i + 1 | bc`

        replicas = replicasNew
        continue
    fi
    
    if [[ $replicas -eq 1 ]]
    then
        memoryUsage=`kubectl get hpa | grep Mi | awk -F' ' '{ print $3 }'`
        memoryUsed=`echo $memoryUsage | tr "/" "\n" | head -n 1`
        memoryUsed=`echo $memoryUsed / 1024 / 1024 | bc`
        
        echo "t$i,$memoryUsed,$replicas" >> izlaz.csv
    
        break
    fi
done

    


