import hashlib
from collections import Counter
import statistics
import platform
from datetime import datetime
import base64
import urllib.parse
import requests
import random
import string
import math
import json
import os
import random
import requests
import time
from colorama import Fore, Style, init
init(autoreset=True)
NV={
    1:'Bậc thầy tấn công',
    2:'Quyền sắt',
    3:'Thợ lặn sâu',
    4:'Cơn lốc sân cỏ',
    5:'Hiếp sĩ phi nhanh',
    6:'Vua home run'
}
def clear_screen():
    os.system('cls' if platform.system() == "Windows" else 'clear')
def prints(r, g, b, text="text", end="\n"):
    print(f"\033[38;2;{r};{g};{b}m{text}\033[0m", end=end)
def banner(game):
    banner="""
████████╗██████╗ ██╗  ██╗
╚══██╔══╝██╔══██╗██║ ██╔╝
   ██║   ██████╔╝█████╔╝ 
   ██║   ██╔═══╝ ██╔═██╗ 
   ██║   ██║     ██║  ██╗
   ╚═╝   ╚═╝     ╚═╝  ╚═╝  
    """
    for i in banner.split('\n'):
        x,y,z=200,255,255
        for j in range(len(i)):
            prints(x,y,z,i[j],end='')
            x-=4
            time.sleep(0.001)
        print()
    prints(247, 255, 97,"✨" + "═" * 45 + "✨")
    prints(32, 230, 151,f"🌟 XWORLD - {game} v8.PRO🌟".center(45))
    prints(247, 255, 97,"═" * 47)
    prints(7, 205, 240,"Telegram: tankeko12")
    prints(7, 205, 240,"Nhóm Zalo: https://zalo.me/g/viiuml595")
    prints(7, 205, 240,"Admin: Duong Phung | Zalo: 0865656488")
    prints(247, 255, 97,"═" * 47)
def load_data_cdtd():
    if os.path.exists('data-xw-cdtd.txt'):
        prints(0, 255, 243,'Bạn có muốn sử dụng thông tin đã lưu hay không? (y/n): ',end='')
        x=input()
        if x=='y':
            with open('data-xw-cdtd.txt','r',encoding='utf-8') as f:
                return json.load(f)
        prints(247, 255, 97,"═" * 47)
    str="""
    Huướng dẫn lấy link:
    1.Truy cập vào trang web xworld.io
    2.Đăng nhập tải khoản của bạn
    3.Tìm và nhấn vào chạy đua tốc độ
    4. Nhấn lập tức truy cập
    5.Copy link trang web đó và dán vào đây
"""
    prints(218, 255, 125,str)
    prints(247, 255, 97,"═" * 47)
    prints(125, 255, 168,'📋Nhập link của bạn:',end=' ')
    link=input()
    # link='http://escapemaster.net/battleroyale/?userId=10232348&secretKey=9c5d6e0e590c25229d6b398111ffb737eec1f385f7a08f2fa60a5815ef6b65c3&language=vi-VN'
    user_id=link.split('&')[0].split('?userId=')[1]
    user_secretkey=link.split('&')[1].split('secretKey=')[1]
    prints(218, 255, 125,f'    User id của bạn là {user_id}')
    prints(218, 255, 125,f'    User secret key của bạn là {user_secretkey}')
    json_data={
        'user-id':user_id,
        'user-secret-key':user_secretkey,
    }
    with open('data-xw-cdtd.txt','w+',encoding='utf-8') as f:
        json.dump(json_data, f, indent=4, ensure_ascii=False)
    return json_data
def top_100_cdtd(s):
    headers = {
        'accept': '*/*',
        'accept-language': 'vi,en;q=0.9',
        'origin': 'https://sprintrun.win',
        'priority': 'u=1, i',
        'referer': 'https://sprintrun.win/',
        'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Mobile Safari/537.36',
    }
    try:
        response = s.get('https://api.sprintrun.win/sprint/recent_100_issues', headers=headers).json()
        nv=[1,2,3,4,5,6]
        kq=[]
        for i in range(1,7):
            kq.append(response['data']['athlete_2_win_times'][str(i)])
        return nv,kq
    except Exception as e:
        prints(255,0,0,f'Lỗi khi lấy top 100: {e}')
        return top_100_cdtd(s)
