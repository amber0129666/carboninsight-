# CarbonInsight - SDG 13 Personal Carbon Tracker
# 對應聯合國永續發展目標 13：氣候行動
# 獨立開發，Python 實作

def calculate_carbon(km, kwh, meals):
    """
    計算每日碳足跡 (kg CO₂)
    km: 開車公里數
    kwh: 用電度數
    meals: 含肉餐數
    """
    car = km * 0.12      # 每公里 0.12kg CO₂ (平均汽車)
    energy = kwh * 0.5   # 每度電 0.5kg CO₂ (台灣平均)
    food = meals * 2.5   # 每餐牛肉 2.5kg CO₂
    return round(car + energy + food, 1)

# 主程式：互動式輸入
print("CarbonInsight - 你的減碳小幫手 (SDG 13)")
print("=" * 50)

km = float(input("今天開車幾公里？ "))
kwh = float(input("今天用電幾度？ "))
meals = int(input("今天吃幾餐含肉？ "))

total = calculate_carbon(km, kwh, meals)
print("\n" + "=" * 50)
print(f"你今天排放 {total} kg CO₂！")
print("=" * 50)

if total > 15:
    print("建議：多搭公車、吃素一天，可減 5kg 以上！")
elif