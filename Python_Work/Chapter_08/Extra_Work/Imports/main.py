# main.py

# 1. import module_name
import greetings
greetings.say_hello("Alice")

# 2. from module_name import function_name
from greetings import say_hello
say_hello("Bob")

# 3. from module_name import function_name as fn
from greetings import say_hello as fn
fn("Charlie")

# 4. import module_name as mn
import greetings as mn
mn.say_hello("Diana")

# 5. from module_name import *
from greetings import *
say_hello("Eve")