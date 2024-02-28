"""
text: [{"a":"b"},{"c","d"},{"e":"f"}] output => [{"1":"2"},{"3","4"},{"5":"6"}]
"""


def fn_hack_10(s):
    result = []
    count = 1
    for item in s:
        new_dict = {}
        for k, v in item.items():
            new_dict[str(count)] = str(count + 1)
            count += 2
        result.append(new_dict)
    return result

print(fn_hack_10([{"a":"b"},{"c":"d"},{"e":"f"}]))