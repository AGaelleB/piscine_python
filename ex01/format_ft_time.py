import time 
from datetime import datetime

time_from_start = time.time()
coma_ver = f"{time_from_start:,.4f}"
scientific_ver = f"{time_from_start:.2e}"

print("Seconds since January 1, 1970: " + str(coma_ver) + " or " + str(scientific_ver) + " in scientific notation")

now = datetime.now()
format = now.strftime("%b %d %Y")

print(format)