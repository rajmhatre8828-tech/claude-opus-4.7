from colorama import Fore, Style, init
import datetime

# Initialize colorama
init(autoreset=True)

def log(message: str, level: str = "INFO"):
    """
    Custom logger with hacker-style formatting.
    """
    timestamp = datetime.datetime.now().strftime("%H:%M:%S")
    
    if level == "INFO":
        prefix = f"{Fore.GREEN}[*] {timestamp}"
    elif level == "WARN":
        prefix = f"{Fore.YELLOW}[!] {timestamp}"
    elif level == "ERROR":
        prefix = f"{Fore.RED}[x] {timestamp}"
    elif level == "GODMODE":
        prefix = f"{Fore.MAGENTA}[GOD] {timestamp}"
    else:
        prefix = f"{Fore.WHITE}[?] {timestamp}"
        
    print(f"{prefix} {Style.BRIGHT}{message}")

def print_banner():
    print(Fore.CYAN + Style.BRIGHT + """
   ___ _                _       _   _      _            _            _ 
  / __| |__ _ _  _ __| |___  | | | |_ _ | |___  __ | |__ ___ __| |
 | (__| / _` | || / _` / -_) | |_| | ' \| / _ \/ _| | / / -_) _` |
  \___|_\__,_|\_,_\__,_\___|  \___/|_||_|_\___/\__| |_\_\___\__,_|
                                               v2.0 :: OPUS 4.6 API
    """)
