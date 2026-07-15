#!/usr/bin/python3
MagicClass = __import__('103-magic_class').MagicClass

circle = MagicClass(5)
print("Area: {}".format(circle.area()))
print("Circumference: {}".format(circle.circumference()))
