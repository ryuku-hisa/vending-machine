

# 投入されたお金の枚数など管理する変数など
money = {
    '10'  : 0,
    '50'  : 0,
    '100' : 0,
    '500' : 0,
    '1000': 0,
}

money_keys = list(money.keys())



# お金の投入処理
def deposit():
    print("Deposit money using " + str(money_keys) + " yen")
    while True:
        print_deposit()
        print("Return: press 0")
        deposit = input()
        if deposit in money:
            money[deposit] += 1
        elif deposit == '0':
            return 0
        else:
            print("Please deposit correct money")
            print("return: " + deposit + "yen")




## 投入金額の表示
def print_deposit():
    print(money)
    deposit_total = 0
    money_num = list(money)
    for kind in money_keys:
        deposit_total += int(kind) * money[kind]

    print("Total: {:d}".format(deposit_total))
## 処理の分岐


# 払い戻し処理

# メイン関数
deposit = deposit()
    
