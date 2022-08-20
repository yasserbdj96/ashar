
<h1>Ashar Encryption and decryption.</h1>

<p>This project is for data encryption with password protection.</p>

<h2>Docker pull,build & run:</h2>

```bash
# pull:
>>> docker pull docker.io/yasserbdj96/ashar:latest

# build:
>>> docker build -t docker.io/yasserbdj96/ashar:latest .

# run:
>>> docker run -e CONDI="<CONDITION*>" -e PASSWD="<PASSWORD*>" -e TEXT="<TEXT*>" -i -t docker.io/yasserbdj96/ashar:latest
# *    = All inputs must be entered.
```

<h2>Github Packages pull,build & run:</h2>

```bash
# pull:
>>> docker pull ghcr.io/yasserbdj96/ashar:latest

# build:
>>> docker build -t ghcr.io/yasserbdj96/ashar:latest .

# run:
>>> docker run -e CONDI="<CONDITION*>" -e PASSWD="<PASSWORD*>" -e TEXT="<TEXT*>" -i -t ghcr.io/yasserbdj96/ashar:latest
```

<h2>Python Package Installation:</h2>

```
# install from pypi:
>>> pip install ashar

# local install:
>>> git clone https://github.com/yasserbdj96/ashar.git
>>> cd ashar
>>> sudo python setup.py install

# uninstall:
>>> pip uninstall ashar
```

<h2>Run without installation:</h2>

```
>>> git clone https://github.com/yasserbdj96/ashar.git
>>> cd ashar
>>> python3 run.py <CONDITION*> <PASSWORD*> <TEXT*>
```

<h2>Script Usage:</h2>

```python
from ashar import ashar
#For encryption
p1=ashar("<PASSWORD>","<TEXT>").encode()
print(p1)
    
#To decrypt
p2=ashar("<PASSWORD>","<ENCRYPTED_TEXT>").decode()
print(p2)

```

<h2>Script Examples:</h2>

```python
from ashar import ashar
# Example:1
#For encryption
p1=ashar("123","Example:1").encode()
print(p1)
    
#To decrypt
p2=ashar("123",p1).decode()
print(p2)

```

<h2>Changelog:</h2>

```
## 1.1.6
 - Delete pipincluder pakage.
 - Fix Bugs.

## 1.1.5
 - Fix Bugs.

## 1.1.4
 - fix bugs.
 - new build.
 
## 1.1.2
 - fix bugs.
 - new build.
 
## 1.1.1
 - Fix bugs.
 
## 1.1.0
 - Import pakages by pipincluder.
 
## 1.0.6
 - You can encrypt anything now.
 - Fix bugs.
 
## 1.0.0
 - Fix bugs.
 
## 0.5.5
 - Fix bugs.
 
## 0.5.4
 - Static encryption.
 - Fix bugs.
 
## 0.5.3
 - Fix bugs.
 
## 0.5.0
 - First public release.

```

<h1></h1> 


Don't forget to star ⭐ this repository
<br>

all posts [`#yasserbdj96`](#yasserbdj96) ,all views my own.

<br>
<div align="center">
    <a href="http://yasserbdj96.github.io/">Go to this link to get more information.</a>
</div>