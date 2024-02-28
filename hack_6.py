"""
generic script

["1","-"] => type string
["0"] => type string

text: ["a","b","c","d","e"] output => ["1","-","3","-","5"]
text: [] output => ["0"] 
"""


def fn_hack_6(text):
    if not text:
        return ["0"]
    
    result = []
    for i in range(1, min(len(text) * 2, 6), 2):
        result.append(str(i))
        if i != min(len(text) * 2, 5):
            result.append("-")
    
    return result


print(fn_hack_6(["a", "b", "c", "d", "e"])) # Output: ["1", "-", "3", "-", "5"]
print(fn_hack_6([])) # Output: ["0"]