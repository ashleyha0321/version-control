import datetime
from datetime import datetime

now = datetime.now()
currentTime = now.strftime("%Y/%m/%d %H:%M:%S")
print("Current Time:", currentTime)

with open("version.md", "w") as file:
    file.write(currentTime)

