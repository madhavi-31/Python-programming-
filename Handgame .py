a=input()
b=input()
if a=="rock" and b== "paper":
    print(' b is win')
elif a=="paper" and b=="scissor":
    print('b is win')
elif a=="rock" and b=="scissor":
    print('a is win')
elif a=="paper" and b== "rock":
    print('a is win')
elif a=="scissor" and b=="paper":
    print('a is win')
elif a=="scissor" and b=="rock":
    print('b is win')
else:
    print('tie')
