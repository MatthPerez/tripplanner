from scapy.all import *
from scapy.layers.dot11 import Dot11, Dot11Beacon, Dot11Elt
import os
import subprocess


def scan_wifi(interface="Wi-fi"):
    if interface not in get_if_list():
        lans = get_if_list()

        for lan in lans:
            print(lan)

        return

    try:
        os.system(f"sudo iwconfig {interface} mode monitor")
    except Exception as e:
        print(f"Erreur lors de la mise en mode monitor : {e}")
        return

    def packet_handler(pkt):
        if pkt.haslayer(Dot11Beacon):
            ssid = pkt[Dot11Elt].info.decode()
            bssid = pkt[Dot11].addr2
            channel = int(ord(pkt[Dot11Elt:3].info))
            print(f"SSID: {ssid}, BSSID: {bssid}, Channel: {channel}")

    print(f"Scan des réseaux Wi-Fi sur l'interface {interface}...")
    sniff(iface=interface, prn=packet_handler, timeout=10)


def scan_wifis():
    command = "netsh wlan show networks"
    result = subprocess.run(
        command,
        capture_output=True,
        text=True,
        shell=True,
    )

    if result.returncode == 0:
        print("Réseaux Wi-Fi disponibles :")
        print(result.stdout)
    else:
        print("Erreur lors de la recherche des réseaux Wi-Fi :", result.stderr)


import subprocess


def get_saved_wifi_passwords():
    command = "netsh wlan show profiles"
    result = subprocess.run(command, capture_output=True, text=True, shell=True)

    if result.returncode != 0:
        print("Erreur lors de la récupération des profils Wi-Fi :", result.stderr)
        return

    profiles = [
        line.split(":")[1].strip()
        for line in result.stdout.splitlines()
        if "Profil Tous les utilisateurs" in line
    ]

    for profile in profiles:
        command = f'netsh wlan show profile name="{profile}" key=clear'
        result = subprocess.run(command, capture_output=True, text=True, shell=True)

        if result.returncode == 0:
            print(f"\nProfil : {profile}")

            for line in result.stdout.splitlines():
                # print(f"contenu : {line}")

                if "Contenu de" in line:
                    print("Mot de passe :", line.split(":")[1].strip())
        else:
            print(
                f"Erreur lors de la récupération du mot de passe pour {profile} :",
                result.stderr,
            )


def get_current_wifi_info():
    command = "netsh wlan show interfaces"
    
    result = subprocess.run(
        command,
        capture_output=True,
        text=True,
        shell=True,
    )

    if result.returncode != 0:
        print("Erreur lors de la récupération des informations Wi-Fi :", result.stderr)
        
        return

    ssid = None

    for line in result.stdout.splitlines():

        if "SSID" in line and "BSSID" not in line:
            ssid = line.split(":")[1].strip()
            break

    if not ssid:
        print(
            "Aucun réseau Wi-Fi trouvé. Tu n'es peut-être pas connecté à un réseau Wi-Fi."
        )
        
        return

    print(f"Réseau actuellement connecté : {ssid}")

    command = f'netsh wlan show profile name="{ssid}" key=clear'
    
    result = subprocess.run(
        command,
        capture_output=True,
        text=True,
        shell=True,
    )

    if result.returncode != 0:
        print(
            f"Erreur lors de la récupération du mot de passe pour {ssid} :",
            result.stderr,
        )
        
        return

    password = None
    for line in result.stdout.splitlines():
        if "Contenu de la clé" in line:
            password = line.split(":")[1].strip()
            break

    if password:
        print(f"Mot de passe : {password}")
    else:
        print(
            "Mot de passe non trouvé (le réseau peut ne pas avoir de mot de passe ou est un réseau public)."
        )


if __name__ == "__main__":
    # scan_wifi()
    # scan_wifis()
    # get_saved_wifi_passwords()
    get_current_wifi_info()
