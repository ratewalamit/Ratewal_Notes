
**Start remote Jupyter Notebook**

Run a jupter noteobook on this server.
```
jupyter-notebook --no-browser --port=8080
```

Now, in your local browser:
```
http://localhost:8080/
```

## Access the remote notebook on

*Option 1: Laptop*
Run following commnad on local machine
```
ssh -L 8080:localhost:8080 camit@192.168.11.251
```
*Option 2: On IPAD*
```shell
#Set-up terminus for port_forward with following credintials
label: Jupyter_forward     \#or some other name
Local Port: 8080
Bind Address : leave blank
Intermediate Host: select your 'pegasus' connection from hosts
Destination Address: localhost
Destination port Number: 8080
```

