import json


def to_json(data):
    if isinstance(data,dict):
        out_str = "{"
        for key in data.keys():
            #out_str += '"%s": %s, ' % (key, to_json(data[key]))
            out_str += '"{}": {}, '.format(key, to_json(data[key]))

        out_str = out_str[:len(out_str) - 2]
        return out_str + "}"

    elif isinstance(data,list):
        some_str = "["
        for element in data:
            some_str += ', "{}"'.format(element)
        some_str += "]"
        some_str = "[" + some_str[3:]
        return some_str

    elif isinstance(data,tuple):
        some_str = "["
        for element in data:
            some_str += ', "{}"'.format(element)
        some_str += "]"
        some_str = "[" + some_str[3:]
        return some_str

    elif isinstance(data,list):
        return '"{}"'.format(data)

    elif isinstance(data,(float,int)):
        if data == True:
            return 'true'
        elif data == False:
            return 'false'
        else:
            return str(data)

    elif isinstance(data,str):
        return '"{}"'.format(str(data))

    elif data== None:
        return "null"
    else:
        raise ValueError("Incorrect Input")


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
    print(json.dumps(10213.2131))

    print("\nChecking tuple in dictionary:")
    print(to_json({"name": "Viktor", "age": 30, "sex": ("not_men", "not_women")}))
    print(json.dumps({"name": "Viktor", "age": 30, "sex": ("not_men", "not_women")}))

    a= True
    b= False
    print(to_json(a))
    print(json.dumps(a))

    print(to_json(b))
    print(json.dumps(b))


Main()
