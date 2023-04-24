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

**search and replace**
using sed (replacing matched content wiht results from some other bash command)
```shell
sed -i -e "s/sim_name  =   galaxy_cosmo171/$(grep -v "^;" config_sim_galB.ini|grep -e "sim_name[[:blank:]]\{0,\}=[[:blank:]]\{0,\}galaxy_cosmo[0-9][0-9]0")/g" config_sim_galB.ini
```

**extract corresponding values from dictionary based on matching column**
```
dict_a={}
for i in range(5):
    dict_a[i]=i*2

x=np.arange(3,6)
x_square=np.array(list(dict_a.map,x))
```

**tile pdf in rows vs columns**
```shell
pdfjam --nup 3x2  $(ls Corner_mass_disruption_*pdf -rt) --outfile row3.pdf
#tile 6 pdfs in 3columns ,2 rows
```


**Wget command over a list of urls saved in file**
```shell
while read -r url; do (qsub -N download_data -v url=$url  -o download_data_$(date '+%Y%m%d-%H%M%S')_$(echo $(basename -- "$url"))  download_call.sh);done <url_list.sh
#only file name   $(echo $(FILE=$(basename -- "$url")|echo "${FILE%%.*}"))

#cat download_call.sh
#!/bin/bash
#PBS -q intermediate
#PBS -l nodes=1:ppn=1
#PBS -j oe
#PBS -l walltime=15:00:00
module load anaconda3 gcc-8.2.0 mpich-3.3.1 latex fftw-2.1.5 gsl-2.6
wget -x -nH   --no-check-certificate  $url -P $PWD
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
