#!/usr/bin/env python3
from googlesearch import search
import argparse
from colorama import Fore
import os
import requests

class Metafind:
    def __init__(self, domain, output):
        self.domain = arguments.domain
        self.output = arguments.output

        def banner():
            print(f'''{Fore.LIGHTCYAN_EX}
                    _.-"\\
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
{Fore.CYAN} / /  / /  __/ /_/ /_/ / __/ / / / / /_/ /  
/_/  /_/\___/\__/\__,_/_/ /_/_/ /_/\__,_/   
                                            
{Fore.LIGHTCYAN_EX}        ╔═════════════════════════╗
        ║{Fore.LIGHTWHITE_EX} Tool Created by MrEmpy  {Fore.LIGHTCYAN_EX}║
        ║{Fore.LIGHTWHITE_EX} Version 1.0             {Fore.LIGHTCYAN_EX}║
        ╚═════════════════════════╝
''')
        
        banner()
        if arguments.output:
            print(f'{Fore.LIGHTBLUE_EX}[*]{Fore.LIGHTWHITE_EX} Starting the search\n')
            for url in search(f'site:*.{arguments.domain} ext:pdf | ext:doc | ext:xls | ext:ppt | ext:odp | ext:ods | ext:docx | ext:xlsx | ext:pptx', pause=3, lang="en", start=0, stop=40):
                print(f'{Fore.LIGHTGREEN_EX}[+]{Fore.LIGHTWHITE_EX} {url}')

                try:
                    os.mkdir(arguments.output)
                except FileExistsError:
                    pass

                with open(f'{arguments.output}/urls.txt', 'a') as urls:
                    urls.write(url + '\n')
                urls.close()

            print(f'\n{Fore.LIGHTBLUE_EX}[*]{Fore.LIGHTWHITE_EX} Downloading the found files\n')
            urls = open(f'{arguments.output}/urls.txt', 'r').readlines()
            for url_f in urls:
                r = requests.get(url_f, allow_redirects=True)
                if r.status_code == 200:
                    with open(f'{arguments.output}/{os.path.basename(url_f)}', 'wb') as result_file:
                        result_file.write(r.content)
                    print(f'{Fore.LIGHTGREEN_EX}[+]{Fore.LIGHTWHITE_EX} Downloaded file: {url_f}'.replace('\n', ''))
            print(f'\n{Fore.LIGHTGREEN_EX}[+]{Fore.LIGHTWHITE_EX} Files downloaded successfully!')

        else:
            print(f'{Fore.LIGHTBLUE_EX}[*]{Fore.LIGHTWHITE_EX} Starting the search\n')
            for url in search(f'site:*.{arguments.domain} ext:pdf | ext:doc | ext:xls | ext:ppt | ext:odp | ext:ods | ext:docx | ext:xlsx | ext:pptx', pause=3, lang="en", start=0, stop=40):
                print(f'{Fore.LIGHTGREEN_EX}[+]{Fore.LIGHTWHITE_EX} {url}')

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-d','--domain', action='store', help='target domain', dest='domain', required=True)
    parser.add_argument('-o','--output', action='store', help='output folder', dest='output', required=False)
    arguments = parser.parse_args()
    Metafind(arguments.domain, arguments.output)