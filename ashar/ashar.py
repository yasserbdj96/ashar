import base64
import hashlib

class ashar:
    def __init__(mysillyobject,key,text):
        mysillyobject.key=key
        mysillyobject.text=text
    
    def encode(abc):
        base64_text=base64.b64encode(abc.text.encode('ascii')).decode('ascii').replace("=","YasserBDJ")
        md5_text=hashlib.md5(abc.text.encode()).hexdigest()
        md5_key=hashlib.md5(abc.key.encode()).hexdigest()
        
        text_list=list(base64_text)
        key_list=list(md5_key)
        text_md5_list=list(md5_text)
        
        x=len(text_list)
        y=len(key_list)
        z=len(text_md5_list)
        
        level_1=''
        for i in range(max(x,y,z)):
            char=""
            if i<y:
                if key_list[i].isupper():
                    char=key_list[i].lower()
                else:
                    char=key_list[i].upper()
                level_1=level_1+char
            if i<x:
                if text_list[i].isupper():
                    char=text_list[i].lower()
                else:
                    char=text_list[i].upper()
                level_1=level_1+char
            if i<z:
                if text_md5_list[i].isupper():
                    char=text_md5_list[i].lower()
                else:
                    char=text_md5_list[i].upper()
                level_1=level_1+char
            level_1=level_1[::-1]
        
        return level_1
    """
    def decode(abc):
        level_1=''
        for i in range(len(abc.text)):
            level_1=level_1[::-1]
       
        print(abc.key,abc.text)
     

p1=ashar("123","Yasser_BDJ").encode()
p2=ashar("123",p1).decode()
print(p1)
"""