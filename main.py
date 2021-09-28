import os 
import sys 
import time 
import pandas 
from scapy.all import * 
from threading import Thread 
import subprocess
import colorama
from colorama import Fore, Back, Style
from prettytable import PrettyTable

#colors

#\033[30m      # black
#\033[31m      # red
#\033[32m      # green
#\033[33m      # yellow
#\033[34m      # blue
#\033[35m      # magenta
#\033[36m      # cyan
#\033[37m      # white
#\033[39m      # reset

networks = pandas.DataFrame(columns=["BSSID", "SSID", "DBM", "CH", "CRYPTO"])
networks.set_index("BSSID", inplace=True)


def CS(X):
    time.sleep(X)
    os.system("clear")

def prompt_sudo():
    ret = 0
    if os.geteuid() != 0:
        msg = "\033[35m[\033[36m+\033[35m] PASSWORD IS NEEDED FOR USER %u >> "
        ret = subprocess.check_call("sudo -v -p '%s'" % msg, shell=True)
    return ret

if prompt_sudo() != 0:
    print("hi")

def banner_net():
        print(Fore.RED+"""
 _  _  _  _____   _____  _______ _______  ______
 |  |  | |     | |     | |______ |______ |_____/
 |__|__| |_____| |_____| |       |______ |    \_
                                                
    Wifi-Hacking and Discovery
                            V 2.0
                                 Scare_Sec_Hackers
 ──────────────────────────────────────────────
     |\_/|                  
     | @ @   Woof! 
     |   <>              _  
     |  _/\------____ ((| |))
     |               `--' |   
 ____|_       ___|   |___.' 
/_/_____/____/_______|
 """)

def scan_networks():
    #dBm_Signal"
    networks = pandas.DataFrame(columns=["BSSID", "SSID", "dBm_Signal", "Channel", "Crypto"])
    networks.set_index("BSSID", inplace=True)

    def callback(packet):
        if packet.haslayer(Dot11Beacon):
            bssid = packet[Dot11].addr2
            ssid = packet[Dot11Elt].info.decode()
            try:
                dbm_signal = packet.dBm_AntSignal
            except:
                dbm_signal = "N/A"
            stats = packet[Dot11Beacon].network_stats()
            channel = stats.get("channel")
            crypto = stats.get("crypto")
            networks.loc[bssid] = (ssid, dbm_signal, channel, crypto)


    def print_all():
        while True:
            os.system("clear")
            banner_net()
            import datetime 
            from datetime import datetime
            import time as t 
            a = str(datetime.now())
            print("\033[35m[\033[36mTime Elapsed > \033[35m]" + a)
            mac = networks
            Mac_table = PrettyTable(["Networks Within Length of Interface"])
            Mac_table.add_row([mac])
            print(Mac_table)
            #print(networks)
            t.sleep(0.5)

    def change_channel():
        ch = 1
        while True:
            os.system(f"iwconfig {interface} channel {ch}")
            ch = ch % 14 + 1
            time.sleep(0.5)


    if __name__ == "__main__":
        banner_net()
        os.system("clear")
        interface = str(input("\033[35m[\033[36m!\033[35m] Interface >>> "))
        print("\033[35m[\033[36m+\033[35m] Starting interface....")
        time.sleep(0.1)
        os.system(f"sudo airmon-ng start {interface}")
        print("\033[35m[\033[36m?\033[35m] Interface Started? ")
        time.sleep(4)
        print("\033[35m[\033[36m+\033[35m] Scanning Networks....")
        time.sleep(3)
        print("\033[35m[\033[36m+\033[35m] CTRL+C When your Done")
        time.sleep(2)
        printer = Thread(target=print_all)
        printer.daemon = True
        printer.start()
        channel_changer = Thread(target=change_channel)
        channel_changer.daemon = True
        channel_changer.start()
        sniff(prn=callback, iface=interface)



#     |\_/|                  
#     | @ @   Woof! 
#     |   <>              _  
#     |  _/\------____ ((| |))
#     |               `--' |   
# ____|_       ___|   |___.' 
#/_/_____/____/_______|

def banner():
    CS(2)
    os.system("clear")
    print(Fore.RED+"""
 _  _  _  _____   _____  _______ _______  ______
 |  |  | |     | |     | |______ |______ |_____/
 |__|__| |_____| |_____| |       |______ |    \_
                                                
    Wifi-Hacking and Discovery
                            V 2.0
                                 Scare_Sec_Hackers
 ──────────────────────────────────────────────
 [1] Scan Networks 
 [2] Deauthenticate Networks 
 [3] Spawn Fake Access Points 
 [4] Spawn Heavy DHCMP Attack
 [5] The All In One ## this is not an option as its under construction 
    """)
    op = str(input(" \033[35m[\033[36mOptions\033[35m] >>> "))

    if op == '1':
        print("\033[35m[\033[36m+\033[35m] Running Module.... ")
        scan_networks()
        banner()
    elif op == '2':
        os.system("sudo ruby deauth.rb")
        banner()
    elif op == '3':
        os.system("sudo ruby fake.rb")
        banner()
    elif op == '4':
        os.system("sudo dhcmp.py")
        banner()
    elif op == '5':
        scan_networks()
        os.system("sudo ruby deauth.rb")
    else:
        print("\033[35m[\033[36m+\033[35m] Not A Command Dumb Dumb..")
        banner()

if __name__ == "__main__":
    banner()
