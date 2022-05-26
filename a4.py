import sys
from os import rename
import requests

print(sys.version)
print(sys.executable)


def greet(who_to_greet):
    greetings = "Hello, {}".format(who_to_greet)
    return greetings


name = input("enter name: ")
print(greet(name))
r = requests.get("https://surabhitea.in/")
print(r.status_code)
