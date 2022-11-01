# Single line nested loop
```shell
for i in 9.0,10.25 10.25,10.6 10.6,11.5; do (  IFS=",";set -- $i;mmin=$1;mmax=$2;IFS=" ";    for j in 0.1,0.3  0.3,0.5  0.5,0.9;do   ( IFS=",";set -- $j;rbmin=$1;rbmax=$2;IFS=" ";    (ls Dsigma_satellite_error_${mmin}_${mmax}_${rbmin}_${rbmax}.dat00* |wc -l; echo ${mmin}_${mmax}_${rbmin}_${rbmax})  )    ;done        );done
```
