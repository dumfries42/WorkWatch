import sqlite3
import datetime

destination_path = "../HistoryTemp"

# Connect to the copied history file
conn = sqlite3.connect(destination_path)
cursor = conn.cursor()

# Execute a query to get URL and title
cursor.execute("SELECT url, title, last_visit_time FROM urls ORDER BY last_visit_time DESC")

# Fetch all results
results = cursor.fetchall()


# Convert Chrome timestamp
def chrome_time_to_str(chrome_time):
    return datetime.datetime(1601, 1, 1) + datetime.timedelta(microseconds=chrome_time)


# Print results
for url, title, last_visit_time in results:
    print(f"URL: {url}, Title: {title}, Last Visited: {chrome_time_to_str(last_visit_time)}")

# Close connection
cursor.close()
conn.close()
