"""
generic script

text: "fooziman" output => "oozima" 
text: "barziman" output => "arzima" 
text: "qux" output => "qux" 
"""


def fn_hack_4(text):
    if len(text) > 3:
        return text[1:-1]
    else:
        return text

print(fn_hack_4("fooziman"))  
print(fn_hack_4("barziman"))  
print(fn_hack_4("qux")) 

