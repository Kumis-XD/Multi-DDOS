#import_module
import os,sys,time,requests,json,random,string

#warna
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
pms = random.choice([m,k,h,b,u,hh,kk,p,x,Z])

#auto_module
try:
   import requests
except ImportError:
   os.system('pip install requests')
   time.sleep(1)
   try:
      import rich
   except ImportError:
      exit('Tidak Dapat Menginstall Module requests, Coba Install Manual (pkg install requests)')
try:
   import nmap
except ImportError:
   os.system('pkg install nmap')
   time.sleep(1)

#system_clear
def hps():
       os.system("clear")

#anim_menulis
def Kumis_XD(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.15)

#banner
def banner():
    print(f"""{asu}
\t░█████╗░████████╗░█████╗░░█████╗░██╗░░██╗
\t██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗██║░██╔╝
\t███████║░░░██║░░░███████║██║░░╚═╝█████═╝░
\t██╔══██║░░░██║░░░██╔══██║██║░░██╗██╔═██╗░
\t██║░░██║░░░██║░░░██║░░██║╚█████╔╝██║░╚██╗
\t╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝
                     {m}•{k}•{H}•{sir}Creeated By Kumis-XD{N}{H}•{k}•{m}•{N}""")
    print("")
    try:sh = requests.get('https://httpbin.org/ip').json()
    except:sh = {'origin':'-'}
    token=string.ascii_letters + string.digits
    v=[]
    for i in range(25):
        v.append(random.choice(token))
    print(f"\tYour IP : {K}"+(sh['origin']))
    print(f"\t{N}Your Token : {H}"+''.join(v),f"{N}[{m}Random{N}]")
    print(f"\t")
#try:
#    r=requests.get("https://httpbin.org")
#except requests.exceptions.ConnectionError:
#    time.sleep(3)
#    exit(f"{m}Periksa Jaringan Anda !!!")

#menu_chose
def menu():
      hps()
      banner()
      print(f"\t>>MENU<<\n01. Lacak IP        [{H}on{N}]\n02. DDOS ATTACK     [{H}on{N}]\n03. Open NMAP       [{H}on{N}]\n04. Report          [{H}on{N}]\n05. Help            [{H}on{N}]\n00. Exit")
      print("")
      ul = input(f"Pilih : {pms}")
      if(ul == '1'):
         try:
             r=requests.get("https://httpbin.org")
         except requests.exceptions.ConnectionError:
             time.sleep(3)
             print(f"{m}Periksa Jaringan Anda !!!")
             main()
         else:
             hps()
             banner()
             print("\t>>TRACKER<<")
             usr=input("Masukan IP target (track) : ")
             r =requests.get("http://ip-api.com/json/?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting"+usr)
             j=json.loads(r.text)
             for i in j:
                 print(f"\033[1;33;40m {i} : \033[0m \033[32;40m{j[i]}\033[0m")
      elif(ul == '2'):
         try:
            r=requests.get("https://httpbin.org")
         except requests.exceptions.ConnectionError:
            print(f"{m}Periksa Jaringan Anda !!!")
            main()
         else:
            hps()
            banner()
            print("\t>>DDOS<<")
            ip = input("Masukan IP target : ")
            port = input("Masukan PORT target : ")
            jlh = int(input("Paket yg akan dikirim : "))
            time.sleep(1)
            print("")
            print(f"\tMemulai DDOS ATTACK")
            for i in range(jlh):
                  print("")
                  print(f"Paket terkirim ke {ip} port {port}")
                  time.sleep(0.10)
            else:
                  exit()
      elif(ul == '3'):
         try:
            r=requests.get("https://httpbin.org")
         except requests.exceptions.ConnectionError:
            time.sleep(3)
            print(f"{m}Periksa Jaringan Anda !!!")
            main()
         else:
            hps()
            banner()
            print("\t>>NMAP<<")
            user=input("Masukan IP target (NMAP) : ")
            print("")
            os.system("nmap "+user)
            exit()
      elif(ul == '5'):
            hps()
            banner()
            Kumis_XD("--Tracker IP atau bisa disebut dengan lacak via IP\n--DDOS ATTACK atau bisa desebut dengan meretas melalui IP\n--NMAP bisa disebut dengan mengetahui DNS/UDP website\nmelalui IP website")
            time.sleep(1)
            exit()
      elif(ul == '4'):
            print("Anda akan di arahkan ke WhatsApp")
            time.sleep(1)
            os.system("xdg-open https://wa.me/6287734390834")
            time.sleep(2)
            menu()
      elif(ul == '00'):
            time.sleep(1)
            exit()
      else:
            print(f"{m}Wrong input!pleease input again")
            time.sleep(1)
            main()

if __name__=='__main__':
         menu()
