from set_interval import *

import time

def interval(name="world"):
  print(f"Hello {name}!")

interval1 = setInterval(interval, 2, autostart=False) 
interval1.change_argument(["Jane"])
interval1.start()

time.sleep(5)
interval1.change_argument(["Rudy"])

# output:
# Hello Jane!
# Hello Jane!
# Hello Rudy!
# Hello Rudy!
# Hello Rudy!
# ...
