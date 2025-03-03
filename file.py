#-----------------[ MODULE ]-------------------#
import os
def modules():
	os.system('pkg update -y && pkg upgrade -y')
	os.system('clear')
	try: 
		import rich
	except ModuleNotFoundError:
		print("\x1b[1;97m• \x1b[1;91m>>\x1b[1;97m RICH IS BEING INSTALLED \033[1;37m")
		os.system('pip install rich --quiet')
		print("\x1b[1;97m• \x1b[1;91m>>\x1b[1;97m RICH HAS BEEN INSTALLED \033[1;37m")
	except:exit()
	try:
		import bs4
	except ModuleNotFoundError:
		print("\x1b[1;97m• \x1b[1;91m>>\x1b[1;97m BS4 IS BEING INSTALLED \033[1;37m")
		os.system('pip install bs4 --quiet')
		print("\x1b[1;97m• \x1b[1;91m>>\x1b[1;97m BS4 HAS BEEN INSTALLED \033[1;37m")
	except:exit()
	try:
		import requests
	except ModuleNotFoundError:
		print("\x1b[1;97m• \x1b[1;91m>>\x1b[1;97m REQUESTS IS BEING INSTALLED \033[1;37m")
		os.system('pip install requests --quiet')
		print("\x1b[1;97m• \x1b[1;91m>>\x1b[1;97m REQUESTS HAS BEEN INSTALLED \033[1;37m")
	except:exit()
	exit()
try:
	import requests,bs4,json,os,sys,random,datetime,time,re,multiprocessing,socket,marshal
	import os, requests, marshal, zlib, base64
	from bs4 import BeautifulSoup as bs
	from bs4 import BeautifulSoup
	import urllib3,rich,base64
	from rich.table import Table as me
	from rich.console import Console as sol
	from bs4 import BeautifulSoup as sop
	from concurrent.futures import ThreadPoolExecutor as tred
	from rich.console import Group as gp
	from rich.panel import Panel as nel
	from rich.panel import Panel
	from rich.tree import Tree
	from rich.panel import Panel as nel
	from rich.panel import Panel as panel
	from rich import print as cetak
	from rich.markdown import Markdown as mark
	from rich.columns import Columns as col
	from rich import print as prints
	from rich import pretty
	from rich.text import Text as tekz
	from time import localtime as lt	
	import os,requests,json,time,re,random,sys,uuid,string,subprocess,platform
	from concurrent.futures import ThreadPoolExecutor as ThreadPool
	pretty.install()
	CON=sol()
except ModuleNotFoundError:
	modules()	
#------------[ COLOR ]--------------#
P = '\x1b[1;97m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[38;5;50m'
Z = "\x1b[38;5;83m"
X = "\x1b[38;5;46m"
m = '\x1b[1;91m'
b = '\33[1;96m'	
#---------------------[IP]---------------------#
try:
	net = requests.get("http://ip-api.com/json/").json()["isp"]
	ipxx = requests.get("https://api.ipify.org").text    
except requests.exceptions.ConnectionError:
	print('\033[1;37m—————————————————————————\x1b[1;97m')
	print("\x1b[1;97m• \x1b[1;91m>>\x1b[1;97m CHECK YOUR INTERNET")
	time.sleep(1)
	exit()
	
#------------------[ USER-AGENT ]-------------------#
def generate_user_agent():
    application_version = f"{random.randint(11, 77)}.0.0.{random.randrange(9, 49)}{random.randint(11, 77)}"
    application_version_code = str(random.randint(000000000, 999999999))
    ua = (
        f"[FBAN/FB4A;FBAV/{application_version};FBBV/{application_version_code};"
        "{density=3.75,width=1080,height=2400};FBLC/en_NZ;FBRV/{random.randint(000000000, 999999999)};"
        "FBCR/Etisalat Af;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/CPH2209;FBSV/10;FBOP/19;"
        "FBCA/armeabi-v7a:armeabi;]")
    return ua
