import os
from colorama import init, Fore, Style
from rich.progress import Progress
from rich.console import Console
from rich.style import Style
from bs4 import BeautifulSoup
import requests
import json
import time
import urllib3
from urllib3.exceptions import SSLError
import sys

console = Console()

version = "1.0"
author = "memb3r"
description = "Powerful OSINT-tool on Python."

def banner():
    print(Fore.LIGHTCYAN_EX + '''\n                                 88                                 
                                 88                                 
                                 88                                 
,adPPYYba, 8b,dPPYba,  ,adPPYba, 88,dPPYba,   ,adPPYba, 8b,dPPYba,  
""     `Y8 88P'   "Y8 a8"     "" 88P'    "8a a8P_____88 88P'   "Y8  
,adPPPPP88 88         8b         88       88 8PP""""""" 88          
88,    ,88 88         "8a,   ,aa 88       88 "8b,   ,aa 88          
`"8bbdP"Y8 88          `"Ybbd8"' 88       88  `"Ybbd8"' 88         \n''')

def loading():
  with Progress() as progress:
    task = progress.add_task("[cyan]Starting...", total=40)
    for _ in range(40):
      time.sleep(0.1)
      progress.update(task, advance=1)

def banner_start():
  os.system('clear')
  time.sleep(1)
  print(Fore.LIGHTCYAN_EX + '''                    _                 
                   | |                
  __ _  _ __   ___ | |__    ___  _ __ 
 / _` || '__| / __|| '_ \  / _ \| '__|
| (_| || |   | (__ | | | ||  __/| |   
 \__,_||_|    \___||_| |_| \___||_| ''' + Fore.WHITE + version)
  console.print(f'\n[bold]Author[/bold]: [grey69]{author}[/grey69]')
  console.print(f'[bold]Description[/bold]: [grey69]{description}[/grey69]')
  console.print(f'\n[cyan bold]1[/cyan bold] - [italic]Phone number lookup.[/italic]')
  console.print(f'\n[cyan bold]2[/cyan bold] - [italic]Telegram scraper.[/italic]')
  console.print(f'\n[cyan bold]3[/cyan bold] - [italic]IP Scan.[/italic]')
  console.print(f'\n[cyan bold]4[/cyan bold] - [italic]Replit scraper.[/italic]')
  console.print(f'\n[cyan bold]5[/cyan bold] - [italic]Subdomain finder.[/italic]')
  console.print(f'\n[cyan bold]6[/cyan bold] - [italic]Ukraine car plane lookup.[/italic]')
  console.print(f'\n[cyan bold]cls[/cyan bold] - [italic]Clear screen.[/italic]')

def answerinp():
  while True:
    answer = console.input(f'\n[cyan]([magenta]![cyan]) [white]Input answer [bold]here[/bold]: ')
    if (answer == "1"):
      phonelook()
    elif (answer == "2"):
      tgscrape()
    elif (answer == "3"):
      ipscan()
    elif (answer == "4"):
      replitscraper()
    elif (answer == "5"):
      subdomainf()
    elif (answer == "6"):
      vehiclenum()
    elif (answer == ""):
      print()
    elif (answer == "cls"):
      os.system('clear')
      print(Fore.LIGHTCYAN_EX + '''                   _                 
                  | |                
  __ _  _ __  ___ | |__    ___  _ __ 
 / _` || '__|/ __|| '_ \  / _ \| '__|
| (_| || |  | (__ | | | ||  __/| |   
 \__,_||_|   \___||_| |_| \___||_| ''' + Fore.WHITE + version)
    else:
      console.print(f"\n[red]([magenta]X[red]) [red]Answer [white]{answer}[red] is not exist.[white]")

def phonelook():
  phone_number = console.input("\n[cyan]([magenta]![cyan]) [white]Input valid phone number (without '-', with country code): ").strip().replace("-", "").replace(" ", "").replace("+", "")
  if (phone_number == ""):
    console.print("\n[red]([magenta]X[red]) [red]Invalid input.")
    return
  http = requests.get(f"https://free-lookup.net/{phone_number}")
  html = BeautifulSoup(http.text, "html.parser")
  infos = html.findChild("ul", {"class": "report-summary__list"}).findAll("div")
  for info in infos:
      key = info.text.strip()
      value = info.find_next("div").text.strip()
      console.print(f"[green]([magenta]+[green])[white] {key}: [white]{value}")

def tgscrape():
  tgurl = console.input("\n[cyan]([magenta]![cyan]) [white]Input public user/channel URL: ")
  response = requests.get(tgurl)
  soup = BeautifulSoup(response.text, "html.parser")
  name = soup.find('span', {'dir': 'auto'})
  nametext = name.text if name else "Not Found"
  username = soup.find('div', {'class': 'tgme_page_extra'})
  usernametext = username.text if username else "Not Found"
  desc = soup.find('div', {'class': 'tgme_page_description'})
  desctext = desc.text if desc else "Not Found"
  console.print(f'\n[green]([magenta]+[green])[white] Name: {nametext}')
  console.print(f'[green]([magenta]+[green])[white] Username: {usernametext}')
  console.print(f'[green]([magenta]+[green])[white] Description: {desctext}')

