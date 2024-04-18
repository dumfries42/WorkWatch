import datetime
import shutil
import sqlite3
import datetime
import pytz


def chrome_time_to_datetime(chrome_time):
    """Convert Chrome's timestamp to a Python datetime object."""
    utc_time = datetime.datetime(1601, 1, 1, tzinfo=pytz.utc) + datetime.timedelta(microseconds=chrome_time)
    local_time = utc_time.astimezone(pytz.timezone('Asia/Shanghai'))  # Adjust to your local timezone
    return local_time


def get_todays_chrome_history(history_path):
    # 连接到历史记录数据库
    conn = sqlite3.connect(history_path)
    cursor = conn.cursor()

    # 获取今天日期的开始和结束时间戳
    now = datetime.datetime.now()
    start_of_today = datetime.datetime(now.year, now.month, now.day)
    end_of_today = start_of_today + datetime.timedelta(days=1)

    # 转换为 Chrome 时间戳
    start_of_today_chrome = int((start_of_today - datetime.datetime(1601, 1, 1)).total_seconds() * 1000000)
    end_of_today_chrome = int((end_of_today - datetime.datetime(1601, 1, 1)).total_seconds() * 1000000)

    # 执行查询：获取今天的历史记录
    query = f"SELECT url, title, last_visit_time FROM urls WHERE last_visit_time >= {start_of_today_chrome} AND last_visit_time < {end_of_today_chrome} ORDER BY last_visit_time DESC"
    cursor.execute(query)

    # 获取结果
    results = cursor.fetchall()

    # 关闭数据库连接
    cursor.close()
    conn.close()

    # 打印结果
    for url, title, last_visit_time in results:
        readable_time = chrome_time_to_datetime(last_visit_time)
        print(f"URL: {url}, Title: {title}, Last Visited: {readable_time}")

    return results

source_path = '/Users/mac/Library/Application Support/Google/Chrome/Default/History'  # Update this path
destination_path = '../HistoryTemp'

# Ensure Chrome is closed before running this script
shutil.copyfile(source_path, destination_path)


# 指定 Chrome 历史数据库复制的路径
history_copy_path = '../HistoryTemp'
get_todays_chrome_history(history_copy_path)
