#!/usr/bin/env python
# coding:utf-8
# code by : Yasser BDJ
# email : by.root96@gmail.com
#s
import base64
import hashlib

#start ashar class:
class ashar:
    def __init__(mysillyobject,key,text):
        mysillyobject.key=key
        mysillyobject.text=text
    
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
        chars='abcdefghijklmnopqrstuvwxyz'
        ucchars='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
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
    def encode(abc):
        key_md5=ashar.tomd5(abc.key)+"#"
        text_base64=ashar.tob64(abc.text)
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
    def decode(abc):
        level_1=abc.text
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
        if key_md5==ashar.tomd5(abc.key) and ashar.tomd5(text_base64)==text_md5:
            return ashar.fromb64(text_base64)
#e