#--------------------[ UA-UPDATE ]--------------#
Ua = generate_user_agent()
#------------------[ CUTS ]---------------#
def clear():
    os.system('clear')
def back():
    menu()	
def contact():
    os.system('xdg-open https://chat.whatsapp.com/GKCh3wB9KoU9oDuy0MsZ7v')
    back()
def linex():
    print('\033[1;37m=====================================================\x1b[1;97m')
def animation(u):
    for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.01)    
#------------------[ LOGO ]-----------------#
logo =f"""    """
#--------------------[ ENTRY ]--------------#    

def entr():
    clear()
    print(logo)
    print(" \x1b[1;91m• \x1b[1;97m1\x1b[1;91m >\x1b[1;97m LOGIN TOOL BY COOKIE")
    print(" \x1b[1;91m• \x1b[1;97m2\x1b[1;91m >\x1b[1;97m WITHOUT COOKIE MENU ")
    print(" \x1b[1;91m• \x1b[1;97m0\x1b[1;91m >\x1b[1;97m CONTACT ADMIN ")
    linex()
    ll = input(' \x1b[1;97m• \x1b[1;91m--->\x1b[1;97m ')
    if ll == '1':
        login()
    elif ll == '2':        
        menu_next()
    elif ll == '0':        
        contact()
    else:
        linex()
        animation('•\x1b[1;91m -->\x1b[1;97m SELECT CORRECTLY ')
        time.sleep(3)
        entr()


#--------------------[ LOGIN BY COOKIE ]--------------#    
ses = requests.Session()
def login():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3)
		except KeyError:
			login_lagi334()
		except requests.exceptions.ConnectionError:
			li = '# INTERNET CONNECTION PROBLEM, CHECK AND TRY AGAIN'
			lo = mark(li, style='red')
			sol().print(lo, style='cyan')
			exit()
	except IOError:
		login_lagi334()


def login_lagi334():
 try:    
  linex()
  print("\033[1;37m \x1b[1;97m• \x1b[1;91m>>\x1b[1;97m USE INSTA ADDED COOKIE !!")
  linex()
  cookie=input(f'{P}\033[1;37m \x1b[1;97m• \x1b[1;91m>>\x1b[1;97m ENTER COOKIE :\x1b[1;92m ')
  linex()
  open(".cok.txt", "w").write(cookie)
  with requests.Session() as rsn:
   try:
    rsn.headers.update({
                    'Accept-Language': 'id,en;q=0.9',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
                    'Referer': 'https://www.instagram.com/',
                    'Host': 'www.facebook.com',
                    'Sec-Fetch-Mode': 'cors',
                    'Accept': '*/*',
                    'Connection': 'keep-alive',
                    'Sec-Fetch-Site': 'cross-site',
                    'Sec-Fetch-Dest': 'empty',
                    'Origin': 'https://www.instagram.com',
                    'Accept-Encoding': 'gzip, deflate',
                })
    response = rsn.get('https://www.facebook.com/x/oauth/status?client_id=124024574287414&wants_cookie_data=true&origin=1&input_token=&sdk=joey&redirect_uri=https://www.instagram.com/brutalid_/', cookies={'cookie':cookie})
    if '"access_token":' in str(response.headers):
     token = re.search('"access_token":"(.*?)"', str(response.headers)).group(1)
     print(f"\033[1;37m \x1b[1;97m• \x1b[1;91m>>\x1b[1;97m UR TOKEN : {b}{token}")
     open(".token.txt", "w").write(token)     
     linex();animation('\033[1;37m \x1b[1;97m• \x1b[1;91m>>\x1b[1;97m COOKIE LOGINED SUCCESSFUL !! ');linex();xxz = input('\033[1;37m \x1b[1;97m• \x1b[1;91m>>\x1b[1;97m PRESS ENTER TO MENU');menu()
     
    else:
     print(''%(m, p))

   except:
    animation(f' {P}\033[1;37m\x1b[1;97m×\x1b[1;91m-->\x1b[1;97m{m} COOKIE EXPIRED!!');linex();xxz = input('\033[1;37m \x1b[1;97m• \x1b[1;91m>>\x1b[1;97m PRESS ENTER TO BACK');back()

  print(f' ');time.sleep(1)
  exit()
 except Exception as e:
  os.system("rm -f .token.txt")
  os.system("rm -f .cok.txt")
  animation('\033[1;37m \x1b[1;97m• \x1b[1;91m>>\x1b[1;97m SELECT CORRECTLY ')
  print(e)
  exit()
  
