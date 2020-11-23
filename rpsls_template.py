"""
第一个小项目:Rock-paper-scissors-lizard-Spock
作者:傅尤强
日期:2020/11/23
"""
import random
def name_to_number(name):
    if name=='rock':
        return 0
    elif name=='spock':
        return 1
    elif name=='paper':
        return 2
    elif name=='lizard':
        return 3
    elif name=='scissors':
        return 4
    else:
        return None
def number_to_name(number):
    if number==0:
        return 'rock'
    elif number==1:
        return 'spock'
    elif number==2:
        return 'paper'
    elif number==3:
        return 'lizard'
    elif number==4:
        return 'scissors'
    else:
        return None
def rpsls(player_choice):
    print('')
    print('Player chooses ' + player_choice)
    player_number = name_to_number(player_choice)
    comp_number = random.randrange(0, 5)
    comp_choice = number_to_name(comp_number)
    print('Computer chooses ' + comp_choice)
    difference = (comp_number - player_number) % 5
    if (difference == 0):
        print('打平了!')
    elif (difference == 1 or difference == 2):
        print('机器赢了!')
    else:
        print('您赢了')
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
print("欢迎使用RPSLS游戏")
print("----------------")
print("请输入您的选择:")
choice_name=input()
rpsls(choice_name)


