# 팩토리얼 계산 프로그램

number = 5
count = number - 1 # 4
while count > 1:
    number = number * count # 5 * 4  
    print(number,count)
    if count == 3:
        break
    count = count - 1
