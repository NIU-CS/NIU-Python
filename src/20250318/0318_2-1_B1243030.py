from decimal import Decimal, ROUND_DOWN, ROUND_UP, ROUND_HALF_UP
from rich import print

if __name__ == "__main__":
    # 測試數值
    numbers = [Decimal("3.265"), Decimal("1.32"), Decimal("5.305")]

    # 定義四捨五入的方法
    rounding_methods = {
        "ROUND_DOWN": ROUND_DOWN,         # 無條件捨去
        "ROUND_UP": ROUND_UP,             # 無條件進位
        "ROUND_HALF_UP": ROUND_HALF_UP,   # 傳統四捨五入
    }

    # 依照不同方法進行四捨五入
    for method, rounding_mode in rounding_methods.items():
        rounded_values = [n.quantize(Decimal("0.01"), rounding=rounding_mode) for n in numbers]
        print(f"[bold cyan]{method}[/bold cyan]: {rounded_values}")
