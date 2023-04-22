## saving data to a ndarray
```
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
