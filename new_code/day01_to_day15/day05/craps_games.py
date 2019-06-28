"""
Craps赌博游戏
    游戏规则如下：玩家掷两个骰子，点数为1到6，
    如果第一次点数和为7或11，则玩家胜，
    如果点数和为2、3或12，则玩家输，
    如果和为其它点数，则记录第一次的点数和，然后继续掷骰，直至点数和等于第一次掷出的点数和，则玩家胜，
    如果在这之前掷出了点数和为7，则玩家输。 
"""

from random import randint
a = randint(1,6)
b = randint(1,6)
sum = a + b
print('和为%d' % sum)
if sum == 7 or sum == 11:
    print('you win')
elif sum == 2 or sum == 3 or sum == 12:
    print('you lose')
else:
    while True:
        a = randint(1,6)
        b = randint(1,6)
        print('丢出了%d点' % (a+b))
        if a + b == 7:
            print('you lose')
            break
        elif a + b == sum:
            print('you win')
            break

"""
这获胜概率还是挺高的
"""