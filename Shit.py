import requests
import string
import random
import threading
import time
import ctypes
from colorama import init, Fore, Style

init(autoreset=True)

hook1 = "" # FOR VALID
hook2 = "" # FOR INVALID

invlc = 0
vlc = 0
tc = 0
invl = []

def rsting(length):
    aphlaaa = string.ascii_letters + string.digits
    return ''.join(random.choice(aphlaaa) for _ in range(length))

def ggl(code):
    return f"https://discord.gift/{code}"

def s2h(hookurllll, message):
    payload = {"content": message}
    response = requests.post(hookurllll, json=payload)
    if response.status_code != 200:
        print(Fore.RED + f"Failed {response.status_code}")
    else:
        print(Fore.GREEN + f"Message sent successfully to Discord webhook {hookurllll}.")

def sweb():
    global invlc, invl
    if invl:
        message = "\n".join(invl)
        s2h(hook2, message)
        invlc += len(invl)
        invl.clear()

def check_gift_code(code):
    global invl, vlc, tc
    tc += 1
    url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true"
    response = requests.get(url)
    if response.status_code == 200:
        s2h(hook1, Fore.BLUE + f"@everyone Mill Gya Bc \n{ggl(code)}")
        vlc += 1
    else:
        invalid_link = ggl(code)
        invl.append(invalid_link)
        if len(invl) == 50:
            sweb()

def ftime(seconds):
    minutes, seconds = divmod(seconds, 60)
    seconds, milliseconds = divmod(seconds, 1)
    return f"{int(minutes)} minutes {int(seconds)} seconds {int(milliseconds * 1000)} ms"

def vrate():
    global vlc, tc
    return (vlc / tc) * 100 if tc != 0 else 0

def kansoletitle():
    aizer = ftime(time.time() - start_time)
    valid_rate = vrate()
    title = f"NITRO GEN | Elapsed: {aizer} | Valid Rate: {valid_rate:.2f}%"
    ctypes.windll.kernel32.SetConsoleTitleW(title)

def genandcheck():
    while True:
        random_string = rsting(18)
        check_gift_code(random_string)
        kansoletitle()
        time.sleep(0.01)  

if __name__ == "__main__":
    start_time = time.time()
    mohit = 25
    print(Fore.LIGHTCYAN_EX + f"""

        ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░              ░▒▓███████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓████████▓▒░ 
        ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░             ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░  ░▒▓█▓▒░     
        ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░             ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░  ░▒▓█▓▒░     
        ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░              ░▒▓██████▓▒░░▒▓████████▓▒░▒▓█▓▒░  ░▒▓█▓▒░     
        ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░                    ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░  ░▒▓█▓▒░     
        ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░                    ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░  ░▒▓█▓▒░     
        ░▒▓████████▓▒░▒▓██████▓▒░░▒▓████████▓▒░      ░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░  ░▒▓█▓▒░     
                                    DEV - AIZER
                                    GG/CODERZ
                                    NOTE - BEST TOOL FOR TIME PASS :)
          \nStarting {mohit} threads to generate ......""")
    kansoletitle() 
    threads = []
    for _ in range(mohit):
        thread = threading.Thread(target=genandcheck)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    sweb()
