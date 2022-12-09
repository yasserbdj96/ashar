<div align="center">
  <h1>Ashar</h1>
  <strong>ashar - free & open source project for text encryption with password protection.</strong>
  <br><br>
</div>

[![Test on Ubuntu latest](https://github.com/yasserbdj96/ashar/actions/workflows/python-app-on-linux.yml/badge.svg)](https://github.com/yasserbdj96/ashar/actions/workflows/python-app-on-linux.yml)
[![Test on Windows latest](https://github.com/yasserbdj96/ashar/actions/workflows/python-app-on-win.yml/badge.svg)](https://github.com/yasserbdj96/ashar/actions/workflows/python-app-on-win.yml)
[![Test on MacOS latest](https://github.com/yasserbdj96/ashar/actions/workflows/python-app-on-mac.yml/badge.svg)](https://github.com/yasserbdj96/ashar/actions/workflows/python-app-on-mac.yml)
[![pypi-setup](https://github.com/yasserbdj96/ashar/actions/workflows/pypi-setup.yml/badge.svg)](https://github.com/yasserbdj96/ashar/actions/workflows/pypi-setup.yml)
![Upload to PYPI](https://github.com/yasserbdj96/ashar/actions/workflows/pipup.yml/badge.svg)
[![Deploy static content to Pages](https://github.com/yasserbdj96/ashar/actions/workflows/pages.yml/badge.svg)](https://github.com/yasserbdj96/ashar/actions/workflows/pages.yml)
[![CodeQL](https://github.com/yasserbdj96/ashar/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/yasserbdj96/ashar/actions/workflows/codeql-analysis.yml)
[![CodeFactor](https://www.codefactor.io/repository/github/yasserbdj96/ashar/badge)](https://www.codefactor.io/repository/github/yasserbdj96/ashar)
[![Supported Versions](https://img.shields.io/pypi/pyversions/ashar.svg)](https://pypi.org/project/ashar) 
[![Visitors](https://visitor-badge.laobi.icu/badge?page_id=yasserbdj96.ashar&format=true)](https://github.com/yasserbdj96/ashar)
[![Open Source](https://img.shields.io/badge/Open%20Source-%E2%99%A5-red)](https://github.com/yasserbdj96/ashar)
[![Stars](https://img.shields.io/github/stars/yasserbdj96/ashar?color=red)](https://github.com/yasserbdj96/ashar)
[![Forks](https://img.shields.io/github/forks/yasserbdj96/ashar?color=red)](https://github.com/yasserbdj96/ashar)
[![Watching](https://img.shields.io/github/watchers/yasserbdj96/ashar?label=Watchers&color=red&style=flat-square)](https://github.com/yasserbdj96/ashar)
![GitHub contributors](https://img.shields.io/github/contributors/yasserbdj96/ashar)
![GitHub closed issues](https://img.shields.io/github/issues-closed/yasserbdj96/ashar)
![GitHub pull requests](https://img.shields.io/github/issues-pr-raw/yasserbdj96/ashar)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/yasserbdj96/ashar)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/yasserbdj96/ashar)
[![GitHub license](https://img.shields.io/github/license/yasserbdj96/ashar)](https://github.com/yasserbdj96/ashar)
[![Join the chat at https://gitter.im/yasserbdj96/ashar](https://badges.gitter.im/yasserbdj96/ashar.svg)](https://gitter.im/yasserbdj96/ashar?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge) [![Join the chat at https://gitter.im/yasserbdj96/ashar](https://badges.gitter.im/yasserbdj96/ashar.svg)](https://gitter.im/yasserbdj96/ashar?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

<br>
<h2>Python Package Installation:</h2>

```
# install from pypi:
❯ pip install ashar

# local install:
❯ git clone https://github.com/yasserbdj96/ashar.git
❯ cd ashar
❯ sudo python setup.py install

# uninstall:
❯ pip uninstall ashar
```

<br>
<h2>Run without installation:</h2>

```
# Dwonload:
❯ git clone https://github.com/yasserbdj96/ashar.git
❯ cd ashar

# default run on any os:
❯ python3 run.py <CONDITION*> <PASSWORD*> <TEXT*>

# Run with Makefile:
❯ make run con="<CONDITION*>" pass="<PASSWORD*>" text="<TEXT*>"

# *         = All inputs must be entered.
# PASSWORD  = The password used for encrypt your text.
# TEXT      = The text to be encrypted.
# CONDITION = The nature of the process is encryption or decryption "encode/decode".
```

<br>
<h2>Script Usage:</h2>

```python
from ashar import ashar
#For encryption
p1=ashar("<PASSWORD*>","<TEXT*>").encode()
# p1=ashar("<PASSWORD*>","<TEXT*>",chars='abcdefghijklmnopqrstuvwxyz',upchars='ABCDEFGHIJKLMNOPQRSTUVWXYZ',smbls=')(}{][><!?$%&-_=+;',numb='1234567890').encode()
print(p1)
    
#To decrypt
p2=ashar("<PASSWORD*>","<ENCRYPTED_TEXT*>").decode()
print(p2)

# *   = All inputs must be entered.

```

<br>
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

<br>
<h2>Changelog History:</h2>
<a href="https://raw.githubusercontent.com/yasserbdj96/ashar/main/CHANGELOG">Click to See changelog History</a>


<br>
<h2>Development By:</h2>

Developer / Author: [yasserbdj96](https://github.com/yasserbdj96)

<br>
<h2>License:</h2>
<p>The content of this repository is bound by the following <a href="https://raw.githubusercontent.com/yasserbdj96/ashar/main/LICENSE">LICENSE</a>.</p>

<br>
<h2>Support:</h2>
<p>If you like `ashar` and want to see it improve furthur or want me to create intresting projects , You can buy me a coffee </p>
<div align="center">
    <a href="https://ko-fi.com/yasserbdj96">
        <img src="https://ko-fi.com/img/githubbutton_sm.svg" alt="ashar by yasserbdj96">
    </a><br>
    BTC: bc1q2dks8w8uurca5xmfwv4jwl7upehyjjakr3xga9<br>
</div>

<br><br>

<p align="center">
  <samp>
    <a href="https://yasserbdj96.github.io/">website</a> .
    <a href="https://github.com/yasserbdj96">github</a> .
    <a href="https://gitlab.com/yasserbdj96">gitlab</a> .
    <a href="https://www.linkedin.com/in/yasserbdj96">linkedin</a> .
    <a href="https://twitter.com/yasserbdj96">twitter</a> .
    <a href="https://instagram.com/yasserbdj96">instagram</a> .
    <a href="https://www.facebook.com/yasserbdj96">facebook</a> .
    <a href="https://www.youtube.com/@yasserbdj96">youtube</a> .
    <a href="https://pypi.org/user/yasserbdj96">pypi</a> .
    <a href="https://hub.docker.com/u/yasserbdj96">docker</a> .
    <a href="https://t.me/yasserbdj96">telegram</a> .
    <a href="https://gitter.im/yasserbdj96/yasserbdj96">gitter</a> .
    <a href="mailto:yasser.bdj96@gmail.com">e-mail</a> .
    <a href="https://ko-fi.com/yasserbdj96">sponsor</a>
  </samp>
</p>