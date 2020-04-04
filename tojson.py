import json
import coverage


def to_json(data):
    if (type(data) == dict):
        out_str = "{"
        for key in data.keys():
            out_str += '"%s": %s, ' % (key, to_json(data[key]))

        out_str = out_str[:len(out_str) - 2]
        return out_str + "}"

    elif (type(data) == list):
        some_str = "["
        for element in data:
            some_str += ', "%s"' % element
        some_str += "]"
        some_str = "[" + some_str[3:]
        return some_str
    elif (type(data) == tuple):
        some_str = "["
        for element in data:
            some_str += ', "%s"' % element
        some_str += "]"
        some_str = "[" + some_str[3:]
        return some_str
    elif (type(data) == str):
        return '"%s"' % data
    elif (type(data) == int):
        return str(data)
    elif (type(data) == float):
        return str(data)
    elif (data == True):
        return "true"
    elif (data == False):
        return "false"
    elif (data == None):
        return "null"
    else:
        return "incorrect input"


def Main():
    print("\nChecking dictionary:")
    print(to_json({"name": "Viktor", "age": 30}))
    print(json.dumps({"name": "Viktor", "age": 30, "sex": "cool_guy"}))

    print("\nChecking tuple:")
    print(to_json(("Porsche", "BMW")))
    print(json.dumps(("Porsche", "BMW")))

    print("\nChecking string:")
    print(to_json(("Hello, this is my string")))
    print(json.dumps(("Hello, this is my string")))

    print("\nChecking float numbers:")
    print(to_json(10213.2131))

    print("\nChecking tuple in dictionary:")
    print(to_json({"name": "Viktor", "age": 30, "sex": ("not_men", "not_women")}))
    print(json.dumps({"name": "Viktor", "age": 30, "sex": ("not_men", "not_women")}))



Main()
