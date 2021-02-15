# # 함수
def open_account():
    print("새로운 계좌가 생성되었습니다.")

# open_account()

# 전달값과 반환값


def deposit(balance, money):  # 입금
    print("입금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance + money))
    return balance + money


def withdrow(balance, money):  # 출금
    if balance >= money:  # 잔액이 출금보다 많으면
        print("출금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance - money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0}원입니다.".format(balance))
        return balance


def withdrow_night(balance, money):  # 저녁에 출금
    commission = 100  # 수수료 100원
    return commission, balance - money - commission


balance = 0  # 현재 잔액
balance = deposit(balance, 1000)
# balance = withdrow(balance, 2000)
# balance = withdrow(balance, 500)
commission, balance = withdrow_night(balance, 500)
print("수수료 {0}원이며, 잔액은 {1}원입니다.".format(commission, balance))
