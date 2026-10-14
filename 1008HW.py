n = int(input('請輸入數字，範圍是1~9: '))


i = 1
while i <= n:
    j = 1
    while j <= n:
        a = format(i,'b')
        b = format(j,'b')
        c = format(i*j,'b')
        print(f'{a:>4}*{b:>4}={c:06}, ', end='  ')
        j += 1
    print()
    i += 1