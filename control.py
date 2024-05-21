import os
import sys 
import time
from time import sleep
from colorama import Fore, Style, init
from termcolor import colored
os.system("clear")

init()
R = f"{Fore.RED}{Style.BRIGHT}"
G = f"{Fore.GREEN}{Style.BRIGHT}"
B = f"{Fore.BLUE}{Style.BRIGHT}"
Y = f"{Fore.YELLOW}{Style.BRIGHT}"
C = f"{Fore.CYAN}{Style.BRIGHT}"
M = f"{Fore.MAGENTA}{Style.BRIGHT}"
W = f"{Fore.WHITE}{Style.BRIGHT}"
D = f"{Fore.BLACK}{Style.BRIGHT}"
ERROR = f"{Y}[{R}!{Y}]{R}"

if os.geteuid() != 0:
    red_sudo = "\033[1;31m" + "sudo" + "\033[0m"
    print(f"{ERROR} {Style.RESET_ALL}please use {Y}root{Style.RESET_ALL} Type a command {red_sudo}")
    sys.exit(1)

print(f'''
                                      {B}.{W}
                                     {B}/ \\{W}
  ____               _               {B}| |{W} 
 / ___|  ___   _ __ | |_ _ __   ___  {B}| |{W}
| |     / {Y}_{W} \ | '_ \| __| '__| / {R}_{W} \ {B}|.|{W}
| |___ | {Y}(0){W} || | | | |_| |   | {R}(0){W} |{B}|.|{W}
 \____| \_{Y}^{W}_/ |_| |_|\__|_|    \_{R}^{W}_/ {B}|:|{W}
                                     {B}|:|{W}
                                  {W}~{Y}\==8==/{W}~
                                      {R}8{W}
                                      {R}0{W}
''')
print(f'''
{R}+------------------------------------------------------------------+
{R}|{G} GitHub{W} : {B}MohmmadALbaqer {W}|{Y} https://www.github.com/MohmmadALbaqer/ {R}|
{R}|{G} Instagram{W} :{B} r94xs {W}      |{Y} https://www.instagram.com/r94xs/       {R}|
{R}+------------------------------------------------------------------+{W}''')

def stop_network_manager():
    os.system("sudo ifconfig wlan0 down")
    os.system("sudo airmon-ng start wlan0")
    os.system("sudo airmon-ng check kill")
    os.system("sudo systemctl stop NetworkManager")
    os.system("clear")
    print(f"{W}[{G}INFO{W}] {B}Activation wlan0 down {G}ON{W}")
    time.sleep(0.25)
    print(f"{W}[{G}INFO{W}] {B}Activation airmon-ng wlan0 {M}START{W}")
    time.sleep(0.50)
    print(f"{W}[{G}INFO{W}] {B}Activation airmon-ng check kill {G}ON{W}")
    time.sleep(0.75)
    print(f"{W}[{G}INFO{W}] {B}Activation NetworkManager {R}STOP{W}")
    time.sleep(1)
    os.system("clear")
    print(f'''
                                      {B}.{W}
                                     {B}/ \\{W}
  ____               _               {B}| |{W} 
 / ___|  ___   _ __ | |_ _ __   ___  {B}| |{W}
| |     / {Y}_{W} \ | '_ \| __| '__| / {R}_{W} \ {B}|.|{W}
| |___ | {Y}(0){W} || | | | |_| |   | {R}(0){W} |{B}|.|{W}
 \____| \_{Y}^{W}_/ |_| |_|\__|_|    \_{R}^{W}_/ {B}|:|{W}
                                     {B}|:|{W}
                                  {W}~{Y}\==8==/{W}~
                                      {R}8{W}
                                      {R}0{W}

+----+---------------------------------+-------+
| {Y}ID{W} | {G}INFORMATION{W}                     | {M}MOD{W}   |
+----+---------------------------------+-------+
| {Y}1{W}  | {G}Activation wlan0 down{W}           | {B}ON{W}    |
| {Y}2{W}  | {G}Activation airmon-ng wlan0{W}      | {G}START{W} |
| {Y}3{W}  | {G}Activation airmon-ng check kill{W} | {B}ON{W}    |
| {Y}4{W}  | {G}Activation NetworkManager{W}       | {R}STOP{W}  |
+----+---------------------------------+-------+ 
''')    



def start_network_manager():
    os.system("sudo systemctl start NetworkManager")
    time.sleep(0.25)
    print(f"{W}[{G}INFO]{W} {B}start network manager {R}OFF{W}")
    time.sleep(1)
    print(f"{W}[{G}INFO]{W} {B}Activation NetworkManager {G}START{W}")
    time.sleep(1)
    os.system("clear")
    print(f'''
                                      {B}.{W}
                                     {B}/ \\{W}
  ____               _               {B}| |{W} 
 / ___|  ___   _ __ | |_ _ __   ___  {B}| |{W}
| |     / {Y}_{W} \ | '_ \| __| '__| / {R}_{W} \ {B}|.|{W}
| |___ | {Y}(0){W} || | | | |_| |   | {R}(0){W} |{B}|.|{W}
 \____| \_{Y}^{W}_/ |_| |_|\__|_|    \_{R}^{W}_/ {B}|:|{W}
                                     {B}|:|{W}
                                  {W}~{Y}\==8==/{W}~
                                      {R}8{W}
                                      {R}0{W}

+----+---------------------------------+-------+
| {Y}ID{W} | {G}INFORMATION{W}                     | {M}MOD{W}   |
+----+---------------------------------+-------+
| {Y}1{W}  | {G}Activation airmon-ng check kill{W} | {R}OFF{W}   |
| {Y}2{W}  | {G}Activation NetworkManager{W}       | {G}START{W} |
+----+---------------------------------+-------+ 
''')

def main():
    print(f"{W}[{G}*{W}] {B}use option:{W}")
    print(f"{W}[{G}1{W}] {Y}Stop Network Manager{W}")
    print(f"{W}[{G}2{W}] {Y}Start Network Manager{W}")

    choice = input(f"{W}[{G}+{W}] {B}Enter your choice (1 or 2): {Y}")
    print(1*f"{W}\n")
    if choice == "1":
        stop_network_manager()
    elif choice == "2":
        start_network_manager()
    else:
        print(f"{Y}[{R}!{Y}] {R}Invalid choice. Please enter 1 or 2.{W}")

if __name__ == "__main__":
    main()
