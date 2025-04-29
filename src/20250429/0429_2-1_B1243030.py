from rich import print

if __name__ == "__main__":
    print("長度轉換工具，附上單位例如 (FT, ft, M, m)")
    length_unit = input("請輸入長度和單位：")
    length_unit = length_unit.strip()

    if "FT" in length_unit.upper():
        length = float(length_unit.upper().replace("FT", ""))
        print(f"{length} feet = {length * 0.3048} meters")
    elif "M" in length_unit.upper():
        length = float(length_unit.upper().replace("M", ""))
        print(f"{length} meters = {length / 0.3048} feet")
    else:
        print("不支援的單位")
