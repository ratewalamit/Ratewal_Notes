## Seaborn is a library of python made on maptloblib. I uses pandas, numpy ,scipy functionalities.
```python
import seaborn as sns
import numpy as np
import pandas as pd
```

### Lineplot
```python
sns.lineplot(x="col1",y="col2",data=sns.load_dataset("somefilenameonseabornserver"),hue="sex",style="sex",pelette="Accent",markers=["o",">"],dashes=False,legend="full",height=10)
plt.grid()
```
Here col1,col2 are columns in ```data```. ```hue``` splits the data set in two(not necessarily) parts. `style` tell based on what we have to choose markers,`pelette` dictates the color.
`dashes` makes dashed lines to solid lines,`legend` is self explainotery.`height` sets figsize.


### Barplot
```python
d1=pd.read_csv("filename")
sns.set(style="dark")  #to set dark grids
#sns.set_style("darkgrid", {"grid.color": ".6", "grid.linestyle": ":"})
order_1=["second","first","third"]
sns.barplot(x=d1.col1,y=d1.col2,hue=d1.sex,order=order_1,hue_order=["Female","Male"],pelette="Accent",orient="v",satureation=100,errcolor="b")
```
It gives mean value of y categorises based on x
Here col1,col2 are columns in `d1`. `hue` splits the data set in two(not necessarily) parts. `order` sets what comes first,`hue_order` dictates which hue comes first,  `saturation` bears cintrst bw hue datasets,`errcolor` decide color of error.

### Countplot
```python
d1=pd.read_csv("filename")
sns.countplot(x=d1.sex,hue=d1.smoker)   #to plot in horizontal direction use y=d1.col1
```

### Histplot
```python
d1=pd.read_csv("filename")
sns.displot(d1.col1,bins=[1,2,3,4,5,6],kde=True,rug=True,color="g")
```
Here col1, `d1`. `kde` sets the kernal density estimator,`rug` dictates ticks


### Scatterplot
```python
d1=pd.read_csv("filename")
m={"Male":"0","Female":"p"}
sns.scatterplot(x=d1.col1,y=d1.col2,hue=d1.sex,hue_order=["Female","Male"],style=d1.sex,size=d1.sex,sizes=(100,60),markers=m,pelette="Accent")
```
`style,size` decides the styles of scatter plot

### Stripplot
similar to scatter plot, but it can distribute the different categories separately, whereas scatterplot put all of them together
```python
d1=pd.read_csv("filename")
m={"Male":"0","Female":"p"}
sns.stripplot(x=d1.days,y=d1.bill,hue=d1.sex,hue_order=["Female","Male"] )
```
### Boxplot
```python
d1=pd.read_csv("filename")
sns.box(x=d1.days,y=d1.bill,hue=d1.sex,hue_order=["Female","Male"],showmeans=True )
```
`showmeans` shows the mean of the data 


### Heatmap
```python
d1=pd.read_csv("filename")  #multidiemsional data
y={"fontsize":20,"color":"r"}
sns.heatmap(d1,vmin=0,vmax=10,cmap="PuOr",annot=True,annot_kws=y,linewidth=10,linecolor="y",cbar=False,xticklabels=False)

#v=sns.heatmap(d1,vmin=0,vmax=10,cmap="PuOr",annot=True,annot_kws=y,linewidth=10,linecolor="y",cbar=False,xticklabels=False)
#v.set(xlabel="col1",ylablel="col2")
#sns.set(font_scale=1)
```
`annot` puts the data values in the box, `annot_kws` passes dictionary style to annote, `linewidth` decides separation bw boxes.


### Violinplot
The box in matplotlib extends from the lower to upper quartile values of the data, with a line at the median.

```python
d1=pd.read_csv("filename")  #multidiemsional data
sns.violinplot(x=d1.day,y=d1.bill,hue=d1.sex,split=True,inner="quart")  #will plot bill of different days separated based on sex
```
`split` will split the data and make only one violing plot instead of two differnent violin plot from male and female.
`inner` will make the box disappear from violin, and put the dashed lines representing the quartiles, it can be used to switch bw box to lines representation

### Pairplot
Like corner plots 

```python
d1=pd.read_csv("filename")  #multidiemsional data
sns.pairplot(d1,vars=["col1","col2"],hue="sex",kind="reg",diag_kind="kde")  #kind= hist,reg,scatter,kde
```
`d1` Total dataset, only two columns `col1,col2` from d1 will be used, `reg` fits a line, `diag_kde` put kde curvers on diagonal subplots.  

### Catplot
**combination of all plot, using keyword kind**
```python
d1=pd.read_csv("filename")  #multidiemsional data
sns.catplot(x=d1.day,y=d1.price,hue="sex",kind="reg")  #kind= box,scatter,violin,bar,box,boxe,etc
```
### FacetGrid
```python
d1=pd.read_csv("filename")  #multidiemsional data
fg=sns.FacetGrid(d1,col=d1.sex,hue="day")
fg.map(plt.scatter,d1.price,d1.tip).add_legend()

```



