import os
from colorama import Fore, Style
from platform import system
from time import sleep
from selenium import webdriver
import webbrowser



if os.path.isdir("output"):
    pass
else:
    os.system('mkdir output')

def cls():
    if system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

banner = f"""\n\n
\t\t{Style.RESET_ALL}  █████▒▄▄▄        █████ {Fore.RED}  █     █░ ▒█████   ██▀███  ▓█████▄ 
\t\t{Style.RESET_ALL}▓██   ▒▒████▄    ▒██▓  ██{Fore.RED}▒▓█░ █ ░█░▒██▒  ██▒▓██ ▒ ██▒▒██▀ ██▌
\t\t{Style.RESET_ALL}▒████ ░▒██  ▀█▄  ▒██▒  ██{Fore.RED}░▒█░ █ ░█ ▒██░  ██▒▓██ ░▄█ ▒░██   █▌
\t\t{Style.RESET_ALL}░▓█▒  ░░██▄▄▄▄██ ░██  █▀ {Fore.RED}░░█░ █ ░█ ▒██   ██░▒██▀▀█▄  ░▓█▄   ▌
\t\t{Style.RESET_ALL}░▒█░    ▓█   ▓██▒░▒███▒█▄{Fore.RED} ░░██▒██▓ ░ ████▓▒░░██▓ ▒██▒░▒████▓ 
\t\t{Style.RESET_ALL} ▒ ░    ▒▒   ▓▒█░░░ ▒▒░ ▒{Fore.RED} ░ ▓░▒ ▒  ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░ ▒▒▓  ▒ 
\t\t{Style.RESET_ALL} ░       ▒   ▒▒ ░ ░ ▒░  ░{Fore.RED}   ▒ ░ ░    ░ ▒ ▒░   ░▒ ░ ▒░ ░ ▒  ▒ 
\t\t{Style.RESET_ALL} ░ ░     ░   ▒      ░   ░{Fore.RED}   ░   ░  ░ ░ ░ ▒    ░░   ░  ░ ░  ░ 
\t\t{Style.RESET_ALL}             ░  ░    ░   {Fore.RED}     ░        ░ ░     ░        ░    
\t\t{Style.RESET_ALL}                         {Fore.RED}                             ░      {Style.RESET_ALL}
                    {Fore.RED}[ t.me/{Style.RESET_ALL}JustFaQTools {Fore.RED}]{Style.RESET_ALL}               {Fore.RED}[ @{Style.RESET_ALL}JustFaQ {Fore.RED}]{Style.RESET_ALL}
                                            
"""


# Functions

def kwTool():
    cls()
    print(banner)
    #webbrowser
    keyword_search = input(f"\t\t{Fore.RED}[{Style.RESET_ALL}${Fore.RED}]{Style.RESET_ALL} Enter something to {Fore.RED}search{Style.RESET_ALL} for: ")
    total_keywords = int(input(f"\n\t\t{Fore.RED}[{Style.RESET_ALL}:{Fore.RED}]{Style.RESET_ALL} Enter {Fore.RED}maximum {Style.RESET_ALL}number of keywords to fetch: "))
    output_file = input(f"\n\t\t{Fore.RED}[{Style.RESET_ALL}?{Fore.RED}]{Style.RESET_ALL} Enter the {Fore.RED}name{Style.RESET_ALL} of the output file? ")
    print_keywords = input(f"\n\t\t{Fore.RED}[{Style.RESET_ALL}?{Fore.RED}]{Style.RESET_ALL} Print the {Fore.RED}output{Style.RESET_ALL} keywords? ")

    driver = webdriver.Chrome()
    sleep(0.5)
    driver.get('https://keywordshitter.com/')
    text_area = driver.find_element_by_id('input')
    text_area.send_keys(keyword_search)
    start_job = driver.find_element_by_id('startjob')
    start_job.click()
    keyword_div = driver.find_element_by_id('numofkeywords')
    shouldLoop = True
    keywords_list = list
    while(shouldLoop):
        keyword_count_text = keyword_div.text.split(':')
        keyword_count_1 = int(keyword_count_text[0])
        keyword_count_2 = int(keyword_count_text[1])
        if(keyword_count_1 >= total_keywords or keyword_count_2 >= total_keywords):
            start_job.click()
            
            shouldLoop = False
            data = text_area.get_attribute('value')
            keywords_list = data.split('\n')
            keywords_list = [i for i in keywords_list if(len(i.strip())!=0)]
            driver.close()


    yes_response = ["y", "Y", "yes", "YES", "ye", "YE", "yea", "YEA", "yup", "YUP", "ya", "YA", "Yes", "Ye", "Yea"]
    if print_keywords in yes_response:
        x = 0
        cls()
        print(banner)
        for k in keywords_list:
            print(f"\t\t{Fore.RED}[{Style.RESET_ALL}{x}{Fore.RED}]{Style.RESET_ALL} {k}")
            x += 1
            with open(f"output//{output_file} - {total_keywords}.txt", "a", encoding="utf-8") as kwfile:
                kwfile.write(f"{k}\n")
                kwfile.close()

    else:
        for k in keywords_list:
            with open(f"output//{output_file} - {total_keywords}.txt", "a", encoding="utf-8") as kwfile:
                kwfile.write(f"{k}\n")
                kwfile.close()
kwTool()