# learning_python.md

## saving data to a ndarray
```python
dt=([ ('col1',np.int64),('col2','<f8'),('col3',[("3a",'<i8'),("3b",'<i8')]) ])
x = np.zeros((1,), dtype=dt)
#assigning data
x['col3']['3a']=5
x['col1']=20
#accesssing data
print(x['col1'])

#save and read the array
np.save("amit", x)
np.load("amit" + '.npy')

#saving this data
x.tofile("amit")
#load this data
np.fromfile("amit", dtype=dt)

```

##  Run bash command in python
```python
import os
import subprocess
import shlex
path_to_file="/mnt/home/student/camit/Project_universemachine/DataStore/UniverseMachine/DR1/SFR_ASCII/sfr_catalog_0.055623.txt"

command=f"wc -l {path_to_file}"
cmd_result=subprocess.run(shlex.split(command),shell=False,text=True,check=True,capture_output=True) #shell=True : you give full command in double quotes
print(cmd_result.stdout) #shell=False give command in list wiht elements in quotss ["wc", "-l"]
```

## Using pandas dataframe
```python
def create_catalog(halos):
    pddf = pd.DataFrame()
    dtype_dict={}
    colnames='ID DescID UPID Flags Uparent_Dist X Y Z VX VY VZ M V MP VMP R Rank1 Rank2 RA RARank SM ICL SFR Obs_SM Obs_SFR Obs_SSFR SM/HM obs_UV'.split()  #column names
    missing_cols=[]
    for i in colnames:
        try:
            pddf[i]=halos[f'{i.lower()}']
            dtype_dict[i]=halos[f'{i.lower()}'].dtype
        except:
            missing_cols.append(i)
            dtype_dict[i]=halos['pos'].dtype
    if missing_cols==   ['X', 'Y', 'Z', 'VX', 'VY', 'VZ', 'Obs_SSFR', 'SM/HM']:
        pddf[['X', 'Y', 'Z', 'VX', 'VY', 'VZ']]=pd.DataFrame(halos['pos'])
        pddf['Obs_SSFR']=pddf.Obs_SFR.values/pddf.Obs_SM.values
        pddf['SM/HM']=0
    pddf=pddf.astype(dtype_dict)
    return pddf
```

## Replacing particular cell value in pandas
```python
 hh['galID'].mask(hh['galID'] == 5, 6, inplace=True)
#syntax: df[‘column_name’].mask( df[‘column_name’] == ‘some_value’, value , inplace=True )

```

## Using Dictionsary 
```shell
dict_mass={}
mass_cat=fits.open('file1.fits')[1].data
st_mass=mass_cat["stellar_mass"]
for ie,obid in enumerate(mass_cat["object_id"]):
    dict_mass[obid]=st_mass[ie]

for fname in glob.glob("file2*.fits"):
    hdulist = fits.open(fname)
    data = hdulist[1].data
    zredt = data["mizuki_photoz_best"]
    obj_id=data['object_id']
    mstelt=np.array(list(map(dict_mass.get, obj_id)))

```


## Using Subplots
```python
import numpy as np
import matplotlib.pyplot as plt

x=np.arange(10)
y=x+2

#subplot If you want to create a single plot in the whole figure,differnece will be visible on saving the figure
plot1=plt.subplot(1,2,1)
plot1.plot(x,y)

#if you want to create the second plot also in the figure
plot2=plt.subplot(211)
plot2.plot(x,y)


#subplots   #create multiple plots in the figure
fig,axes=plt.subplots(2,2)
axes[0,0].plot(x,y)
axes[0,0].plot(x,y+2)
axes[1,1].plot(x,x+y)

```

## Using 3d Plots
```python
#signle 3d plot
ax=plt.axes(projection="3d")
ax.plot(x,y,z)
ax.scatter(x,y,z)

#multiple 3d plots
plot1=plt.subplot(2,2,1,projection="3d")
plot1.scatter(x,y,z)

plot2=plt.subplot(2,2,2)
plot2.scatter(x,y)

plot3=plt.subplot(2,2,3,projection="3d")
X,Y=np.meshgrid(x,y)
Z=X**2+Y**2
plot3.scatter(X,Y,Z)

plot4=plt.subplot(2,2,4,projection="3d")
X,Y=np.meshgrid(x,y)
Z=X**2+Y**2
plot4.plot_surface(X,Y,Z)


```



## Changing dirctory
```python
import os
import pathlib.Path as PATH
base_path=str(PATH.home())
os.chdir(f"{base_path}/some_folder")
````


## Python if else block in one line
```python
if <expression>: <perform_action_01>; <perform_action_02>; <perform_action_03>   #aprart from 1,it wont perform 2,3 also if expression is false
#or
 <perform_action_01> if <expression> else <perform_action_02>
```



## Using system command in python
```python
#use of os.system is not recommended since it reflects changes on the terminal
if 0!=os.system("complicated command to be executed"): print("Command executed with error")   #check the output status only   #recommended to change directory
if 0!=os.system("complicated command to be executed   >>/dev/null 2>&1 "): print("Command executed with error")     #to hide the output

#Recommended subprocess.run
result=subprocess.run("wc -l a.py",shell=True,text=True,capture_output=True)    #shell =True uses bash to do computation, capture_outpute skips output printing
result=subprocess.run("wc -l a.py".split(),shell=False,text=True,capture_output=True) #shall =False skip use of bash
#remember when you dont use shell =true, you need to pass the command as a combination of strings, whereas  shell=True, 
result=subprocess.run("ls -l  |wc -l",shell=True,text=True,capture_output=True) #use complicated command with shell=True
#Note It will cause problems in using cd command since it uses cd in the subprocess only, not in the actual terminal directory
```

