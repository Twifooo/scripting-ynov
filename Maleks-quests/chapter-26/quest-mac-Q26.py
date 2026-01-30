import subprocess
import argparse
import re


def verifier_interface(interface):
    pattern = re.compile(r'^[a-zA-Z0-9]+$')
    if pattern.match(interface):
        return True
    else:
        print("Interface invalide!")
        return False


def changer_mac(interface, nouvelle_mac):
    print(f"Changement de l'adresse MAC de {interface}...")
    
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", nouvelle_mac])
    subprocess.call(["ifconfig", interface, "up"])
    
    print(f"Nouvelle adresse MAC: {nouvelle_mac}")


parser = argparse.ArgumentParser()
parser.add_argument('-i', '--interface', type=str, help="Interface reseau a modifier")
parser.add_argument('-m', '--mac', type=str, help="Nouvelle adresse MAC")

args = parser.parse_args()

if verifier_interface(args.interface):
    changer_mac(args.interface, args.mac)