#------------------[ MENU ]----------------#
def menu():
    clear(),print(logo)       
    try:
        cok = open('.cok.txt','r').read()
        token = open('.token.txt','r').read()
    except (IOError,KeyError,FileNotFoundError):
        entr()
    try:
        info_datafb = ses.get(f"https://graph.facebook.com/me?fields=name,id&access_token={token}", cookies = {'cookies':cok}).json()
        id = info_datafb["id"]
        nama = info_datafb["name"]
    except requests.exceptions.ConnectionError:
        exit(' \x1b[1;97m• \x1b[1;91m>>\x1b[1;97m CHECK YOUR INTERNET !! ')
    except KeyError:
        try:
            os.remove(".cok.txt")
            os.remove(".token.txt")
        except:
            pass  
    print(f""" \x1b[1;91m• \x1b[1;97m1 \x1b[1;91m>\x1b[1;97m CREATE MIX SERIES FILE  """)
    print(f""" \x1b[1;91m• \x1b[1;97m2 \x1b[1;91m>\x1b[1;97m CREATE NEW SERIES FILE  """)
    print(f""" \x1b[1;91m• \x1b[1;97m3 \x1b[1;91m>\x1b[1;97m CREATE FILE FROM FOLLOWERS """)
    print(f""" \x1b[1;91m• \x1b[1;97m4 \x1b[1;91m>\x1b[1;97m SEPARATE FILE IDS""")
    print(f""" \x1b[1;91m• \x1b[1;97m5 \x1b[1;91m>\x1b[1;97m REMOVE DUP ID""")
    print(""" \x1b[1;91m• \x1b[1;97m6 \x1b[1;91m>\x1b[1;97m CONTACT ADMIN """)
    print(""" \x1b[1;91m• \x1b[1;97m0 \x1b[1;91m>\x1b[1;97m LOGOUT COOKIE """)
    linex()
    HEART = input(' \x1b[1;97m• \x1b[1;91m --->\x1b[1;97m  ')
    if HEART in ['111']:
        login()
        dump_massal()
    elif HEART in ['1']:
        dump_file()
    elif HEART in ['02','2']:
    	dump_new()
    elif HEART in ['03','3']:
    	dump_followers()
    elif HEART in ['4','04']:
        saprate()
    elif HEART in ['5','05']:
        remove_dub()
    elif HEART in ['0']:    			
        os.system('rm -rf .cok.txt && rm -rf .token.txt');linex()
        animation('\033[1;37m \x1b[1;97m• \x1b[1;91m>>\x1b[1;97m SUCESSFULLY REMOVED COOKIE')
        entr()
    elif HEART in ['6']:
        contact()
    else:
        animation("\033[1;37m \x1b[1;97m• \x1b[1;91m>>\x1b[1;97m INVALID OPTION !!")
        back()
        
 #------------------[ MENU NEXT ]----------------#
def menu_next():
    linex()
    print(""" \x1b[1;91m• \x1b[1;97m1 \x1b[1;91m>\x1b[1;97m SEPARATE LINK""")
    print(""" \x1b[1;91m• \x1b[1;97m2 \x1b[1;91m>\x1b[1;97m REMOVE DUP ID""")
    print(""" \x1b[1;91m• \x1b[1;97m0\x1b[1;91m >\x1b[1;97m BACK TO MENU """)
    linex()
    nyx = input(' \x1b[1;97m• \x1b[1;91m---> \x1b[1;97m ')
    if nyx == '111':
        login()
        dump_massal()
    elif nyx == '1':
        saprate()
    elif nyx == '2':
        remove_dub()
    elif nyx == '0':
    	back()
    else:
        animation("\033[1;37m \x1b[1;97m• \x1b[1;91m>>\x1b[1;97m INVALID OPTION !!")
        menu_next()


