ans = input('請問要以民國紀年尋找還是西元紀年(回應民國or西元)尋找12生肖?')

if ans == '民國':
    民國紀年 = int(input('請輸入民國年份：'))

    if 民國紀年 % 12 == 0:
        print('屬豬')
    elif 民國紀年 % 12 == 1:
        print('屬鼠')
    elif 民國紀年 % 12 == 2:
        print('屬牛')
    elif 民國紀年 % 12 == 3:
        print('屬虎')
    elif 民國紀年 % 12 == 4:
        print('屬兔')
    elif 民國紀年 % 12 == 5:
        print('屬龍')
    elif 民國紀年 % 12 == 6:
        print('屬蛇')
    elif 民國紀年 % 12 == 7:
        print('屬馬')
    elif 民國紀年 % 12 == 8:
        print('屬羊')
    elif 民國紀年 % 12 == 9:
        print('屬猴')
    elif 民國紀年 % 12 == 10:
        print('屬雞')
    elif 民國紀年 % 12 == 11:
        print('屬狗')

elif ans == '西元':
    西元紀年 = int(input('請輸入西元年份：'))

    if 西元紀年 % 12 == 0:
        print('屬猴')
    elif 西元紀年 % 12 == 1:
        print('屬雞')
    elif 西元紀年 % 12 == 2:
        print('屬狗')
    elif 西元紀年 % 12 == 3:
        print('屬豬')
    elif 西元紀年 % 12 == 4:
        print('屬鼠')
    elif 西元紀年 % 12 == 5:
        print('屬牛')
    elif 西元紀年 % 12 == 6:
        print('屬虎')
    elif 西元紀年 % 12 == 7:
        print('屬兔')
    elif 西元紀年 % 12 == 8:
        print('屬龍')
    elif 西元紀年 % 12 == 9:
        print('屬蛇')
    elif 西元紀年 % 12 == 10:
        print('屬馬')
    elif 西元紀年 % 12 == 11:
        print('屬羊')