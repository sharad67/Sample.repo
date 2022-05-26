import sys
import requests

print(sys.executable)


def welcomeMessage(name, place):
    print("My name is: {}".format(name))
    print("I am from: {}".format(place))


r = requests.get("https://surabhitea.in/")
print(r.status_code)
