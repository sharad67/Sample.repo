import sys

print(sys.version)
print(sys.executable)


def welcomeMessage(name, place):
    print("My name is: {}".format(name))
    print("I am from: {}".format(place))


welcomeMessage("Sharad", "Siliguri")
welcomeMessage("Monika", "Kolkata")
