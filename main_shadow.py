#!/Users/mac/miniconda3/bin/python
# -*- coding:utf-8 -*-

import datetime
import os
import time


def add(path, content):
    with open(path, 'a') as f:
        f.write(content + '\n')

def get_today_zsh_history():
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


def get_today_note_path():
    current_date = datetime.datetime.now()
    date_string = current_date.strftime('%Y-%m-%d')
    note_name = date_string + "_auto.md"
    vault_path = "/Users/mac/Library/Mobile Documents/iCloud~md~obsidian/Documents/SecondBrain"
    note_path = "/".join([vault_path, note_name])
    return note_path


if __name__ == '__main__':

    # 保存每天的函数
    zsh_history_today = get_today_zsh_history()
    note_path = get_today_note_path()
    print(note_path)
    with open(note_path, "w") as note_file:
        note_file.write("## Command Lines \n")
        note_file.write("```\n")
        for command in zsh_history_today:
            note_file.write(command + "\n")
        note_file.write("```\n")
