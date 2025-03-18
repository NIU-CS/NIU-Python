from decimal import Decimal, ROUND_HALF_DOWN, ROUND_HALF_EVEN, ROUND_UP
from rich import print

def custom_round_05up(value):
    """
    模擬 ROUND_05UP：如果第三位小數為 0 或 5，則進位，否則四捨六入
    """
    value_decimal = Decimal(value)
    third_decimal_place = int((value_decimal * 1000) % 10)  # 取得第三位數字
    if third_decimal_place in [0, 5]:  # 若第三位小數為 0 或 5
        return value_decimal.quantize(Decimal("0.01"), rounding=ROUND_UP)
    return value_decimal.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)  # 否則用正常四捨五入

if __name__ == "__main__":
    # 測試數值
    numbers = [Decimal("3.265"), Decimal("1.32"), Decimal("5.305")]

    # 定義四捨五入的方法
    rounding_methods = {
        "ROUND_HALF_DOWN": ROUND_HALF_DOWN,  # 四捨六入，五不入
        "ROUND_HALF_EVEN": ROUND_HALF_EVEN,  # 四捨六入，五偶數才入
    }

    # 依照不同方法進行四捨五入
    for method, rounding_mode in rounding_methods.items():
        rounded_values = [n.quantize(Decimal("0.01"), rounding=rounding_mode) for n in numbers]
        print(f"[bold cyan]{method}[/bold cyan]: {rounded_values}")

    # 手動處理 ROUND_05UP
    rounded_05up = [custom_round_05up(n) for n in numbers]
    print(f"[bold cyan]ROUND_05UP[/bold cyan]: {rounded_05up}")
