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