def top_10_cdtd(s, headers):
    params = ''
    try:
        response = s.get('https://api.sprintrun.win/sprint/recent_10_issues', params=params, headers=headers).json()
        ki=[]
        kq=[]
        for i in response['data']['recent_10']:
            ki.append(i['issue_id'])
            kq.append(i['result'][0])
        return ki,kq
    except Exception as e:
        prints(255,0,0,f'Lỗi khi lấy top 10: {e}')
        return top_10_cdtd(s, headers)
def print_data(data_top10_cdtd,data_top100_cdtd):
    prints(247, 255, 97,"═" * 47)
    prints(0, 255, 250,"DỮ LIỆU 10 VÁN GẦN NHẤT:".center(50))
    for i in range(len(data_top10_cdtd[0])):
        prints(255,255,0,f'Kì {data_top10_cdtd[0][i]}: Người về nhất : {NV[int(data_top10_cdtd[1][i])]}')
    prints(247, 255, 97,"═" * 47)
    prints(0, 255, 250,"DỮ LIỆU 100 VÁN GẦN NHẤT:".center(50))
    for i in range(6):
        prints(255,255,0,f'{NV[int(i+1)]} về nhất {data_top100_cdtd[1][int(i)]} lần')
    prints(247, 255, 97,"═" * 47)
def selected_NV(data_top10_cdtd, data_top100_cdtd,htr,heso,bet_amount0):
    bet_amount=bet_amount0
    if len(htr)>=1:
        if htr[len(htr)-1]['kq']==False:
            bet_amount=heso*htr[len(htr)-1]['bet_amount']

    try:
        while True:
            res=random.randint(1,6)
            if res!=data_top10_cdtd[1][0]:
                break
        return res,bet_amount
    except Exception as e:
        prints(255,0,0,f'Lỗi khi chọn: {e}')
        return random.randint(1,6),bet_amount
def kiem_tra_kq_cdtd(s, headers,kq,ki):
    start=time.time()
    prints(0, 255, 37,f'Đang đợi kết quả của kì #{ki}')
    while True:
        data_top10_cdtd=top_10_cdtd(s, headers)
        if int(data_top10_cdtd[0][0])==int(ki):
            prints(0, 255, 30,f'Kết quả của kì {ki}: Người về nhất {NV[int(data_top10_cdtd[1][0])]}')
            if data_top10_cdtd[1][0]==kq:
                prints(255, 0, 0,'Bạn đã thua. Chúc bạn may mắn lần sau!')
                return False
            else:
                prints(0, 255, 37,'Xin chúc mừng. Bạn đã thắng!')
                return True
        prints(0, 255, 197,f'Đang đợi kết quả {time.time()-start:.0f}...',end='\r')
def user_asset(s, headers):
    try:
        json_data = {
            'user_id': int(headers['user-id']),
            'source': 'home',
        }

        response = s.post('https://wallet.3games.io/api/wallet/user_asset', headers=headers, json=json_data).json()
        asset={
            'USDT':response['data']['user_asset']['USDT'],
            'WORLD':response['data']['user_asset']['WORLD'],
            'BUILD':response['data']['user_asset']['BUILD']
        }
        return asset
    except Exception as e:
        prints(255,0,0,f'Lỗi khi lấy số dư: {e}')
        return user_asset(s, headers)
def print_stats_cdtd(stats,s,headers,Coin):
    try:
        asset=user_asset(s, headers)
        prints(70, 240, 234,'Thống kê:')
        prints(50, 237, 65,f'Số trận thắng : {stats['win']}/{stats['win']+stats['lose']}')
        prints(50, 237, 65,f'Chuỗi thắng : {stats['streak']}(max:{stats['max_streak']})')
        prints(0, 255, 20, f"Lời: {asset[Coin] - stats['asset_0']:.2f} {Coin}")

    except Exception as e:
        prints(255,0,0,f'Lỗi khi in thống kê: {e}')

def print_wallet(s, asset):
    prints(23, 232, 159,f' USDT:{asset['USDT']:.2f}    WORLD:{asset['WORLD']:.2f}    BUILD:{asset['BUILD']:.2f}'.center(50))
