#!/usr/bin/micropython

import sys

print(".".join(map(str,sys.implementation[1])))
