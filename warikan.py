def main():
    amount = int(input("金額を入力してください : "))
    member = int(input("人数を入力してください : "))
    print(f"1あたり{str(amount // member)}円です。端数は{str(amount % member)}円です。")

if __name__ == '__main__':
    main()