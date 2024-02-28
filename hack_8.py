"""
generic script

text: ["a","b","c","d","e"] output => ["e-5","d-4","c-3","b-2","a-1"]
text: ["a","b","c"] output => ["c-3","b-2","a-1"]
text: ["a","b","c","d"] output => ["4","3","2","1"]
text: ["a","b"] output => ["2","1"]
"""

def fn_hack_8(s):
    if len(s) % 2 == 0:  
        return [str(len(s)-i) for i, _ in enumerate(s, start=0)]
    else:  
        return [f"{elem}-{len(s)-i}" for i, elem in enumerate(s[::-1], start=0)]

print(fn_hack_8(["a","b","c","d","e"]))  # Output: ["e-5","d-4","c-3","b-2","a-1"]
print(fn_hack_8(["a","b","c"]))          # Output: ["c-3","b-2","a-1"]
print(fn_hack_8(["a","b","c","d"]))      # Output: ["4","3","2","1"]
print(fn_hack_8(["a","b"]))              # Output: ["2","1"]