#----------------[ CREATE FILE ]-----------------#
import requests
import random
import time

file_name = ''

def dump_file():
    global file_name
    idxx = []  
    linex()
    try:
        token = open('.token.txt', 'r').read().strip()
        cok = open('.cok.txt', 'r').read().strip()
    except IOError:
        login()
    
    print(' \x1b[1;97m• \x1b[1;91m>>\x1b[1;97m ENTER FILE NAME WITHOUT "/SDCARD/"');linex()
    naame = input(' \x1b[1;97m• \x1b[1;91m>>\x1b[1;97m FILE NAME : ')
    linex()
    file_name = '/sdcard/' + naame

    try:
        id_limit = int(input(' \x1b[1;97m• \x1b[1;91m>>\x1b[1;97m INPUT UID LIMIT : '))
        linex()
    except ValueError:
        animation("\x1b[1;91m×--> SELECT CORRECTLY!!")
        return menu()  
        
    if id_limit < 1 or id_limit > 100000000:
        animation("\x1b[1;91m×--> LIMIT OUT OF RANGE!!")
        return menu()  

    ses = requests.Session()
    uid = []
    id = []
    non_public_uids = []  
    color = [
        '\x1b[38;5;226m', '\x1b[38;5;46m', '\x1b[1;91m', 
        '\x1b[38;5;248m', '\x1b[38;5;44m', '\x1b[38;5;46m', 
        '\x1b[38;5;208m', '\x1b[38;5;46m', '\x1b[38;5;231m', 
        '\x1b[38;5;46m', '\x1b[1;91m'
    ]

    for SAURAVXX in range(id_limit):
        saurauuu_uidzz = input(' \x1b[1;97m• \x1b[1;91m>>\x1b[1;97m INPUT UID ' + str(SAURAVXX + 1) + ' : ')
        uid.append(saurauuu_uidzz)

    linex()
    wanna_limit = input(' \x1b[1;97m• \x1b[1;91m>>\x1b[1;97m WANNA LIMIT TO STOP (y/n): ').strip().lower()

    if wanna_limit == 'y':
        try:
            extract_limit = int(input(' \x1b[1;97m• \x1b[1;91m>>\x1b[1;97m SELECT LIMIT : '));linex()
        except ValueError:
            animation("\x1b[1;91m×--> SELECT CORRECTLY!!");linex()
            return menu()  
    else:
        extract_limit = 0  
    

    try:
        speed = int(input(' \x1b[1;97m• \x1b[1;91m>>\x1b[1;97m ENTER SPEED (1 TO 100) : '))
        if speed < 1 or speed > 100:
            raise ValueError
        speed = 101 - speed 
    except ValueError:
        animation("\x1b[1;91m×--> SELECT CORRECTLY!!")
        return menu()  
    
    total_extracted = 0  
    all_private = True  

    for userx in uid:
        head = {
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36'
        }
        params = {
            'access_token': token,
            'fields': 'friends'
        }
        
        try:
            url = requests.get(f'https://graph.facebook.com/{userx}', params=params, headers=head, cookies={'cookies': cok}).json()
            linex()

            if 'error' in url:
                error_message = url['error'].get('message', '')
                if 'Unsupported get request' in error_message or 'privacy' in error_message:
                    non_public_uids.append(userx)  
                    continue

            all_private = False

            for xxx in url.get('friends', {}).get('data', []):
                abc = xxx['id']
                if abc not in id:
                    id.append(abc)
        except KeyError:
            pass
        except IOError:
            pass
        except requests.exceptions.ConnectionError:
            exit()

    if all_private:
        animation(" \x1b[1;97m• \033[1;31m>> UID NOT PUBLIC ")
        return menu()  
    linex()
    print(' \x1b[1;97m• \x1b[1;91m>>\x1b[1;97m TOTAL IDS DUMPED TO FILE : \x1b[1;91m' + str(len(id)))
    print(' \x1b[1;97m• \x1b[1;91m>>\x1b[1;97m USE CTRL+Z TO STOP ')
    linex()
    for user_lado in id:
        mix_color = random.choice(color)

        if extract_limit > 0 and total_extracted >= extract_limit:  
            break  
        
        print(f' \x1b[1;97m• \x1b[1;91m>>\x1b[1;97m{mix_color} ID DUMPED SUCCESSFULLY : {user_lado}  ')
        
        try:
            urlx = requests.get(f'https://graph.facebook.com/{user_lado}', params=params, headers=head, cookies={'cookies': cok}).json()
            for xyx in urlx.get('friends', {}).get('data', []):
                saurav_xx = xyx['id'] + '|' + xyx['name']
                with open(file_name, 'a') as f:
                    f.write(saurav_xx + '\n')
                if saurav_xx not in idxx:
                    idxx.append(saurav_xx)  
                    total_extracted += 1  
                    print(f"   \x1b[1;91m>< \x1b[1;97mTOTAL EXTRACTED : [{total_extracted}]   ", end='\r')
                    
                    if extract_limit > 0 and total_extracted >= extract_limit:  
                        break  
        except KeyError:
            pass
        except IOError:
            pass
        except requests.exceptions.ConnectionError:
            exit()

        
        time.sleep(speed / 1000.0) 

    finish(idxx)

