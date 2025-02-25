import json

with open("20250225/age.json", "r") as file:
    data = json.load(file)

age = int(input("請輸入你的年齡: "))

if age >= data["Taiwan"]:
    print("你有投票權")
else:
    print("你沒有投票權")
