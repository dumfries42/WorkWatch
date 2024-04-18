import os
import time


def read_zsh_history():
    # 获取今天的日期
    today = time.strftime('%Y-%m-%d')
    home_directory = os.path.expanduser('~')
    history_path = os.path.join(home_directory, '.zsh_history')

    today_history = []
    try:
        with open(history_path, 'r', errors='ignore') as file:
            for line in file:
                # 尝试提取时间戳和命令
                parts = line.split(';')
                if len(parts) < 2:
                    continue

                timestamp = int(parts[0].split(':')[1])
                command = parts[1]

                # 将时间戳转换为日期
                command_date = time.strftime('%Y-%m-%d', time.localtime(timestamp))

                # 如果命令是今天的，则添加到列表
                if command_date == today:
                    today_history.append(command.strip())
    except FileNotFoundError:
        print("Zsh history file not found.")

    return today_history


# 调用函数并打印输出
zsh_history_today = read_zsh_history()
for command in zsh_history_today:
    print(command)
