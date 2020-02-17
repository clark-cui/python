
# 猜数字小游戏

#重启函数
def restart():
    enterName = input('please input begin to play again ')
    if enterName == 'begin':
        playGame()
    else:
        print('your game is over')
        restart()

#游戏函数
def playGame():
    secret_num = 9
    index = 0
    x = input('guess ')
    index += 1
    # 考虑输入不合法的情况

    try:
        while (int(x) != secret_num and index < 3):
            # logic:
            # true true  true
            # true false false
            # false true false
            # false false false
            # so use and
            index += 1
            x = input('guess ')
    except ValueError as e:
        print('please input int number')
        restart()

    else:

        if int(x) == secret_num:
            print(f"congratulations! your {index}'s ansewer is correct")
            restart()
        else:
            print('your time is over')
            restart()

#开始执行
playGame()
