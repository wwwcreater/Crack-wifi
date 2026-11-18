#!/bin/bash

echo -e "\e[1;36m[*] Setting up environment...\e[0m"

# ၁။ ဖုန်း Storage ခွင့်ပြုချက်တောင်းခြင်း
termux-setup-storage
sleep 2

# ၂။ Python Install လုပ်ခြင်း
pkg update -y
pkg install python -y

# ၃။ GitHub မှ Wifi.py ကို ဆွဲချခြင်း
curl -sL https://raw.githubusercontent.com/wwwcreater/Crack-wifi/main/Wifi.py -o Wifi.py

echo -e "\e[1;32m[+] Setup completed! Starting program...\e[0m"
sleep 1
clear

# ၄။ Termux အသစ်တစ်ခုအနေနဲ့ တိုက်ရိုက် run ပေးမည့် ပုံစံ
python Wifi.py
