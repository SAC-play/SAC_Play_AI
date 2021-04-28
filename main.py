import time

time_duration_milisec = 1000
prev_mili_sec = time.time() * 1000

while True:
    cur_mili_sec = time.time() * 1000
    #below if statement is necessary to check for 1sec
    if cur_mili_sec - prev_mili_sec < time_duration_milisec :
        continue

    """ to check whether time tick is correctly working or not
    from datetime import datetime
    print(datetime.now().strftime("%H:%M:%S"))
    """
    prev_mili_sec = cur_mili_sec