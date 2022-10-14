#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r'''
WEB-TOOL/src
~~~~~~~~~~~~~~
Coded By https://github.com/msfpt
'''

from src import *
import requests
import socket
import time
import os

try:
    from colorama import Fore, Style
except ImportError as err:
    os.system("pip install colorama")
    from colorama import Fore, Style


def setTitle(title: str):
  print(f'\33]0;{title}\a', end='', flush=True) if (os.name == 'posix') else os.system(f'title {title}')

setTitle("WEB-TOOL")


def clear(msg: str = None) -> 0:
  os.system(['clear', 'cls'][os.name == 'nt'])
  if(msg != None):
    print(msg)

clear()


def banner():

    clear()
    print(f""" {Fore.CYAN}
     _       ____________     __________  ____  __
    | |     / / ____/ __ )   /_  __/ __ \/ __ \/ /
    | | /| / / __/ / __  |    / / / / / / / / / /
    | |/ |/ / /___/ /_/ /    / / / /_/ / /_/ / /___
    |__/|__/_____/_____/    /_/  \____/\____/_____/
    
       {Fore.RESET}
            {Fore.CYAN}[{Fore.LIGHTCYAN_EX}1{Fore.CYAN}]{Fore.LIGHTGREEN_EX} Ping Tool
            {Fore.CYAN}[{Fore.LIGHTCYAN_EX}2{Fore.CYAN}]{Fore.LIGHTGREEN_EX} Server whois
            {Fore.CYAN}[{Fore.LIGHTCYAN_EX}3{Fore.CYAN}]{Fore.LIGHTGREEN_EX} Admin page finder (9073 Page)
            {Fore.CYAN}[{Fore.LIGHTCYAN_EX}4{Fore.CYAN}]{Fore.LIGHTGREEN_EX} Wordpress Usernames
            {Fore.CYAN}[{Fore.LIGHTCYAN_EX}5{Fore.CYAN}]{Fore.LIGHTGREEN_EX} Host to IP
            {Fore.CYAN}[{Fore.LIGHTCYAN_EX}6{Fore.CYAN}]{Fore.LIGHTGREEN_EX} IP Information
            {Fore.CYAN}[{Fore.LIGHTCYAN_EX}7{Fore.CYAN}]{Fore.LIGHTGREEN_EX} Subdomain finder (8210 Subdomain)
            {Fore.CYAN}[{Fore.LIGHTCYAN_EX}8{Fore.CYAN}]{Fore.LIGHTGREEN_EX} Port Scanner
            {Fore.CYAN}[{Fore.LIGHTCYAN_EX}9{Fore.CYAN}]{Fore.LIGHTGREEN_EX} Cloudflare bypasser

            {Fore.CYAN}[{Fore.LIGHTCYAN_EX}0{Fore.CYAN}]{Fore.LIGHTGREEN_EX} EXIT

{Fore.RESET}""")

    choose = input(f"{Style.RESET_ALL} {Fore.LIGHTBLUE_EX}{os.getlogin()}@WEB-TOOL:{Fore.WHITE} ")

    if choose == '1':
        clear()
        ping.ping()
        input(f"{Fore.LIGHTBLUE_EX} [#] Press Enter for back to menu")
        banner()

    elif choose == '2':
        clear()
        whois.whois()
        input(f"{Fore.LIGHTBLUE_EX} [#] Press Enter for back to menu")
        banner()

    elif choose == '3':
        clear()

        try:
            website = input(f"{Fore.WHITE} [ {Fore.RED}+{Fore.WHITE} ] Enter your target:: ")
            if not website.startswith("http://") or not website.startswith("https://"):
                website = "http://" + website

            ## url file (You can change it)
            urlfile = open("Web-Tool/src/files/login.txt")
            print("")

            ## find admin page
            for url in urlfile:
                url = url.strip("\n")
                full_address = website + "/" + url
                response = requests.post(full_address)
                if response.status_code == 200:
                    print("{} [200] {} ==> FOUND".format(Fore.GREEN, full_address))
                else:
                    print("{} [404] {} ==> NOT FOUND".format(Fore.RED, full_address))
        except:
            print(f"{Fore.RED}  [!] Please check your Internet connection or Domain")

        input(f"{Fore.LIGHTBLUE_EX} [#] Press Enter for back to menu")
        banner()

    elif choose == '4':
        clear()
        wordpress.usernames()
        print()
        input(f"{Fore.LIGHTBLUE_EX} [#] Press Enter for back to menu")
        banner()

    elif choose == '5':
        clear()
        host_ip.find()
        input(f"{Fore.LIGHTBLUE_EX} [#] Press Enter for back to menu")
        banner()

    elif choose == '6':
        clear()
        ip_info.info()
        print()
        input(f"{Fore.LIGHTBLUE_EX} [#] Press Enter for back to menu")
        banner()

    elif choose == '7':
        clear()

        target = input(f"{Fore.WHITE} [ {Fore.RED}+{Fore.WHITE} ] Enter yout target:: ")
        file = open("Web-Tool/src/files/subdomain.txt")
        content = file.read()
        subs = content.splitlines()

        for subdomain in subs:
            url = f"http://{subdomain}.{target}"
            ip_url = f"{subdomain}.{target}"

            try:
                requests.get(url)
            except requests.ConnectionError:
                print(f"\n{Fore.RED}  [!] NetWork Connection Error")

            else:
                print(f"{Fore.GREEN} [ DISCOVERED ] {url} -> {socket.gethostbyname(ip_url)}")

        input(f"\n{Fore.LIGHTBLUE_EX}  [#] Press Enter for back to menu")
        banner()

    elif choose == '8':
        clear()
        port.scanner()
        print()
        input(f"\n{Fore.LIGHTBLUE_EX}  [#] Press Enter for back to menu")
        banner()

    elif choose == '9':
        clear()
        cloudflare.bypass()
        print()
        input(f"\n{Fore.LIGHTBLUE_EX}  [#] Press Enter for back to menu")
        banner()

    elif choose == '0':
        print(Style.RESET_ALL)
        clear()
        exit()

    else:
        clear()
        print(f"\n{Fore.RED}  [!] Please choose a valid option")
        time.sleep(1)
        banner()

try:
    banner() if __name__ == '__main__' else quit()
except KeyboardInterrupt as err:
    print(Style.RESET_ALL)
    clear()
    exit()
except EOFError as err:
    print(Style.RESET_ALL)
    clear()
    exit()
