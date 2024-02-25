import urllib.request
import json
import datetime
import random
import string
import time
import os
import sys
os.system('cls' if os.name == 'nt' else 'clear')
print(''' __     __     ______     ______     ______                                                      
      	 /\ \  _ \ \   /\  __ \   /\  == \   /\  == \                                                     
	 \ \ \/ ".\ \  \ \  __ \  \ \  __<   \ \  _-/                                                     
 	  \ \__/".~\_\  \ \_\ \_\  \ \_\ \_\  \ \_\                                                       
 	   \/_/   \/_/   \/_/\/_/   \/_/ /_/   \/_/ ''')
print('''/\ \/\ \   /\ "-.\ \   /\ \       /\ \   /\ "-./  \   /\ \   /\__  _\ /\  ___\   /\  __-.        
	 \ \ \_\ \  \ \ \-.  \  \ \ \____  \ \ \  \ \ \-./\ \  \ \ \  \/_/\ \/ \ \  __\   \ \ \/\ \       
 	  \ \_____\  \ \_\\"\_\  \ \_____\  \ \_\  \ \_\ \ \_\  \ \_\    \ \_\  \ \_____\  \ \____-       
  	   \/_____/   \/_/ \/_/   \/_____/   \/_/   \/_/  \/_/   \/_/     \/_/   \/_____/   \/____/''')
print(''' ______     ______     __   __     ______     ______     ______     ______   ______     ______   
	 /\  ___\   /\  ___\   /\ "-.\ \   /\  ___\   /\  == \   /\  __ \   /\__  _\ /\  __ \   /\  == \  
	 \ \ \__ \  \ \  __\   \ \ \-.  \  \ \  __\   \ \  __<   \ \  __ \  \/_/\ \/ \ \ \/\ \  \ \  __<  
 	  \ \_____\  \ \_____\  \ \_\\"\_\  \ \_____\  \ \_\ \_\  \ \_\ \_\    \ \_\  \ \_____\  \ \_\ \_\
 	   \/_____/   \/_____/   \/_/ \/_/   \/_____/   \/_/ /_/   \/_/\/_/     \/_/   \/_____/   \/_/ /_/''')
    
referrer = input("Your WARP+ Public ID:")
def genString(stringLength):
	try:
		letters = string.ascii_letters + string.digits
		return ''.join(random.choice(letters) for i in range(stringLength))
	except Exception as error:
		print(error)		    
def digitString(stringLength):
	try:
		digit = string.digits
		return ''.join((random.choice(digit) for i in range(stringLength)))    
	except Exception as error:
		print(error)	
url = f'https://api.cloudflareclient.com/v0a{digitString(3)}/reg'
def run():
	try:
		install_id = genString(22)
		body = {"key": "{}=".format(genString(43)),
				"install_id": install_id,
				"fcm_token": "{}:APA91b{}".format(install_id, genString(134)),
				"referrer": referrer,
				"warp_enabled": False,
				"tos": datetime.datetime.now().isoformat()[:-3] + "+07:00",
				"type": "Android",
				"locale": "vi_VN"}
		data = json.dumps(body).encode('utf8')
		headers = {'Content-Type': 'application/json; charset=UTF-8',
					'Host': 'api.cloudflareclient.com',
					'Connection': 'Keep-Alive',
					'Accept-Encoding': 'gzip',
					'User-Agent': 'okhttp/4.9.0'
					}
		req         = urllib.request.Request(url, data, headers)
		response    = urllib.request.urlopen(req)
		status_code = response.getcode()	
		return status_code
	except Exception as error:
		print(error)	

g = 0
b = 0
while True:
	result = run()
	if result == 200:
		g = g + 1
		os.system('cls' if os.name == 'nt' else 'clear')
		animation = ["[-][■□□□□□□□□□] 10%","[\][■■□□□□□□□□] 20%", "[|][■■■□□□□□□□] 30%", "[/][■■■■□□□□□□] 40%", "[-][■■■■■□□□□□] 50%", "[\][■■■■■■□□□□] 60%", "[|][■■■■■■■□□□] 70%", "[/][■■■■■■■■□□] 80%", "[-][■■■■■■■■■□] 90%", "[✓][■■■■■■■■■■] 100%"] 
		for i in range(len(animation)):
			time.sleep(0.5)
			sys.stdout.write("\r Adding traffic... " + animation[i % len(animation)])
			sys.stdout.flush()
		print(f"\n Added traffic to ID: {referrer}")    
		print(f"≈ {g} GB has been added to your account.")
		print(f"Tổng: {g} Success {b} Failed")
		print("[-]The process will start again in 20 seconds...", end="\r")
		time.sleep(1)
		print("[\]The process will start again in 19 seconds...", end="\r")
		time.sleep(1)
		print("[|]The process will start again in 18 seconds...", end="\r")
		time.sleep(1)
		print("[/]The process will start again in 17 seconds...", end="\r")
		time.sleep(1)
		print("[-]The process will start again in 16 seconds...", end="\r")
		time.sleep(1)
		print("[\]The process will start again in 15 seconds...", end="\r")
		time.sleep(1)
		print("[|]The process will start again in 14 seconds...", end="\r")
		time.sleep(1)
		print("[/]The process will start again in 13 seconds...", end="\r")
		time.sleep(1)
		print("[-]The process will start again in 12 seconds...", end="\r")
		time.sleep(1)
		print("[\]The process will start again in 11 seconds...", end="\r")
		time.sleep(1)
		print("[|]The process will start again in 10 seconds...", end="\r")
		time.sleep(1)
		print("[/]The process will start again in 9 seconds...", end="\r")
		time.sleep(1)
		print("[-]The process will start again in 8 seconds...", end="\r")
		time.sleep(1)
		print("[\]The process will start again in 7 seconds...", end="\r")
		time.sleep(1)
		print("[|]The process will start again in 6 seconds...", end="\r")
		time.sleep(1)
		print("[/]The process will start again in 5 seconds...", end="\r")
		time.sleep(1)
		print("[-]The process will start again in 4 seconds...", end="\r")
		time.sleep(1)
		print("[\]The process will start again in 3 seconds...", end="\r")
		time.sleep(1)
		print("[|]The process will start again in 2 seconds...", end="\r")
		time.sleep(1)
		print("[/]The process will start again in 1 second...", end="\r")
		time.sleep(1)
		print("[-]The process will start again in 0 second...", end="\r")
		print("[✓]Starting the process again...", end="\r")
	else:
		b = b + 1
		os.system('cls' if os.name == 'nt' else 'clear')
		print("An error occurred while connecting to CloudFlare's servers")
		print(f"[#] Total: {g} Success {b} Failed")	
