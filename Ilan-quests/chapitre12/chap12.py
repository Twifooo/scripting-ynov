import multiprocessing
import time
import random
import os

def tache(nom, duree):
    print(f"{nom} PID {os.getpid()} démarre – {duree:.0f}s")
    time.sleep(duree)
    print(f"{nom} terminé")

if __name__ == "__main__":
    processus = []
    for i in range(5):
        nom = f"P{i+1}"
        duree = random.uniform(10, 40)
        p = multiprocessing.Process(target=tache, args=(nom, duree))
        processus.append(p)
        p.start()

    print("\nRegardez avec :  ps aux | grep python\n")
    input("Entrée pour tout arrêter → ")
    
    for p in processus:
        if p.is_alive():
            p.terminate()