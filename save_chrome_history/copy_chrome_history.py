import shutil
import os

source_path = '/Users/mac/Library/Application Support/Google/Chrome/Default/History'  # Update this path
destination_path = '../HistoryTemp'

# Ensure Chrome is closed before running this script
shutil.copyfile(source_path, destination_path)
