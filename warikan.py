def main():
    amount = int(input("金額を入力してください : "))
    member = int(input("人数を入力してください : "))
    payment = amount // member
    reminder = amount % member
    payment, reminder = divmod(amount, member)
    print(f"1あたり{str(payment)}円です。端数は{str(reminder)}円です。")


if __name__ == '__main__':
    main()