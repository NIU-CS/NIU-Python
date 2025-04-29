from rich import print

if __name__ == "__main__":
    # tasks = ["寫報告", "交作業", "回覆 Email", "繳電話費", "準備期中考"]
    tasks = []
    while True:
        task = input("請輸入任務：")
        if task == "":
            break
        tasks.append(task)
    tasks_iterator = iter(tasks)
    finished_task_count = 0
    current_task_index = -1
    while True: # input = s(skip)/q(quit)/enter
        current_task_index += 1
        if current_task_index == len(tasks):
            print("已完成或跳過所有任務！")
            break
        task = next(tasks_iterator)
        print(f"任務：{task}")
        choose = input("請選擇操作：s(跳過)/q(退出)/enter(完成)")
        if choose == "s":
            continue
        elif choose == "q":
            break
        elif choose == "":
            print(f"已完成 {finished_task_count + 1} 個任務：{task}")
            finished_task_count += 1
        else:
            print("無效的選擇，請重新輸入。")
