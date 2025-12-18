import signal
import time
import sys

def stop_programme(sig, frame):
    print("\n\nCTRL+C effectué ! Arrêt du programme..")
    sys.exit(0)
    
    
signal.signal(signal.SIGINT, stop_programme)

print("Programme démarré. Appuyez sur CTRL+C pour arrêter le programme..")

while True:
    print("Programme en cours d'exécution.. (CTRL+C pour quitter le programme)")
    time.sleep(3)