def finish(idxx):
    global file_name  
    linex()
    print(f' \x1b[1;97m• \x1b[1;91m>>\x1b[1;97m TOTAL FETCHED IDS   :\x1b[1;91m {len(idxx)}')
    print(f' \x1b[1;97m• \x1b[1;91m>>\x1b[1;97m DUMPED IDS SAVED IN : \x1b[1;91m{file_name}')
    linex()
    input(' \x1b[1;97m• \x1b[1;91m>>\x1b[1;97m PRESS ENTER TO GO BACK ')
    menu()

#------------------------------------[ NEW SERIES ONLY ]--------------------------------------#
import requests
import random
import time

file_name = ''

def dump_new():
    global file_name
    idxx = []  
    linex()
    
    
    try:
        token = open('.token.txt', 'r').read().strip()
        cok = open('.cok.txt', 'r').read().strip()
    except IOError:
        login()
    
    print(' \x1b[1;97m• \x1b[1;91m>>\x1b[1;97m ENTER FILE NAME WITHOUT "/SDCARD/"')
    linex()
    naame = input(' \x1b[1;97m• \x1b[1;91m>>\x1b[1;97m FILE NAME : ')
    linex()
    file_name = '/sdcard/' + naame

    try:
        id_limit = int(input(' \x1b[1;97m• \x1b[1;91m>>\x1b[1;97m INPUT UID LIMIT : '))
        linex()
    except ValueError:
        return menu()  
        
    if id_limit < 1 or id_limit > 100000000:
        return menu()  

    uid = []
    id = []
    color = [
        '\x1b[38;5;226m', '\x1b[38;5;46m', '\x1b[1;91m', 
        '\x1b[38;5;248m', '\x1b[38;5;44m', '\x1b[38;5;46m', 
        '\x1b[38;5;208m', '\x1b[38;5;46m', '\x1b[38;5;231m', 
        '\x1b[38;5;46m', '\x1b[1;91m'
    ]

    for SAURAVXX in range(id_limit):
        saurauuu_uidzz = input(' \x1b[1;97m• \x1b[1;91m>>\x1b[1;97m INPUT UID ' + str(SAURAVXX + 1) + ' : ')
        
        
        if saurauuu_uidzz.startswith(('6155', '6156')):
            uid.append(saurauuu_uidzz)

    linex()
    wanna_limit = input(' \x1b[1;97m• \x1b[1;91m>>\x1b[1;97m WANNA LIMIT TO STOP (y/n): ').strip().lower()

    if wanna_limit == 'y':
        try:
            extract_limit = int(input(' \x1b[1;97m• \x1b[1;91m>>\x1b[1;97m SELECT LIMIT : '))
            linex()
        except ValueError:
            return menu()  
    else:
        extract_limit = 0  
    
    
    try:
        speed = int(input(' \x1b[1;97m• \x1b[1;91m>>\x1b[1;97m ENTER SPEED (1 TO 100) : '))
        if speed < 1 or speed > 100:
            raise ValueError
        speed = 101 - speed  
    except ValueError:
        return menu()  
    
    total_extracted = 0  
    all_private = True  

    for userx in uid:
        head = {
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36'
        }
        params = {
            'access_token': token,
            'fields': 'friends'
        }
        
        try:
            
            url = requests.get(f'https://graph.facebook.com/{userx}', params=params, headers=head, cookies={'cookies': cok}).json()

            if 'error' in url:
                continue

            # Handle friends data
            all_private = False
            for xxx in url.get('friends', {}).get('data', []):
                abc = xxx['id']
                if abc not in id:
                    id.append(abc)
        except KeyError:
            continue
        except IOError:
            continue
        except requests.exceptions.ConnectionError:
            exit()


        time.sleep(speed / 1000.0)

    if all_private:
        return menu()  
    linex()
    print(' \x1b[1;97m• \x1b[1;91m>>\x1b[1;97m TOTAL IDS DUMPED TO FILE : \x1b[1;91m' + str(len(id)))
    print(' \x1b[1;97m• \x1b[1;91m>>\x1b[1;97m USE CTRL+Z TO STOP ')
    linex()
    
    for user_lado in id:
        if extract_limit > 0 and total_extracted >= extract_limit:  
            break  
        
        
        mix_color = random.choice(color)
        print(f' \x1b[1;97m• \x1b[1;91m>>\x1b[1;97m{mix_color} ID DUMPED SUCCESSFULLY : {user_lado}')  # Print dumped IDs
        
        try:
            urlx = requests.get(f'https://graph.facebook.com/{user_lado}', params=params, headers=head, cookies={'cookies': cok}).json()
            for xyx in urlx.get('friends', {}).get('data', []):
                saurav_xx = xyx['id'] + '|' + xyx['name']
      
                if saurav_xx.startswith(('6155', '6156')):
                    with open(file_name, 'a') as f:
                        f.write(saurav_xx + '\n')
                    if saurav_xx not in idxx:
                        idxx.append(saurav_xx)  
                        total_extracted += 1  
                        print(f"   \x1b[1;91m>< \x1b[1;97mTOTAL EXTRACTED : [{total_extracted}]   ", end='\r')
                        
                        if extract_limit > 0 and total_extracted >= extract_limit:  
                            break  
        except KeyError:
            continue
        except IOError:
            continue
        except requests.exceptions.ConnectionError:
            exit()

        
        time.sleep(speed / 1000.0)

    finish(idxx)

