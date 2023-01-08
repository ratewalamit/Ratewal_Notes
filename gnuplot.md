## Important command in gnuplot

**plotting multiplt files**
```shell
plot for [i=0:319] sprintf("Dsigma_Satellite_SHAPENOISE_9.0_10.25_0.4_0.9.dat00%03d",i) using 8:6 title ""
```

**Plot  over all files in Directory**
```shell
FILES = system("ls *.dat")
plot for [data in FILES] data u 8:6  notitle
#plot for [data in FILES] data u 1:2 w p pt 1 lt rgb 'black' notitle
```
