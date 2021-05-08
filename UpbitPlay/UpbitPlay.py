# import sys
# sys.path.append('../Stock/Upbit')
# import UpbitApi as Upbit
import os
import sys
import json
api_dirName=os.path.dirname(os.path.realpath(__file__))+'/../../Stock/Upbit/api'
sys.path.append(api_dirName)
import UpbitApi as UA


def do_work() :
    with open(os.path.dirname(os.path.realpath(__file__))+'/strategy/ardr.json', 'r') as f:
        json_data = json.load(f)
    UA.get_market_info_ticker(json_data['market'])
