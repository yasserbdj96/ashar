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
from ashar import ashar

# Example:1
#For encryption
#p1=ashar("123","Example:1",chars="abcdefghijklmnopqrstuvwxyz",upchars=False,smbls=False,numb=False).encode()
#p1=ashar("<PASSWORD*>","<TEXT*>",chars='abcdefghijklmnopqrstuvwxyz',upchars='ABCDEFGHIJKLMNOPQRSTUVWXYZ',smbls=')(}{][><!?$%&-_=+;',numb='0123456789').encode()
p1=ashar("123","Example:1").encode()
print(p1)
    
#To decrypt
p2=ashar("123",p1).decode()
print(p2)

#}END.
