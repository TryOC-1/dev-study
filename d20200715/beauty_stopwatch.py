import time

import pyperclip


def convert_just(t, num):
    return str(t).rjust(num)


print(
    "Press Enter to begin.\n"
    'press enter to "click" the stopwatch.\n'
    "press Ctrl-C to quit."
)
input()
print("Started.")
start_time = time.time()
last_time = start_time
lap_num = 1
temp_list = []

try:
    while True:
        input()
        lap_time = round(time.time() - last_time, 2)
        total_time = round(time.time() - start_time, 2)
        lap_num_rjust = convert_just(lap_num, 3)
        total_time_rjust = convert_just(total_time, 5)
        lap_time_rjust = convert_just(lap_time, 5)
        output = f"Lap #{lap_num_rjust} : {total_time_rjust} ({lap_time_rjust})"
        print(output, end="")
        lap_num += 1
        last_time = time.time()
        temp_list.append(output)
except KeyboardInterrupt:
    pyperclip.copy("\n".join(temp_list))
    print("\nDone.")