def ipscan():
    ipinput = console.input("\n[cyan]([magenta]![cyan]) [white]Input IP to scan: ")
    request_url = 'http://ip-api.com/json/'

    http = urllib3.PoolManager()

    try:
        response = http.request('GET', request_url + ipinput)

        if response.status == 200:
            ipdata = response.data.decode('utf-8')  # Decode the response data
            # Check if the response is not empty
            if ipdata:
                try:
                    ipvalues = json.loads(ipdata)
                    console.print(f'\n[green]([magenta]+[green]) [white]IP: {ipinput}')
                    console.print(f'[green]([magenta]+[green]) [white]Country code: {ipvalues["countryCode"]}')
                    console.print(f'[green]([magenta]+[green]) [white]Country: {ipvalues["country"]}')
                    console.print(f'[green]([magenta]+[green]) [white]City: {ipvalues["city"]}')
                    console.print(f'[green]([magenta]+[green]) [white]Organisation: {ipvalues["org"]}')
                    console.print(f'[green]([magenta]+[green]) [white]ZIP: {ipvalues["zip"]}')
                    console.print(f'[green]([magenta]+[green]) [white]Latitude: {ipvalues["lat"]}')
                    console.print(f'[green]([magenta]+[green]) [white]Longitude: {ipvalues["lon"]}')
                    console.print(f'[green]([magenta]+[green]) [white]Timezone: {ipvalues["timezone"]}')
                except json.JSONDecodeError as e:
                    console.rint(f'\n[cyan]([red]-[cyan]) [white]Failed to parse JSON: {e}')
            else:
                console.print(f'\n[cyan]([red]-[cyan]) [white]Empty response from the server')
        else:
            console.print(f'\n[cyan]([red]-[cyan]) [white]Failed to fetch data for IP: {ipinput}')
    except SSLError as e:
        console.print(f'\n[cyan]([red]-[cyan]) [white]SSL Error: {e}')

def replitscraper():
  replurl = console.input("\n[cyan]([magenta]![cyan]) [white]Input public user URL: ")
  response = requests.get(replurl)
  soup = BeautifulSoup(response.text, "html.parser")
  name = soup.find('h1', {'class': 'css-1iqbb3j'})
  nametext = name.text if name else "Not Found"
  username = soup.find('span', {'class': 'css-162rtbe'})
  usernametext = username.text if username else "Not Found"
  desc = soup.find('span', {'class': 'Linkify'})
  desctext = desc.text if desc else "Not Found"
  acti = soup.find('span', {'class': 'css-1hlx567'})
  actitext = acti.text if acti else "Not Found"
  console.print(f'\n[green]([magenta]+[green])[white] Name: {nametext}')
  console.print(f'[green]([magenta]+[green])[white] Username: {usernametext}')
  console.print(f'[green]([magenta]+[green])[white] Description: {desctext}')
  console.print(f'[green]([magenta]+[green])[white] Activity: {actitext}')

def subdomainf():
  domainf = console.input("\n[cyan]([magenta]![cyan]) [white]Input domain: ")
  file = open('wordlist.txt','r')
  content = file.read()
  subdomains = content.splitlines()
  urlfound = 0
  for subdomain in subdomains:
      url1 = f"https://{subdomain}.{domainf}"
      try:
        response1 = requests.get(url1)
        if response1.status_code == 200:
            console.print(f"\n[green]([magenta]+[green])[white] [bold]Discovered URL[/bold]: {url1}")
            urlfound =  urlfound + 1
      except requests.exceptions.RequestException as e:
        pass
  console.print(f"\n[green]([magenta]+[green])[white] [bold]Discovered {urlfound} subdomains.[/bold]")

def vehiclenum():
  vehiclenuminp = console.input("\n[cyan]([magenta]![cyan]) [white]Input vehicle number: ")
  gaiurl = "https://baza-gai.com.ua/nomer/" + vehiclenuminp
  response = requests.get(gaiurl)
  soup = BeautifulSoup(response.text, "html.parser")
  items = soup.find('li', class_='list-group-item plate-model__list-item')
  carreg = items.find('span', class_='d-block plate-model__list-item-text') if items else None
  carregtext = carreg.text if carreg else "Not Found"
  console.print(f"\n[green]([magenta]+[green])[white] Registration date: {carregtext}")
  items2 = soup.find_all('li', class_='list-group-item plate-model__list-item')
  carreg2 = items2[1].find('span', class_='d-block plate-model__list-item-text') if len(items2) > 1 else None
  carregtext2 = carreg2.text if carreg2 else "Not Found"
  console.print(f"\n[green]([magenta]+[green])[white] Signs: {carregtext2}")
  items3 = soup.find_all('li', class_='list-group-item plate-model__list-item')
  carreg3 = items3[2].find('span', class_='d-block plate-model__list-item-text') if len(items3) > 2 else None
  carregtext3 = carreg3.text if carreg3 else "Not Found"
  console.print(f"\n[green]([magenta]+[green])[white] Operations: {carregtext3}")
  items4 = soup.find_all('li', class_='list-group-item plate-model__list-item')
  carreg4 = items4[3].find('span', class_='d-block plate-model__list-item-text') if len(items4) > 2 else None
  carregtext4 = carreg4.text if carreg4 else "Not Found"
  console.print(f"\n[green]([magenta]+[green])[white] Address: {carregtext4}")
  vin_element = soup.find('span', class_='vin-code-erased')
  data_full = vin_element['data-full'] if vin_element else "Not Found"
  console.print(f"\n[green]([magenta]+[green])[white] VIN: {data_full}")

if __name__ == '__main__':
  banner()
  loading()
  banner_start()
  answerinp()