def finish(idxx):
    global file_name  
    linex()
    print(f' \x1b[1;97m• \x1b[1;91m>>\x1b[1;97m TOTAL FETCHED IDS   :\x1b[1;91m {len(idxx)}')
    print(f' \x1b[1;97m• \x1b[1;91m>>\x1b[1;97m DUMPED IDS SAVED IN : \x1b[1;91m{file_name}')
    linex()
    input(' \x1b[1;97m• \x1b[1;91m>>\x1b[1;97m PRESS ENTER TO GO')
    menu()
    

#---------------------------------[ FROM FACEBOOK FOLLOWERS ]--------------------------------#
import requests
import random
import time

file_name = ''

def dump_followers():
    global file_name
    idxx = []  
    linex()

    # Read token and cookies
    try:
        token = open('.token.txt', 'r').read().strip()
        cok = open('.cok.txt', 'r').read().strip()
    except IOError:
        login()

    print(' \x1b[1;97m• \x1b[1;91m>>\x1b[1;97m ENTER FILE NAME WITHOUT "/SDCARD/"')
    linex()
    naame = input(' \x1b[1;97m• \x1b[1;91m>>\x1b[1;97m FILE NAME : ')
    linex()
    file_name = '/sdcard/' + naame

    try:
        id_limit = int(input(' \x1b[1;97m• \x1b[1;91m>>\x1b[1;97m INPUT UID LIMIT : '))
        linex()
    except ValueError:
        animation("\x1b[1;91m×--> SELECT CORRECTLY!!")
        return menu()  

    if id_limit < 1 or id_limit > 100000000:
        animation("\x1b[1;91m×--> LIMIT OUT OF RANGE!!")
        return menu()  

    uid = []
    for SAURAVXX in range(id_limit):
        saurauuu_uidzz = input(' \x1b[1;97m• \x1b[1;91m>>\x1b[1;97m INPUT UID ' + str(SAURAVXX + 1) + ' : ')
        uid.append(saurauuu_uidzz)

    linex()
    wanna_limit = input(' \x1b[1;97m• \x1b[1;91m>>\x1b[1;97m WANNA LIMIT TO STOP (y/n): ').strip().lower()

    if wanna_limit == 'y':
        try:
            extract_limit = int(input(' \x1b[1;97m• \x1b[1;91m>>\x1b[1;97m SELECT LIMIT : '))
            linex()
        except ValueError:
            animation("\x1b[1;91m×--> SELECT CORRECTLY!!"); linex()
            return menu()  
    else:
        extract_limit = 0  
    
    try:
        speed = int(input(' \x1b[1;97m• \x1b[1;91m>>\x1b[1;97m ENTER SPEED (1 TO 100) : '))
        if speed < 1 or speed > 100:
            raise ValueError
        speed = 101 - speed  
    except ValueError:
        animation("\x1b[1;91m×--> SELECT CORRECTLY!!")
        return menu()  
    
    total_extracted = 0  
    all_private = True  

    for userx in uid:
        head = {
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36'
        }
        params = {
            'access_token': token,
            'fields': 'subscribers.limit(100)'  # Set limit for pagination
        }

        try:
            while True:
                response = requests.get(f'https://graph.facebook.com/{userx}/subscribers', params=params, headers=head).json()

                if 'data' in response:
                    for follower in response['data']:
                        follower_id = follower['id']
                        follower_name = follower.get('name', 'No Name')
                        if follower_name == 'No Name':  
                            continue  

                        id_entry = f'{follower_id}|{follower_name}'
                        with open(file_name, 'a') as file:
                            file.write(id_entry + '\n')

                        total_extracted += 1
                        if extract_limit > 0 and total_extracted >= extract_limit:  
                            break

                    if 'paging' in response and 'next' in response['paging']:
                        params = {'access_token': token}  
                        params.update(requests.get(response['paging']['next']).params)
                    else:
                        break
                else:
                    break

        except Exception as e:
            continue

        time.sleep(speed / 1000.0)  

    finish(total_extracted)

