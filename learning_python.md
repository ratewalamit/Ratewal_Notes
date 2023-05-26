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
