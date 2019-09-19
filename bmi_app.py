def main():
    height = float(input("身長を入力してください (cm) : "))/100
    weight = float(input("体重を入力してください (kg) : "))
    bmi = round(weight/(height**2),2)
    print("あなたのbmiは"+str(bmi)+"です。")

if __name__ == '__main__':
    main()