def finish(total_extracted):
    global file_name  
    linex()
    print(f' \x1b[1;97m• \x1b[1;91m>>\x1b[1;97m TOTAL FETCHED IDS   :\x1b[1;91m {total_extracted}')
    print(f' \x1b[1;97m• \x1b[1;91m>>\x1b[1;97m DUMPED IDS SAVED IN : \x1b[1;91m{file_name}')
    linex()
    input(' \x1b[1;97m• \x1b[1;91m>>\x1b[1;97m PRESS ENTER TO GO BACK')
    menu()

#-------------[ sprt.uids]--------------------#

def saprate():
    linex()
    try:
        limit = int(input(' \x1b[1;97m• \x1b[1;91m>>\x1b[1;97m HOW MANY LINKS DO U WANT TO SEPARATE : '))
    except ValueError:
        limit = 1
    linex()
    print(f""" \x1b[1;97m• \x1b[1;91m>>\x1b[1;97m PUT YOUR FILE FOR SEPARATION""")
    linex()
    print(' \x1b[1;97m• \x1b[1;91m>>\x1b[1;97m EXAMPLE : /sdcard/OLD.txt')
    linex()
    file_name = input(' \x1b[1;97m• \x1b[1;91m>>\x1b[1;97m FILE NAME : ')
    
    if not os.path.isfile(file_name):
        animation(' \x1b[1;91m×-->\x1b[1;97m FILE NOT FOUND !!')
        linex()
        input(' \x1b[1;97m• \x1b[1;91m>>\x1b[1;97m PRESS ENTER TO BACK ')
        menu()
    
    linex()
    print(f""" \x1b[1;97m• \x1b[1;91m>>\x1b[1;97m PUT YOUR NEW FILE NAME""")
    linex()
    print(' \x1b[1;97m• \x1b[1;91m>>\x1b[1;97m EXAMPLE : /sdcard/NEW.txt')
    linex()
    new_save = input(' \x1b[1;97m• \x1b[1;91m>>\x1b[1;97m NEW FILE NAME : ')
    linex()
    
    y = 0
    print(' \x1b[1;97m• \x1b[1;91m>>\x1b[1;97m EXAMPLE : 10001,10002,10003')
    linex()
    
    for k in range(limit):
        y += 1
        links = input(' \x1b[1;97m• \x1b[1;91m>>\x1b[1;97m PUT LINKS %s : ' % y)
        os.system(f'grep "{links}" {file_name} >> {new_save}')
    
    linex()
    print(' \x1b[1;97m• \x1b[1;91m>>\x1b[1;97m LINKS GRABBED SUCCESSFULLY')
    linex()
    print(' \x1b[1;97m• \x1b[1;91m>>\x1b[1;97m TOTAL GRABBED LINKS : ' +
          str(len(open(new_save).read().splitlines())))
    linex()
    print(' \x1b[1;97m• \x1b[1;91m>>\x1b[1;97m NEW FILE SAVE AS : \x1b[1;91m' + new_save)
    linex()
    input(' \x1b[1;97m• \x1b[1;91m>>\x1b[1;97m PRESS ENTER TO BACK ')
    menu()

