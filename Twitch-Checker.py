try:import random,re;from colorama import Fore;from requests import post,get
except ModuleNotFoundError:exit('[!] Download The Missing Module !')
def saver(user):
    ID=''#Telegram id
    token=''#Telegram bot token
    try:post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=• New username’s Claimed @{user} 🦦\n\nBy\t@TweakPY\t-\t@vv1ck')
    except:pass
    with open('Available.txt', 'a') as x:
        x.write(user+'\n')
def with_list():
	error,count,done=0,0,0
	try:file=open('user.txt', 'r')
	except FileNotFoundError:exit('[!] No users File Detected - Note users file must be in user.txt File ..')
	while True:
		user=file.readline().split('\n')[0]
		ru=post(f"https://gql.twitch.tv/gql",headers={'Host': 'gql.twitch.tv','User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0','Accept': '*/*','Accept-Language': 'en-US','Accept-Encoding': 'gzip, deflate','Referer': 'https://www.twitch.tv/','Client-Id': '85lcqzxpb9bqu9z6ga1ol55du','Content-Type': 'text/plain;charset=UTF-8','Origin': 'https://www.twitch.tv','Content-Length': '199','Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-site','Te': 'trailers','Connection': 'close'},data='[{"operationName":"UsernameValidator_User","variables":{"username":"'+user+'"},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"fd1085cf8350e309b725cf8ca91cd90cac03909a3edeeedbd0872ac912f3d660"}}}]').text#@if09l
		if '"isUsernameAvailable":true' in ru:
			print(f'\r[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN} Available <{done}>{Fore.RESET} | {Fore.RED} Not Available <{error}>{Fore.RESET} | {Fore.LIGHTYELLOW_EX} count <{count}> {Fore.RESET}  ',end='')
			done+=1
			count+=1
			saver(user)
		elif '"isUsernameAvailable":false' in ru:
			print(f'\r[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN} Available <{done}>{Fore.RESET} | {Fore.RED} Not Available <{error}>{Fore.RESET} | {Fore.LIGHTYELLOW_EX} count <{count}> {Fore.RESET}  ',end='')
			error+=1
			count+=1
		else:
			print(f'\r[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN} Available <{done}>{Fore.RESET} | {Fore.RED} Not Available <{error}>{Fore.RESET} | {Fore.LIGHTYELLOW_EX} count <{count}> {Fore.RESET}  ',end='')
			error+=1
			count+=1
def without_list():
	count,done,error=0,0,0
	user=""
	lena=input('[?] Length: ');length=(int(lena))
	chars="qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnm12345678901234567890"
	while True:
		for user in range(1):
			user=""
			for item in range(length):
				user+=random.choice(chars)
		ru=post(f"https://gql.twitch.tv/gql",headers={'Host': 'gql.twitch.tv','User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0','Accept': '*/*','Accept-Language': 'en-US','Accept-Encoding': 'gzip, deflate','Referer': 'https://www.twitch.tv/','Client-Id': '85lcqzxpb9bqu9z6ga1ol55du','Content-Type': 'text/plain;charset=UTF-8','Origin': 'https://www.twitch.tv','Content-Length': '199','Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-site','Te': 'trailers','Connection': 'close'},data='[{"operationName":"UsernameValidator_User","variables":{"username":"'+user+'"},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"fd1085cf8350e309b725cf8ca91cd90cac03909a3edeeedbd0872ac912f3d660"}}}]').text
		if '"isUsernameAvailable":true' in ru:
			print(f'\r[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN} Available <{done}>{Fore.RESET} | {Fore.RED} Not Available <{error}>{Fore.RESET} | {Fore.LIGHTYELLOW_EX} count <{count}> {Fore.RESET}  ',end='')
			done+=1
			count+=1
			saver(user)
		elif '"isUsernameAvailable":false' in ru:
			print(f'\r[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN} Available <{done}>{Fore.RESET} | {Fore.RED} Not Available <{error}>{Fore.RESET} | {Fore.LIGHTYELLOW_EX} count <{count}> {Fore.RESET}  ',end='')
			error+=1
			count+=1
		else:
			print(f'\r[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN} Available <{done}>{Fore.RESET} | {Fore.RED} Not Available <{error}>{Fore.RESET} | {Fore.LIGHTYELLOW_EX} count <{count}> {Fore.RESET}  ',end='')
			error+=1
			count+=1
print("""
████████╗██╗    ██╗       ██████╗██╗  ██╗
╚══██╔══╝██║    ██║      ██╔════╝██║  ██║
   ██║   ██║ █╗ ██║█████╗██║     ███████║
   ██║   ██║███╗██║╚════╝██║     ██╔══██║
   ██║   ╚███╔███╔╝      ╚██████╗██║  ██║
   ╚═╝    ╚══╝╚══╝        ╚═════╝╚═╝  ╚═╝
                            
        By @TweakPY - @vv1ck                          
""")
LW=int(input("[1] without List\n[2] with List\n---------------\nEnter > : "))
if LW==1:without_list()
elif LW==2:with_list()
else:exit('\n[!] Exit... \n\nBy @TweakPY - @vv1ck')
