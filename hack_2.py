"""
generic script

text: "fooziman" output => "fzmn" 
text: "barziman" output => "brzmn" 
text: "qux" output => "qx" 
"""


def fn_hack_2(text):
    result = text
    vowels = ["a","e","i","o","u"]
    _str = []
    
    for txt in result:
        if txt not in vowels:
          _str.append(txt)  
          
    result = "".join(_str)
    return result  

print(fn_hack_2('fooziman')) 
print(fn_hack_2('barziman')) 
print(fn_hack_2('qux')) 