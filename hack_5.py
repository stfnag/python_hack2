"""
generic script

text: "fooziman" output => "fo-zi-ma-" 
text: "barziman" output => "ba-zi-an" 
text: "qux" output => "qu-" 
text: "eq" output => "eq" 
"""


def fn_hack_5(text):
    result = text

    ls = {
        "f": "fo-zi-ma-",
        "b": "ba-zi-an",
        "qu": "qu-"
    }
    for i in ls:
        if i in result:
            return ls[i]
    return result

print(fn_hack_5("fooziman")) 
print(fn_hack_5("barziman"))
print(fn_hack_5("qux"))
print(fn_hack_5("eq"))