#-------------[ DUB.IDZ ]------------------#    
def remove_dub():
    linex()
    print(f" \x1b[1;97m• \x1b[1;91m>>\x1b[1;97m DUBBLE LINKS CUTTER")
    linex()
    print(' \x1b[1;97m• \x1b[1;91m>>\x1b[1;97m EXAMPLE : /sdcard/rizzzy.txt')
    linex()
    file_path = input(' \x1b[1;97m• \x1b[1;91m>>\x1b[1;97m FILE NAME : ')

    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
        
        with open(file_path, "w") as file:
            file.writelines(set(lines))
        
        linex()
        print(" \x1b[1;97m• \x1b[1;91m>>\x1b[1;97m SUCCESSFULLY REMOVED DUBBLE UIDS ")
        linex()
        print(" \x1b[1;97m• \x1b[1;91m>>\x1b[1;97m YOUR TOTAL IDZ :\x1b[1;91m " + str(len(open(file_path).read().splitlines())))
    
    except FileNotFoundError:
        animation(" \x1b[1;91m×-->\x1b[1;97m FILE NOT FOUND! ")
    
    except Exception as e:
        print(f" \x1b[1;91m×-->\x1b[1;97m AN ERROR OCCURRED: {e}")
    
    linex()
    input(' \x1b[1;97m• \x1b[1;91m>>\x1b[1;97m PRESS ENTER TO BACK ')
    menu()

#-----------------------[ SYSTEM ]--------------------#
# try:
    # os.mkdir('/sdcard/rohiteyyy')
# except FileExistsError:
    # pass
# try:
    # os.mkdir('data')
# except FileExistsError:
    # pass
menu()