def bet_cdtd(s, headers,ki,kq,Coin,bet_amount):
    prints(255,255,0,f'Đang đặt {Coin} cho kì {ki}:')
    try:
        json_data = {
            'issue_id': int(ki),
            'bet_group': 'not_winner',
            'asset_type': Coin,
            'athlete_id': kq,
            'bet_amount': bet_amount,
        }
        response = s.post('https://api.sprintrun.win/sprint/bet', headers=headers, json=json_data).json()
        print(response)
        if response['code']==0 and response['msg']=='ok':
            prints(0, 255, 19,f'Đã đặt {bet_amount} {Coin} thành công vào "Ai không là quán quân"')
    except Exception as e:
        prints(255,0,0,f'Lỗi khi đặt {Coin}: {e}')
def main_cdtd():
    s=requests.Session()
    banner("CHẠY ĐUA TỐC ĐỘ")
    data=load_data_cdtd()
    headers = {
        'accept': '*/*',
        'accept-language': 'vi,en;q=0.9',
        'cache-control': 'no-cache',
        'country-code': 'vn',
        'origin': 'https://xworld.info',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://xworld.info/',
        'sec-ch-ua': '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
        'user-id': data['user-id'],
        'user-login': 'login_v2',
        'user-secret-key': data['user-secret-key'],
        'xb-language': 'vi-VN',
    }
    asset=user_asset(s, headers)
    print_wallet(s, user_asset(s, headers))
    str="""
    Nhập loại tiền mà bạn muốn chơi:
        1.USDT
        2.BUILD
        3.WORLD
    """
    prints(219, 237, 138,str)
    while True:
        prints(125, 255, 168,'Nhập loại tiền bạn muốn chơi (1/2/3):',end=' ')
        x=input()
        if int(x)>=1 and int(x)<=3:
            if x=='1':
                Coin='USDT'
                break
            elif x=='2':
                Coin='BUILD'
                break
            else:
                Coin='WORLD'
                break
        else:
            prints(247, 30, 30, 'Nhập sai, vui lòng nhập lại ...', end='\r')
    bet_amount0=float(input(f'Nhập số {Coin} muốn đặt: '))
    heso=int(input('Nhập hệ số cược sau thua: '))
    delay1=int(input('Sau bao nhiêu ván thì tạm nghỉ (Nhập 999 nếu không muốn tạm nghỉ): '))
    delay2=int(input(f'Sau {delay1} ván thì tạm nghỉ bao nhiêu ván (Nhập 0 nếu không muốn nghỉ): '))
    stats={
        'win':0,
        'lose':0,
        'streak':0,
        'max_streak':0,
        'asset_0':asset[Coin]
    }
    clear_screen()
    banner('CHẠY ĐUA TỐC ĐỘ')
    htr=[]
    tong=0
    while True:
        tong+=1
        prints(247, 255, 97,"═" * 47)
        print_wallet(s, user_asset(s, headers))
        data_top10_cdtd=top_10_cdtd(s, headers)
        data_top100_cdtd=top_100_cdtd(s)
        kq,bet_amount=selected_NV(data_top10_cdtd, data_top100_cdtd,htr,heso,bet_amount0)
        print_stats_cdtd(stats,s,headers,Coin)
        prints(0, 246, 255,f'BOT CHỌN : {NV[int(kq)]}')
        cycle = delay1 + delay2
        pos = (tong - 1) % cycle
        if pos < delay1:
            stop=False
            bet_cdtd(s, headers,data_top10_cdtd[0][0]+1,kq,Coin,bet_amount)
        else:
            stop=True
            prints(255,255,0,f'Ván này tạm nghỉ')
            bet_amount=bet_amount0
        result=kiem_tra_kq_cdtd(s, headers,kq,data_top10_cdtd[0][0]+1)
        if result==True:
            stats['win']+=1
            stats['streak']+=1
            stats['max_streak']=max(stats['max_streak'],stats['streak'])
            if stop==False:
                htr.append({'kq':True,'bet_amount':bet_amount})
        elif result== False:
            stats['streak']=0
            stats['lose']+=1
            if stop==False:
                htr.append({'kq':False,'bet_amount':bet_amount})

        time.sleep(10)
main_cdtd()
