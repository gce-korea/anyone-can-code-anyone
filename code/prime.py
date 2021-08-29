#소수 판별 프로그램
# 1과 그 자신만을 약수로 가지는 수
# 17 2 ~ 16
def is_prime(number):
    count = 2
    while count < number:
        print(count)
        if number % count == 0:
            print("소수가 아닙니다.")
            break
        count = count + 1

is_prime(25)
