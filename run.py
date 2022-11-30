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

try:
    import os
    import sys
    #
    CONDI = os.environ['CONDI'] if "CONDI" in os.environ else sys.argv[1]
    PASSWD = os.environ['PASSWD'] if "PASSWD" in os.environ else sys.argv[2]
    TEXT = os.environ['TEXT'] if "TEXT" in os.environ else sys.argv[3]

    if CONDI.upper()=="encode".upper():
        p1=ashar(PASSWD,TEXT).encode()
        print(p1)
    elif CONDI.upper()=="decode".upper():
        p2=ashar(PASSWD,TEXT).decode()
        print(p2)

except Exception as e:
    print(f"USAGE : python3 {sys.argv[0]} <CONDITION*> <PASSWORD*> <TEXT*>")
    print("CONDITION*: encode/decode")
    exit()
    #pass
#}END.