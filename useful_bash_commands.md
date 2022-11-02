**Single line nested loop**
```shell
for i in 9.0,10.25 10.25,10.6 10.6,11.5; do (  IFS=",";set -- $i;mmin=$1;mmax=$2;IFS=" ";    for j in 0.1,0.3  0.3,0.5  0.5,0.9;do   ( IFS=",";set -- $j;rbmin=$1;rbmax=$2;IFS=" ";    (ls Dsigma_satellite_error_${mmin}_${mmax}_${rbmin}_${rbmax}.dat00* |wc -l; echo ${mmin}_${mmax}_${rbmin}_${rbmax})  )    ;done        );done
```
**search and replace**
```shell
sed "s#img_dir=./output#img_dir=./output_$shear#g; s/shear_value[[:blank:]]\{1,\}=[[:blank:]]\{1,\} [0-9].[0-9][0-9]/shear_value = $shear/g" $dirfpfs/examples/config_sim_gal.ini  > $dirfpfs/examples/tmp_configs/tmp_config_sim_gal.ini
```

**Reading line by line from a file**
```shell
while IFS= read -r line; do     echo "$line"; done < doit.sh

#or
#cat do.sh|while read in;do echo $in ;done
```






<!--- 
# How to write in Readme.md

README.md writing sytle [help](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#section-links)

**This is bold text**	This is bold text

*This text is italicized*	This text is italicized

~~This was mistaken text~~	This was mistaken text

**This text is _extremely_ important**	This text is extremely important

***All this text is important***	All this text is important
 --->
