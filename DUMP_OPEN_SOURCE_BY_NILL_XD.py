# WRITTEN BY NILL-XD
import os
import uuid
import json
import requests
from random import choice as ch

colors = ['\033[91m','\033[92m','\033[93m','\033[94m','\033[95m','\033[96m','\033[97m']
xuid = str(uuid.uuid4())

def ONE__(token,uid):
    headers = {
        'Host': 'graph.facebook.com',
        'Priority': 'u=3, i',
        'Content-Type': 'application/x-www-form-urlencoded',
        'X-Graphql-Client-Library': 'graphservice',
        'X-Fb-Privacy-Context': 'c0000000ebe595b4',
        'X-Fb-Background-State': '1',
        'User-Agent': '[FBAN/FB4A;FBAV/369.0.0.18.103;FBBV/373751439;FBDM/{density=1.6,width=720,height=1474};FBLC/en_US;FBRV/0;FBCR/Grameenphone;FBMF/realme;FBBD/realme;FBPN/com.facebook.katana;FBDV/RMX2185;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]',
        'X-Fb-Net-Hni': '47001',
        'X-Fb-Sim-Hni': '47001',
        'Authorization': f'OAuth {token}',
        'X-Fb-Connection-Type': 'WIFI',
        'X-Fb-Device-Group': '2572',
        'X-Tigon-Is-Retry': 'False',
        'X-Fb-Friendly-Name': 'FriendListContentQuery',
        'X-Fb-Request-Analytics-Tags': 'graphservice',
        'X-Fb-Http-Engine': 'Liger',
        'X-Fb-Client-Ip': 'True',
        'X-Fb-Server-Cluster': 'True',
    }
    var = {"profile_id":uid,
           "profile_image_size":96,
           "friends_paginating_first":20}
    data = {
        'client_doc_id': '36431518109556416924349542983',
        'method': 'post',
        'locale': 'en_US',
        'pretty': 'false',
        'format': 'json',
        'purpose': 'fetch',
        'variables': json.dumps(var),
        'fb_api_req_friendly_name': 'FriendListContentQuery',
        'fb_api_caller_class': 'graphservice',
        'fb_api_analytics_tags': '["At_Connection","GraphServices"]',
        'server_timestamps': 'true',
    }
    try:
        response = requests.post('https://graph.facebook.com/graphql', headers=headers, data=data).json()
        for friend in response['data']['user']['friends']['edges']:
            friend_id = friend['node']['id']
            friend_name = friend['node']['name']
            print(f"{ch(colors)}{friend_id}|{friend_name}\033[0m")
            with open('DUMP.txt', 'a', encoding='utf-8') as f:
                f.write(friend_id+'|'+friend_name+'\n')
        e_c = response['data']['user']['friends']['page_info']['end_cursor']
    except Exception:
        exit('ERROR')
    return two9(e_c,token,uid)


def two9(e_c,token,uid):
    headers = {
        'Host': 'graph.facebook.com',
        'Priority': 'u=3, i',
        'Content-Type': 'application/x-www-form-urlencoded',
        'X-Graphql-Client-Library': 'graphservice',
        'X-Fb-Privacy-Context': 'c0000000ebe595b4',
        'X-Fb-Background-State': '1',
        'User-Agent': '[FBAN/FB4A;FBAV/369.0.0.18.103;FBBV/373751439;FBDM/{density=1.6,width=720,height=1474};FBLC/en_US;FBRV/0;FBCR/Grameenphone;FBMF/realme;FBBD/realme;FBPN/com.facebook.katana;FBDV/RMX2185;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]',
        'X-Fb-Net-Hni': '47001',
        'X-Fb-Sim-Hni': '47001',
        'Authorization': f'OAuth {token}',
        'X-Fb-Connection-Type': 'WIFI',
        'X-Fb-Device-Group': '2572',
        'X-Tigon-Is-Retry': 'False',
        'X-Fb-Friendly-Name': 'FriendListContentQuery',
        'X-Fb-Request-Analytics-Tags': 'graphservice',
        'X-Fb-Http-Engine': 'Liger',
        'X-Fb-Client-Ip': 'True',
        'X-Fb-Server-Cluster': 'True',
    }
    var = {
    "friends_paginating_at_stream_use_customized_batch": False,
    "profile_image_size": 96,
    "paginationPK": uid,
    "profile_id": uid,
    "friends_paginating_first": 20,
    "friends_paginating_after_cursor": e_c
    }
    data = {
        "client_doc_id": "24605340978403080720500702641",
        "method": "post",
        "locale": "user",
        "pretty": "false",
        "format": "json",
        "purpose": "fetch",
        "fb_api_client_context": '{"load_next_page_counter":1,"client_connection_size":20}',
        "variables": json.dumps(var),
        "fb_api_req_friendly_name": "FriendListContentQuery_At_Connection_Pagination_User_friends_paginating",
        "fb_api_caller_class": "ConnectionManager",
        "fb_api_analytics_tags": '["At_Connection","GraphServices"]',
        "client_trace_id": xuid,
        "server_timestamps": "true"
    }
    response = requests.post('https://graph.facebook.com/graphql', headers=headers, data=data).json()
    friends = response['data']['node']['friends']['edges']
    for friend in friends:
        print(f"{ch(colors)}{friend['node']['id']}|{friend['node']['name']}\033[0m")
        with open('DUMP.txt', 'a', encoding='utf-8') as f:
            f.write(friend['node']['id'] + '|' + friend['node']['name'] + '\n')
    e_c = response['data']['node']['friends']['page_info']['end_cursor']
    return two9(e_c,token,uid)


def menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\n-----------------------------------\n    DUMPING TOOL BY NILL XD\n          OPEN SOURCE\n-----------------------------------')
    token = str(input('PUT YOUR TOKEN HERE >>\033[92m '))
    uid = str(input('\033[97mPUT PUBLIC UID        >>\033[92m '))
    print('\033[97m\n-----------------------------------\n    DUMPING TOOL BY NILL XD\n          OPEN SOURCE\n-----------------------------------')
    ONE__(token,uid)

menu()
