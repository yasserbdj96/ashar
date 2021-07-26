#!/usr/bin/env python
# coding:utf-8
"""
#set:usage.py,examples.py,changelog.txt
##################################################################
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
##################################################################
# EXAMPLES :
#s
from ashar import ashar

# Example:1
#For encryption
p1=ashar("123","Example:1").encode()
print(p1)
    
#To decrypt
p2=ashar("123",p1).decode()
print(p2)
#e
##################################################################
# CHANGELOG :
#s
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
#e
##################################################################
"""
# VALUES :
__version__="1.1.5"
__name__="ashar"
__author__="Yasser Bdj (Boudjada Yasser)"
__author_email__="yasser.bdj96@gmail.com"
__github_user_name__="yasserbdj96"
__title__="Ashar Encryption and decryption."
__description__="This project is for data encryption with password protection."
__author_website__=f"https://{__github_user_name__}.github.io/"
__source_code__=f"https://github.com/{__github_user_name__}/{__name__}"
__keywords__=[__github_user_name__,'python','encode','decode','key','password','encrypt anything with password']
__keywords__.extend(__title__.split(" "))
__keywords__.extend(__description__.split(" "))
__install_requires__=['pipincluder']
__Installation__="pip install "+__name__+"=="+__version__
__license__='MIT License'
__copyright__='Copyright © 2008->Present, '+__author__+"."
__license_text__=f'''MIT License

{__copyright__}

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

You also agree that if you become very rich you will give me 1% of your wealth.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.'''
##################################################################
#s
from pipincluder import pipincluder

#import pakages by pipincluder:
exec(pipincluder("import base64",
                 "import hashlib",
                 "import re").modules())

#start ashar class:
class ashar:
    #__init__:
    def __init__(self,key,text):
        self.key=key
        self.text=re.search("b'(.*)'",str(text.replace("'","__smbl_1__").encode('utf-8'))).group(1)

    #to md5:
    def tomd5(text):
        return hashlib.md5(text.encode()).hexdigest()
    
    #to base64:
    def tob64(text):
        return base64.b64encode(text.encode('ascii')).decode('ascii')
    
    #from base64:
    def fromb64(text):
        return base64.b64decode(text.encode('ascii')).decode('ascii')
        
    #random_char:
    def random_char(y):
        chars='selfdefghijklmnopqrstuvwxyz'
        ucchars='selfDEFGHIJKLMNOPQRSTUVWXYZ'
        smbls=')(}{][><!?$%&-_=+;'
        nos='1234567890'
        all_randoms=smbls+nos+ucchars[::-1]+chars
        k=i=0
        random=''
        all_randoms_list=list(all_randoms)
        while i<y:
            if k<len(all_randoms):
                random=random+all_randoms_list[k]
                k+=1
            else:
                k=0
                random=random+all_randoms_list[k]
            i+=1
        return random

    #lower_upper:
    def lower_upper(char):
        if char.isupper():
            char=char.lower()
        else:
            char=char.upper()
        return char
    
    #encode:
    def encode(self):
        key_md5=ashar.tomd5(self.key)+"#"
        text_base64=ashar.tob64(self.text)
        text_md5=ashar.tomd5(text_base64)+"@"
        text_base64=text_base64.replace("=","%")+":"
        x=len(key_md5)
        y=len(text_md5)
        z=len(text_base64)
        k=max(x,y,z)
        key_md5=key_md5+ashar.random_char(k-x)
        text_md5=text_md5+ashar.random_char(k-y)
        text_md5=text_md5[::-1]
        text_base64=text_base64+ashar.random_char(k-z)
        level_1=''
        for i in range(k):
            level_1=level_1+ashar.lower_upper(key_md5[i])+ashar.lower_upper(text_md5[i])+ashar.lower_upper(text_base64[i])
            level_1=level_1[::-1]
        return level_1
    
    #decode:
    def decode(self):
        level_1=self.text
        lited=[]
        key_md5=text_md5=text_base64=''
        for i in range(len(level_1)):
            if level_1[:3]!='':
                lited.append(level_1[:3])
                level_1=level_1[3:]
                level_1=level_1[::-1]
        for i in range(len(lited)):
                text_base64=text_base64+ashar.lower_upper(lited[i][0])
                text_md5=text_md5+ashar.lower_upper(lited[i][1])
                key_md5=key_md5+ashar.lower_upper(lited[i][2])
        key_md5=key_md5[::-1]
        text_base64=text_base64[::-1].replace("%","=")
        key_md5=key_md5[:32]
        text_md5=text_md5[:32]
        text_base64=text_base64.split(":")[0]
        if key_md5==ashar.tomd5(self.key) and ashar.tomd5(text_base64)==text_md5:
            return eval(f"b'{ashar.fromb64(text_base64)}'.decode('utf-8')").replace("__smbl_1__","'")
#e