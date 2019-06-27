"""
    if...elif...else

    if xxx:

    elif xxx:

    else:

"""

"""
掷骰子决定做什么
"""

from random import randint

face = randint(1,6)
if face == 1:
    result = '随到1'
elif face==2:
    result = '随到2'
else:
    result = '除了1和2'
print(result)