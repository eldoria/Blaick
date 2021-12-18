'''
import json


def check_if_register(id: int) -> str:
    with open('data.json', 'r') as openfile:
        json_object = json.load(openfile)
    try:
        json_object[f"{id}"]
    except KeyError:
        register(id)
        return "You have been registered"
    return "You are already registered"


def register(id: int):
    with open('data.json', 'r') as openfile:
        json_object = json.load(openfile)
    json_object["123"] = "456"
    json_object.to_json()
    print(json_object)


if __name__ == "__main__":
    # print(check_if_register(329611671016570880))
    # print(check_if_register(32961167101657088))
    print(register(3))
'''
