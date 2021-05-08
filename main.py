import time
import sys

if len(sys.argv) < 2 :
    print("###Program should be start with  'main.py [Category:ex'Upbit','Creon' and so on]' ###")
    exit()

play_category=sys.argv[1]

time_duration_milisec = 1000
prev_mili_sec = time.time() * 1000

while True:
    cur_mili_sec = time.time() * 1000
    #below if statement is necessary to check for 1sec
    if cur_mili_sec - prev_mili_sec < time_duration_milisec :
        continue

    if play_category == 'Upbit' :
        import os
        upbit_dir=os.path.dirname(__file__)+'/./UpbitPlay'
        print(upbit_dir)
        sys.path.append(upbit_dir)
        import UpbitPlay as Upbit
        Upbit.do_work()

    if play_category == 'Creon':
        print("Creon")
    
    if play_category == "Kiwoom":
        print("Kiwoom")

    """ to check whether time tick is correctly working or not
    from datetime import datetime
    print(datetime.now().strftime("%H:%M:%S"))
    """
    prev_mili_sec = cur_mili_sec