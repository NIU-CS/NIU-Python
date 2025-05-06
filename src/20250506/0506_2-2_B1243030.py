from rich import print

if __name__ == "__main__":
    account = input("請輸入帳號：")
    password = input("請輸入密碼：")
    mid_index = len(password) // 2
    half_length = len(password) // 4
    core_password = password[mid_index - half_length : mid_index + half_length + (len(password) % 2)]

    print(f"\n代碼字首：{account[:2] + account[-2:]}")
    print(f"核心密碼片段：{core_password}")

    enc_result = account[:2] + account[-2:] + core_password
    print(f"加密後結果：{enc_result[::-1]}")

    print(f"最終結果：{enc_result[::-1] * 2}")
