import math
import os
import sys

import requests

print(sys.executable)


def welcomeMessage(name, place):
    test = "good"
    print("My name is: {}".format(name))
    print("I am from: {}".format(place))


r = requests.get("https://www.ndtv.com/")
print(r.status_code)