#!/bin/bash

echo -e "\e[1;36m[*] Setting up environment...\e[0m"

# ၁။ ဖုန်း Storage ခွင့်ပြုချက်တောင်းခြင်း
termux-setup-storage
sleep 2

# ၂။ Python Update နှင့် Install လုပ်ခြင်း
echo -e "\e[1;36m[*] Installing Python...\e[0m"
pkg update -y
pkg install python -y

# ၃။ GitHub မှ Wifi.py ကို အလိုအလျောက် ဒေါင်းလုဒ်ဆွဲခြင်း
echo -e "\e[1;36m[*] Downloading script from GitHub...\e[0m"
curl -sL https://raw.githubusercontent.com/wwwcreater/Crack-wifi/main/Wifi.py -o Wifi.py

echo -e "\e[1;32m[+] Setup completed! Starting program...\e[0m"
sleep 1
clear

# ၄။ Python Script ကို တန်းစတင်ခြင်း
python Wifi.py
