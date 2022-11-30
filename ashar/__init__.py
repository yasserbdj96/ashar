#!/usr/bin/env python
# coding:utf-8
#   |                                                          |
# --+----------------------------------------------------------+--
#   |   Code by : yasserbdj96                                  |
#   |   Email   : yasser.bdj96@gmail.com                       |
#   |   Github  : https://github.com/yasserbdj96               |
#   |   BTC     : bc1q2dks8w8uurca5xmfwv4jwl7upehyjjakr3xga9   |
# --+----------------------------------------------------------+--  
#   |        all posts #yasserbdj96 ,all views my own.         |
# --+----------------------------------------------------------+--
#   |                                                          |

#START{
import base64
import hashlib
import re

#start ashar class:
class ashar:
    #__init__:
    def __init__(self,key,text,chars='abcdefghijklmnopqrstuvwxyz',upchars='ABCDEFGHIJKLMNOPQRSTUVWXYZ',smbls=')(}{][><!?$%&-_=+;',numb='1234567890'):
        #
        if chars!=False:
            self.chars=chars
        else:
            self.chars=""
        
        #
        if upchars!=False:
            self.upchars=upchars
        else:
            self.upchars=""

        #
        if smbls!=False:
            self.smbls=smbls
        else:
            self.smbls=""
        
        #
        if numb!=False:
            self.numb=numb
        else:
            self.numb=""
        
        #
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
    def random_char(self,y):
        all_randoms=self.smbls+self.numb+self.upchars[::-1]+self.chars
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
        key_md5=key_md5+ashar.random_char(self,k-x)
        text_md5=text_md5+ashar.random_char(self,k-y)
        text_md5=text_md5[::-1]
        text_base64=text_base64+ashar.random_char(self,k-z)
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

#}END.