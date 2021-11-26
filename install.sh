#!/bin/bash
main() {
    if [ "$EUID" -ne 0 ]
        then printf "\033[0;34m[*] \033[0;37mPlease run as root\n"
        exit
    fi

    printf '\033[0;36m                    _.-"\\
                _.-"     \\
             ,-"          \\
            ( \            \\
             \ \            \\
              \ \            \\
               \ \         _.-;
                \ \    _.-"   :
                 \ \,-"    _.-"
                  \(   _.-"  
                   `--"
    __  ___     __        _____           __
   /  |/  /__  / /_____ _/ __(_)___  ____/ /
  / /|_/ / _ \/ __/ __ `/ /_/ / __ \/ __  / 
 / /  / /  __/ /_/ /_/ / __/ / / / / /_/ /  
/_/  /_/\___/\__/\__,_/_/ /_/_/ /_/\__,_/   '
    printf "\n\n\033[0;34m[*] \033[0;37mInstalling...\n"
    apt-get install python3 python3-pip -y
    pip install -r requirements.txt
    chmod +x metafind.py
    cp metafind.py /usr/bin/metafind
    chmod +x /usr/bin/metafind
    printf "\n\033[0;32[+] \033[0;37Tool installed successfully! Run 'metafind' to start."
}

main
