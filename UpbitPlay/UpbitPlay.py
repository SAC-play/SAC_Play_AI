# import sys
# sys.path.append('../Stock/Upbit')
# import UpbitApi as Upbit
import os
import sys
import json
Current_path =os.path.dirname(os.path.realpath(__file__))
api_dirName=Current_path+'/../../Stock/Upbit/api'
sys.path.append(api_dirName)
import UpbitApi as UA
Craw_api_dirName=Current_path+'/../../Crawling'
sys.path.append(Craw_api_dirName)
import CrawilngAPI as CRAW

def do_work() :
    #전략 불러오기
    with open(Current_path+'/strategy/ardr.json', 'r') as f:
        json_data = json.load(f)
    coinName = json_data['market']
    ceiling = int(json_data['ceiling'])
    floor = int(json_data['floor'])
    f.close

    # 전략 코인 조회
    json_ticker = UA.get_market_info_ticker(coinName)
    for a in json_ticker:
        tradePrice = int(a['trade_price'])

    print(coinName + ' 현재 가격 : ' + str(tradePrice) + '원')
    # print(json_ticker)
    #계좌 내용 조회 
    accountData = UA.get_my_account_info()
    # "market" : "KRW-XRP",
    # "ceiling" : "5",
    # "floor" : "2"
    buy_sell_execute(coinName, accountData, ceiling, floor, tradePrice)
    CRAW.crawling(accountData)
# 사고 파는 함수   
def buy_sell_execute(coinName, accountData, ceiling, floor, tradePrice) :
    # 전략의 데이터가 계좌에 존재할 때,
    if any(coinName[coinName.find("-")+1:] in s['currency'] for s in accountData) :
        for a in accountData:
            if(a['currency']==coinName[coinName.find("-")+1:]):
                avgBuyPrice=int(a['avg_buy_price'])
                print('평단가 : ' + str(avgBuyPrice) +', 평단가+5% :' + str(avgBuyPrice+avgBuyPrice*(ceiling/100)))
                if avgBuyPrice+avgBuyPrice*(ceiling/100) <= tradePrice :
                    print('평단보다 5% 많아 판매를 진행합니다.') #판매함수 넣기
                elif avgBuyPrice-avgBuyPrice*(floor/100) >= tradePrice :
                    print('평단보다 2% 낮아 판매를 진행합니다.') #판매함수 넣기
                else :
                    print('어느 전략에도 도달하지 않았습니다.')
    #전략의 데이터가 계좌에 존재하지 않을 때, 사고 팔기
    else :
        print(coinName + "은 계좌에 존재하지 않습니다.")