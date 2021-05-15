
<p align="center"><img align="center" src="https://raw.githubusercontent.com/byRo0t96/ashar/main/screenshot/screenshot.png"></p>
<h1>Ashar Encryption and decryption.</h1>

<p>This project is for data encryption with password protection.</p>
<p align="center">
    <img align="center" src="https://travis-ci.com/byRo0t96/ashar.svg?branch=main">
    <img align="center" src="https://img.shields.io/github/issues/byRo0t96/ashar">
    <img align="center" src="https://img.shields.io/github/forks/byRo0t96/ashar">
    <img align="center" src="https://img.shields.io/github/stars/byRo0t96/ashar">
    <img align="center" src="https://img.shields.io/badge/license-Apache--2.0-green.svg">
    <img align="center" src="https://img.shields.io/badge/python-3.x.x-blue">
</p>
<h2>Installation:</h2>

```
pip install ashar==1.1.2
```

<h2>Usage:</h2>

```python
# USAGE :
#s
from ashar import ashar

#For encryption
p1=ashar("<PASSWORD>","<TEXT>").encode()
print(p1)
    
#To decrypt
p2=ashar("<PASSWORD>","<ENCRYPTED_TEXT>").decode()
print(p2)
#e

```

<h2>Examples:</h2>

```python
# EXAMPLES :
#s
from ashar import ashar

# Example:1
#For encryption
p1=ashar("123","Example:1").encode()
print(p1)
    
#To decrypt
p2=ashar("123","p1").decode()
print(p2)
#e

```

<h2>Changelog:</h2>

```
## 1.1.2
 - fix bugs.
 - new build 

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
<br>
<br>
<p align="center">
    <a align="center" href="https://byro0t96.github.io/">
        <img alt="byRo0t96" height="100" align="center" src="https://raw.githubusercontent.com/byRo0t96/byRo0t96/main/images/Ro0t-96_v.3.1.png">
    </a>
</p>

<p align="center">
    <a align="center" href="https://www.facebook.com/yasser.bdj.31">
        <img alt="facebook" align="center" src="https://img.shields.io/badge/Facebook-%2Fyasser.bdj.31-blue">
    </a>
	
   <a align="center" href="https://www.youtube.com/channel/UC53dtKxc84BNPyDb51rtRPg">
        <img align="center"  alt="youtube" src="https://img.shields.io/badge/-YouTube-red">
    </a>
	
   <a href="https://www.linkedin.com/in/boudjada-yasser-a53543196" align="center" >
        <img align="center" alt="LinkedIn" src="https://img.shields.io/badge/-linkedin-blue">
    </a> 
    
   <a href="https://www.instagram.com/bdj.yasser/" align="center" >
        <img align="center" alt="instagram" src="https://img.shields.io/badge/instagram-%2Fbdj.yasser-orange">
    </a> 
        
   <a href="https://github.com/byRo0t96/" align="center" >
        <img align="center" alt="visitor-badge" src="https://visitor-badge.laobi.icu/badge?page_id=byRo0t96.byRo0t96">
    </a>
</p>

<p align="center">
    <a align="center" href="https://ko-fi.com/L3L34CEPV">
        <img alt="ko-fi" align="center" src="https://ko-fi.com/img/githubbutton_sm.svg">
    </a>
</p>