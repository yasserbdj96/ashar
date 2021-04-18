#!/usr/bin/env python
# coding:utf-8
# code by : Yasser BDJ
# email : by.root96@gmail.com
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