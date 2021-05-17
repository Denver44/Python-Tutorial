# -------------------------- TIME ------------------------
import time
initial = time.time()
i = 0
while i < 5:
    print(i, end=" ")
    time.sleep(2)  # we can sleep the function for 2 seond.
    i += 1

print()
print((time.time() - initial), " sec")


# --------------------- To print local time and date----------------
localtime = time.asctime(time.localtime())
print(localtime)

# time.time count the ticks.
# localtime goves the current time in tuple
# asctime convert the covert like below.
