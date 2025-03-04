from rich import print

def base_convert(number: str, from_base: int, to_base: int) -> str:
    try:
        # 先將數字從 from_base 轉為 10 進制
        decimal_number = int(number, from_base)

        # 再將 10 進制數字轉為目標進制
        if to_base == 10:
            return str(decimal_number)

        digits = "0123456789ABCDEF"
        result = ""
        while decimal_number > 0:
            remainder = decimal_number % to_base
            result = digits[remainder] + result
            decimal_number //= to_base

        return result if result else "0"
    except ValueError:
        return "[red]無效的輸入，請確認數字與進制是否正確！[/red]"

if __name__ == "__main__":
    conversion_from, conversion_to = input("請輸入想要的轉換進制 (例如 2 10 或 16 8): ").split()
    conversion_from, conversion_to = int(conversion_from), int(conversion_to)

    if conversion_from not in {2, 4, 8, 10, 16} or conversion_to not in {2, 4, 8, 10, 16}:
        print("[red]僅支援 2、4、8、10、16 進制！[/red]")
    else:
        number = input(f"請輸入 {conversion_from} 進制的數字: ")
        result = base_convert(number, conversion_from, conversion_to)
        print(f"[green]{conversion_from} 進制的 {number} 轉為 {conversion_to} 進制為: {result}[/green]")
