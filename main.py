# Modules
# A module in Python is basically a file with some Python code.
# And we use modules to organize our code into files.
# Instead of writing all of our code, functions and classes in
# mian.py, we want to break up our code into multiple files.
# We refer to each file as a module. With this, not only our
# code better organized and structured, but we'll also have
# the ability to reuse our code.

import converters
from converters import kg_to_lbs # import specific functions from module
print(kg_to_lbs(100))
print(converters.kg_to_lbs(70))

from utils import find_max

print (find_max([7,8,21,41,5]))

# Package
# Packages are basically another way to organize our code, so currently
# We have only have 3 files for modules in our project but a real
# project can contain hundreds or even thousands of modules.
# We don't want to add all the modules here, brcause over time
# this directory will get bloated with so many files, so a better
# approach is to organize related modules, instead of a packageg,
# so a package is a container for multiple modules. In file system
# terms a package is a directory or folder. So in our project we
# can add a new directory and in that directory we can add all
# the directed modules.

# Three ways to import functions from Package
import ecommerce.shipping
ecommerce.shipping.calc_shipping()

from ecommerce.shipping import calc_shipping
calc_shipping()

from ecommerce import shipping

shipping.calc_shipping()

# Files and Directories
from pathlib import Path
path = Path("ecommerce")
print(path.exists())

path = Path("emails")
print(path.mkdir())

path = Path("emails")
print(path.rmdir())

path = Path()
for file in path.glob('*.py'):
    print(file)
