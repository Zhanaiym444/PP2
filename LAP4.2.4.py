from datetime import datetime

date1 = datetime(2025, 10, 1, 12, 0, 0)
date2 = datetime(2025, 10, 9, 12, 0, 0)
diff = date2 - date1
print("Difference in seconds:", diff.total_seconds())
